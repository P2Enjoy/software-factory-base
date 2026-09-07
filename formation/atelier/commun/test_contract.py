# @spec formation/SPECIFICATION.md#atelier | BACKLOG.md#dem-01 | BACKLOG.md#dem-02 | DAT.md#contrats
# @verifies formation/SPECIFICATION.md#atelier | BACKLOG.md#dem-01 | BACKLOG.md#dem-02
import http.client
import json
from pathlib import Path
import tempfile
import threading
import unittest
from app import PROFILES, Server
from domain import can_close, validate_title


class DomainContract(unittest.TestCase):
    def test_title_bounds_and_normalization(self):
        self.assertEqual(validate_title("  Bonjour  "), "Bonjour")
        for title in ("abc", "a" * 80):
            self.assertEqual(validate_title(title), title)
        for title in (None, 42, "", "   ", "ab", "a" * 81):
            with self.assertRaises(ValueError, msg=repr(title)):
                validate_title(title)

    def test_role_and_ownership_matrix(self):
        for name, owner, allowed in (("alice", "bob", True), ("bob", "bob", True),
                                     ("bob", "alice", False), ("eve", "eve", False)):
            self.assertEqual(can_close(PROFILES[name], {"owner": owner}), allowed, (name, owner))


class ApiContract(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.server = Server(("127.0.0.1", 0), Path(self.tmp.name) / "test.sqlite3")
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.thread.join()
        self.server.server_close()
        self.tmp.cleanup()

    def request(self, method, path, body=None, cookie=None, form=False):
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=5)
        headers = {"Content-Type": "application/x-www-form-urlencoded" if form else "application/json"}
        if cookie:
            headers["Cookie"] = cookie
        payload = body if form else json.dumps(body or {})
        connection.request(method, path, payload if method == "POST" else None, headers)
        response = connection.getresponse()
        result = response.status, dict(response.getheaders()), response.read().decode()
        connection.close()
        return result

    def login(self, name):
        status, headers, _ = self.request("POST", "/session", f"profil={name}", form=True)
        self.assertEqual(status, 303)
        return headers["Set-Cookie"].split(";")[0]

    def test_no_session_and_reader_cannot_write(self):
        self.assertEqual(self.request("GET", "/api/demandes")[0], 401)
        eve = self.login("eve")
        self.assertEqual(self.request("POST", "/api/demandes", {"title": "Bonjour"}, eve)[0], 403)
        self.assertEqual(self.request("POST", "/api/demandes/2/fermer", {}, eve)[0], 403)

    def test_creation_is_persisted_and_owned_by_actor(self):
        bob = self.login("bob")
        status, _, raw = self.request("POST", "/api/demandes", {"title": "  Installer le réseau  ", "owner": "alice"}, bob)
        self.assertEqual(status, 201)
        self.assertEqual(json.loads(raw)["owner"], "bob")
        rows = json.loads(self.request("GET", "/api/demandes", cookie=bob)[2])
        self.assertEqual(len(rows), 4)
        self.assertEqual(rows[-1]["title"], "Installer le réseau")

    def test_repeated_closure_and_missing_request(self):
        bob = self.login("bob")
        for _ in range(2):
            self.assertEqual(self.request("POST", "/api/demandes/2/fermer", {}, bob)[0], 200)
        self.assertEqual(self.request("POST", "/api/demandes/999/fermer", {}, bob)[0], 404)
        rows = json.loads(self.request("GET", "/api/demandes", cookie=bob)[2])
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[1]["status"], "ferme")

    def test_invalid_title_is_refused_without_creation(self):
        bob = self.login("bob")
        # Le test unitaire du starter expose le défaut. Ce test le prouve via HTTP.
        status = self.request("POST", "/api/demandes", {"title": "   "}, bob)[0]
        self.assertEqual(status, 400)
        self.assertEqual(len(json.loads(self.request("GET", "/api/demandes", cookie=bob)[2])), 3)

    def test_foreign_request_refused_without_mutation(self):
        bob = self.login("bob")
        self.assertEqual(self.request("POST", "/api/demandes/1/fermer", {}, bob)[0], 403)
        rows = json.loads(self.request("GET", "/api/demandes", cookie=bob)[2])
        self.assertEqual(rows[0]["status"], "ouvert")


if __name__ == "__main__":
    unittest.main()
