# 🐺🐻 Gare au Loup - Classificateur d'Images

> Système de classification d'images pour identifier automatiquement les loups, les ours et autres animaux à partir de photos de caméras de surveillance pour refuges d'animaux.

## 📋 Description

Ce projet utilise le deep learning pour classifier automatiquement des images capturées par des caméras de surveillance installées dans un refuge d'animaux. Le modèle distingue trois catégories :

- **🐺 Loup** : Images de loups
- **🐻 Ours** : Images d'ours
- **🦌 Autre** : Autres animaux (cerfs, ânes, moutons, poules) ou paysages vides

Le modèle atteint **~95% de précision** sur le jeu de validation avec une architecture légère (ResNet18), ce qui permet un déploiement sur du matériel modeste.

## 🎯 Caractéristiques

- ✅ Modèle léger basé sur **ResNet18** avec transfer learning
- ✅ Entraînement rapide avec **FastAI**
- ✅ Code modulaire et réutilisable
- ✅ Scripts CLI pour entraînement et prédiction
- ✅ Notebooks Jupyter pour exploration interactive
- ✅ Visualisations des résultats (confusion matrix, top losses)
- ✅ Configuration moderne avec `pyproject.toml`

## 🚀 Installation

### Prérequis

- Python 3.9, 3.10 ou 3.11
- pip ou conda
- (Optionnel) GPU CUDA pour accélération

### Installation standard

```bash
# Cloner le repository
git clone https://github.com/fflakito/gare-au-loup.git
cd gare-au-loup

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install -e .
```

### Installation avec extras

```bash
# Pour développement (avec linting, tests, etc.)
pip install -e ".[dev]"

# Pour utiliser les notebooks
pip install -e ".[notebook]"

# Tout installer
pip install -e ".[all]"
```

## 📖 Usage

### 1️⃣ Entraînement du modèle

```bash
# Entraînement basique
python src/train.py --data-path data --epochs 2

# Entraînement personnalisé
python src/train.py \
    --data-path data \
    --epochs 5 \
    --image-size 299 \
    --batch-size 32 \
    --model-name my_model
```

**Options disponibles :**
- `--data-path` : Chemin vers le dossier de données (défaut : `data`)
- `--epochs` : Nombre d'époques (défaut : `2`)
- `--valid-pct` : Pourcentage de validation (défaut : `0.2`)
- `--image-size` : Taille des images (défaut : `224`)
- `--batch-size` : Taille des batchs (défaut : `64`)
- `--model-name` : Nom du modèle sauvegardé (défaut : `weights`)

### 2️⃣ Prédiction sur de nouvelles images

```bash
# Prédiction sur une image
python src/predict.py --image path/to/image.jpg

# Prédiction sur un dossier
python src/predict.py --image-dir path/to/images/

# Utiliser un modèle spécifique
python src/predict.py --model-path data/models/my_model.pkl --image test.jpg
```

### 3️⃣ Utilisation dans du code Python

```python
from src.data.dataset import create_databunch
from src.models.classifier import AnimalClassifier

# Charger les données
data = create_databunch("data", valid_pct=0.2)

# Créer et entraîner le modèle
classifier = AnimalClassifier(data)
classifier.train(epochs=2)
classifier.save("my_model")

# Faire des prédictions
pred_class, pred_idx, probs = classifier.predict("path/to/image.jpg")
print(f"Prédiction : {pred_class} (confiance : {max(probs):.2%})")
```

### 4️⃣ Exploration avec Jupyter

```bash
# Lancer Jupyter
jupyter notebook notebooks/

# Ouvrir "Loups vs ours.ipynb"
```

## 📁 Structure du Projet

```
gare-au-loup/
├── src/
│   ├── __init__.py
│   ├── train.py              # Script d'entraînement
│   ├── predict.py            # Script de prédiction
│   ├── data/
│   │   ├── __init__.py
│   │   └── dataset.py        # Gestion des datasets
│   ├── models/
│   │   ├── __init__.py
│   │   └── classifier.py     # Modèle de classification
│   └── utils/
│       ├── __init__.py
│       └── visualization.py  # Visualisations
├── notebooks/
│   └── Loups vs ours.ipynb   # Notebook d'exploration
├── scripts/
│   └── google_images_scraper/ # Scraper d'images (obsolète)
├── data/
│   ├── train/                # Données d'entraînement
│   │   ├── loup/
│   │   ├── ours/
│   │   └── autre/
│   └── models/               # Modèles sauvegardés
├── tests/                    # Tests unitaires
├── docs/                     # Documentation
├── pyproject.toml            # Configuration du projet
├── README.md
└── .gitignore
```

## 🎨 Architecture du Modèle

Le modèle utilise **ResNet18** pré-entraîné sur ImageNet avec les modifications suivantes :

1. **Transfer Learning** : Utilisation des poids ImageNet
2. **Fine-tuning** : Adaptation de la dernière couche pour 3 classes
3. **Data Augmentation** : Flips horizontaux, rotations légères
4. **Normalisation** : Stats ImageNet (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
5. **Optimisation** : One-cycle policy avec FastAI

### Hyperparamètres par défaut

| Paramètre | Valeur |
|-----------|--------|
| Architecture | ResNet18 |
| Taille d'image | 224×224 |
| Batch size | 64 |
| Epochs | 2 |
| Validation split | 20% |

## 📊 Résultats

### Performance sur le jeu de validation

- **Accuracy** : ~95%
- **Dataset** :
  - Entraînement : ~524 images
  - Validation : ~130 images
- **Classes** : loup, ours, autre

### Matrice de Confusion (exemple)

```
              Prédit
              autre  loup  ours
Réel  autre     45     1     3
      loup       0    46     1
      ours       2     0    34
```

### Observations

✅ **Points forts :**
- Excellente précision pour la classification loup/ours
- Peu de faux positifs critiques
- Entraînement rapide (quelques minutes sur CPU)

⚠️ **Points d'amélioration :**
- Confusion occasionnelle classe "autre" (besoin de plus de données variées)
- Images de faible qualité/nocturnes nécessitent amélioration
- Dataset pourrait être enrichi avec photos réelles des caméras du refuge

## 🛠️ Développement

### Configuration de l'environnement de développement

```bash
# Installer avec dépendances de dev
pip install -e ".[dev]"

# Installer pre-commit hooks
pre-commit install

# Lancer les tests
pytest

# Linting
black src/ tests/
ruff check src/ tests/
mypy src/
```

### Standards de code

- **Formatter** : Black (line length: 100)
- **Linter** : Ruff
- **Type checking** : MyPy
- **Tests** : Pytest

### Pre-commit Hooks

Les hooks suivants s'exécutent automatiquement avant chaque commit :
- Formatage avec Black
- Vérification avec Ruff
- Vérification des trailing whitespaces
- Vérification des fins de fichier
- Validation YAML

## 📚 Documentation Technique

### Dataset

Le dataset doit être organisé selon la structure suivante :

```
data/
├── train/
│   ├── loup/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   ├── ours/
│   │   └── ...
│   └── autre/
│       └── ...
└── valid/ (optionnel, sinon split automatique à 80/20)
```

### Ajouter de nouvelles images

1. Placer les images dans le dossier de la classe appropriée
2. Formats supportés : JPG, PNG
3. Taille minimale recommandée : 224×224 pixels
4. Qualité : éviter images trop compressées ou floues

### Améliorer le modèle

```python
from src.models.classifier import AnimalClassifier
from src.data.dataset import create_databunch

data = create_databunch("data")
classifier = AnimalClassifier(data)

# 1. Trouver le learning rate optimal
classifier.learner.lr_find()
classifier.learner.recorder.plot()

# 2. Entraîner avec learning rate personnalisé
classifier.train(epochs=5, learning_rate=1e-3)

# 3. Fine-tuner les couches profondes
classifier.learner.unfreeze()
classifier.learner.fit_one_cycle(5, max_lr=slice(1e-5, 1e-3))
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

### Idées de contributions

- [ ] Améliorer le dataset (plus d'images variées)
- [ ] Tester d'autres architectures (ResNet34, EfficientNet)
- [ ] Ajouter une API REST pour déploiement
- [ ] Créer une interface web simple
- [ ] Ajouter détection d'objets (bounding boxes)
- [ ] Support pour vidéos en temps réel
- [ ] Export ONNX pour déploiement optimisé

## 📝 Historique des Versions

### Version 0.2.0 (2025-01-XX)
- ✨ Refactoring complet en modules Python
- ✨ Ajout de scripts CLI (train.py, predict.py)
- ✨ Configuration moderne avec pyproject.toml
- ✨ Mise à jour des dépendances (PyTorch 2.x, FastAI 2.7+)
- ✨ Ajout de linting et pre-commit hooks
- 📚 Documentation complète

### Version 0.1.0 (2021-XX-XX)
- 🎉 Version initiale
- 🤖 Modèle ResNet18 avec ~95% accuracy
- 📓 Notebook Jupyter d'exploration
- 🔧 Script de scraping Google Images

## ⚠️ Limitations Connues

1. **Scraper obsolète** : Le script de scraping Google Images ne fonctionne plus
2. **Dataset limité** : ~650 images, pourrait bénéficier de plus de données
3. **Classes déséquilibrées** : La classe "autre" manque de diversité
4. **Conditions nocturnes** : Performance réduite sur images infrarouges/nuit
5. **Généralisation** : Entraîné sur images web, peut nécessiter fine-tuning sur photos du refuge

## 📄 License

MIT License - voir le fichier LICENSE pour plus de détails.

## 🙏 Remerciements

- **FastAI** pour le framework de deep learning accessible
- **PyTorch** pour la fondation
- Dataset scraped depuis Google Images (usage éducatif/recherche)
- Client : refuge d'animaux (projet réel)

## 📧 Contact

Pour questions ou suggestions : [créer une issue](https://github.com/fflakito/gare-au-loup/issues)

---

**Note** : Ce projet a été développé dans un contexte d'urgence pour un refuge d'animaux. Il reste des pistes d'amélioration documentées dans le code et les notebooks.
