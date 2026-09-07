# M15 — Assembler la software factory

Objectif : reconstruire la configuration finale et expliquer chaque pièce.
Durée animée : 150 min. Exercices E29 et E30.

## Revenir aux problèmes rencontrés

Depuis le début du cours, vous avez appris à distinguer une proposition et
une action, cadrer un résultat, lire un flux, conserver une décision, spécifier
des exemples, réaliser une unité, reproduire un environnement et produire des
preuves. Vous avez ensuite encadré les droits, Git, la délégation et les
automatismes. L'usine assemble maintenant ces acquis.

![Assemblage final des contrats, du contexte, des preuves et de l'automatisation](../illustrations/15-factory.svg)

Le dépôt n'impose pas une application ou une architecture métier. Il fournit
une base de méthode. Une application dérivée doit ajouter son propre besoin,
ses contrats, sa stack, ses commandes et ses preuves. Copier les fichiers sans
adapter les informations locales ne donne pas un projet opérationnel.

## Relier une pièce à sa fonction

| Pièce du socle | Problème traité | Acquisition préparatoire |
| --- | --- | --- |
| CLAUDE.md | conventions durables de décision, édition et preuve | M1 à M11 |
| AGENTS.md | point d'entrée de lecture pour Codex | M3, M5 |
| CLAUDE_PROJECT.md dans le projet cible | contexte produit explicite | M4, M5, M8 |
| README/DAT/BACKLOG/JOURNAL | exécution, architecture, unités et reprise | M2 à M8 |
| Design system et compagnon local | cohérence et validation de l'interface | M5, M9, M10 |
| Rôles spécialisés | lectures et preuves bornées | M12 |
| AUTOMATION et hooks | invariants mécaniques | M11, M13 |
| CloudWorker et .routine | cycle planifié et reprise | M7, M8, M14 |

Pour chaque fichier, exigez une phrase de fonction et une limite. Exemple :
« Le hook repère la forme d'une référence, pas sa pertinence. » Cette limite
indique le travail de revue encore nécessaire. Un fichier qui n'a pas de
responsabilité distincte risque de recopier une règle et de diverger.

## Une adoption progressive et vérifiable

Commencez par un dépôt d'exercice ou un projet neuf autorisé. Établissez son
README et ses commandes. Ajoutez une unité stable et une spécification.
Reliez le contexte local au point d'entrée de l'agent. Effectuez une petite
unité et vérifiez code, données, parcours et documentation. Activez les
garde-fous après lecture de leur contrat et adaptation des contrôles de projet.

L'identité Git est celle du responsable déclarée dans le dépôt, sans surcharge.
La méthode choisit sa stratégie de branches ; le worker du socle impose main
et origin/main dans son contexte. La CI distante et l'ordonnanceur restent à
configurer séparément sur des services autorisés. Aucune présence de fichier
ne certifie leur activation ou leur bon fonctionnement.

## Comparer l'intention et l'état réel

Dans cette édition, le socle est un aboutissement de méthode en cours de
stabilisation. Certains passages du worker portent encore des paramètres
d'hôte et des procédures qu'il faut examiner dans leur contexte. Le cours
ne les transforme pas en prérequis universels. Il enseigne comment les repérer
et demander la preuve qui permet de les appliquer.

La publication de recherche antérieure mentionnée par le responsable n'a pas
été fournie dans le contexte accessible. Le présent support ne lui attribue
aucune conclusion. La comparaison avec cette publication et sa révision
après stabilisation du dépôt appartiennent à une étape éditoriale ultérieure.
Cela ne retire rien aux manipulations et corrigés complets de ce parcours.

## Transfert vers votre projet

Choisissez une petite unité réelle et non sensible. Écrivez son acteur, ses
critères et son périmètre. Identifiez la route ou fonction, les données et
les preuves. Faites produire un changement, relisez-le et testez une reprise
sans votre ancienne conversation. Mesurez le temps, les erreurs évitées et
les points restés dépendants d'une explication orale.

Votre premier objectif de transfert est cette unité prouvée. L'automatisation
du projet entier vient lorsque les commandes, les contrats et les retours
d'erreur sont suffisamment reproductibles pour être confiés au protocole.
L'assemblage final doit conserver une responsabilité compréhensible.

## Faire et vérifier

E29 reconstruit la carte du dépôt de mémoire avant de la comparer aux fichiers.
E30 prépare une adoption dans le laboratoire et justifie les pièces retenues.
Extension : identifier une règle locale candidate à devenir générale et en
retirer tout vocabulaire produit avant de la proposer à la méthode.

Q15.1 : quelles informations manque-t-il après une simple copie du socle ?
Q15.2 : qui configure la CI et l'ordonnanceur réels ? Q15.3 : quel résultat
permet d'évaluer votre première adoption ? Voir [CORRIGES](../CORRIGES.md).

Vous êtes prêt pour l'évaluation finale DEM-03 : livrer une petite évolution
et montrer que ses contrats, ses preuves et sa reprise sont cohérents.
