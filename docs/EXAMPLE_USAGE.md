# Exemples d'utilisation

Ce document présente différents cas d'usage de Gare au Loup.

## 📚 Table des matières

1. [Entraînement de base](#entraînement-de-base)
2. [Entraînement avancé](#entraînement-avancé)
3. [Prédiction](#prédiction)
4. [Utilisation en code Python](#utilisation-en-code-python)
5. [Fine-tuning](#fine-tuning)
6. [Visualisations](#visualisations)

## Entraînement de base

### Entraînement simple

```bash
python src/train.py
```

Cette commande utilise les paramètres par défaut :
- Dataset : `data/`
- Époques : 2
- Validation : 20%
- Taille images : 224×224
- Batch size : 64

### Personnaliser l'entraînement

```bash
python src/train.py \
    --data-path ./my_data \
    --epochs 5 \
    --image-size 299 \
    --batch-size 32 \
    --model-name wolf_bear_v2
```

## Entraînement avancé

### Script Python personnalisé

```python
from src.data.dataset import create_databunch
from src.models.classifier import AnimalClassifier
from src.utils.visualization import plot_confusion_matrix, plot_top_losses

# 1. Charger les données avec augmentation personnalisée
data = create_databunch(
    data_path="data",
    valid_pct=0.2,
    image_size=224,
    batch_size=64,
    do_flip=True,
)

print(f"Classes : {data.classes}")
print(f"Train : {len(data.train_ds)} images")
print(f"Valid : {len(data.valid_ds)} images")

# 2. Créer le modèle
classifier = AnimalClassifier(data)

# 3. Trouver le meilleur learning rate (optionnel)
classifier.learner.lr_find()
classifier.learner.recorder.plot()

# 4. Entraîner
classifier.train(epochs=3, learning_rate=1e-3)

# 5. Sauvegarder
classifier.save("weights-custom")

# 6. Analyser les résultats
interp = classifier.get_interpretation()
plot_confusion_matrix(interp, figsize=(8, 8))
plot_top_losses(interp, k=12)
```

### Fine-tuning complet

```python
from src.models.classifier import AnimalClassifier
from src.data.dataset import create_databunch

data = create_databunch("data")
classifier = AnimalClassifier(data)

# Phase 1 : Entraîner seulement la dernière couche
classifier.train(epochs=2)
classifier.save("phase1")

# Phase 2 : Dégeler et fine-tuner toutes les couches
classifier.learner.unfreeze()
classifier.learner.fit_one_cycle(
    5,
    max_lr=slice(1e-6, 1e-4)  # LR différencié par couche
)
classifier.save("phase2_finetuned")
```

## Prédiction

### Prédiction sur une image

```bash
python src/predict.py \
    --model-path data/models/export.pkl \
    --image test_images/wolf.jpg
```

Sortie :
```
🎯 Prédiction : loup

📊 Probabilités :
  loup       : 98.45%
  ours       :  1.23%
  autre      :  0.32%
```

### Prédiction batch sur un dossier

```bash
python src/predict.py \
    --model-path data/models/export.pkl \
    --image-dir test_images/
```

### Prédiction en Python

```python
from src.models.classifier import load_trained_model

# Charger le modèle
classifier = load_trained_model("data/models/export.pkl")

# Prédire
pred_class, pred_idx, probs = classifier.predict("test.jpg")

print(f"Classe : {pred_class}")
print(f"Confiance : {max(probs):.2%}")

# Obtenir toutes les probabilités
for class_name, prob in zip(classifier.data.classes, probs):
    print(f"{class_name}: {prob:.2%}")
```

## Utilisation en code Python

### Pipeline complet

```python
from pathlib import Path
from src.data.dataset import create_databunch
from src.models.classifier import AnimalClassifier

def train_and_evaluate(data_path: str, model_name: str = "model"):
    """Pipeline complet d'entraînement et évaluation."""

    # 1. Données
    print("📊 Chargement des données...")
    data = create_databunch(data_path, valid_pct=0.2)

    # 2. Modèle
    print("🤖 Création du modèle...")
    classifier = AnimalClassifier(data)

    # 3. Entraînement
    print("🚀 Entraînement...")
    classifier.train(epochs=2)

    # 4. Sauvegarde
    print(f"💾 Sauvegarde : {model_name}")
    classifier.save(model_name)

    # 5. Évaluation
    print("📈 Évaluation...")
    interp = classifier.get_interpretation()

    # Matrice de confusion
    from src.utils.visualization import plot_confusion_matrix
    plot_confusion_matrix(interp)

    # Métriques
    from sklearn.metrics import classification_report
    y_true = [data.classes[i] for i in interp.y_true]
    y_pred = [data.classes[i] for i in interp.pred_class]

    print("\n📊 Rapport de classification :")
    print(classification_report(y_true, y_pred))

    return classifier

# Utilisation
if __name__ == "__main__":
    classifier = train_and_evaluate("data", "my_model")
```

### Prédiction avec seuil de confiance

```python
from src.models.classifier import load_trained_model

def predict_with_threshold(
    model_path: str,
    image_path: str,
    confidence_threshold: float = 0.8
):
    """Prédire avec un seuil de confiance minimum."""

    classifier = load_trained_model(model_path)
    pred_class, pred_idx, probs = classifier.predict(image_path)

    max_prob = max(probs)

    if max_prob < confidence_threshold:
        print(f"⚠️ Confiance faible ({max_prob:.2%} < {confidence_threshold:.0%})")
        print("Suggestion : révision manuelle requise")
    else:
        print(f"✅ Prédiction : {pred_class} ({max_prob:.2%})")

    return pred_class, max_prob

# Utilisation
predict_with_threshold(
    "data/models/export.pkl",
    "uncertain_image.jpg",
    confidence_threshold=0.85
)
```

## Fine-tuning

### Avec votre propre dataset

```python
from src.data.dataset import create_databunch
from src.models.classifier import AnimalClassifier

# 1. Préparez vos données dans cette structure :
#    my_data/
#    ├── train/
#    │   ├── loup/
#    │   ├── ours/
#    │   └── autre/
#    └── valid/ (optionnel)

# 2. Créer databunch
data = create_databunch("my_data", valid_pct=0.2)

# 3. Charger modèle pré-entraîné et fine-tuner
classifier = AnimalClassifier(data)
classifier.load("weights-02")  # Partir d'un modèle existant

# 4. Fine-tuning
classifier.learner.unfreeze()
classifier.train(epochs=5, learning_rate=1e-5)
classifier.save("finetuned_custom")
```

## Visualisations

### Afficher des échantillons

```python
from src.data.dataset import create_databunch
from src.utils.visualization import plot_data_samples

data = create_databunch("data")
plot_data_samples(data, rows=4, figsize=(15, 10))
```

### Analyser les erreurs

```python
from src.models.classifier import AnimalClassifier
from src.utils.visualization import plot_top_losses, plot_confusion_matrix

classifier = AnimalClassifier(data)
classifier.load("weights-02")

interp = classifier.get_interpretation()

# Top 16 erreurs
plot_top_losses(interp, k=16, figsize=(20, 15))

# Matrice de confusion normalisée
plot_confusion_matrix(interp, normalize=True)
```

### Métriques d'entraînement

```python
from src.utils.visualization import plot_training_metrics

# Après entraînement
plot_training_metrics(classifier.learner)
```

## Export et déploiement

### Export pour production

```python
from src.models.classifier import AnimalClassifier

classifier = AnimalClassifier(data)
classifier.load("weights-02")

# Export FastAI
classifier.learner.export("export.pkl")

# Pour ONNX (nécessite torch et onnx)
# import torch
# dummy_input = torch.randn(1, 3, 224, 224)
# torch.onnx.export(classifier.learner.model, dummy_input, "model.onnx")
```

### Inférence optimisée

```python
from fastai.vision import load_learner

# Charger modèle exporté
learn = load_learner(".", "export.pkl")

# Prédiction rapide
from fastai.vision import open_image
img = open_image("test.jpg")
pred_class, pred_idx, outputs = learn.predict(img)

print(f"Classe : {pred_class}")
```

---

## 🔗 Ressources supplémentaires

- [Documentation FastAI](https://docs.fast.ai/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Guide des bonnes pratiques](../CONTRIBUTING.md)
