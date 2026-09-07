# @spec formation/SPECIFICATION.md#atelier
"""Prototype de formation : deux défauts intentionnels, jamais pour la production."""


def validate_title(value):
    """Défaut à reproduire : la longueur minimale n'est pas contrôlée."""
    if not isinstance(value, str):
        raise ValueError("Le titre doit être du texte.")
    title = value.strip()
    if len(title) > 80:
        raise ValueError("Le titre doit contenir entre 3 et 80 caractères.")
    return title


def can_close(actor, request):
    """Défaut à reproduire : la propriété de la demande n'est pas contrôlée."""
    return actor["role"] in ("responsable", "contributeur")
