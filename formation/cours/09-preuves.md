# M9 — Construire la preuve

Objectif : corriger une cause et montrer ce que chaque vérification établit.
Durée animée : 150 min. Exercices E17 et E18.

## Lire un rouge sans paniquer

Dans le laboratoire de départ, la suite contient sept tests. Quatre échouent :
les deux défauts sont chacun détectés au niveau unitaire et par l'API. Le nombre
de rouges ne correspond donc pas au nombre de causes. Une erreur avant le
lancement du test, par exemple un module introuvable, est un défaut de dispositif.
Elle ne démontre aucun résultat produit.

Exécutez `python3 -m unittest -v`. Repérez le nom du test, la ligne d'assertion,
la valeur attendue et la valeur obtenue. Dans le cas du titre vide, la réponse
HTTP est 201 alors que le contrat exige 400. Rejouez seulement l'unité concernée :

```bash
python3 -m unittest -v test_contract.DomainContract.test_title_bounds_and_normalization
```

Le test doit échouer sur la version de départ. Ouvrez `validate_title` : le code
retire les espaces mais vérifie uniquement la longueur maximale. La correction
doit porter sur la plage complète. Une condition spéciale pour trois espaces
laisserait passer `ab` ; la table du module 6 prévient ce faux remède.

## Une correction avec sa preuve

```python
title = value.strip()
if not 3 <= len(title) <= 80:
    raise ValueError("Le titre doit contenir entre 3 et 80 caractères.")
return title
```

Conservez aussi le contrôle du type avant `strip`. Le test ciblé devient vert.
Rejouez ensuite le test API de validation, puis la suite complète. Les deux
tests d'autorisation restent rouges tant que DEM-02 n'est pas corrigée. Votre
compte rendu doit le dire : DEM-01 corrigée ; DEM-02 encore en cours. Un objectif
de « tout vert » n'autorise pas à désactiver les tests qui gênent.

Une preuve utile associe code testé, état des données, commande, résultat et
contrat. Un simple « OK » dans le chat est impossible à auditer. Enregistrez la
sortie utile et son contexte dans votre dossier de preuves. Si vous relancez
après une autre modification, actualisez le résultat.

## Quatre regards complémentaires

![Quatre preuves complémentaires pour une même règle](../illustrations/04-preuves.svg)

Le **test unitaire** exerce une petite règle isolée : `validate_title` refuse une
entrée hors limites. Il est rapide et localise bien une erreur. Le **test
d'intégration** fait collaborer plusieurs éléments. Ici, le test API démarre
un vrai serveur et une vraie base SQLite temporaire ; il vérifie la réponse et
les données. Il peut révéler une route qui oublie d'appeler la bonne fonction.

Le **test E2E**, de bout en bout, parcourt le système par les actions de son
utilisateur. Dans notre cas : accueil, choix du profil, création, message puis
liste. Il montre que l'action est découvrable et que les couches fonctionnent
ensemble. L'**inspection visuelle** regarde le rendu réel : texte coupé, erreur
illisible, focus invisible, bouton hors écran. Un script peut passer à côté de
ces défauts s'il ne les mesure pas.

Le test API qui contourne l'interface pour éprouver une autorisation et le test
visuel qui suit le parcours canonique ont deux objets différents. Faites les
deux. Ne présentez pas l'appel direct comme une validation de l'ergonomie.
La documentation [Playwright](https://playwright.dev/python/docs/writing-tests)
illustre les actions et assertions dans le navigateur ; le kit de production
utilise cet outil pour vérifier l'atelier de référence.

## Bien choisir les données

Un **seed** est un ensemble de données initiales reproductibles. Les demandes
1, 2 et 3 couvrent ici plusieurs propriétaires et statuts. Les tests créent leur
base temporaire et ne dépendent pas de la base où vous avez exploré. Sans cet
isolement, un test peut réussir uniquement parce qu'un exercice précédent a
préparé son état. Une preuve doit expliquer d'où viennent ses données.

Un **mock** simule un composant. Il peut servir pour un fournisseur inaccessible,
mais son comportement doit correspondre au contrat réel. Simuler la base pour
prouver une contrainte de base, ou simuler un refus pour prouver les droits du
serveur, retire justement l'élément à vérifier. Le laboratoire emploie SQLite
réel pour les preuves d'intégration.

## Diagnostiquer une régression

Si une preuve échoue après votre correction, vérifiez si elle passait avant sur
un état comparable. Une commande `git stash` retire des modifications non
committées ; elle n'annule pas un commit qui contient déjà la correction.
Comparez explicitement l'identifiant du code testé. Dans le laboratoire, deux
dossiers neufs « départ » et « référence » permettent une comparaison sans
effacement. Une comparaison d'environnement différent doit être qualifiée.

En cas d'échec, reproduisez, identifiez l'attendu, localisez la cause, gardez un
test qui la détecte, corrigez puis rejouez les preuves affectées. N'ajoutez pas
un délai arbitraire ou une capture d'exception vide pour obtenir un succès.

## Faire et vérifier

E17 corrige DEM-01 avec une séquence rouge/vert. E18 réalise le parcours visuel,
construit le dossier de preuves et qualifie les rouges restants. Extension :
ajouter un test qui observe la persistance après un redémarrage réel du serveur.

Q9.1 : un serveur qui ne démarre pas constitue-t-il une preuve de régression ?
Q9.2 : que ne prouve pas un test unitaire de validation ? Q9.3 : pourquoi une
capture ne remplace-t-elle pas le test de refus direct ? Voir les corrigés.

Point de sortie : DEM-01 est corrigée et ses preuves sont identifiables ; les
limites sont écrites, en particulier l'autorisation encore défaillante.
