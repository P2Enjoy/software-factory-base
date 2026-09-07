# Reproduire les supports

La lecture du cours, la projection, les PDF et le laboratoire ne nécessitent
aucune installation de ces outils de fabrication. Cette page s'adresse à la
personne qui modifie les sources et reconstruit une nouvelle édition.

## Sources et sorties

| Source | Résultat |
| --- | --- |
| programme.json et SYLLABUS.md | ordre, objectifs et durées des quinze modules |
| cours/*.md et compléments Markdown | cours, cahier, corrigés et guide d'animation |
| slides.json | texte, exemples, questions et notes des 80 slides |
| illustrations.json | 15 figures SVG éditables et équivalents textuels |
| styles.css et lecteur-slides.js | lecture, impression, projection et navigation |
| atelier/ | trois versions du laboratoire et contrats exécutables |

Les scripts n'installent pas les hooks, ne planifient aucun worker et n'effectuent
aucun commit ou push. Ils écrivent les fichiers générés sous `formation/exports/`,
les figures sous `formation/illustrations/` et le guide `ILLUSTRATIONS.md`.
Conserver les modifications de source avant régénération. Ne pas éditer les
exports comme source principale : la prochaine fabrication les remplacera.

## Installer les outils d'édition

Dans la racine du dépôt ou du ZIP décompressé : Python 3.11+, Node.js compatible
avec les dépendances verrouillées et un navigateur Chromium pour Playwright.
La fabrication est prévue sous Linux et reste reproductible avec les prérequis
décrits ici.
Ces commandes téléchargent des outils et demandent donc une connexion lors de
la préparation, contrairement à la lecture des supports déjà produits.

```bash
python3 -m venv .venv-formation
.venv-formation/bin/python -m pip install -r formation/outils/requirements.txt
npm ci --prefix formation/outils --ignore-scripts
node formation/outils/node_modules/playwright/cli.js install chromium
```

Sous Windows, créer l'environnement avec `py -3 -m venv .venv-formation`, puis
utiliser `.venv-formation\Scripts\python.exe`. Les commandes Node sont identiques.
Si l'environnement virtuel ou pip est absent de votre distribution, installer
ce composant par le canal habituel du poste ; ce n'est pas un défaut du cours.

Un Chromium déjà disponible peut être fourni avec la variable
`FORMATION_CHROMIUM`, contenant son chemin absolu. `FORMATION_PYTHON` choisit
l'interpréteur du laboratoire dans le contrôle navigateur ; à défaut, `python3`.
Ne pas copier les chemins d'une autre machine. Les dépendances d'édition ne
sont pas incluses dans le ZIP ; le laboratoire n'en dépend pas.

## Construire et vérifier

```bash
.venv-formation/bin/python formation/outils/construire.py
node formation/outils/exporter.cjs
node formation/outils/verifier-atelier.cjs
node formation/outils/verifier-processus.cjs
.venv-formation/bin/python formation/outils/emballer.py
.venv-formation/bin/python formation/outils/verifier.py
.venv-formation/bin/python formation/outils/emballer.py
.venv-formation/bin/python formation/outils/verifier.py --archive-only
```

La première archive permet de contrôler tous les liens de livraison. La seconde
intègre le rapport de vérification fraîchement produit. Le dernier contrôle
relit le manifeste de cette archive et compare les octets, sans réécrire le kit.
Toutes les commandes doivent réussir, sauf les quatre rouges du prototype
détectés et qualifiés par le contrôleur de laboratoire lui-même.

Le contrôle d'atelier crée un dossier temporaire neuf et des bases fictives,
lance seulement des serveurs `127.0.0.1` sur ports attribués par le système,
puis arrête ses propres processus. Il conserve les copies et le chemin dans
son rapport pour permettre le diagnostic. Les supprimer plus tard relève d'un
nettoyage explicite, pas d'une condition de réussite. Dans un environnement
restreint, l'ouverture d'un port local et Chromium peuvent demander une
autorisation du poste ; ne pas élargir l'écoute pour contourner ce refus.

## Examiner les résultats

Ouvrir les cinq HTML, les cinq PDF et le PowerPoint. Contrôler plusieurs pages
du cours, les longues tables, les schémas, les titres longs et la dernière slide.
Lire le cours à 390 px ; tester boutons, clavier et notes du diaporama. Examiner
les captures d'erreur, de liste et de réouverture du laboratoire. Les fichiers
`controle-rendu.json`, `controle-atelier.json` et `controle-edition.json`
indiquent les observations automatiques et leur portée, pas une certification.

Le PDF des slides est rendu depuis le HTML. Le PowerPoint contient des zones
de texte et des notes éditables ; les schémas y sont des PNG issus des SVG fournis.
Sa structure et son contenu sont contrôlés. Une vérification visuelle dans
PowerPoint ou LibreOffice est une qualification supplémentaire propre au logiciel
et aux polices de la machine de projection, non simulée par le rendu HTML.

## Dépendance d'édition signalée

L'audit npm signale `image-size`, dépendance transitive de
PptxGenJS, et son parent : deux alertes élevées liées à des boucles de parseurs
d'images ICNS/JXL/HEIF. Aucune version corrigée n'est annoncée dans les avis
[ICNS](https://github.com/advisories/GHSA-w3rx-r6r6-pgpr) et
[JXL/HEIF](https://github.com/advisories/GHSA-5p2g-fcmc-qvqq) consultés.

La fabrication de cette édition utilise uniquement ses propres PNG produits
par Chromium à partir des schémas locaux, sans import d'image fournie par un
tiers ni endpoint de téléversement. Le paquet vulnérable est présent dans les
dépendances de développement de l'édition, pas dans le laboratoire ni dans les
HTML/PDF lus par les participants. Ne pas transformer ce générateur en service
d'import d'images non fiables. Réexaminer l'avis avant une nouvelle publication ;
ne pas lancer `npm audit fix --force`, qui propose ici un retour majeur ancien
et ne constitue pas une qualification de compatibilité.

## Distribution et maintenance

Le ZIP conserve `formation/` et les sources du socle nécessaires à sa lecture.
Il n'inclut ni `.git`, ni environnement virtuel, ni `node_modules`, ni base
SQLite. Ouvrir `formation/README.md` ou `formation/exports/cours.html` après
décompression. Le manifeste SHA-256 permet de constater une modification des
fichiers ; ce n'est ni une signature d'auteur ni une preuve de qualité.

La remise conserve les changements dans le working tree, sans commit ni push
automatique. Sur le poste de fabrication, des exclusions Git locales concernent
notamment SPECIFICATION.md, DECISIONS.md et les BACKLOG/DAT du laboratoire.
Ils sont bien présents dans le ZIP. Avant un futur commit de publication,
contrôler explicitement leur inclusion : un simple ajout des fichiers visibles
dans `git status` ne suffit pas à garantir un clone autonome. Les exclusions
locales du responsable n'ont pas été modifiées par cette tâche.

Avant de modifier le programme, conserver l'ordre des quinze modules validés.
Avant d'annoncer une nouvelle réussite, rejouer les preuves sur le nouvel état,
mettre à jour VERIFICATION.md et reconstruire le kit. La recherche antérieure
sera confrontée au contenu lors de la révision éditoriale ultérieure, sans lui
attribuer aujourd'hui des conclusions inconnues.
