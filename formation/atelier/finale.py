# @spec formation/SPECIFICATION.md#atelier | formation/CORRIGE_FINAL.md#raisonnement-et-implementation
"""Assembler le corrigé DEM-03 uniquement dans un laboratoire fraîchement créé."""
from pathlib import Path


def complete(target: Path):
    domain = target / "domain.py"
    domain.write_text(domain.read_text(encoding="utf-8") + '\n\ndef can_reopen(actor):\n    return actor["role"] == "responsable"\n', encoding="utf-8")
    app = target / "app.py"
    content = app.read_text(encoding="utf-8")
    changes = [
        ("from domain import can_close, validate_title", "from domain import can_close, can_reopen, validate_title"),
        ('self.path.endswith("/fermer")', 'self.path.endswith(("/fermer", "/rouvrir"))'),
        ('if not can_close(actor, row):', 'reopen = self.path.endswith("/rouvrir")\n                permitted = can_reopen(actor) if reopen else can_close(actor, row)\n                if not permitted:'),
        ('Ce profil ne peut pas clore cette demande.', 'Ce profil ne peut pas effectuer cette transition.'),
        ('db.execute("UPDATE requests SET status=\'ferme\' WHERE id=?", (identifier,))', 'state = "ouvert" if reopen else "ferme"\n                db.execute("UPDATE requests SET status=? WHERE id=?", (state, identifier))'),
        ('result["status"] = "ferme"', 'result["status"] = state'),
        ('                content += "</article>"', '''                if row["status"] == "ferme" and can_reopen(actor):
                    content += f'<form action="/demandes/{row["id"]}/rouvrir" method="post"><button>Rouvrir la demande {row["id"]}</button></form>'
                content += "</article>"'''),
    ]
    for old, new in changes:
        if content.count(old) != 1:
            raise RuntimeError(f"Le patron source a changé, substitution non sûre : {old}")
        content = content.replace(old, new)
    app.write_text(content, encoding="utf-8")
    (target / "test_finale.py").write_text(Path(__file__).with_name("test_finale.py.modele").read_text(encoding="utf-8"), encoding="utf-8")
    readme = target / "README.md"
    readme.write_text(readme.read_text(encoding="utf-8") + "\n## DEM-03 — Réouverture fournie\n\nPOST /api/demandes/3/rouvrir : Alice peut rouvrir, Bob/Eve sont refusés. Le bouton apparaît sur les demandes fermées pour Alice. Aucun changement de schéma. Rejouer les douze tests et le parcours réel avant de qualifier l'unité.\n", encoding="utf-8")
    backlog = target / "BACKLOG.md"
    backlog.write_text(backlog.read_text(encoding="utf-8").replace("- [ ] Permettre uniquement au responsable", "- [~] Code de référence fourni, preuves à rejouer : permettre uniquement au responsable").replace("elle n'est pas livrée au départ", "son corrigé est fourni dans cette copie finale"), encoding="utf-8")
