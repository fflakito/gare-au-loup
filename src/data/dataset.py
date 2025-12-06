"""Gestion des datasets pour la classification d'images."""

from pathlib import Path
from typing import Optional, Tuple

from fastai.vision import ImageDataBunch, get_transforms, imagenet_stats


def create_databunch(
    data_path: str | Path,
    valid_pct: float = 0.2,
    image_size: int = 224,
    batch_size: int = 64,
    do_flip: bool = True,
) -> ImageDataBunch:
    """
    Crée un ImageDataBunch pour l'entraînement.

    Args:
        data_path: Chemin vers le dossier contenant les données (train/valid).
        valid_pct: Pourcentage de données à utiliser pour la validation.
        image_size: Taille des images (redimensionnement carré).
        batch_size: Taille des batchs.
        do_flip: Appliquer le flip horizontal pour l'augmentation.

    Returns:
        ImageDataBunch configuré et normalisé.
    """
    tfms = get_transforms(do_flip=do_flip)

    data = ImageDataBunch.from_folder(
        data_path,
        valid_pct=valid_pct,
        ds_tfms=tfms,
        size=image_size,
        bs=batch_size,
    )

    # Normalisation avec les stats d'ImageNet
    data.normalize(imagenet_stats)

    return data


def get_class_names(data: ImageDataBunch) -> list[str]:
    """
    Récupère les noms des classes depuis le DataBunch.

    Args:
        data: ImageDataBunch configuré.

    Returns:
        Liste des noms de classes.
    """
    return data.classes
