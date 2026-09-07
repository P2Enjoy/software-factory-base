# @spec formation/SPECIFICATION.md#atelier
"""Règles corrigées du laboratoire pédagogique."""


def validate_title(value):
    if not isinstance(value, str):
        raise ValueError("Le titre doit être du texte.")
    title = value.strip()
    if not 3 <= len(title) <= 80:
        raise ValueError("Le titre doit contenir entre 3 et 80 caractères.")
    return title


def can_close(actor, request):
    return actor["role"] == "responsable" or (
        actor["role"] == "contributeur" and actor["id"] == request["owner"]
    )
