#!/usr/bin/env python3
# @spec formation/SPECIFICATION.md#atelier
"""Créer un laboratoire neuf sans modifier le dépôt des supports."""
import argparse
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("destination", type=Path)
parser.add_argument("--version", choices=("depart", "reference", "finale"), default="depart")
args = parser.parse_args()
source = Path(__file__).resolve().parent
target = args.destination.expanduser().resolve()
if target.exists():
    parser.error("La destination existe déjà. Choisissez un nouveau dossier ; rien n'a été remplacé.")
target.mkdir(parents=True)
for path in (source / "commun").iterdir():
    if path.is_file():
        shutil.copy2(path, target / path.name)
shutil.copy2(source / ("reference" if args.version == "finale" else args.version) / "domain.py", target / "domain.py")
if args.version == "finale":
    from finale import complete
    complete(target)
print(f"Laboratoire {args.version} créé : {target}")
print("Ouvrez ce dossier dans votre éditeur, puis suivez son README.md.")
