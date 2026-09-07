#!/usr/bin/env python3
# @spec formation/SPECIFICATION.md#edition
"""Assembler un kit local contrôlable, sans dépendance installée ni données privées."""
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
OUT = ROOT / 'exports'
ARCHIVE = OUT / 'formation-complete.zip'
MANIFEST = OUT / 'inventaire.json'
EXCLUDED_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', '.venv-formation'}
EXCLUDED_SUFFIXES = {'.pyc', '.sqlite3', '.sqlite', '.db', '.log'}

# Liste bornée de références pédagogiques ; aucune collecte générale de fichiers cachés.
baseline = ['README.md','LICENSE','AGENTS.md','CLAUDE.md','.gitignore',
            'docs/AUTOMATION.md','docs/DESIGN_SYSTEM.md','docs/DESIGN_SYSTEM_APP.md',
            'docs/CloudWorker.md','docs/.routine','.codex/config.toml']
files = [REPO / name for name in baseline]
for directory in ['.codex/agents','.githooks','scripts/git-hooks','tests/git-hooks']:
    files.extend(p for p in (REPO / directory).rglob('*') if p.is_file())
for p in ROOT.rglob('*'):
    if not p.is_file() or p in (ARCHIVE,MANIFEST):
        continue
    if EXCLUDED_DIRS.intersection(p.relative_to(ROOT).parts) or p.suffix in EXCLUDED_SUFFIXES:
        continue
    if p.name.startswith('.env'):
        continue
    files.append(p)
files = sorted(set(files))
inventory = {}
for p in files:
    if p.is_symlink() or not p.is_file():
        raise RuntimeError(f'Ressource manquante ou lien symbolique refusé : {p}')
    relative = p.relative_to(REPO).as_posix()
    data = p.read_bytes()
    inventory[relative] = {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
MANIFEST.write_text(json.dumps({'algorithm':'SHA-256','files':inventory},ensure_ascii=False,indent=2),encoding='utf-8')
with ZipFile(ARCHIVE,'w',ZIP_DEFLATED,compresslevel=9) as archive:
    for p in files + [MANIFEST]:
        archive.write(p,p.relative_to(REPO).as_posix())
print(json.dumps({'archive':str(ARCHIVE),'files':len(files)+1,'bytes':ARCHIVE.stat().st_size},ensure_ascii=False))
