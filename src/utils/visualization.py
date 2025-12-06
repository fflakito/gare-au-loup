"""Utilitaires de visualisation pour l'analyse des modèles."""

from typing import Optional

import matplotlib.pyplot as plt
from fastai.vision import ClassificationInterpretation, ImageDataBunch


def plot_data_samples(
    data: ImageDataBunch,
    rows: int = 3,
    figsize: tuple[int, int] = (12, 6),
) -> None:
    """
    Affiche un échantillon d'images du dataset.

    Args:
        data: ImageDataBunch à visualiser.
        rows: Nombre de lignes d'images à afficher.
        figsize: Taille de la figure matplotlib.
    """
    data.show_batch(rows=rows, figsize=figsize)
    plt.show()


def plot_top_losses(
    interp: ClassificationInterpretation,
    k: int = 9,
    figsize: tuple[int, int] = (15, 11),
) -> None:
    """
    Affiche les images avec les plus grandes erreurs de prédiction.

    Args:
        interp: Objet ClassificationInterpretation.
        k: Nombre d'images à afficher.
        figsize: Taille de la figure.
    """
    interp.plot_top_losses(k, figsize=figsize)
    plt.show()


def plot_confusion_matrix(
    interp: ClassificationInterpretation,
    figsize: tuple[int, int] = (8, 8),
    normalize: bool = False,
) -> None:
    """
    Affiche la matrice de confusion du modèle.

    Args:
        interp: Objet ClassificationInterpretation.
        figsize: Taille de la figure.
        normalize: Normaliser les valeurs (True pour pourcentages).
    """
    interp.plot_confusion_matrix(figsize=figsize, normalize=normalize)
    plt.show()


def plot_training_metrics(learner, figsize: tuple[int, int] = (10, 6)) -> None:
    """
    Affiche les métriques d'entraînement (loss, error rate).

    Args:
        learner: Learner FastAI avec historique d'entraînement.
        figsize: Taille de la figure.
    """
    learner.recorder.plot_losses()
    plt.show()
