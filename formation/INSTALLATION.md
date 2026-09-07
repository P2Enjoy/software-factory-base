# Préparer son poste et son laboratoire

## Matériel nécessaire

Un ordinateur avec éditeur, terminal, navigateur, Git et Python 3.11 ou plus.
Votre agent de code doit déjà fonctionner : aucune souscription nouvelle n'est
requise par le cours. Son accès peut être payant selon votre offre ; utilisez
votre accès existant et ses limites. Le laboratoire et les supports fonctionnent
sans appel à un modèle ; sans agent disponible, les corrigés permettent de
réaliser les gestes manuellement et de reprendre l'assistance plus tard.

Les commandes suivantes sont à saisir dans le terminal, pas dans le dialogue
de l'agent. Dans le dossier qui contient le dépôt des supports :

```bash
python3 --version
git --version
python3 formation/atelier/preparer.py ../bureau-demandes
```

Sous Windows, si `python3` n'existe pas, utiliser `py -3` à chaque occurrence.
Sous macOS ou Linux, conserver `python3`. Le chemin `../bureau-demandes` crée
un dossier voisin du socle : vous y travaillerez sans altérer les supports.
Si ce dossier existe, choisir un autre nom. Le préparateur refuse de remplacer
un dossier existant. Dans un ZIP décompressé, ouvrir un terminal à sa racine,
puis utiliser la même commande : le kit conserve le dossier `formation/`.

## Premier repère Git, avant les exercices

Dans le dossier neuf `bureau-demandes`, initialiser une mémoire locale. Aucun
dépôt distant ni publication n'est nécessaire. Ces quelques gestes seront
expliqués en profondeur au module 11 ; ils donnent dès maintenant une référence
réelle aux observations et à la passation du module 4.

```bash
git init
git config user.name
git config user.email
```

Si l'identité affichée est absente ou incorrecte, définir votre propre identité
localement avec `git config user.name "Votre nom"` et
`git config user.email "votre-adresse"`. Remplacer les exemples avant exécution.
Ne pas copier l'identité de l'auteur du cours. Puis :

```bash
git status --short
git add .gitignore README.md DAT.md BACKLOG.md SCENARIO_VISUEL.md app.py domain.py style.css test_contract.py
git diff --cached --stat
git diff --cached
git commit -m "Conserver le laboratoire de départ et ses défauts connus"
git rev-parse --short HEAD
```

Garder l'identifiant affiché. Il désigne le code de départ, pas une version
corrigée. Un commit conserve aussi un défaut connu. Les nouvelles notes non
committées doivent être signalées comme telles dans une passation. Les fichiers
SQLite et les caches restent ignorés ; ne pas ajouter de secret. Avant et après
une mission, `git status --short` et `git diff` aident à repérer les changements.

## Constater le comportement de départ

Ouvrir ce nouveau dossier dans l'éditeur et le terminal, puis :

```bash
python3 -m unittest -v
python3 app.py --port 8765
```

La version de départ comporte deux défauts, détectés par quatre tests rouges :
un unitaire et un test API pour chaque défaut. Les trois autres tests passent.
Ces résultats vous donnent une observation initiale. Un message d'import ou
une impossibilité de démarrer n'est pas le rouge pédagogique attendu.

Le terminal affiche une adresse locale. Ouvrir http://127.0.0.1:8765 dans le
navigateur. Choisir Bob et entrer. Trois demandes s'affichent. Garder le terminal
ouvert pendant la navigation. Ctrl+C arrête le serveur et conserve la base.

## Démarrer son agent dans le bon dossier

Ouvrez votre agent dans `bureau-demandes`, puis donnez cette première mission :

> Lis README.md, BACKLOG.md et DAT.md. Explore sans modifier les fichiers.
> Indique les commandes documentées, le trajet d'une création de demande et
> les deux défauts annoncés. Cite les fonctions que tu as lues. N'utilise aucun
> secret ou service externe. Attends une mission d'implémentation avant d'éditer.

Vérifiez le dossier que l'outil affiche. Une réponse de l'agent ne suffit pas
à prouver sa configuration : examinez ses actions, les chemins et le diff.
Les fichiers d'instructions Codex et Claude Code sont détaillés au module 5 ;
les versions et options d'interface évoluent, leurs sources sont dans SOURCES.

## Problème de poste

| Symptôme | Vérification | Suite |
| --- | --- | --- |
| Commande Python inconnue | Essayer `py -3 --version` sous Windows | Installer Python via le canal habituel de votre organisation si absent |
| `No module named sqlite3` | Vérifier la distribution Python | Employer une installation Python avec SQLite ; ne pas modifier les tests |
| Port déjà utilisé | Relancer avec `--port 8766` | Ouvrir exactement cette nouvelle adresse |
| Page inaccessible | Lire le terminal du serveur | Le serveur doit rester actif ; vérifier l'adresse et le port |
| `no such table: requests` | Le fichier base choisi est-il le bon ? | Choisir un nom de base neuf ; conserver l'ancien pour diagnostic |
| Aucun test découvert | Vérifier que test_contract.py est dans le dossier courant | Ouvrir le terminal dans le laboratoire |
| Agent indisponible | Lire les explications et les exemples | Avancer manuellement puis reprendre les missions d'agent |

## Référence et reprise

Pour comparer sans écraser votre travail :

```bash
python3 formation/atelier/preparer.py ../bureau-reference --version reference
```

Dans le ZIP, conserver le préfixe `formation/`. La référence contient les deux
corrections, pas la réouverture de l'évaluation finale. Son README et son backlog
restent des fiches à qualifier avec vos propres exécutions : la présence du code
ne certifie pas que vous l'avez testé.

Consignez dans vos preuves : OS, version Python, navigateur, version de l'agent,
commandes et résultats. Le [bilan de cette édition](VERIFICATION.md) distingue
les environnements réellement testés des consignes proposées pour les autres.
