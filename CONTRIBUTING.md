# Guide de Contribution

Merci de votre intérêt pour contribuer à Gare au Loup ! 🎉

## 🚀 Démarrage rapide

1. **Fork** le projet
2. **Clone** votre fork
   ```bash
   git clone https://github.com/VOTRE-USERNAME/gare-au-loup.git
   cd gare-au-loup
   ```
3. **Installez** les dépendances de développement
   ```bash
   pip install -e ".[dev]"
   pre-commit install
   ```

## 📝 Processus de contribution

### 1. Créer une branche

```bash
git checkout -b feature/ma-fonctionnalite
# ou
git checkout -b fix/mon-correctif
```

### 2. Développer

- Écrivez du code clair et lisible
- Suivez les conventions de code (Black, Ruff)
- Ajoutez des tests si possible
- Documentez vos fonctions avec des docstrings

### 3. Tester localement

```bash
# Linting
black src/ tests/
ruff check src/ tests/
mypy src/

# Tests
pytest

# Pre-commit hooks
pre-commit run --all-files
```

### 4. Commit

Utilisez des messages de commit clairs et descriptifs :

```bash
git commit -m "feat: ajoute support pour architecture ResNet34"
git commit -m "fix: corrige bug de prédiction sur images PNG"
git commit -m "docs: améliore README avec exemples"
```

Formats recommandés :
- `feat:` nouvelle fonctionnalité
- `fix:` correction de bug
- `docs:` documentation
- `refactor:` refactoring
- `test:` ajout de tests
- `chore:` maintenance

### 5. Push et Pull Request

```bash
git push origin feature/ma-fonctionnalite
```

Ensuite, créez une Pull Request sur GitHub avec :
- Un titre clair
- Une description détaillée des changements
- Des captures d'écran si pertinent
- Référence aux issues liées

## 🎨 Standards de code

### Style

- **Formatage** : Black avec ligne max 100 caractères
- **Linting** : Ruff avec configuration du projet
- **Type hints** : Encouragés mais non obligatoires
- **Docstrings** : Format Google/NumPy

Exemple :

```python
def classify_image(image_path: str, model_path: str) -> dict[str, float]:
    """
    Classifie une image avec un modèle entraîné.

    Args:
        image_path: Chemin vers l'image à classifier.
        model_path: Chemin vers le modèle (.pkl).

    Returns:
        Dictionnaire {classe: probabilité}.

    Raises:
        FileNotFoundError: Si l'image n'existe pas.
    """
    ...
```

### Tests

- Utilisez `pytest` pour les tests
- Nommez les fichiers `test_*.py`
- Visez une couverture raisonnable (pas d'obsession du 100%)
- Tests unitaires pour la logique métier
- Tests d'intégration pour les workflows complets

### Documentation

- README à jour
- Docstrings pour toutes les fonctions publiques
- Commentaires pour la logique complexe
- Exemples d'usage dans les docstrings

## 🐛 Signaler un bug

Créez une issue avec :
- Description claire du bug
- Steps to reproduce
- Comportement attendu vs observé
- Environnement (OS, Python version, etc.)
- Logs ou messages d'erreur

## 💡 Proposer une fonctionnalité

Créez une issue avec :
- Description de la fonctionnalité
- Use case / motivation
- Proposition d'implémentation (optionnel)
- Mockups ou exemples (optionnel)

## 📚 Idées de contributions

### Facile
- [ ] Améliorer la documentation
- [ ] Ajouter des exemples d'usage
- [ ] Corriger des typos
- [ ] Ajouter des tests

### Moyen
- [ ] Supporter d'autres architectures (ResNet34, EfficientNet)
- [ ] Améliorer les visualisations
- [ ] Créer un script de download de dataset
- [ ] Ajouter export ONNX

### Avancé
- [ ] API REST avec FastAPI
- [ ] Interface web (Gradio/Streamlit)
- [ ] Détection d'objets (bounding boxes)
- [ ] Pipeline d'entraînement distribué
- [ ] Quantization et optimisation

## 🔍 Review process

1. Un mainteneur reviewera votre PR
2. Des changements peuvent être demandés
3. Une fois approuvée, la PR sera merged
4. Votre contribution sera dans la prochaine release !

## 📄 License

En contribuant, vous acceptez que votre code soit sous license MIT.

## 🙏 Remerciements

Merci de contribuer à améliorer Gare au Loup ! Chaque contribution compte. 🚀
