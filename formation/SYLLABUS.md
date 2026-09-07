# Syllabus — programme développé

Ce parcours reprend les quinze modules validés, dans leur ordre. Les fondamentaux
et le travail préparatoire occupent les modules 1 à 11 ; l'orchestration et
l'usine occupent les modules 12 à 15. Le dépôt constitue l'aboutissement du cours.

## Public et prerequis

Public mixte sachant lancer Codex ou Claude Code et ayant déjà vibecodé de petites
applications. Savoir ouvrir un dossier, lancer une commande et modifier un fichier
avec assistance. Les réflexes d'ingénierie ne sont pas présupposés. Aucun diplôme
n'est requis. L'agent reste autorisé durant le cours ; chacun doit pouvoir
expliquer son besoin, ses décisions et ses preuves.

## Promesse

Transformer une demande en travail agentique cadré, documenté, reproductible et
vérifié. Faire évoluer un projet avec des agents, puis assembler progressivement
la méthode et les contrôles qui rendent une software factory possible.

## Les quinze modules valides

| Module | Question directrice | Production |
| --- | --- | --- |
| 1. De l'assistant à l'agent | Que change l'accès au dépôt, au terminal et à Git ? | carte des pouvoirs, responsabilités et risques |
| 2. Transformer une demande en unité de travail | Comment éviter le périmètre flou et les ajouts implicites ? | unité cohérente et critères d'acceptation |
| 3. Construire le contexte | Que doit savoir l'agent avant de modifier ? | protocole d'exploration et hiérarchie des sources |
| 4. Externaliser la mémoire | Comment conserver les décisions au-delà de la conversation ? | architecture README, DAT, JOURNAL, BACKLOG, CHANGELOG |
| 5. Séparer méthode globale et contexte local | Quelles règles sont réutilisables et lesquelles appartiennent au produit ? | premier CLAUDE.md et compagnon local |
| 6. Spécifier avant d'implémenter | Comment relier besoin, décision, backlog, code et tests ? | spécification stable et chaîne de traçabilité |
| 7. Concevoir la boucle d'exécution | Dans quel ordre comprendre, décider, documenter, coder et persister ? | protocole de session et checkpoints |
| 8. Rendre l'environnement reproductible | Comment retrouver les mêmes états après un clone ou une interruption ? | bootstrap, configuration et seed |
| 9. Construire la preuve | Qu'est-ce qui permet de déclarer une fonctionnalité terminée ? | tests unitaires, API, E2E et visuel |
| 10. Encadrer sécurité et production | Quelles actions exigent une autorité explicite ? | politique d'accès, migrations et retour arrière |
| 11. Utiliser Git comme mémoire durable | Comment conserver et collaborer sans écraser l'existant ? | commit, push, synchronisation et récupération |
| 12. Orchestrer plusieurs agents | Quand déléguer et comment garder un responsable ? | rôles et missions bornées |
| 13. Automatiser les invariants | Que contrôle la machine et que doit juger le relecteur ? | hooks, entrées de CI et garde de session |
| 14. Passer au worker autonome | Comment reprendre dans un environnement éphémère ? | cycle planifié et protocole d'arrêt |
| 15. Assembler la software factory | Comment les pièces forment-elles une méthode cohérente ? | reconstruction puis comparaison avec le dépôt |

## Rythme

Chaque module dure 150 minutes : concepts 30 ; démonstration 25 ; exercice
d'analyse 25 ; exercice d'application 45 ; débrief 15 ; quiz/passation 10.
Quinze modules = 2 250 minutes. Évaluation finale = 270 minutes. Total = 2 520
minutes, soit 42 heures hors pauses. Les trente exercices ont les identifiants
E01 à E30 ; chaque module dispose de trois questions de quiz corrigées.

| Journée | Programme | Minutes |
| --- | --- | --- |
| J1 | M1, M2, 120 premières minutes de M3 | 420 |
| J2 | fin M3 (30), M4, M5, début M6 (90) | 420 |
| J3 | fin M6 (60), M7, M8, début M9 (60) | 420 |
| J4 | fin M9 (90), M10, M11, début M12 (30) | 420 |
| J5 | fin M12 (120), M13, M14 | 420 |
| J6 | M15 puis évaluation finale | 420 |

Les pauses et repas s'ajoutent. Le guide d'animation décrit les reprises des
modules fractionnés. Une autre répartition calendaire peut conserver l'ordre,
les durées et les points de reprise sans modifier le programme.

## Autonomie et animation premium

Le cours contient toutes les explications, exemples, manipulations, indices,
corrigés, ressources et barème. En autonomie : lire le chapitre, réaliser les
deux exercices, répondre au quiz, comparer les corrigés et refaire le point mal
compris avant de poursuivre. La durée personnelle varie selon l'expérience.

L'animation ajoute les démonstrations commentées, l'échange de productions,
la revue en binôme et le feedback individuel. Le socle de compétences reste
identique. Les plus avancés réalisent les extensions après le livrable principal.
Le formateur accompagne les débutants sans supprimer une preuve critique.

## Évaluation et accessibilite

Diagnostic d'entrée sans note : distinguer réponse et preuve, lire cinq lignes
de code avec assistance, nommer le dossier courant. Trente exercices formatifs,
45 réponses de quiz, puis une évolution nouvelle évaluée sur 100. Le seuil
pédagogique est 70 sans critère critique manquant ; voir EVALUATION.

Les figures ont une explication textuelle ; HTML et PDF offrent du texte
sélectionnable ; les manipulations sont accessibles au clavier. Le temps peut
être fractionné en autonomie et adapté en animation sans changer les comportements
à prouver. La formation n'est pas présentée comme une certification d'éditeur,
une certification réglementaire ou un audit de produit.
