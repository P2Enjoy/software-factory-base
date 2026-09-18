# Étude de révision des supports de formation

Étude réalisée le 18 septembre 2026 à partir des deux premières sessions
réellement animées avec le parcours « Coder avec un agent : les bases, la
méthode, puis l'usine » (mardi 8 septembre 2026, 2 h 47 ; mardi 15 septembre
2026, 4 h 10). Elle répond à la demande du responsable : extraire ce qui a été
enseigné lors de ces deux sessions, puis étudier comment réorganiser les supports
de `formation/` sans modifier la méthode ni ses implémentations.

Le guide d'animation prévoyait cette révision : « Après une première session
réelle, relever les durées observées, questions récurrentes et exercices qui
nécessitent trop d'aide » ([ANIMATION.md](ANIMATION.md), section Maintenance de
l'animation). Le bilan de l'édition précisait qu'aucune séance avec apprenants
n'avait encore eu lieu ([VERIFICATION.md](VERIFICATION.md), Limites explicites).
Les deux sessions de septembre 2026 sont donc le premier retour de terrain.

État du document : les sections 1 à 3 et 9 sont rédigées à partir du dépôt et
du kit. Les sections 4 à 8 (enseignement réel des sessions, écarts, options,
recommandation et plan) sont en cours de rédaction à partir des transcriptions
et seront ajoutées dans le commit suivant, avec le compte rendu `SESSIONS.md`.

## 1. Périmètre

Révisable dans cette étude : tout ce qui se trouve sous `formation/` (chapitres,
exercices, corrigés, quiz, fiches, glossaire, syllabus, guide d'animation,
évaluation, slides, illustrations, laboratoire, outils de fabrication, exports,
portail Pages) ainsi que le workflow `.github/workflows/pages.yml` qui publie ces
exports.

Hors périmètre, par instruction explicite du responsable : `CLAUDE.md`,
`docs/CloudWorker.md`, `docs/DESIGN_SYSTEM.md`, `AGENTS.md`, les rôles de
`.claude/agents/` et `.codex/agents/`, les garde-fous `scripts/git-hooks/` et
`.githooks/`, leur harnais `tests/git-hooks/`. La formation enseigne cette
méthode telle qu'elle est ; elle ne la modifie pas. Lorsqu'un écart entre la
méthode et les supports est constaté, ce sont les supports qui s'alignent.

L'étude produit une analyse et un plan. Elle ne réécrit pas encore les supports :
le plan de révision (section 8) sera exécuté unité par unité, chaque unité
emportant ses preuves et la régénération des exports concernés.

## 2. Sources

- Les notes et transcriptions Google Meet des deux sessions, conservées dans le
  Drive du responsable (dossiers « Meet Recordings » et « Google Meet / IA USINE
  DIGITALE (recurring) »). Elles contiennent des données personnelles des
  participants ; elles ne sont ni copiées ni citées nominativement dans le
  dépôt. Le compte rendu factuel de ce qui a été enseigné, anonymisé, est
  produit avec la section 4 dans le fichier `SESSIONS.md`.
- L'édition actuelle des supports : [SYLLABUS.md](SYLLABUS.md),
  [programme.json](programme.json), les quinze chapitres de `cours/`,
  [EXERCICES.md](EXERCICES.md), [CORRIGES.md](CORRIGES.md),
  [EVALUATION.md](EVALUATION.md), [ANIMATION.md](ANIMATION.md),
  [FICHES.md](FICHES.md), [GLOSSAIRE.md](GLOSSAIRE.md),
  [INSTALLATION.md](INSTALLATION.md), [slides.json](slides.json),
  [illustrations.json](illustrations.json), l'atelier `atelier/`, et les
  documents d'édition [SPECIFICATION.md](SPECIFICATION.md),
  [DECISIONS.md](DECISIONS.md), [PRODUCTION.md](PRODUCTION.md),
  [VERIFICATION.md](VERIFICATION.md), [SOURCES.md](SOURCES.md).
- Les outils de fabrication et de contrôle `outils/`, le portail
  `site/index.html` et le workflow Pages, lus pour établir les contraintes de
  la section 9.

## 3. État de l'édition actuelle

### 3.1 Ce que l'édition livre

Un parcours de quinze modules de 150 minutes et une évaluation finale de
270 minutes, soit 42 heures animées sur six journées, pour un public mixte qui
sait déjà lancer Codex ou Claude Code. Chaque module comprend une situation de
départ, des notions, un exemple commenté, deux exercices (un de 25 minutes, un de
45), trois questions de quiz et un point de sortie. Les onze premiers modules
posent les bases et les gestes d'ingénierie ; les quatre derniers introduisent
l'orchestration, les invariants automatisés, le worker et l'assemblage de la
software factory.

Le fil rouge est le laboratoire « Bureau des demandes » (Python, SQLite, un
navigateur) : deux défauts intentionnels DEM-01 (validation du titre) et DEM-02
(droits de clôture) sont corrigés au fil des modules 6 à 10, et l'évaluation
finale DEM-03 (réouverture d'une demande) exige une petite évolution complète,
prouvée et documentée.

Le kit comprend trente exercices, quarante-cinq questions de quiz corrigées,
quatre-vingts slides avec notes, quinze figures SVG, un guide d'animation minuté,
huit fiches réutilisables, un glossaire, et des exports hors ligne (HTML, PDF,
PowerPoint, ZIP) publiés sur GitHub Pages.

### 3.2 Décisions d'édition qui encadrent la révision

- Le responsable a validé l'ordre des quinze modules et écarté une condensation
  en huit modules ([DECISIONS.md](DECISIONS.md)). [PRODUCTION.md](PRODUCTION.md)
  et [ANIMATION.md](ANIMATION.md) demandent de conserver cet ordre lors des
  ajustements.
- Le cours est conçu pour être utilisable seul ; l'animation ajoute les
  démonstrations, le travail en binôme et le retour individuel
  ([SYLLABUS.md](SYLLABUS.md), section Autonomie et animation premium).
- Les supports restent indépendants des éditeurs d'outils : ils enseignent la
  méthode et renvoient aux sources officielles pour les détails d'interface,
  qui évoluent ([SOURCES.md](SOURCES.md)).
- La confrontation avec la publication de recherche antérieure est une étape
  éditoriale ultérieure, distincte de cette révision
  ([SPECIFICATION.md](SPECIFICATION.md), Périmètre éditorial).

### 3.3 Défauts de l'état livré constatés pendant l'étude

Ces constats ne dépendent pas des sessions ; ils ont été faits en lisant le clone
et le kit. Ils entrent dans le plan de révision lorsqu'ils concernent
`formation/`, et dans le registre `docs/INCONSISTENCY_REPORT.md` sinon.

1. `formation/atelier/commun/BACKLOG.md` et `formation/atelier/commun/DAT.md`
   sont absents du dépôt (jamais committés, sur aucune branche) alors qu'ils sont
   présents dans `exports/formation-complete.zip`, exigés par
   `outils/verifier.py` (ressources critiques du kit), lus par
   `atelier/finale.py` pour préparer la version finale, cités par
   [INSTALLATION.md](INSTALLATION.md), le README de l'atelier, les chapitres
   11 et 12, [FICHES.md](FICHES.md), et référencés par les en-têtes `@spec` et
   `@verifies` du laboratoire. Conséquence : une personne qui clone le dépôt
   (au lieu d'utiliser le ZIP) ne peut ni suivre la séquence Git d'installation,
   ni préparer la version finale ; la chaîne de vérification ne peut pas réussir
   depuis un clone.
2. `docs/AUTOMATION.md` est absent du dépôt et présent dans le ZIP ; `outils/emballer.py`
   le liste parmi les fichiers du socle à empaqueter et s'arrête s'il manque. Le
   kit ne peut donc pas être reconstruit depuis un clone. Ce fichier appartient à
   la méthode : il est hors périmètre de la révision et consigné au registre.
3. Les documents décrivent une correspondance « contrôlée » entre
   `programme.json` et [SYLLABUS.md](SYLLABUS.md) ; aucun outil ne la calcule.
   La cohérence entre `slides.json` et `programme.json` (figure, exercices et
   quiz par bloc de cinq slides), et entre [ANIMATION.md](ANIMATION.md) et
   `slides.json` (textes d'ouverture, questions et réponses recopiés, numéros de
   slides), n'est vérifiée par aucun script : elle est vraie par construction
   manuelle et se perdra à la première réorganisation si elle n'est pas outillée.
4. Quatorze exercices sur trente portent une mention « Durée : 25 min » ou
   « Durée : 45 min » ; la règle impair/pair énoncée en tête du cahier n'est pas
   contrôlée.
5. `outils/verifier.py` requiert `pdfinfo` et `pdftotext` (Poppler), absents de
   [PRODUCTION.md](PRODUCTION.md) et de `outils/requirements.txt`.
6. Les couvertures `illustrations/generated/*.png` sont des sources suivies par
   Git sans procédé de génération documenté dans `formation/`.
7. `site/index.html` est écrit à la main et hors de tout contrôle : ses libellés
   chiffrés (« Quinze chapitres, trente exercices », « quatre-vingts étapes ») et
   ses liens doivent être alignés manuellement à chaque changement de structure.

## 9. Contraintes de fabrication et de vérification

Cette section fixe ce qu'une réorganisation peut changer librement, ce qui exige
de modifier un outil ou un contrôle, et ce qui exige de régénérer les exports.
Les références de lignes correspondent à l'état du dépôt au 18 septembre 2026.

### 9.1 Source d'autorité de la structure

`programme.json` est la seule source lue par les outils : `module_minutes` (150),
`evaluation_minutes` (270) et une liste `modules` de quinze objets portant `id`,
`title`, `file` (chapitre dans `cours/`), `objective`, `deliverable`,
`exercises` (exactement deux identifiants) et `figure` (identifiant de
`illustrations.json`). `outils/construire.py` l'utilise pour l'ordre des chapitres
et le titre du cours (l. 20, 161 à 162) ; `outils/verifier.py` vérifie que les
identifiants valent 1 à 15 dans l'ordre (l. 62), que 15 × 150 + 270 = 2 520
(l. 63), que la concaténation des exercices vaut E01 à E30 (l. 69) et que chaque
chapitre contient « Objectif : », ses deux identifiants d'exercices et le nom de
sa figure (l. 71 à 74). `programme.json` ne contient ni quiz, ni journées, ni
phases internes, ni numéros de slides : ces éléments sont écrits à la main dans
[SYLLABUS.md](SYLLABUS.md), [ANIMATION.md](ANIMATION.md), `slides.json` et
chaque chapitre.

### 9.2 Invariants codés en dur

| Invariant | Où il est codé | Où il est répété en prose |
| --- | --- | --- |
| 15 modules, identifiants 1 à 15 dans l'ordre | `verifier.py` l. 62, 75, 79, 141 ; `construire.py` l. 162, 169 (« Module NN / 15 ») ; `exporter.cjs` l. 126 | `site/index.html` l. 56 ; README de la formation, SYLLABUS, SPECIFICATION, DECISIONS, PRODUCTION, ANIMATION, VERIFICATION, README racine, slide S01 |
| 30 exercices, deux par module, E01 à E30 en ordre dans EXERCICES.md et CORRIGES.md | `verifier.py` l. 66 à 69 ; `construire.py` l. 162 | `site/index.html` l. 56 ; README de la formation ; SYLLABUS ; `docs/DESIGN_SYSTEM_APP.md` |
| 45 quiz, trois par module, identifiants Q{n}.1 à Q{n}.3 couplés au numéro de module, réponses en table dans CORRIGES.md | `verifier.py` l. 73 à 77 | SYLLABUS ; ANIMATION (« les trois quiz du chapitre ») |
| 80 slides : 2 d'accueil (module 0), 5 par module (contenu avec visuel, figure, cas, contenu, contenu), 3 d'évaluation (module 16) ; six clés de notes non vides | `verifier.py` l. 78 à 79, 114, 122 à 123 ; `exporter.cjs` l. 50 à 53, 57, 65, 68 ; `construire.py` l. 92, 165, 193 | ANIMATION (« Slides a à b » par module, l. 6, 34, 454) ; `site/index.html` l. 62 ; `docs/DESIGN_SYSTEM_APP.md` ; VERIFICATION |
| 15 figures SVG, un fichier par entrée de `illustrations.json`, `kind` parmi flow, grid, split, rights, roles | `verifier.py` l. 80 ; `construire.py` l. 57 à 72, 86 | ILLUSTRATIONS.md (régénéré) ; VERIFICATION ; PRODUCTION |
| Durées 150 et 270 minutes, total 2 520 | `programme.json` l. 3 à 4 ; `verifier.py` l. 63 ; `construire.py` l. 92 (« 42 heures ») | chaque chapitre (« Durée animée : 150 min ») ; SYLLABUS ; ANIMATION (bornes 0–30, 30–55, 55–125, 125–150 répétées quinze fois) ; EVALUATION ; `slides.json` (cinq chaînes `minutage` par module et slides 78 à 80) ; SPECIFICATION ; README ; VERIFICATION ; DECISIONS |
| Noms des livres assemblés et des PDF | `construire.py` l. 162 à 165 ; `exporter.cjs` l. 19, 32 ; `verifier.py` l. 64 à 65, 109, 137 ; `emballer.py` l. 18 à 31 | README de la formation ; PRODUCTION ; `site/index.html` l. 53 à 92 |

### 9.3 Ce qui peut changer sans toucher aux outils

Sous réserve de régénérer les exports (section 9.5) :

- le texte des chapitres, des exercices, des corrigés, des fiches, du glossaire,
  du guide d'animation, des slides et de leurs notes, les nœuds et sous-titres
  des figures ;
- les titres, objectifs et livrables de `programme.json`, les titres des
  chapitres et les noms de leurs fichiers (via le champ `file` ; aucun outil
  n'impose le préfixe `NN-`, mais les ancres HTML des exports en dérivent) ;
- l'ordre des modules, à condition que les identifiants restent 1 à 15 dans
  l'ordre de la liste, que chaque chapitre déplacé emporte ses deux exercices,
  sa figure et ses trois quiz renumérotés, que le bloc de cinq slides suive, et
  que les renvois en prose d'un module à l'autre soient réécrits (ils existent
  dans les chapitres 1, 2, 3, 4, 7, 8, 9, 11, 13, 14 et 15, dans EXERCICES.md,
  CORRIGES.md, INSTALLATION.md, EVALUATION.md et ANIMATION.md) ;
- l'attribution d'une figure à un module, en alignant la chaîne `{figure}.svg`
  du chapitre et les champs `figure` et `visual` des cinq slides du bloc
  (`construire.py` l. 181 s'arrête si l'identifiant n'existe pas) ;
- le minutage réel d'une animation, tant que la durée nominale de 150 minutes
  par module reste celle des outils ; un scénario d'animation différent peut
  être documenté comme une répartition calendaire distincte, ce que
  [SYLLABUS.md](SYLLABUS.md) autorise déjà (« Une autre répartition calendaire
  peut conserver l'ordre, les durées et les points de reprise »).

### 9.4 Ce qui exige de modifier un outil ou un contrôle

- Changer le nombre de modules, d'exercices par module, de quiz par module, de
  slides par module ou de figures : toutes les lignes de la table 9.2, plus les
  phrases en prose qui les répètent.
- Changer les durées nominales : `programme.json`, `verifier.py` l. 63, les
  quinze chapitres, les cinq chaînes `minutage` de chaque bloc de slides, les
  bornes de chaque section de [ANIMATION.md](ANIMATION.md), [EVALUATION.md](EVALUATION.md).
- Renommer ou déplacer un fichier Markdown assemblé : listes de `construire.py`
  l. 162 à 165 et `exporter.cjs` l. 19, contrôles de `verifier.py` l. 50, 64 à
  65, 72, liens dans les documents de tête.
- Modifier un titre de section cité par une ancre `@spec` ou `@verifies` :
  « Edition », « Slides », « Verification », « Atelier » de
  [SPECIFICATION.md](SPECIFICATION.md) ; « Raisonnement et implémentation » et
  « Preuves de référence » de [CORRIGE_FINAL.md](CORRIGE_FINAL.md) ; « Consulter
  la formation depuis GitHub » du README de la formation ; « Composition » de
  `docs/DESIGN_SYSTEM_APP.md`. Les garde-fous du socle ne vérifient que la forme
  de ces marqueurs, pas l'existence de l'ancre ; la méthode exige leur cohérence.
- Ajouter un fichier `.py`, `.cjs`, `.js`, `.css`, `.html`, `.yml` ou `.toml` :
  en-tête `@spec chemin.md#ancre` dans les soixante premières lignes, et
  `@verifies` pour un fichier de test (`scripts/git-hooks/check-staged` l. 46 à
  71).
- Modifier l'atelier : `outils/verifier-atelier.cjs` attend sept tests dont
  exactement quatre échecs nommés au départ, sept réussites sur la référence et
  douze sur la finale (l. 52 à 54) ; `atelier/finale.py` applique des
  substitutions textuelles uniques dans `app.py` et `domain.py` (l. 11 à 26)
  qui échouent si le texte source change.

### 9.5 Ce qui exige de régénérer les exports

Toute modification de `programme.json`, `slides.json`, `illustrations.json`,
`styles.css`, `lecteur-slides.js`, d'un Markdown assemblé, des couvertures PNG ou
de l'atelier, et tout ajout d'un fichier sous `formation/` (le ZIP et son
inventaire embarquent tout `formation/` hors exclusions). La chaîne complète est
celle de [PRODUCTION.md](PRODUCTION.md) : `construire.py`, `exporter.cjs`,
`verifier-atelier.cjs`, `verifier-processus.cjs`, `emballer.py`, `verifier.py`,
puis une seconde passe `emballer.py` et `verifier.py --archive-only`. Les
rapports `controle-rendu.json` et `controle-atelier.json` enregistrent les
empreintes des sources qu'ils qualifient ; `verifier.py` l. 140 les compare aux
fichiers courants, donc toute source modifiée invalide le rapport tant que la
chaîne n'a pas été rejouée.

Le workflow `.github/workflows/pages.yml` ne fabrique rien : il publie les
exports committés sur `main` (déclencheur limité aux chemins
`formation/exports/**`, `formation/site/**` et au workflow lui-même) avec
`site/index.html` comme page d'accueil. Une révision n'est donc visible en ligne
qu'après régénération, commit des exports et fusion sur `main`.

Prérequis de fabrication sur un poste : Python 3.11 ou plus avec markdown-it-py,
Node.js avec les dépendances verrouillées de `outils/package.json` (Playwright,
PptxGenJS), un Chromium, et Poppler (`pdfinfo`, `pdftotext`) pour le contrôle
éditorial. Sur le poste de cette étude, seuls Python et Node sont présents ;
aucune fabrication n'a été tentée, et elle ne pourrait pas aboutir tant que les
fichiers manquants de la section 3.3 ne sont pas rétablis.
