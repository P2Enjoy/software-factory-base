# M12 — Orchestrer plusieurs agents

Objectif : déléguer une mission indépendante et garder un responsable de l'unité.
Durée animée : 150 min. Exercices E23 et E24.

## Partir d'un travail qui mérite une délégation

Vous disposez maintenant d'une unité spécifiée, d'un code et de preuves.
Certaines lectures peuvent être confiées à un autre agent : suivre une dépendance
inconnue, relire une règle de droits ou analyser la sortie d'un test. La délégation
est utile lorsque la mission est isolable et apporte plus qu'elle ne coûte en
contexte, coordination et vérification.

Demander à trois agents d'effectuer une même petite correction crée trois
versions à rapprocher. Leur nombre ne garantit ni une meilleure décision ni
une preuve indépendante. Une revue qui lit le même contrat peut apporter un
regard utile ; son résultat doit encore être vérifié par le responsable.

![Le principal reçoit les constats de trois rôles bornés](../illustrations/09-roles.svg)

Le socle choisit un agent principal comme seul éditeur des fichiers suivis et
seul opérateur Git modificatif. Les rôles auxiliaires restent dans la mission.
Ils ne choisissent pas le produit, ne clôturent pas l'unité et ne créent pas
de branche ou de sous-agent supplémentaire. Cette organisation est le choix
de méthode étudié ici, pas une propriété de tous les systèmes multi-agents.

## Les trois rôles

L'**explorateur** répond à une incertitude de périmètre ou de flux. Exemple :
« Où une clôture peut-elle entrer dans l'application et où le droit est-il
vérifié ? » Son livrable contient références, chemin réel et inconnues. Il ne
modifie rien pour rendre sa description vraie.

Le **relecteur** examine un changement cohérent contre son contrat. Exemple :
« Le refus Bob/demande 1 préserve-t-il les données ? » Chaque constat indique
fichier, ligne ou symbole, conséquence et preuve utile. L'absence de défaut
trouvé n'est pas une garantie absolue ; le rapport nomme ce qu'il n'a pas examiné.

Le **vérificateur** exécute une commande ciblée sur un arbre stabilisé. Certains
outils produisent caches, rapports, captures ou builds : ces artefacts attendus
sont autorisés dans le cadre défini. Les sources et l'état Git ne sont pas
modifiés. L'état avant/après permet de détecter un effet inattendu.

## Écrire le contrat de mission

Le contexte transmis doit suffire à la question. Une mission nomme son objectif,
son périmètre, les sources précises, les pouvoirs et le résultat attendu. Pour
une preuve : commande documentée, état requis, artefacts et limite de temps.
Un mandat « vérifie tout » est difficile à achever et à interpréter.

Exemple de revue :

> Lis BACKLOG.md DEM-02, DAT.md Contrats, can_close dans domain.py et la route
> de clôture dans app.py. Lecture seule. Vérifie l'origine du rôle et du
> propriétaire, l'ordre contrôle/UPDATE et le cas Bob visant Alice. Rends des
> constats sourcés, les limites de ta lecture et une preuve minimale proposée.

Exemple de vérification : la suite unitaire et API du laboratoire sur une copie
stable, avec base temporaire et port local choisi par le système. Le principal
doit vérifier que ces écritures temporaires correspondent au périmètre autorisé.
L'indisponibilité du rôle n'empêche pas de réaliser la même vérification soi-même.

## Recevoir et examiner le résultat

Un agent écrit « l'autorisation manque ». Demandez quelle route, quel acteur
et quelle ressource. Ouvrez le code cité : la règle est-elle appelée avant la
mutation ? Reproduisez le cas avec le dispositif prévu si nécessaire. Le
principal décide alors de corriger, ou explique avec une source pourquoi le
constat ne s'applique pas. La synthèse relève de sa responsabilité.

Si un vérificateur produit un fichier suivi modifié, ne nettoyez pas aveuglément.
Identifiez le fichier et la cause ; une commande mal choisie peut réécrire un
lockfile ou un snapshot. L'arbre n'était peut-être pas réellement stable. Cette
anomalie doit être résolue avant de présenter le résultat comme une preuve du
changement prévu.

## Faire et vérifier

E23 réalise une revue bornée. E24 prépare puis interprète une mission de preuve
avec un artefact inattendu fictif. Extension : mesurer le temps de lecture,
d'exécution et de synthèse afin de comparer délégation et travail direct.

Q12.1 : quel rôle décide de la correction ? Q12.2 : pourquoi stabiliser l'arbre
avant une preuve déléguée ? Q12.3 : un rôle indisponible bloque-t-il l'unité ?
Voir [CORRIGES](../CORRIGES.md).

Point de sortie : chaque mission est bornée, son résultat est vérifiable et
personne ne confond délégation et transfert de responsabilité.
