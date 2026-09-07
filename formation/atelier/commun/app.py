#!/usr/bin/env python3
# @spec formation/SPECIFICATION.md#atelier | BACKLOG.md#lab-00 | DAT.md#flux
"""Laboratoire local uniquement ; identités simulées, sans compte réel."""
import argparse
import html
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
import secrets
import sqlite3
from urllib.parse import parse_qs
from domain import can_close, validate_title

PROFILES = {
    "alice": {"id": "alice", "name": "Alice", "role": "responsable"},
    "bob": {"id": "bob", "name": "Bob", "role": "contributeur"},
    "eve": {"id": "eve", "name": "Eve", "role": "lectrice"},
}
SEED = [(1, "Préparer la salle", "alice", "ouvert"),
        (2, "Vérifier le vidéoprojecteur", "bob", "ouvert"),
        (3, "Ranger les câbles", "bob", "ferme")]


def initialize(path):
    new = not path.exists()
    with sqlite3.connect(path) as db:
        if new:
            db.execute("CREATE TABLE requests (id INTEGER PRIMARY KEY, title TEXT NOT NULL, owner TEXT NOT NULL, status TEXT NOT NULL CHECK(status IN ('ouvert','ferme')))")
            db.executemany("INSERT INTO requests VALUES(?,?,?,?)", SEED)
        else:
            db.execute("SELECT id,title,owner,status FROM requests LIMIT 1")


class Server(HTTPServer):
    def __init__(self, address, path):
        if address[0] != "127.0.0.1":
            raise ValueError("Ce laboratoire écoute uniquement sur 127.0.0.1.")
        initialize(path)
        self.db_path = path
        self.sessions = {}
        super().__init__(address, Handler)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def actor(self):
        try:
            cookie = SimpleCookie(self.headers.get("Cookie", ""))
            sid = cookie.get("atelier_session")
            return PROFILES.get(self.server.sessions.get(sid.value if sid else ""))
        except Exception:
            return None

    def send(self, status, body, mime="text/html; charset=utf-8", headers=None):
        raw = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'self'; frame-ancestors 'none'; form-action 'self'")
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(raw)

    def page(self, title, content, status=200):
        self.send(status, '<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                  '<link rel="icon" href="data:,"><link rel="stylesheet" href="/style.css">'
                  f'<title>{html.escape(title)} · Bureau des demandes</title><a class="skip" href="#contenu">Aller au contenu</a>'
                  '<header><strong>Bureau des demandes</strong><nav aria-label="Navigation"><a href="/demandes">Demandes</a><a href="/">Changer de profil</a></nav></header>'
                  f'<main id="contenu"><h1>{html.escape(title)}</h1>{content}</main></html>')

    def fail(self, status, message, value=""):
        if self.path.startswith("/api/"):
            self.send(status, json.dumps({"error": message}), "application/json")
        elif self.path == "/nouvelle":
            self.new_form(message, value, status)
        else:
            self.page("Action refusée", f'<p class="error" role="alert">{html.escape(message)}</p><a href="/demandes">Retour aux demandes</a>', status)

    def rows(self):
        with sqlite3.connect(self.server.db_path) as db:
            db.row_factory = sqlite3.Row
            return [dict(row) for row in db.execute("SELECT * FROM requests ORDER BY id")]

    def new_form(self, error="", value="", status=200):
        alert = f'<p id="erreur" class="error" role="alert">{html.escape(error)}</p>' if error else ""
        self.page("Nouvelle demande", alert + '<form method="post" action="/nouvelle"><label for="title">Titre de la demande</label>'
                  f'<input id="title" name="title" value="{html.escape(value, quote=True)}" aria-describedby="aide{" erreur" if error else ""}">'
                  '<p id="aide">De 3 à 80 caractères après suppression des espaces aux extrémités.</p><button>Créer la demande</button></form>', status)

    def do_GET(self):
        if self.path == "/style.css":
            self.send(200, Path(__file__).with_name("style.css").read_text(encoding="utf-8"), "text/css")
            return
        if self.path == "/":
            self.page("Choisir un profil de démonstration", '<p class="notice">Identités simulées pour cet atelier local. Aucune donnée réelle.</p>'
                      '<form action="/session" method="post"><label for="profil">Profil</label><select name="profil" id="profil">'
                      '<option value="alice">Alice — responsable</option><option value="bob">Bob — contributeur</option><option value="eve">Eve — lectrice</option>'
                      '</select><button>Entrer</button></form>')
            return
        actor = self.actor()
        if not actor:
            self.fail(401, "Choisissez un profil depuis l'accueil.")
            return
        if self.path == "/api/demandes":
            self.send(200, json.dumps(self.rows(), ensure_ascii=False), "application/json")
        elif self.path == "/nouvelle":
            if actor["role"] == "lectrice":
                self.fail(403, "Ce profil ne peut pas créer de demande.")
            else:
                self.new_form()
        elif self.path == "/demandes":
            content = f'<p>Profil : {actor["name"]} · {actor["role"]}</p>'
            if actor["role"] != "lectrice":
                content += '<a class="button" href="/nouvelle">Nouvelle demande</a>'
            rows = self.rows()
            if not rows:
                content += "<p>Aucune demande.</p>"
            for row in rows:
                label = "Ouverte" if row["status"] == "ouvert" else "Fermée"
                content += f'<article aria-label="Demande {row["id"]}"><h2>{html.escape(row["title"]) or "(Titre vide)"}</h2><p>Demande {row["id"]} · {PROFILES[row["owner"]]["name"]} · <span class="status">{label}</span></p>'
                if row["status"] == "ouvert" and can_close(actor, row):
                    content += f'<form action="/demandes/{row["id"]}/fermer" method="post"><button>Clore la demande {row["id"]}</button></form>'
                content += "</article>"
            self.page("Demandes", content)
        else:
            self.fail(404, "Page introuvable.")

    def do_POST(self):
        origin = self.headers.get("Origin")
        if origin and origin != f"http://127.0.0.1:{self.server.server_port}":
            self.fail(403, "Origine refusée.")
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 <= length <= 8192:
                raise ValueError("Corps trop volumineux.")
            raw = self.rfile.read(length).decode("utf-8")
            data = json.loads(raw or "{}") if self.path.startswith("/api/") else {k: v[0] for k,v in parse_qs(raw, keep_blank_values=True).items()}
            if not isinstance(data, dict):
                raise ValueError("Objet attendu.")
        except (ValueError, UnicodeError):
            self.fail(400, "Requête invalide.")
            return
        if self.path == "/session":
            if data.get("profil") not in PROFILES:
                self.fail(400, "Profil inconnu.")
                return
            old = SimpleCookie(self.headers.get("Cookie", "")).get("atelier_session")
            if old:
                self.server.sessions.pop(old.value, None)
            sid = secrets.token_urlsafe(24)
            self.server.sessions[sid] = data["profil"]
            self.send(303, "", headers={"Location": "/demandes", "Set-Cookie": f"atelier_session={sid}; HttpOnly; SameSite=Strict; Path=/"})
            return
        actor = self.actor()
        if not actor:
            self.fail(401, "Choisissez un profil depuis l'accueil.")
            return
        if self.path in ("/api/demandes", "/nouvelle"):
            if actor["role"] == "lectrice":
                self.fail(403, "Ce profil ne peut pas créer de demande.")
                return
            try:
                title = validate_title(data.get("title"))
            except ValueError as exc:
                self.fail(400, str(exc), data.get("title") if isinstance(data.get("title"), str) else "")
                return
            with sqlite3.connect(self.server.db_path) as db:
                cursor = db.execute("INSERT INTO requests(title,owner,status) VALUES(?,?,'ouvert')", (title, actor["id"]))
                result = {"id": cursor.lastrowid, "title": title, "owner": actor["id"], "status": "ouvert"}
        elif self.path.endswith("/fermer") and self.path.startswith(("/api/demandes/", "/demandes/")):
            try:
                identifier = int(self.path.split("/")[-2])
            except ValueError:
                self.fail(404, "Demande introuvable.")
                return
            with sqlite3.connect(self.server.db_path) as db:
                db.row_factory = sqlite3.Row
                row = db.execute("SELECT * FROM requests WHERE id=?", (identifier,)).fetchone()
                if row is None:
                    self.fail(404, "Demande introuvable.")
                    return
                if not can_close(actor, row):
                    self.fail(403, "Ce profil ne peut pas clore cette demande.")
                    return
                db.execute("UPDATE requests SET status='ferme' WHERE id=?", (identifier,))
                result = dict(row)
                result["status"] = "ferme"
        else:
            self.fail(404, "Action introuvable.")
            return
        if self.path.startswith("/api/"):
            self.send(201 if self.path == "/api/demandes" else 200, json.dumps(result, ensure_ascii=False), "application/json")
        else:
            self.send(303, "", headers={"Location": "/demandes"})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--db", type=Path, default=Path("atelier.sqlite3"))
    args = parser.parse_args()
    with Server(("127.0.0.1", args.port), args.db) as server:
        print(f"Atelier local : http://127.0.0.1:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Atelier arrêté ; données conservées.")
