"""Tests pour le module data.dataset."""

import pytest
from pathlib import Path


class TestDataset:
    """Tests pour les fonctions de gestion des datasets."""

    def test_create_databunch_default_params(self, tmp_path):
        """Test de création d'un DataBunch avec paramètres par défaut."""
        # Ce test nécessite des données réelles, donc on le skip pour l'instant
        pytest.skip("Nécessite un dataset complet pour fonctionner")

    def test_get_class_names(self):
        """Test de récupération des noms de classes."""
        pytest.skip("Nécessite un DataBunch pour fonctionner")


# Exemple de fixture pour créer un dataset de test
@pytest.fixture
def sample_data_dir(tmp_path):
    """Crée un répertoire de données de test."""
    data_dir = tmp_path / "data"
    train_dir = data_dir / "train"

    # Créer structure
    for class_name in ["loup", "ours", "autre"]:
        (train_dir / class_name).mkdir(parents=True)

    return data_dir
