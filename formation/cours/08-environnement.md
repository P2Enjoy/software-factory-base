# M8 — Rendre l'environnement reproductible

Objectif : retrouver le même fonctionnement après une installation ou une reprise.
Durée animée : 150 min. Exercices E15 et E16.

## Le code ne travaille pas seul

Un programme dépend d'un runtime, de bibliothèques, de configuration, de services
et de données. Le **runtime** exécute le langage ; ici Python. Une commande lancée
avec une autre version ou dans un autre dossier peut produire un autre résultat.
« Cela marche sur mon poste » devient utile lorsque ce poste et sa préparation
sont décrits assez précisément pour être reproduits.

![Code, runtime, configuration et données composent l'environnement](../illustrations/14-environnement.svg)

Le laboratoire limite les dépendances à Python avec SQLite et un navigateur.
Cette simplicité facilite l'apprentissage des gestes. Une application plus
large peut utiliser un serveur de base, une file de messages et un stockage.
Chacun doit avoir une commande de préparation et un signal utile de disponibilité.

## Écrire les commandes qui font autorité

Le README doit dire : prérequis, installation, démarrage, initialisation,
tests, build s'il existe, arrêt et reprise. L'agent lit ces commandes ; il ne
choisit pas `npm test` uniquement parce qu'il a déjà vu un projet JavaScript.
Dans notre laboratoire, `python3 -m unittest -v` lance la suite et
`python3 app.py --port 8765` démarre l'application.

Le port identifie le point d'écoute local. Si 8765 est déjà occupé, choisir
8766 avec la même option et la même adresse dans le navigateur. Ne pas tuer
un programme inconnu pour libérer le port. Un « connection refused » peut
simplement signifier que le serveur n'est pas lancé ou que l'adresse est fausse.

Une **variable d'environnement** fournit une configuration au processus. Un
projet doit expliquer son nom, son rôle, son format, son caractère obligatoire
et un exemple non sensible. Le laboratoire utilise des options de ligne de
commande et n'a pas de secret à configurer. Dans un vrai produit, un fichier
d'exemple peut porter les noms et valeurs fictives ; les valeurs réelles ne
doivent pas être versionnées ou copiées dans les supports.

## Seed et état initial

Le seed crée les données nécessaires à une démonstration ou à un test. Il doit
couvrir les profils, statuts et cas importants avec des identifiants stables
lorsque les assertions en dépendent. Ici : Alice possède la demande 1 ouverte,
Bob la 2 ouverte et la 3 fermée. Les permissions ont ainsi de vrais objets
sur lesquels être éprouvées.

Au premier lancement sur un fichier absent, le laboratoire crée le schéma et
les trois demandes. Au redémarrage, il conserve la base. Pour recommencer,
utilisez un nom de fichier neuf avec `--db`, jamais une suppression implicite.
Les tests créent leurs bases temporaires et ne modifient pas votre démonstration.
Deux exécutions ne doivent pas dépendre d'un état caché de l'autre.

Un seed réaliste suit autant que possible les mécanismes du produit. Une
notification de démonstration doit passer par le service local si l'objectif
est de prouver ce service. Insérer une ligne « notification envoyée » ne
prouve aucun envoi. Dans notre laboratoire, le seed initialise les demandes ;
la création et les transitions sont ensuite testées par les vraies routes.

## Services, conteneurs et migrations

Un conteneur peut empaqueter une application et ses dépendances. Une configuration
de services, telle qu'un fichier Compose, peut documenter leur démarrage ensemble.
Le conteneur n'invente pas les bons secrets et ne garantit pas des données
correctes. Il faut encore préciser versions, volumes, disponibilité et seed.

Le socle demande une conteneurisation lorsqu'elle est raisonnablement applicable.
Pour ce petit matériel pédagogique, l'exécution Python directe est une exception
locale explicitée pour limiter les installations ; elle n'est pas un patron
de production. Aucun démon Docker n'est nécessaire pour réaliser les exercices.

Une migration versionnée transforme le schéma ou les données dans un ordre
déterminé. Elle doit être rejouée sur un état local connu et prévoir l'impact
sur les données existantes. Le module 10 approfondira l'autorisation de l'opération,
la sauvegarde et le retour arrière. Créer une base neuve ne teste pas à lui seul
une migration depuis l'ancienne version.

## Diagnostiquer sans inventer

Commencez par le message exact, la commande, le dossier et la version. Déterminez
si le programme a atteint le comportement à vérifier. Un navigateur absent
empêche un test E2E avant son assertion ; ce n'est pas une preuve de régression
produit. Une base existante sans la table attendue demande d'identifier la
bonne cible ou la migration ; elle ne justifie pas un effacement automatique.

Un journal court indique la cause observée, la correction de préparation et
les preuves rejouées. Si la préparation change, corrigez le README. L'historique
du terminal ne doit pas devenir l'unique recette de démarrage.

## Faire et vérifier

E15 reconstruit le seed sans effacer les données. E16 classe des erreurs de
runtime, de port et de base, puis produit une fiche de configuration. Extension :
décrire deux services avec leurs conditions de disponibilité, sans les déployer.

Q8.1 : un conteneur garantit-il la bonne configuration ? Q8.2 : pourquoi le seed
doit-il couvrir les refus ? Q8.3 : créer une base neuve prouve-t-il une migration
sur une base existante ? Voir [CORRIGES](../CORRIGES.md).

Point de sortie : vos commandes et données de départ permettent de rejouer
une observation indépendamment de la mémoire du poste.
