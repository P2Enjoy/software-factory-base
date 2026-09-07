# M7 — Concevoir la boucle d'exécution

Objectif : ordonner les gestes pour livrer une petite unité vérifiable.
Durée animée : 150 min. Exercices E13 et E14.

## Donner un ordre au travail

Vous savez maintenant cadrer une unité, lire son contexte, conserver les décisions
et écrire ses exemples. Une session d'implémentation met ces éléments en mouvement.
Un ordre explicite évite de coder une hypothèse, d'oublier une décision ou de
remettre toutes les preuves à une fin de session qui n'arrive pas.

![La boucle d'une unité cohérente et ses retours de correction](../illustrations/13-boucle.svg)

La boucle comporte : comprendre, spécifier, persister, implémenter, prouver,
mettre à jour et transmettre. Un défaut trouvé pendant la preuve ramène vers
la cause et les éléments concernés. Une contradiction de contrat ramène à une
décision explicite ; elle n'autorise pas le code à inventer une règle.

Dans la méthode du socle, la décision et la spécification sont persistées avant
le code qui en dépend. La documentation représente le comportement courant et
ses preuves. Une unité reprise avec une spécification complète ne nécessite
pas de réécrire toute cette spécification avant d'avancer.

## Les checkpoints

Un **checkpoint** est un état cohérent auquel le travail peut être rattaché.
Il peut porter une spécification avant code, une petite implémentation ou une
correction. Il doit être lisible et son statut doit être exact. Un checkpoint
peut être incomplet du point de vue du produit ; il ne doit pas prétendre le
contraire. Git permet de conserver ces états ; les gestes minimaux sont dans
INSTALLATION et l'étude approfondie viendra au module 11.

Avant de modifier, regardez l'état Git et les fichiers en cours. Après modification,
relisez la sélection du checkpoint. La méthode demande des commits cohérents
et des pushes selon le workflow autorisé. Dans le laboratoire sans remote, on
nomme l'absence de push au lieu de la simuler. L'environnement éphémère et la
sauvegarde distante seront étudiés au module 14.

## Une correction pas à pas

Pour DEM-01, une séquence correcte commence par le contrat écrit. Le test fourni
de borne minimale permet de constater le défaut. L'agent lit validate_title,
propose la correction de plage et garde les contrôles de type. Vous relisez
le diff, exécutez le test ciblé et vérifiez le parcours. Le module 9 réalisera
ce travail avec toute la matrice de preuves.

Une séquence fragile commence par « réécris la création », puis adapte les
assertions à la nouvelle sortie et déclare terminé quand le serveur démarre.
Le problème n'est pas seulement la taille du code : l'attendu n'est plus
indépendant de l'implémentation. Il devient impossible de savoir si l'on a
corrigé le produit ou simplement renommé le défaut.

## Definition of Done

Les critères d'acceptation décrivent le résultat demandé. La Definition of Done
ajoute les conditions applicables de fin : code lisible, règles au bon endroit,
tests spécifiques, preuve du parcours, données et documents à jour, état Git
connu. Elle doit être utilisée comme une vérification de faits, pas comme une
liste décorative.

Pour DEM-01, le titre valide est créé, les titres invalides sont refusés sans
insertion, les tests ciblés réussissent et l'erreur est visible et corrigeable.
Si le serveur ne démarre pas sur votre poste, une preuve unitaire peut rester
valide, mais le parcours est non exécuté. Le statut `[~]` conserve cette nuance.
Un build vert ne prouve pas à lui seul une règle d'accès ou l'ergonomie.

## Diagnostic et traitement des écarts

Classez d'abord l'écart : contrat ambigu, bug de code, données inattendues ou
environnement non opérationnel. Pour un bug, reproduisez puis cherchez la cause.
Pour un problème de poste, conservez le message exact et vérifiez le runtime,
les chemins, les ports et les services documentés. Ne désactivez pas un test
pour contourner une panne du navigateur.

Un défaut étranger à l'unité est consigné avec son impact. S'il bloque concrètement
la tâche, traitez le préalable autorisé puis revenez au résultat. Sinon, ne
transformez pas chaque découverte en nouvelle refonte. Une unité cohérente
terminée apporte plus de clarté qu'une collection de corrections sans relation.

## Budget et compte rendu

Réservez du temps aux preuves et à la passation dès le début. Une session de
90 minutes peut prévoir 15 de compréhension, 15 de contrat, 30 de réalisation,
20 de preuves et 10 de compte rendu. C'est un exemple de budget, à adapter aux
durées mesurées. Une campagne de tests longue se prépare ; elle ne se réduit
pas en silence pour annoncer la fin.

Le compte rendu nomme ce qui a changé, ce qui a été exécuté, les résultats,
les limites et la prochaine action. Il doit rester lisible sans votre ancien
dialogue. Les fiches F3 et F7 fournissent des modèles.

## Faire et vérifier

E13 remet une session désordonnée dans un ordre justifié. E14 audite une clôture
trop rapide et construit la DoD. Extension : organiser une reprise d'unité déjà
spécifiée sans produire une documentation redondante.

Q7.1 : un checkpoint cohérent signifie-t-il unité terminée ? Q7.2 : faut-il
réécrire une spécification complète à chaque reprise ? Q7.3 : comment annoncer
une preuve impossible à exécuter ? Réponses dans [CORRIGES](../CORRIGES.md).

Point de sortie : vous savez où un résultat est décidé, conservé, vérifié et
transmis, et comment le statut change selon les preuves disponibles.
