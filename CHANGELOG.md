# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [0.2.0] - 2025-01-06

### ✨ Ajouté

- Refactoring complet du code en modules Python réutilisables
- Scripts CLI `train.py` et `predict.py` pour entraînement et prédiction
- Configuration moderne avec `pyproject.toml`
- Structure de projet professionnelle (src/, tests/, notebooks/, docs/)
- Documentation complète dans README.md
- Guide de contribution (CONTRIBUTING.md)
- Configurations de linting : Black, Ruff, MyPy
- Pre-commit hooks pour vérifications automatiques
- Tests unitaires (squelettes)
- LICENSE MIT
- .gitignore complet et moderne
- CHANGELOG.md

### 🔄 Modifié

- Mise à jour des dépendances vers versions modernes :
  - PyTorch 2.x
  - FastAI 2.7+
  - scikit-learn 1.3+
  - pandas 2.0+
  - numpy 1.24+
  - Selenium 4.x (pour scraper, bien que non fonctionnel)
- Organisation du projet en structure modulaire
- Déplacement du notebook dans `notebooks/`
- Déplacement du scraper dans `scripts/`

### 📚 Documentation

- README enrichi avec installation, usage, exemples
- Documentation des modules avec docstrings
- Guide de contribution
- README pour le scraper (marqué comme obsolète)

### 🔧 Technique

- Support Python 3.9, 3.10, 3.11
- Type hints dans le code
- Code formaté avec Black (line-length: 100)
- Linting avec Ruff
- Type checking avec MyPy

## [0.1.0] - 2021-XX-XX

### ✨ Ajouté

- Première version du projet
- Modèle ResNet18 avec FastAI
- Notebook Jupyter d'exploration "Loups vs ours.ipynb"
- Script de scraping Google Images
- Dataset avec classes loup/ours/autre
- ~95% accuracy sur validation set
- Configurations de base (requirements.txt, .gitignore)

### 📊 Résultats

- Accuracy : ~95% sur jeu de validation
- Dataset : 524 images d'entraînement, 130 de validation
- Entraînement : 2 epochs seulement
- Architecture : ResNet18 pré-entraîné

---

[0.2.0]: https://github.com/fflakito/gare-au-loup/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/fflakito/gare-au-loup/releases/tag/v0.1.0
