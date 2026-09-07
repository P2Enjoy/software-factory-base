# Contrat de la formation — Du prototype à la software factory

Support pédagogique en français. Ce document spécifie les
supports et leurs outils de production. Il ne modifie pas la méthode globale.

## Public et résultat

Public mixte sachant lancer Codex ou Claude Code et ayant déjà créé de petites
applications avec l'IA. Les réflexes d'ingénierie ne sont pas présupposés.
Le participant sait, en sortie, cadrer une petite évolution, examiner le diff,
produire des preuves, documenter la reprise et assembler un protocole d'agent.

## Parcours

Les quinze modules du syllabus validé sont conservés dans leur ordre :
assistant/agent ; unité de travail ; contexte ; mémoire ; global/local ;
spécification ; boucle d'exécution ; environnement ; preuves ; sécurité ;
Git ; délégation ; invariants automatisés ; worker ; assemblage final.
Chaque module dure 150 minutes et l'évaluation finale 270 minutes : 42 heures
hors pauses, réparties sur six journées de sept heures. Le support
autonome contient les connaissances, les manipulations et les corrigés ;
l'animation premium ajoute les démonstrations, le feedback et les échanges.
La vitesse autonome dépend de l'expérience ; aucune durée de réussite garantie.

Les onze premiers modules établissent les bases et les gestes d'ingénierie.
Les quatre derniers introduisent progressivement l'orchestration et l'usine.
Une fiche de sécurité et les gestes Git minimaux accompagnent les premières
manipulations ; leur approfondissement garde sa place au syllabus. Les preuves
ciblées accompagnent les premières corrections avant leur étude systématique.

## Edition

Livrables : guide de démarrage et syllabus, quinze chapitres développés, trente
exercices avec indices et corrigés séparés, quiz corrigés, évaluation finale et
barème, notes d'animation minutées, fiches réutilisables, glossaire, sources,
illustrations vectorielles avec équivalents textuels, slides avec notes par
diapositive. Les sources éditables sont remises dans le dépôt avec les exports,
sans commit ni push automatique de cette livraison. Une édition HTML
consultable hors ligne, des PDF et un PowerPoint sont produits localement.
Les exports n'exigent aucun compte externe pour être lus. Le paquet ZIP contient
les sources, les exports et le matériel d'atelier.

Tous les exercices nomment leur point de départ, les opérations, le livrable,
les critères et le corrigé. Les notions nouvelles sont définies avant l'usage.
L'ensemble forme un parcours réalisable sans intervention du formateur.

## Atelier

Le matériel pédagogique « Bureau des demandes » utilise Python 3.11 ou plus,
SQLite et un navigateur ; aucune dépendance Python pour le parcours principal.
Il s'agit d'un laboratoire local à identité simulée, sans secret ni donnée réelle,
non destiné à être déployé. L'écoute est limitée à 127.0.0.1.
Un préparateur crée un dossier neuf, refuse les cibles existantes et y copie le
starter ou le corrigé. Aucun exercice ne modifie le socle hébergeant le cours.

Contrat final : titre de 3 à 80 caractères après suppression des espaces de bord ;
statuts ouvert/ferme ; profils Alice responsable, Bob contributeur et Eve
lectrice. Tous lisent ; Alice et Bob créent ; le responsable clôt toute demande,
le contributeur clôt uniquement les siennes ; la lectrice ne modifie rien.
Une clôture répétée est sans effet supplémentaire. Toute donnée invalide est
refusée côté serveur. Le seed ne remplace jamais une base existante.

La version de départ conserve deux défauts intentionnels : titre vide accepté et
clôture d'une demande tierce autorisée au contributeur. Ces défauts sont isolés
dans domain.py et annoncés comme tels. La suite de contrats complète doit
détecter ces deux défauts, puis réussir sur la référence. Le serveur commun
traite correctement les erreurs : aucun faux succès supplémentaire n'est enseigné.

## Slides

Diaporama 16:9, français, une idée directrice par diapositive, taille lisible à
la projection, notes comprenant intention, explication, question et transition.
Navigation HTML accessible par boutons et clavier, numéro de slide, notes
affichables, impression sans notes. PowerPoint avec texte éditable et notes.
Les illustrations expliquent des relations ; aucune image décorative n'est
requise. Palette P2Enjoy, schémas SVG originaux, aucune ressource distante au rendu.

## Verification

Vérifier les liens locaux et les identifiants, la présence de chaque corrigé,
les durées, le nombre et les notes des slides, les cas de l'atelier, les exports
et leur ouverture. Exécuter les tests de contrat sur les deux versions et les
parcours navigateur sur la référence. Inspecter les rendus grand écran, mobile
et plusieurs slides, mesurer les débordements de toutes les slides, contrôler
les PDF et la structure du PowerPoint. Produire un bilan factuel.

## Perimetre editorial

La pièce jointe de recherche évoquée par le responsable n'est pas accessible.
Le cours est autonome et fondé sur les contrats disponibles et des sources
primaires citées. Il ne prétend ni résumer cette recherche ni en reprendre les
conclusions. La révision de la publication de méthode et la qualification d'une
configuration définitive restent des travaux éditoriaux ultérieurs, distincts
de la livraison complète de cette édition pédagogique.
