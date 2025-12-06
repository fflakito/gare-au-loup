"""Script de prédiction avec un modèle entraîné."""

import argparse
from pathlib import Path

from models.classifier import load_trained_model


def predict_image(model_path: str, image_path: str, show_probs: bool = True) -> None:
    """
    Prédit la classe d'une image.

    Args:
        model_path: Chemin vers le modèle (.pkl).
        image_path: Chemin vers l'image à classifier.
        show_probs: Afficher les probabilités de chaque classe.
    """
    print(f"📂 Chargement du modèle : {model_path}")
    classifier = load_trained_model(model_path)

    print(f"🖼️  Analyse de l'image : {image_path}")
    pred_class, pred_idx, probs = classifier.predict(image_path)

    print(f"\n🎯 Prédiction : {pred_class}")

    if show_probs:
        print("\n📊 Probabilités :")
        classes = classifier.data.classes
        for class_name, prob in zip(classes, probs):
            print(f"  {class_name:10s} : {prob:6.2%}")


def predict_batch(model_path: str, image_dir: str) -> None:
    """
    Prédit les classes pour toutes les images d'un dossier.

    Args:
        model_path: Chemin vers le modèle (.pkl).
        image_dir: Dossier contenant les images.
    """
    print(f"📂 Chargement du modèle : {model_path}")
    classifier = load_trained_model(model_path)

    image_paths = list(Path(image_dir).glob("*.jpg")) + list(Path(image_dir).glob("*.png"))
    print(f"\n🖼️  {len(image_paths)} images trouvées\n")

    results = []
    for img_path in image_paths:
        pred_class, pred_idx, probs = classifier.predict(img_path)
        results.append((img_path.name, pred_class, max(probs)))
        print(f"  {img_path.name:40s} → {pred_class:10s} ({max(probs):6.2%})")

    print(f"\n✅ Prédictions terminées pour {len(results)} images")


def main():
    """Point d'entrée du script."""
    parser = argparse.ArgumentParser(description="Prédit la classe d'images")
    parser.add_argument(
        "--model-path",
        type=str,
        default="data/models/export.pkl",
        help="Chemin vers le modèle (.pkl)",
    )
    parser.add_argument(
        "--image",
        type=str,
        help="Chemin vers une image à classifier",
    )
    parser.add_argument(
        "--image-dir",
        type=str,
        help="Dossier contenant plusieurs images à classifier",
    )
    parser.add_argument(
        "--no-probs",
        action="store_true",
        help="Ne pas afficher les probabilités",
    )

    args = parser.parse_args()

    if args.image and args.image_dir:
        print("❌ Erreur : spécifiez soit --image soit --image-dir, pas les deux")
        return

    if not args.image and not args.image_dir:
        print("❌ Erreur : spécifiez --image ou --image-dir")
        return

    if args.image:
        predict_image(args.model_path, args.image, show_probs=not args.no_probs)
    elif args.image_dir:
        predict_batch(args.model_path, args.image_dir)


if __name__ == "__main__":
    main()
