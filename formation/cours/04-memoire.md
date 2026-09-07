# M4 — Externaliser la mémoire

Objectif : rendre le travail reproductible et transmissible.
Durée animée : 150 min. Exercices E07 et E08.

## La session se termine, le projet continue

Conservez l'état observé de votre prototype, avec ses défauts encore ouverts.
Fermez le dialogue de votre agent. Ouvrez une nouvelle session dans le même
laboratoire. Demandez-lui quelle unité est en cours, ce qui a été vérifié et ce
qu'il faut faire ensuite. S'il doit inventer ou vous questionner sur une décision
déjà prise, cherchez quel fichier manque ou dit encore autre chose.

La conversation est utile pour travailler. Le projet durable doit porter son
propre état. Une passation décrit une référence de code, les comportements
livrés, les preuves réalisées, leurs limites et la prochaine action. « Tout est
presque fini » ne permet pas de reprendre. « DEM-01 corrigée ; preuve API réussie ;
parcours mobile non effectué ; démarrer app.py et suivre SCENARIO_VISUEL » le permet.

## Les documents ont des questions différentes

![Chaque document répond à une question durable du projet](../illustrations/06-memoire.svg)

| Document | Question à laquelle il répond |
| --- | --- |
| README | Comment installer, lancer, tester et arrêter aujourd'hui ? |
| DAT | Comment les composants et les données s'articulent-ils ? |
| BACKLOG | Quelles unités restent à faire ou à prouver ? |
| JOURNAL | Quelle décision a été prise, pourquoi, et où reprendre ? |
| CHANGELOG | Quel comportement a changé, et est-il réellement publié ? |
| Manuel | Comment l'utilisateur réalise-t-il son travail ? |
| Contrat de déploiement | Quelles opérations restent à appliquer et à vérifier ? |

Dans un petit projet, la documentation peut rester courte. Sa valeur vient de
sa justesse et de son usage. Évitez de recopier une même commande dans cinq
documents : gardez une référence opérationnelle et des renvois. Si la commande
change, mettez à jour cette source et les références affectées dans la même unité.

La méthode P2Enjoy distingue `[ ]` non commencé, `[~]` en cours ou insuffisamment
prouvé, `[x]` terminé avec sa Definition of Done. Un code livré mais sans parcours
E2E reste `[~]`. Le fichier ne devient pas plus vrai parce que toutes ses cases
sont cochées. Retirez une mention de blocage quand elle n'existe plus ; gardez
la chronologie dans le journal.

## Un environnement reproductible

Le **bootstrap** est la procédure qui prépare l'environnement. Il doit préciser
les versions nécessaires, la configuration, les services et les données. Le
**seed** fournit les états initiaux utiles. Une commande de lancement peut créer
un seed ou ne pas le faire : le README doit décrire le comportement réel.

Notre laboratoire crée sa base seulement si elle n'existe pas. Un redémarrage
ne réinitialise pas les demandes. Pour une session neuve sans effacer l'ancienne,
choisissez un autre fichier avec `--db session-m6.sqlite3`. Vérifiez les trois
demandes initiales et leurs propriétaires. Cette opération est explicitement
locale ; elle ne s'applique jamais par défaut à une base partagée.

La conteneurisation, par exemple avec Docker, peut rendre une pile plus facile
à reproduire lorsqu'elle comporte plusieurs services. Elle ne résout pas à elle
seule les différences de secrets, de données ou de versions d'images. Ce petit
atelier pédagogique fait le choix documenté d'une exécution directe Python
pour minimiser l'installation. Le principe transférable reste la reproductibilité
des commandes et des états.

## Trois lieux de conservation

Le disque conserve les fichiers ; le commit conserve une version dans le dépôt
local ; le push transmet des commits ailleurs. Dans un environnement éphémère,
la destruction de la machine peut supprimer les deux premiers. Le contrat de
worker du socle impose donc des checkpoints poussés. Cela suppose un remote
autorisé, une stratégie de branche et des règles de publication cohérentes.

Un push n'est pas forcément un déploiement. Si une infrastructure déploie
automatiquement chaque push sur `main`, pousser un checkpoint encore incomplet
peut produire un effet de production. Il faut établir ce couplage avant
d'automatiser. Le cours ne pousse rien vers un compte ou un service partagé.
L'exercice E08 traite la reprise sur table et dans une nouvelle session locale.

## Écrire une passation utilisable

Un exemple de passation future, après les corrections du module 10 :

> DEM-01 et DEM-02 corrigées dans domain.py. Sept tests de contrat exécutés avec
> succès sur la référence de code indiquée ci-dessous. Parcours Alice/Bob/Eve
> effectué sur une base neuve ; capture mobile conservée. Les profils restent
> simulés. Prochaine unité : préparer DEM-03, sans modifier de données partagées.
> Démarrage : commande du README. Vérifier git status avant toute édition.

Remplacez « référence de code indiquée » par votre identifiant réel. Ne copiez pas
« sept tests réussis » si vous ne les avez pas lancés. Le destinataire doit pouvoir
rejouer une preuve et retrouver une décision sans vous demander le contexte oral.

## Faire et vérifier

E07 répartit les informations dans les documents. E08 simule une interruption
et teste la passation. Extension : décrire un bootstrap conteneurisé pour une
application à deux services, avec versions, health checks et seed ; aucun achat
ou déploiement n'est requis.

Q4.1 : quels éléments disparaissent au redémarrage de notre serveur ? Q4.2 : que
garantit un commit que ne garantit pas un fichier simplement enregistré ? Q4.3 :
quand un checkpoint poussé peut-il avoir un effet de production ? Voir les corrigés.

Point de sortie : une nouvelle session poursuit le travail à partir des fichiers,
et votre environnement retrouve les mêmes états initiaux quand vous le demandez.
