"""Script d'entraînement du modèle de classification."""

import argparse
from pathlib import Path

from data.dataset import create_databunch
from models.classifier import AnimalClassifier
from utils.visualization import plot_confusion_matrix, plot_data_samples, plot_top_losses


def train_model(
    data_path: str,
    model_name: str = "weights",
    epochs: int = 2,
    valid_pct: float = 0.2,
    image_size: int = 224,
    batch_size: int = 64,
    show_samples: bool = True,
) -> None:
    """
    Entraîne le modèle de classification.

    Args:
        data_path: Chemin vers le dossier de données.
        model_name: Nom du modèle à sauvegarder.
        epochs: Nombre d'époques d'entraînement.
        valid_pct: Pourcentage de validation.
        image_size: Taille des images.
        batch_size: Taille des batchs.
        show_samples: Afficher des échantillons de données.
    """
    print(f"📊 Chargement des données depuis {data_path}...")
    data = create_databunch(
        data_path=data_path,
        valid_pct=valid_pct,
        image_size=image_size,
        batch_size=batch_size,
    )

    print(f"✅ Données chargées : {len(data.train_ds)} train, {len(data.valid_ds)} valid")
    print(f"🏷️  Classes : {data.classes}")

    if show_samples:
        print("\n📸 Échantillons de données :")
        plot_data_samples(data, rows=3)

    print(f"\n🤖 Création du modèle...")
    classifier = AnimalClassifier(data)

    print(f"🚀 Entraînement pour {epochs} époques...")
    classifier.train(epochs=epochs)

    print(f"\n💾 Sauvegarde du modèle : {model_name}")
    classifier.save(model_name)

    print("\n📈 Analyse des résultats...")
    interp = classifier.get_interpretation()

    print("\n🔍 Top erreurs :")
    plot_top_losses(interp, k=9)

    print("\n📊 Matrice de confusion :")
    plot_confusion_matrix(interp, figsize=(6, 6))

    print(f"\n✅ Entraînement terminé ! Modèle sauvegardé : {model_name}")


def main():
    """Point d'entrée du script."""
    parser = argparse.ArgumentParser(description="Entraîne le modèle de classification")
    parser.add_argument(
        "--data-path",
        type=str,
        default="data",
        help="Chemin vers le dossier de données",
    )
    parser.add_argument(
        "--model-name",
        type=str,
        default="weights",
        help="Nom du modèle à sauvegarder",
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=2,
        help="Nombre d'époques d'entraînement",
    )
    parser.add_argument(
        "--valid-pct",
        type=float,
        default=0.2,
        help="Pourcentage de validation (0-1)",
    )
    parser.add_argument(
        "--image-size",
        type=int,
        default=224,
        help="Taille des images",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=64,
        help="Taille des batchs",
    )
    parser.add_argument(
        "--no-samples",
        action="store_true",
        help="Ne pas afficher d'échantillons",
    )

    args = parser.parse_args()

    train_model(
        data_path=args.data_path,
        model_name=args.model_name,
        epochs=args.epochs,
        valid_pct=args.valid_pct,
        image_size=args.image_size,
        batch_size=args.batch_size,
        show_samples=not args.no_samples,
    )


if __name__ == "__main__":
    main()
