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
  dépôt. Le compte rendu factuel de ce qui a été enseigné, anonymisé, est dans
  [SESSIONS.md](SESSIONS.md).
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

## 4. Ce qui a été enseigné

Le compte rendu factuel des deux sessions, avec le vocabulaire employé, les
procédures montrées, les exercices réellement conduits et les réactions des
participants, est dans [SESSIONS.md](SESSIONS.md). Trois traits le résument.

La session 1 (2 h 47) enseigne à cadrer un agent. Son objet central est la
« fiche de goal », un fichier d'objectifs produit en dialoguant avec un assistant
sous un prompt qui interdit l'ambiguïté, puis remis à l'agent comme contexte.
Autour de cet objet viennent une hiérarchie d'outillage (assistant, harnais,
agent, orchestrateur, usine), la dérive d'instructions, la décomposition en
sous-systèmes, le few-shot prompting et le métaprompting.

La session 2 (4 h 10) enseigne à industrialiser. Après une digression d'environ
cinquante-cinq minutes sur le matériel et la chaîne d'approvisionnement, elle
traite le choix entre les trois modes d'un outil, la configuration complète d'un
espace de travail local avec ses garde-fous, le passage obligé par un dépôt Git
hébergé, le contrôle à distance, la planification de routines, la création d'un
agent spécialisé enregistré dans un dossier d'agents, la distinction entre agent
et compétence, puis l'usine : rôles séparés, communication entre agents, agents
de contrôle qualité qui relancent les développeurs, preuves visuelles par cycle,
et une économie explicite du choix des modèles.

Le troisième trait est le support de travail : les participants n'ont jamais
manipulé de laboratoire pédagogique. Ils ont travaillé sur leurs propres projets,
et sont repartis de la session 2 avec un dépôt, un contrôle à distance
opérationnel et un agent enregistré sur leur machine.

## 5. Écarts entre les sessions et les supports

### 5.1 Format et volume

Les supports décrivent 42 heures animées sur six journées, quinze modules de
150 minutes et une évaluation de 270 minutes, avec un minutage interne fixe
(30 minutes de concepts, 25 de démonstration, 25 puis 45 d'exercices, 15 de
débrief, 10 de quiz). Les deux sessions totalisent 6 h 57, plus une troisième
session de deux à trois heures annoncée, soit environ un quart du volume prévu.
Aucun module n'a été animé selon son minutage, aucune journée n'a été jouée.

Le guide d'animation prévoit une cohorte allant jusqu'à huit personnes par
évaluateur, du travail en binôme avec alternance des rôles pilote et relecteur,
et 25 minutes de restitution finale. Le format réel est un formateur pour deux
participants, conversationnel, sans binôme possible.

### 5.2 Le support de travail n'a pas servi

Le laboratoire « Bureau des demandes » structure le parcours : il est prérequis
du module 3, porte les deux défauts corrigés aux modules 9 et 10, et fournit le
sujet de l'évaluation finale. La mesure faite sur le cahier d'exercices donne
21 exercices sur 30 ancrés dans ce laboratoire par un nom de fichier, une unité
DEM, un profil ou une commande ; 9 seulement sont transposables tels quels.

Aucune trace de ce laboratoire dans les deux sessions : ni les profils, ni les
unités DEM, ni les fichiers du prototype, ni son contrat de titre, ni sa matrice
de droits. Le support pédagogique le plus coûteux de l'édition n'a pas été
mobilisé une seule fois.

### 5.3 Les exercices et l'évaluation n'ont pas été utilisés

Les trente exercices identifiés, les quarante-cinq questions de quiz et
l'évaluation notée sur 100 avec son barème et ses critères critiques n'ont pas
été employés. Le cahier d'exercices a été promis aux participants en début de
session 1 mais n'a pas été présenté en séance.

Ce qui a effectivement été fait : un exercice oral de classement de situations
(trois situations posées sur quatre annoncées), un exercice de rédaction d'un
premier goal sur un sujet fictif avec restitution, un atelier de configuration
guidée d'un agent de veille sur le projet réel d'un participant, et la mise en
place complète du dépôt et du contrôle à distance chez les deux participants.

### 5.4 Les slides et le guide d'animation n'ont pas été employés

Les 80 diapositives, leurs notes et le guide minuté ne sont pas apparus. Le
formateur a projeté un site web publié pour l'occasion en session 1, puis
exclusivement des outils réels en session 2.

### 5.5 Couverture module par module

| Module | Traité en session ? | Observation |
| --- | --- | --- |
| M1 De l'assistant à l'agent | oui, et dépassé | les sessions ajoutent le harnais, la hiérarchie jusqu'à l'usine, les trois modes d'outil et la dérive d'instructions, absents du chapitre |
| M2 Demande en unité de travail | partiellement | les écrans « transformer une demande en unité » et « découper une demande trop large » ont été parcourus, mais la forme écrite enseignée est la fiche de goal, absente du chapitre |
| M3 Construire le contexte | partiellement | « créer le contexte du goal » et la distinction faits, hypothèses, décisions ont été enseignés ; l'exploration du code du laboratoire ne l'a pas été |
| M4 Externaliser la mémoire | non | les documents montrés (journal d'exécution, document d'exploration, backlog numéroté, dossier d'architecture) recoupent le sujet, sans la répartition README, DAT, JOURNAL, BACKLOG, CHANGELOG du chapitre |
| M5 Séparer global et local | non | aucune mention d'un contrat global et de son compagnon local, ni du routage de lecture selon l'outil |
| M6 Spécifier avant d'implémenter | non | ni table d'exemples discriminants, ni oracle, ni marqueurs de traçabilité ; le cadrage anti-ambiguïté joue un rôle voisin, par le dialogue et non par une table |
| M7 Concevoir la boucle | partiellement | Definition of Done énoncée et appuyée ; la boucle de session et ses checkpoints n'ont pas été enseignés |
| M8 Environnement reproductible | non | seed, bootstrap, ports, migrations absents ; la session 2 traite l'installation d'outils, qui est un autre sujet |
| M9 Construire la preuve | autrement | enseigné : exiger un rapport de bas niveau, la tendance de l'outil à « tricher » sur les tests d'interface, les captures comme preuve de cycle, des agents de test distincts selon la nature de la preuve. Non enseigné : la matrice unitaire, API, E2E, visuel du chapitre et la correction guidée |
| M10 Sécurité et production | autrement | enseigné : session dédiée pour le contrôle clavier et souris, illusion du secret par messagerie, chiffrement asymétrique, probabilité cumulée de défaut, mémoire spécialisée d'un réviseur. Non enseigné : autorisation serveur, matrice rôle et propriété, refus sans mutation |
| M11 Git comme mémoire durable | non | Git a servi de prérequis d'outillage (créer un dépôt, authentifier, cloner, laisser l'agent pousser) ; ni index, ni diff, ni récupération distante, ni divergence |
| M12 Orchestrer plusieurs agents | avec une autre architecture | voir 5.6 |
| M13 Automatiser les invariants | marginalement | l'agent pragmatique qui refuse un commit sans marqueur est cité une fois, en fin de session 1 ; hooks, entrées et CI non traités |
| M14 Passer au worker autonome | autrement, et réellement | voir 5.7 |
| M15 Assembler la software factory | autrement | le chapitre fait reconstruire l'arborescence du socle ; les sessions construisent une usine d'agents avec des rôles agiles et une économie de modèles |

### 5.6 Deux architectures d'orchestration coexistent

Le module 12 enseigne l'organisation du socle : un agent principal, seul éditeur
et seul opérateur Git, assisté de trois rôles auxiliaires en lecture seule
(explorateur, relecteur, vérificateur) qui ne décident rien, ne clôturent rien et
ne délèguent pas. Le mot « orchestrateur » n'apparaît nulle part dans le chapitre.

Les sessions enseignent autre chose : un orchestrateur qui est lui-même un agent,
doté de son propre fichier d'objectifs, qui décide quand et comment appeler les
phases ; des agents qui s'envoient des messages entre eux ; un agent de contrôle
qualité qui relance automatiquement les agents de développement tant que son
exigence n'est pas satisfaite ; et un jeu de rôles calqué sur une équipe agile.
L'humain n'y est plus l'agent principal mais le client.

Ces deux architectures ne se contredisent pas : la première est le contrat de
travail d'une session assistée, la seconde celui d'une usine autonome. Les
supports n'enseignent que la première et nomment la seconde sans la décrire. Le
chapitre 15 conclut le parcours sur un assemblage de fichiers, là où les sessions
concluent sur une organisation d'agents.

### 5.7 L'outillage a rattrapé puis dépassé le support

Le module 14 enseigne le worker autonome comme un exercice sur table. Il l'écrit
explicitement : la démonstration utilise « une carte d'interruption, pas un
ordonnanceur réel », « ce cours simule ce geste sans créer de service extérieur »,
et la réponse de quiz retenue est qu'un fichier de déclenchement n'installe aucune
planification, un mécanisme externe devant exister réellement.

En session 2, ce mécanisme externe a été configuré en direct, en quelques minutes,
par une commande de l'outil, avec une routine horaire de test, puis illustré par
une usine réelle s'exécutant toutes les quatre heures et rendant ses preuves en
captures d'écran. Le contrôle à distance, le pilotage depuis un téléphone, une
machine hébergée fournie avec l'abonnement et l'exécution sur serveur distant
relèvent du même constat : ce que le support présente comme hors de portée du
cours est devenu une manipulation de séance.

Un second point de dérive, indépendant des sessions : le module 13 affirme que le
socle « ne fournit pas de workflow CI distant », l'exercice E25 demande de
« constater son absence » et son corrigé la confirme. Le dépôt contient
`.github/workflows/pages.yml` depuis le 7 septembre 2026 à 13 h 08, soit deux
heures après le commit qui a introduit ces chapitres. Ce workflow publie les
exports et n'exécute aucun contrôle, mais la formulation absolue des trois
passages met en difficulté une personne qui fait l'exercice aujourd'hui.

### 5.8 Notions enseignées sans emplacement dans les supports

Vérification faite sur les quinze chapitres, le cahier d'exercices, les corrigés,
les fiches, le glossaire et les slides : les termes « goal », « few-shot »,
« métaprompting », « compétence » au sens de l'outil, « Definition of Ready »,
« consigner » et le taux de rétention des instructions n'apparaissent nulle part.
« Harnais » n'apparaît qu'une fois, au module 13, dans un autre sens (le harnais
de test des garde-fous). « Orchestrateur » n'apparaît dans aucun chapitre.

Liste des notions enseignées lors des deux sessions et absentes des supports :

1. la fiche de goal : sa raison d'être, sa structure, sa production ;
2. la procédure de cadrage anti-ambiguïté avec un assistant, y compris le prompt
   d'ouverture, les questions à choix multiples avec option recommandée et les
   réponses par codes ;
3. la hiérarchie assistant, harnais, agent, orchestrateur, usine ;
4. le choix entre les trois modes d'un outil, et ce que chacun permet ;
5. la dérive d'instructions, sa cause et ses conséquences pratiques ;
6. le few-shot prompting et le métaprompting ;
7. la décomposition en sous-systèmes et unités d'action ;
8. « consigner » plutôt qu'exécuter, et la Definition of Ready ;
9. la configuration d'un espace de travail local et ses garde-fous (dossier de
   travail, listes blanches de dossiers et de sites, appareil de confiance,
   enregistrement d'écran, instructions globales) ;
10. la planification de routines et le contrôle à distance ;
11. l'enregistrement d'un agent, son dossier, sa mémoire isolée, et la
    distinction entre un agent et une compétence ;
12. la communication entre agents ;
13. les rôles de l'usine et leur séparation stricte ;
14. les agents de contrôle qualité qui relancent les agents de développement ;
15. l'économie du choix des modèles par rôle et le coût d'exploitation ;
16. la mémoire spécialisée d'un agent comme moyen de compenser un modèle ;
17. l'usage d'un protocole d'outillage plutôt que du contrôle clavier et souris
    pour tester une interface.

### 5.9 Notions des supports non enseignées

Les onze premiers modules portent, selon la spécification, « les bases et les
gestes d'ingénierie ». La quasi-totalité de leur contenu propre n'a pas été
traitée : spécification par l'exemple et oracle, chaîne de traçabilité,
reproductibilité de l'environnement et seed, matrice de preuves, autorisation
côté serveur et refus sans mutation, états de Git et synchronisation, répartition
documentaire entre les cinq documents, séparation entre méthode globale et
contexte local.

Ce constat n'invalide pas ces contenus. Il indique qu'un cycle court avec ce
public commence par l'usine et n'atteint pas les fondations, alors que le
parcours écrit fait l'inverse.

### 5.10 Le public et sa demande

La définition du public est juste : des personnes qui savent lancer un outil de
code et ont déjà produit de petites applications, sans réflexes d'ingénierie
formalisés. La promesse écrite (« transformer une demande en travail agentique
cadré, documenté, reproductible et vérifié ») décrit correctement ce qui a été
enseigné.

La demande exprimée en séance est plus étroite et plus concrète : industrialiser
des projets qui existent déjà, déléguer sans perdre le contrôle, disposer d'un
journal de ce que font les agents, maîtriser le coût d'exploitation, arbitrer
entre exécution locale et service hébergé. Les participants arrivent avec des
projets et repartent avec des agents configurés sur ces projets. Un parcours dont
le support de travail est un laboratoire fictif ne répond pas à cette demande.

## 6. Options de réorganisation

Quatre options ont été instruites.

**Option A, ne rien changer au parcours et publier un scénario court à côté.**
Coût minimal, aucun invariant touché. Elle laisse les quinze chapitres décrire un
contenu qui ne couvre pas la moitié de ce qui est enseigné, et laisse le
laboratoire sans usage constaté. Écartée : elle traite le symptôme (le format) et
non la cause (le contenu manquant).

**Option B, réorganiser l'ordre des quinze modules pour commencer par l'usine.**
Elle rapprocherait le parcours de la séquence réellement animée. Elle contredit
une décision explicite du responsable, consignée dans
[DECISIONS.md](DECISIONS.md) et rappelée dans [PRODUCTION.md](PRODUCTION.md) et
[ANIMATION.md](ANIMATION.md), qui conserve l'ordre validé et écarte une
condensation. Elle contredit aussi la logique du chapitre 15, qui suppose que
l'usine répond à des problèmes rencontrés avant elle. Son coût est élevé :
renumérotation des quiz, réécriture de tous les renvois entre modules, blocs de
slides, journées du guide d'animation, table de remédiation. Écartée.

**Option C, enrichir les quinze modules de tout ce qui a été enseigné.**
Elle comble les manques là où ils appartiennent, sans toucher aux invariants de
structure. Prise seule, elle gonfle un parcours déjà à 42 heures et ne résout pas
le problème du format court, ni celui du support de travail.

**Option D, retenue, combiner un enrichissement ciblé des chapitres et une
couche de parcours au-dessus.** Les chapitres restent la référence de
connaissances, dans leur ordre validé, et reçoivent les notions manquantes qui
relèvent de leur sujet. Un document de parcours décrit séparément les
déclinaisons du même socle, dont celle qui a été réellement animée. Les exercices
reçoivent une variante sur projet réel là où ils dépendent du laboratoire. Aucune
constante des outils n'est touchée : ni le nombre de modules, ni celui des
exercices, des quiz, des slides ou des figures, ni les durées nominales.

## 7. Décision

L'option D est retenue, avec les motifs suivants, dans l'ordre de la ligne de
décision de la méthode.

**Un seul comportement, partout.** Le socle de connaissances reste unique et
ordonné une seule fois. Les formats d'animation deviennent des vues sur ce socle,
pas des parcours concurrents qui divergeraient.

**Le moindre coût pour la personne.** Un participant en cycle court trouve un
document qui lui dit quels chapitres lire, dans quel ordre, et avec quelle
variante d'exercice sur son propre projet. Un lecteur autonome garde le parcours
complet. Aucun des deux n'a besoin de reconstituer l'information.

**La réversibilité.** Ajouter un document et enrichir des textes se défait par un
retrait. Renuméroter les modules, déplacer des exercices ou changer le nombre de
slides engage les outils, les rapports d'empreintes et tous les renvois croisés.

**L'invariant appliqué là où il fait autorité.** L'ordre des quinze modules est
une décision du responsable ; elle n'est pas remise en cause. L'écart réel, qui
est l'absence de notions enseignées, est traité là où il se constate, dans le
texte des chapitres.

Deux points tranchés au passage, avec leur motif :

- **Le laboratoire est conservé.** Il n'a pas servi, mais il est la seule base
  déterministe qui permette des exercices corrigés, une évaluation notée et un
  contrôle automatisé. Le supprimer retirerait la preuve sans rien apporter. Il
  cesse en revanche d'être le seul support : chaque exercice qui en dépend reçoit
  une variante sur projet réel.
- **Aucune notion enseignée n'est écartée au motif qu'elle dépend d'un outil.**
  Les supports nomment les fonctions par leur rôle plutôt que par leur libellé
  commercial, et renvoient aux sources officielles pour les détails d'interface,
  comme le fait déjà [SOURCES.md](SOURCES.md). Une fonction qui existe chez les
  deux fournisseurs principaux est enseignée comme un geste, pas comme un produit.

## 8. Plan de révision

Onze unités, à exécuter dans cet ordre, chacune emportant son texte, ses renvois
et la régénération des exports quand elle la déclenche. Les unités 1 et 2 sont des
préalables : elles rétablissent la capacité à fabriquer et à vérifier le kit.

| # | Unité | Fichiers principaux | Invariant touché |
| --- | --- | --- | --- |
| 1 | Rétablir les deux documents manquants du laboratoire, versionnés à l'identique de ceux du kit | `atelier/commun/BACKLOG.md`, `atelier/commun/DAT.md` | aucun |
| 2 | Documenter les prérequis de fabrication réels et retirer les mentions devenues fausses | `PRODUCTION.md`, `outils/requirements.txt` | aucun |
| 3 | Créer le document de parcours décrivant les trois déclinaisons du socle et la séquence réellement animée | `PARCOURS.md` (nouveau), renvois depuis `README.md` et `SYLLABUS.md` | aucun |
| 4 | Publier le compte rendu des sessions comme source de la révision | `SESSIONS.md` | aucun |
| 5 | Enrichir M1 : hiérarchie assistant, harnais, agent, orchestrateur, usine ; les trois modes d'outil et leur critère de choix | `cours/01-assistant-agent.md`, `GLOSSAIRE.md` | aucun |
| 6 | Enrichir M2 et M3 : la fiche de goal comme forme écrite de l'unité ; la procédure de cadrage anti-ambiguïté ; le few-shot ; la dérive d'instructions et l'isolement des tâches | `cours/02-unite.md`, `cours/03-contexte.md`, `FICHES.md` | aucun |
| 7 | Enrichir M5 et M7 : métaprompting ; consigner plutôt qu'exécuter ; Definition of Ready | `cours/05-global-local.md`, `cours/07-boucle.md` | aucun |
| 8 | Enrichir M12 : orchestrateur agent, agent contre compétence, enregistrement et mémoire isolée, communication entre agents, rôles de l'usine, agents de contrôle qualité, choix du modèle par rôle | `cours/12-agents.md`, `GLOSSAIRE.md` | aucun |
| 9 | Réviser M13 et M14 : corriger les affirmations sur l'absence de workflow distant ; remplacer la simulation de planification par la planification réelle, le contrôle à distance et les garde-fous d'un espace de travail local | `cours/13-invariants.md`, `cours/14-worker.md`, `EXERCICES.md` (E25), `CORRIGES.md` (E25, E29) | aucun |
| 10 | Enrichir M15 : le renversement de rôle vers le client, les rôles agiles et leurs rituels, l'économie d'exploitation | `cours/15-factory.md` | aucun |
| 11 | Ajouter à chaque exercice ancré dans le laboratoire une variante sur projet réel, et aligner le portail et les chiffres affichés | `EXERCICES.md`, `CORRIGES.md`, `site/index.html` | aucun |

Après les unités 5 à 11, les blocs de slides des modules touchés sont mis à jour
dans `slides.json` à structure constante (cinq diapositives par module,
quatre-vingts au total), et les sections correspondantes du guide d'animation
sont resynchronisées, puisque ce guide recopie aujourd'hui à la main les textes
des slides sans contrôle mécanique.

Deux travaux d'outillage sont proposés hors de ce plan, parce qu'ils touchent les
scripts de fabrication et non les supports : un contrôle de cohérence entre
`programme.json`, `SYLLABUS.md` et `slides.json`, et un contrôle de la règle de
durée des exercices. Ils lèveraient les écarts décrits en 3.3, points 3 et 4.

Aucune unité de ce plan ne modifie `CLAUDE.md`, `docs/CloudWorker.md`,
`docs/DESIGN_SYSTEM.md`, `AGENTS.md`, les définitions de rôles ni les garde-fous
du socle. La révision porte sur les supports de formation et sur eux seuls.

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
| Durées 150 et 270 minutes, total 2 520 | `programme.json` l. 3 à 4 ; `verifier.py` l. 63 ; `construire.py` l. 92 (« 42 heures ») | chaque chapitre (« Durée animée : 150 min ») ; SYLLABUS ; ANIMATION (bornes 0 à 30, 30 à 55, 55 à 125, 125 à 150 répétées quinze fois) ; EVALUATION ; `slides.json` (cinq chaînes `minutage` par module et slides 78 à 80) ; SPECIFICATION ; README ; VERIFICATION ; DECISIONS |
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
