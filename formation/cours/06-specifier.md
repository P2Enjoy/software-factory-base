# M6 — Spécifier avant d'implémenter

Objectif : donner à l'agent un résultat vérifiable avant qu'il implémente.
Durée animée : 150 min. Exercices E11 et E12.

## Du souhait au comportement

« Améliore les titres » laisse plusieurs réponses plausibles : modifier leur
police, les raccourcir à l'affichage ou limiter leur saisie. Une spécification
fixe ce qui doit arriver dans des situations observables. Elle décrit la personne,
son action, l'état initial, le résultat et les refus. Elle permet de dire plus
tard pourquoi une sortie est correcte.

Pour DEM-01, le besoin est d'éviter les demandes sans intitulé exploitable. Le
contrat retenu est précis : après suppression des espaces aux extrémités, un
titre doit avoir entre 3 et 80 caractères ; sinon le serveur renvoie HTTP 400,
ne crée aucune ligne et l'interface permet de corriger la saisie. Cette règle
définit aussi qui fait autorité : le serveur. Un attribut HTML peut aider à la
saisie, mais une requête directe doit subir la même validation.

## Écrire des exemples qui discriminent

| Entrée | Résultat attendu | Ce que le cas vérifie |
| --- | --- | --- |
| `abc` | acceptée | borne basse incluse |
| `ab` | refusée | valeur juste sous la borne |
| trois espaces | refusée, aucune création | normalisation avant validation |
| `  Bonjour  ` | stockée `Bonjour` | règle de trim |
| 80 lettres | acceptée | borne haute incluse |
| 81 lettres | refusée | dépassement |
| nombre ou absence de titre | refusée | type de donnée |

Un exemple utile départage des implémentations. « Le titre fonctionne » ne le
fait pas. Tester uniquement `Bonjour` ne distingue pas la version de départ du
corrigé. Le mot **oracle** désigne ce qui vous permet de déterminer le résultat
attendu d'un test : ici, le contrat et cette table. L'agent ne doit pas inventer
l'oracle à partir du code qu'il vient d'écrire.

Le laboratoire compte les caractères comme Python avec `len` après `strip`.
Pour des textes contenant certains emoji ou accents combinés, le nombre de
points de code peut différer du nombre de symboles perçus. Cette précision est
documentée dans le DAT. On peut choisir un autre contrat dans un produit ; il
faut alors adapter validation et tests ensemble.

## Découper verticalement

![Une unité relie besoin, comportement, code, tests et documents](../illustrations/03-trace.svg)

Une tranche **verticale** traverse les couches nécessaires à un petit résultat
utilisateur. DEM-01 contient règle serveur, effet sur la base, message d'erreur,
tests et documentation. Une tranche « faire tout le backend » peut consommer
beaucoup de temps sans livrer un parcours utilisable. Le bon découpage permet
de prouver une unité avant d'en commencer une autre.

Pour DEM-02, séparez la matrice des droits de la mécanique d'affichage. Alice
clôt toutes les demandes. Bob clôt les siennes. Eve ne clôt rien. Écrivez un
cas de refus où Bob vise la demande d'Alice et ajoutez « la demande reste ouverte ».
Un simple statut HTTP 403 serait insuffisant si le serveur modifiait la base
avant de renvoyer l'erreur.

## Donner une référence stable

Le backlog nomme l'unité DEM-01. Le DAT décrit le flux et les données. Les tests
doivent indiquer ce contrat. La méthode du socle utilise les marqueurs `@spec`
et `@verifies`. Dans un dépôt applicatif qui adopte le socle, on pourra écrire :

```python
# @spec docs/BACKLOG.md#dem-01 | docs/DAT.md#validation
# @verifies docs/BACKLOG.md#dem-01 | docs/DAT.md#validation
```

Les chemins de cet exemple doivent exister dans le projet cible. Dans le petit
laboratoire, BACKLOG.md et DAT.md sont à la racine : adaptez les références en
conséquence. La syntaxe vérifiable ne garantit pas que le commentaire cite la
bonne règle ; la relecture doit examiner son sens.

Une décision durable est écrite dès qu'elle est prise. Le journal en conserve le
motif ; la spécification porte le comportement courant. Lorsque le comportement
change, la spécification est réécrite pour décrire la nouvelle réalité. Le journal
peut conserver la chronologie sans laisser deux règles contradictoires actives.

## Une mission d'implémentation complète

> Implémente DEM-01 selon BACKLOG.md et DAT.md. Commence par lire le chemin de
> création existant. Confirme les cas de la table de validation. Conserve les
> données déjà créées. Corrige uniquement la validation et les éléments nécessaires
> à son retour d'erreur. Exécute les tests ciblés, puis le parcours de création.
> Rends le diff, les commandes, leurs résultats et les limites restantes.

Le prompt est un point d'entrée vers des références durables. Les variantes de
phrasing ne remplacent pas un comportement attendu bien défini. Un détail qui
change le produit et ne peut pas se déduire des sources mérite une décision
explicite ; une limite déjà fixée dans le contrat doit être appliquée.

## Faire et vérifier

E11 transforme une demande vague en contrat. E12 construit la matrice de droits
et le découpage des unités. Extension : préciser le comportement lorsque deux
utilisateurs tentent de clore la même demande ; comparer « déjà fermée » en
erreur et « reste fermée » sans effet supplémentaire.

Q6.1 : pourquoi tester 2, 3, 80 et 81 caractères ? Q6.2 : quelle preuve manque à
« le serveur a répondu 403 » ? Q6.3 : un commentaire `@spec` suffit-il à établir
la conformité ? Réponses dans [CORRIGES](../CORRIGES.md).

Point de sortie : un autre participant doit pouvoir écrire les tests de votre
spécification sans vous demander ce que « correct » signifie.
