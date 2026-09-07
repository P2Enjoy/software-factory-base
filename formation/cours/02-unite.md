# M2 — Transformer une demande en unité de travail

Objectif : passer d'une intention à un résultat borné que vous pourrez examiner.
Durée animée : 150 min. Exercices E03 et E04.

## Identifier ce qui doit changer pour quelqu'un

« Je veux une application professionnelle » exprime une ambition. Pour commencer
le travail, il faut nommer un acteur, une situation et une amélioration observable.
Dans notre fil rouge, une personne reçoit des demandes de matériel. Elle souhaite
éviter les demandes sans intitulé et distinguer ce qui reste ouvert. Ces deux
besoins sont compréhensibles sans choisir un framework.

Un besoin peut être décrit par « quand [situation], [personne] veut [action]
afin d'obtenir [résultat] ». Ce patron n'est pas une formule magique : il force
à préciser qui profite du changement. Si aucun résultat ne peut être observé,
demandez comment on saura que le besoin est satisfait.

## Une unité cohérente

![Décomposer une ambition en un résultat, des limites et une preuve](../illustrations/12-unite.svg)

Une unité cohérente regroupe les changements nécessaires à un résultat. Elle
peut traverser plusieurs fichiers, mais reste explicable en une phrase.
« Refuser une création dont le titre est vide » possède un début, une fin et
une preuve. « Faire tout le frontend » peut produire beaucoup de code sans
garantir un seul parcours achevé.

La taille de l'unité dépend du système. Un formulaire simple peut tenir dans
un petit changement. Une facturation complète combine calcul, données, droits,
paiement et états ; il faut chercher une première tranche vérifiable. Le
découpage ne doit pas laisser un comportement présenté comme complet alors
qu'une couche indispensable manque.

Pour décider si l'unité est praticable, posez trois questions : connaît-on le
résultat ? peut-on identifier les parties concernées ? sait-on comment observer
la réussite ? Une réponse inconnue peut devenir une petite mission d'exploration,
avec une question et un livrable, avant l'implémentation.

## Critères d'acceptation et limites

Les **critères d'acceptation** décrivent ce que le résultat doit satisfaire.
Ils sont spécifiques à l'unité. Une **Definition of Done** rassemble aussi les
conditions de qualité et de preuve communes ; nous l'étudierons au module 7.
Pour l'instant, écrivez un succès, un refus et ce qui doit rester inchangé.

Exemple de première unité : « Lorsqu'un contributeur soumet un titre invalide,
la demande n'est pas créée et il voit comment corriger sa saisie. » Il reste
à définir « invalide » : le module 6 fera préciser bornes, types et normalisation.
Au cadrage, cette inconnue est nommée au lieu d'être discrètement décidée par
le code généré.

Décrivez aussi le hors périmètre utile : « pas de refonte visuelle, pas de
nouvelle connexion externe, pas de changement des droits de clôture ». Il sert
à protéger l'unité contre des ajouts plausibles mais indépendants. Ce n'est
pas un inventaire de toutes les choses qu'on ne fera jamais.

## Gérer les questions et décisions

Une question produit que les sources ne permettent pas de trancher peut mener
à des comportements différents. Demandez alors une décision ciblée : « un titre
trop long doit-il être refusé ou tronqué ? » Montrez la conséquence : une
troncature perd une partie de la saisie. Dans notre contrat pédagogique, le
refus explicite est retenu.

Une routine technique réversible peut être décidée dans le périmètre autorisé,
avec un motif. Changer une forme publique déjà utilisée, engager une dépense
ou écrire en production demande une autorité adaptée. « Continue jusqu'au bout »
fixe une attente de persistance ; cela n'autorise pas automatiquement ces actions.

Une décision prise doit être écrite. À ce stade, une note courte suffit :
problème, choix, raison, conséquence. Le module 4 donnera une place durable à
ces notes. Ne laissez pas « à confirmer » dans un document après avoir vraiment
tranché ; ne présentez pas non plus une hypothèse comme une validation humaine.

## Déléguer une unité à l'agent

Message de cadrage : « Lis la description du besoin. Propose la plus petite unité
qui produit un résultat utile, indique trois critères d'acceptation et les
inconnues qui l'empêchent. N'implémente pas encore. » Examinez si la proposition
ajoute un tableau de bord, des notifications ou une nouvelle stack sans nécessité.
Ramenez l'agent au résultat choisi et gardez les idées utiles pour un autre
moment, sans les mêler à la tâche courante.

Lorsque vous autorisez l'implémentation, la mission doit désigner cette unité et
ses références. La phrase « fais ce qu'on a dit » dépend trop de la mémoire du
dialogue. Une référence écrite et stable rend l'attendu consultable par une
nouvelle session ou un relecteur.

## Faire et vérifier

E03 cadre une demande trop large. E04 choisit une première tranche et traite
les inconnues avec des décisions explicites. Extension : comparer deux
découpages sur le délai avant la première preuve utile.

Q2.1 : pourquoi le nombre de fichiers ne mesure-t-il pas seul la cohérence ?
Q2.2 : quelle différence entre critère d'acceptation et envie d'amélioration ?
Q2.3 : que change l'autorisation « continue » pour une dépense non prévue ?
Voir [CORRIGES](../CORRIGES.md).

Point de sortie : vous pouvez donner une mission dont le résultat, les frontières
et les questions sont compréhensibles avant de lire l'implémentation.
