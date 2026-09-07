# Évaluation finale — Rouvrir une demande

Durée animée : 270 min, hors pauses. Travail individuel avec agent autorisé.
Vous pouvez consulter le cours et les fiches. Le corrigé final est réservé à la
comparaison après remise. En autonomie, conservez une première réponse datée.

## Point de depart

Utiliser votre laboratoire après M10, avec les sept tests verts, ou une copie
neuve de la version `reference`. Commencer avec une base neuve. L'unité DEM-03
du backlog nomme l'évolution ; lire son contrat puis le préciser ci-dessous.
Les données, profils et commandes restent ceux du laboratoire.

## Demande produit

Alice veut rouvrir une demande fermée par erreur. Après réouverture, la demande
redevient ouverte, conserve son identifiant, son titre et son propriétaire, et
peut suivre la clôture habituelle. Seul le profil responsable peut rouvrir.
Bob et Eve ne peuvent pas le faire, même si la demande appartient à Bob. Une
tentative sans session est refusée. Une demande absente n'est pas créée.
Rouvrir une demande déjà ouverte avec Alice laisse le même état, sans doublon.

Contrat HTTP : `POST /api/demandes/3/rouvrir` avec JSON `{}` ; 200 autorisé,
401 sans session, 403 non autorisé, 404 demande absente. L'état ne change pas
sur un refus. L'interface présente « Rouvrir la demande 3 » à Alice sur une
demande fermée. Le parcours part de l'accueil et du choix de profil.

## Travail attendu

1. Inspecter le dépôt et l'état Git, reformuler le contrat et ses risques.
2. Écrire la spécification et les cas limites avant la modification.
3. Produire une petite implémentation cohérente, sans réécrire le système entier.
4. Ajouter tests unitaires et API/SQLite de succès, refus, absence et répétition.
5. Rejouer les tests existants et parcourir réellement l'interface.
6. Mettre à jour le README, le backlog et la passation. Relire le diff.
7. Expliquer individuellement une décision et une preuve critique.

Le dossier de remise contient : spécification, diff, code, tests, sorties réelles,
captures observées, statut du backlog et passation. Un identifiant Git réel peut
référencer le checkpoint. Aucun remote, déploiement, abonnement ou système partagé
n'est requis. Ne créez pas de fausse preuve de push.

## Répartition du temps

Diagnostic 25 min ; spécification 35 ; implémentation 100 ; preuves 55 ; documentation
et revue 30 ; restitution 25. À la minute 160, passez aux preuves même si le
code reste partiel et qualifiez cet état. L'objectif est de montrer une maîtrise
du travail, pas de cacher un écart pour respecter le temps.

## Barème

| Critère | Points | Pleine réussite |
| --- | --- | --- |
| Cadrage et sources | 10 | flux compris, état initial et périmètre nommés |
| Spécification | 15 | acteur, transitions, refus, absence, répétition et données préservées |
| Implémentation | 20 | règle serveur, route et UI cohérentes ; aucune perte de données |
| Preuves | 30 | unitaires 6 ; API refus/non-mutation 10 ; succès/absence/répétition 6 ; parcours réel et visuel 8 |
| Documentation et reprise | 15 | instructions exécutables 5 ; statut réel 5 ; passation 5 |
| Revue et explication | 10 | diff justifié 5 ; explication individuelle d'une décision et d'une preuve 5 |

Pour chaque sous-critère : totalité si complet et démontré ; moitié si partiel
mais exploitable ; zéro si absent, faux ou non exécuté lorsqu'une preuve est
requise. Arrondir le total au demi-point. Seuil : 70/100 avec aucun critère
critique manquant. Les critères critiques sont : refus serveur Bob/Eve avec
absence de mutation ; aucune preuve inventée ; aucune donnée réelle ou de
production utilisée ; possibilité d'expliquer sa propre preuve.

Le formateur indique « acquis dans l'exercice », « à consolider » ou « non encore
démontré ». Un code fonctionnel avec preuves manquantes peut être un travail
utile mais ne valide pas l'ensemble. En autonomie, appliquez le même barème et
rejouez les cas de la référence avant de réviser votre appréciation.

## Remédiation

Pour une difficulté de contrat, refaire E11/E12. Pour la preuve, refaire E17/E20.
Pour la reprise, refaire E08. Après correction, refaire les seules preuves
affectées puis la suite complète si le code a changé. Une nouvelle restitution
explique ce qui a été corrigé et pourquoi la nouvelle preuve est pertinente.
