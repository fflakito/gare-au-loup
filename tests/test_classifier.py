"""Tests pour le module models.classifier."""

import pytest


class TestAnimalClassifier:
    """Tests pour la classe AnimalClassifier."""

    def test_classifier_initialization(self):
        """Test d'initialisation du classificateur."""
        pytest.skip("Nécessite un DataBunch pour fonctionner")

    def test_predict(self):
        """Test de prédiction sur une image."""
        pytest.skip("Nécessite un modèle entraîné pour fonctionner")


# Note: Ces tests sont des squelettes
# Pour les implémenter complètement, il faudrait :
# 1. Créer des fixtures avec des mini-datasets
# 2. Utiliser des modèles pré-entraînés ou mock objects
# 3. Ajouter des tests d'intégration avec de vraies images
