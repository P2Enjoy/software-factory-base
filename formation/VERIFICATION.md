# Bilan de vérification des supports

Campagne de fabrication et vérification des supports pédagogiques. Ce bilan
distingue contenu livré, preuves exécutées
et limites. Les commandes de reproduction sont dans [PRODUCTION](PRODUCTION.md).

## Couverture de la demande

| Exigence | Livrable et preuve |
| --- | --- |
| Respecter le syllabus | quinze modules dans l'ordre validé, de l'assistant à l'assemblage final ; correspondance contrôlée dans programme.json et SYLLABUS.md |
| Enseigner les bases avant l'usine | M1–M11 : agent, unité, contexte, mémoire, contrats, boucle, environnement, preuve, sécurité et Git ; M12–M15 : orchestration progressive et conclusion |
| Support utilisable seul | quinze chapitres développés, installation, exemples, indices, points de sortie, glossaire et fiches ; cours HTML et PDF de 90 pages |
| Exercices et corrections complets | E01–E30, 45 questions de quiz corrigées, évaluation DEM-03 et barème sur 100 ; cahier PDF de 24 pages et corrigés de 14 pages |
| Illustrations explicatives | 15 SVG originaux, descriptions accessibles, équivalents textuels et PNG pour les slides |
| Slides et notes | 80 slides HTML/PDF/PowerPoint ; texte et 80 notes conservés dans le PowerPoint ; notes Markdown séparées |
| Animation premium | scénario de 42 heures, six journées, démonstrations, travail en binôme, remédiation et restitution ; guide avec notes de 46 pages |
| Atelier réellement utilisable | trois copies neuves exécutées, tests de contrat et parcours navigateur avec données fictives |
| Remise hors ligne | cinq HTML autonomes, cinq PDF, PowerPoint et ZIP avec sources et manifeste SHA-256 |

La revue pédagogique en lecture seule a contrôlé l'ordre, les associations
d'exercices et les réponses de quiz. Elle a fait corriger l'initialisation Git
avant E08, compléter la synchronisation dans M11, retirer l'anticipation du
worker dans E26 et réparer un renvoi de module. Une seconde revue a renforcé
les preuves navigateur, l'arrêt des processus, les alternatives des figures
PowerPoint et le traitement des fragments de navigation invalides.

## Environnement effectivement exécuté

Linux, Python 3.14.4 avec SQLite, Git 2.53.0, Node.js 24.20.0,
Playwright 1.63.0, Chromium 151.0.7922.34, PptxGenJS 4.0.1,
markdown-it-py 3.0.0. Aucun modèle n'est requis pour exécuter le laboratoire.
Les installations Windows/macOS sont des consignes proposées, pas des postes
effectivement testés durant cette campagne.

Les appels HTTP de test et Chromium ont nécessité l'autorisation de l'environnement
d'exécution. Les serveurs sont restés sur `127.0.0.1`, avec des bases temporaires.
Aucun hook du socle, ordonnanceur, service externe, déploiement ou push n'a été
activé pour les exercices. Le commit de démonstration Git a été créé seulement
dans une copie temporaire, pas dans le dépôt des supports.

## Preuves exécutées

| Campagne | Résultat | Portée |
| --- | --- | --- |
| Prototype | 7 tests exécutés : 3 réussites et exactement 4 échecs attendus | les deux défauts annoncés sont détectés au niveau unitaire et HTTP/SQLite |
| Référence DEM-01/02 | 7 tests réussis | validation, droits, succès, refus, conservation et répétition |
| Corrigé final DEM-03 | 12 tests réussis | les sept contrats existants plus cinq tests de réouverture |
| Contrôle d'atelier | 49 contrôles réussis | préparation sans écrasement, parcours depuis l'accueil, profils, refus sans mutation, persistance après redémarrage, titre long/mobile, Tab puis Entrée |
| Contrôle de rendu | 22 contrôles réussis | images, ancres HTML, mobile, boutons, notes, fragments invalides, géométrie des 80 slides et absence de ressource distante au rendu |
| Arrêt de processus | 3 cas réussis | enfant déjà sorti, enfant déjà terminé par signal et enfant ignorant SIGINT/SIGTERM |
| Installation Git | init, indexation explicite, revue, commit et lecture de référence réussis | référence initiale réelle disponible avant la passation ; aucun distant requis |
| Contrôle éditorial | voir le rapport machine | liens locaux, durées, 30 corrigés, 45 quiz, 80 notes, syntaxe, PDF et contenu du PowerPoint |
| Archive | intégrité et comparaison au manifeste | fichiers distribués identiques aux octets recensés, y compris BACKLOG/DAT du laboratoire et contrat pédagogique |

Le ZIP a aussi été décompressé dans un nouveau dossier temporaire. La commande
documentée `python3 formation/atelier/preparer.py ... --version finale`, exécutée
depuis cette copie distribuée, a produit le laboratoire final ; ses douze tests
ont réussi. Cela confirme notamment que les fichiers locaux ignorés par Git mais
nécessaires au cours sont bien inclus dans le kit.

Rapports : [rendu](exports/controle-rendu.json),
[atelier et sorties des tests](exports/controle-atelier.json),
[édition](exports/controle-edition.json), [inventaire](exports/inventaire.json).
Les rapports de rendu et d'atelier enregistrent les empreintes des sources
qu'ils qualifient ; le contrôle éditorial les compare à l'état courant.
Les résultats propres au laboratoire ne qualifient aucun système de production.

## Observation des rendus

Les captures ont été ouvertes et examinées : couverture, cours mobile, première
page de chapitre PDF, slides de concepts, schémas de flux, responsabilités,
assemblage final et barème. Texte, hiérarchie, contrastes et retours à la ligne
ont été observés sur ces rendus. Les 80 compositions sont également mesurées
automatiquement : position des blocs, chevauchement avec la conclusion, pieds
de page et débordement interne des blocs plafonnés. Ce contrôle géométrique ne
remplace pas un jugement pédagogique sur chaque phrase.

Dans le laboratoire, l'erreur conserve la saisie, la liste montre propriétaire
et statut, le titre de 80 caractères revient à la ligne à 390 px et le focus
clavier est visible. La réouverture conduit à l'état ouvert et à la commande
de clôture attendue. Les preuves API complètent ces observations visuelles.

Exemples : [slide de flux](exports/captures/slide-04.png),
[responsabilités](exports/captures/slide-59.png),
[cours mobile](exports/captures/cours-mobile.png),
[refus de validation](exports/captures/atelier-refus.png),
[liste mobile](exports/captures/atelier-mobile.png),
[focus clavier](exports/captures/atelier-clavier.png),
[réouverture mobile](exports/captures/atelier-finale-mobile.png).

## Limites explicites

Le PowerPoint a été contrôlé comme archive OOXML : 80 slides, 80 notes, titres,
corps, conclusions et alternatives des schémas. Il n'a pas été rendu dans une
installation de Microsoft PowerPoint ou LibreOffice. Le PDF des slides vient
du HTML ; ce n'est pas une capture du PowerPoint. La projection sur une autre
machine peut substituer des polices. Le HTML et le PDF constituent des formats
de projection déjà rendus et examinés.

Les contrôles clavier, mobile et alternatives ne constituent pas un audit
exhaustif d'accessibilité ni une certification WCAG. Aucune session avec une
cohorte d'apprenants n'a été prétendue : les 42 heures sont un scénario d'animation,
à ajuster par observations lors d'une première session réelle sans déplacer
l'ordre validé des modules.

L'audit des outils d'édition conserve deux alertes npm élevées liées à une
dépendance transitive de traitement d'images, sans version corrigée annoncée.
La restriction aux PNG produits localement, la portée et les avis sont détaillés
dans [PRODUCTION](PRODUCTION.md). Aucun de ces
paquets n'est nécessaire aux participants pour lire les supports ou exécuter
l'atelier. L'audit n'est donc pas présenté comme vert.

La pièce jointe de recherche antérieure n'était pas accessible. Aucune conclusion
ne lui est attribuée ; sa confrontation et la révision de la publication après
stabilisation du socle restent l'étape éditoriale ultérieure annoncée par le
responsable. Le cours livré couvre son amont sans supposer cette validation.
