"""Modèles de classification d'images basés sur FastAI."""

from pathlib import Path
from typing import Optional

from fastai.vision import (
    ClassificationInterpretation,
    ImageDataBunch,
    cnn_learner,
    error_rate,
    load_learner,
    models,
)


class AnimalClassifier:
    """Classificateur d'images pour identifier loups, ours et autres animaux."""

    def __init__(
        self,
        data: ImageDataBunch,
        architecture=models.resnet18,
        pretrained: bool = True,
    ):
        """
        Initialise le classificateur.

        Args:
            data: ImageDataBunch contenant les données d'entraînement.
            architecture: Architecture du modèle (par défaut ResNet18).
            pretrained: Utiliser les poids pré-entraînés sur ImageNet.
        """
        self.data = data
        self.learner = cnn_learner(
            data,
            architecture,
            metrics=error_rate,
            pretrained=pretrained,
        )

    def train(
        self,
        epochs: int = 2,
        learning_rate: Optional[float] = None,
    ) -> None:
        """
        Entraîne le modèle.

        Args:
            epochs: Nombre d'époques d'entraînement.
            learning_rate: Taux d'apprentissage (None = auto).
        """
        if learning_rate is None:
            self.learner.fit_one_cycle(epochs)
        else:
            self.learner.fit_one_cycle(epochs, max_lr=learning_rate)

    def save(self, name: str = "weights") -> None:
        """
        Sauvegarde les poids du modèle.

        Args:
            name: Nom du fichier de sauvegarde (sans extension).
        """
        self.learner.save(name)

    def load(self, name: str = "weights") -> None:
        """
        Charge les poids du modèle.

        Args:
            name: Nom du fichier à charger (sans extension).
        """
        self.learner.load(name)

    def get_interpretation(self) -> ClassificationInterpretation:
        """
        Récupère l'objet d'interprétation pour analyser les résultats.

        Returns:
            ClassificationInterpretation pour visualisations et analyses.
        """
        return ClassificationInterpretation.from_learner(self.learner)

    def predict(self, image_path: str | Path) -> tuple[str, int, list[float]]:
        """
        Prédit la classe d'une image.

        Args:
            image_path: Chemin vers l'image à classifier.

        Returns:
            Tuple (classe_prédite, index_classe, probabilités).
        """
        from fastai.vision import open_image

        img = open_image(image_path)
        pred_class, pred_idx, outputs = self.learner.predict(img)
        return str(pred_class), int(pred_idx), outputs.tolist()


def load_trained_model(model_path: str | Path) -> AnimalClassifier:
    """
    Charge un modèle déjà entraîné depuis un fichier .pkl.

    Args:
        model_path: Chemin vers le fichier .pkl du modèle.

    Returns:
        Instance d'AnimalClassifier avec le modèle chargé.
    """
    learner = load_learner(Path(model_path).parent, Path(model_path).name)
    classifier = AnimalClassifier.__new__(AnimalClassifier)
    classifier.learner = learner
    classifier.data = learner.data
    return classifier
