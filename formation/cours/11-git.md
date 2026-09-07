# M11 — Utiliser Git comme mémoire durable

Objectif : circonscrire une modification, relire ce qui sera conservé et
raisonner sur sa synchronisation sans écraser de travail.
Durée animée : 150 min. Exercices E21 et E22.

## Ce que vous autorisez

L'agent peut disposer d'outils de lecture, d'écriture, de terminal et de réseau.
Une mission précise décrit le résultat et les pouvoirs nécessaires : « corriger
la validation du titre dans le laboratoire local, sans service externe ». La
permission de lire le dépôt n'implique pas celle de publier, d'acheter un service
ou d'écrire dans une base de production. Les paramètres d'autorisation de l'outil
complètent les consignes ; les deux doivent correspondre au travail.

Commencez par un environnement local et des données fictives. Examinez une
demande d'autorisation en regardant l'action, la cible et l'effet attendu. Si le
test réclame un accès à une base de production, il faut changer le dispositif
de test. La sécurité réelle s'appuie sur les capacités disponibles, pas sur la
seule promesse « je ne ferai rien de dangereux ».

## Les trois états que Git distingue

![Fichier de travail, index et commit ; un push conserve le commit ailleurs](../illustrations/02-git.svg)

Le **répertoire de travail** contient les fichiers que vous éditez. L'**index**
est la sélection préparée pour le prochain commit. Un **commit** conserve un
instantané identifié de cette sélection dans l'historique local. Un **push**
transmet des commits à un dépôt distant configuré. Un fichier enregistré dans
l'éditeur n'est pas forcément indexé ; un commit local n'est pas forcément poussé.

Dans le laboratoire neuf, initialisez Git comme indiqué dans son README. Gardez
votre identité habituelle. Avant une mission, exécutez :

```bash
git status --short
git diff
```

`git diff` montre les modifications non indexées des fichiers suivis. Il ne
montre pas le contenu complet d'un nouveau fichier non suivi : `git status`
permet de le repérer, puis vous devez l'ouvrir. Pour voir la sélection du
prochain commit, utilisez `git diff --cached`. C'est une distinction centrale
de la documentation [Git](https://git-scm.com/docs/git-diff).

## Lire un diff avec une question

Imaginez une demande de correction du titre. Le diff ajoute une limite de
longueur, supprime un test d'autorisation et change une dépendance. La première
modification correspond à la mission. Les deux autres demandent une explication
et ne doivent pas être intégrées par habitude. Lisez les changements en demandant :
quel critère cette ligne sert-elle ? Quel comportement existant pourrait-elle
affecter ? Quelle preuve couvre ce changement ?

Une ligne supprimée apparaît avec `-`, une ligne ajoutée avec `+`. Ces signes ne
signifient pas « mauvais » et « bon ». Une suppression peut être la correction
juste ; un ajout peut introduire une régression. Une **régression** est un
comportement auparavant correct qui cesse de l'être après un changement.

Préparez uniquement les fichiers de l'unité :

```bash
git add domain.py test_contract.py BACKLOG.md
git diff --cached
git diff --cached --check
git commit -m "Corriger la validation des titres"
```

Ces commandes sont un exemple pour le moment où ces fichiers contiennent une
correction cohérente et vérifiée. Ne les exécutez pas prématurément au module 11.
Le contrôle `--check` détecte certains défauts d'espacement, pas les erreurs
fonctionnelles. Si l'index contient déjà le travail d'une autre personne,
identifiez-le avant de préparer votre propre sélection.

## Une petite unité permet une vraie revue

« Rendre l'application professionnelle » mélange trop de sujets. « Refuser les
titres hors limites, sans création, avec un message visible » possède un résultat
borné. Une unité peut toucher code, tests et documents : sa cohérence vient du
comportement livré, pas du nombre de fichiers. Après un checkpoint, notez si
l'unité est encore en cours. Une sauvegarde intermédiaire n'est pas une livraison.

Pour récupérer une erreur, commencez par identifier ce qui est suivi, indexé et
committé. Conservez les fichiers utiles avant toute opération qui retire des
modifications. Dans cette formation, on ne s'entraîne pas à effacer un dépôt.
Pour comparer deux versions, `git show IDENTIFIANT:domain.py` lit un ancien
fichier sans changer le code courant. L'identifiant vient de `git log --oneline`.

La méthode P2Enjoy choisit un agent principal comme seul éditeur et conserve la
branche courante ; le worker cible `main`. Ce sont ses conventions d'organisation.
Elles ne sont pas des propriétés de Git. Dans un autre collectif, la stratégie
de branches doit être explicitement définie avant de demander à l'agent d'agir.

## Faire et vérifier

### Synchroniser sans confondre les états

Un **remote** est un nom associé à une adresse de dépôt ; `origin` est une
convention, pas un serveur universel. `main` est une branche locale ; `HEAD`
désigne habituellement le commit courant de la branche active. `origin/main`
est une référence conservée sur votre machine, décrivant ce que Git a observé
de cette branche distante lors de la dernière récupération. Elle n'est pas
une consultation en direct du serveur.

Avant de synchroniser un vrai projet, lire sa stratégie de branches, vérifier
`git status --short`, `git branch --show-current` et `git remote -v`. Ne pas
diffuser une adresse contenant un jeton ; corriger cette configuration par le
canal de sécurité du projet. Si la destination ou son effet de déploiement est
inconnu, s'arrêter avant le push. Dans notre laboratoire, aucun remote n'est
nécessaire et la séquence suivante est un exemple expliqué, pas une invitation
à publier son dépôt.

```bash
git fetch origin
git log --oneline --left-right HEAD...origin/main
git diff HEAD origin/main
```

`fetch` récupère des objets et actualise les références de suivi concernées ;
il ne fusionne pas ces changements dans vos fichiers de travail. Le log compare
les commits exclusifs à chaque côté : `<` local, `>` suivi distant. Le diff
compare les contenus des deux états. Voir la documentation de
[git fetch](https://git-scm.com/docs/git-fetch).

| Observation après fetch | Décision sûre |
| --- | --- |
| Aucun commit exclusif | Les références comparées coïncident ; vérifier aussi les fichiers non committés |
| Seulement `>` : la branche locale est en retard | Sur un arbre propre et selon le contrat du projet, `git merge --ff-only origin/main` avance sans créer de fusion |
| Seulement `<` : commits locaux en avance | Relire et prouver, puis pousser uniquement vers la destination autorisée |
| `<` et `>` : histoires divergentes | Conserver les deux travaux ; comprendre les changements et appliquer la stratégie de fusion/rebase du collectif, pas de push forcé improvisé |

`--ff-only` refuse une divergence plutôt que de fabriquer une fusion. Si une
fusion autorisée produit un conflit, Git marque les portions à arbitrer : ce
n'est pas une invitation à garder aveuglément « notre » version. Lire les deux
intentions, résoudre dans le périmètre, relancer les preuves, puis terminer
l'opération documentée. Les possibilités dépendent de l'opération engagée ;
le message de `git status` et la documentation de
[git merge](https://git-scm.com/docs/git-merge) guident la suite. Conserver les
modifications non committées avant toute opération susceptible de les retirer.

Après une synchronisation qui change le code, les preuves antérieures ne
qualifient plus automatiquement le nouvel état. Relancer celles affectées.
Un push rejeté car le distant a avancé demande une nouvelle lecture et
synchronisation, pas `--force`. Le workflow de ce socle reste sur sa branche
courante et définit ses propres gardes ; d'autres équipes utilisent des branches
de travail et des revues de fusion.

### Exemple corrigé de reprise

Situation sur table : A est commun. Votre branche contient A–B (correction des
titres), le dépôt distant A–C (changement de route). Votre `origin/main` vaut
encore A. Avant fetch, une comparaison avec cette référence ne voit pas C.
Après fetch, le log indique `< B` et `> C` : divergence. B et C touchent peut-être
la même création ; demander une intégration conforme au workflow, lire le diff,
rejouer validation et API, puis seulement publier si cela est autorisé. Un
`merge --ff-only` ne peut pas résoudre ce cas et doit refuser.

Si B est déjà partagé mais incorrect, une nouvelle correction explicite garde
l'historique compréhensible. `git revert IDENTIFIANT` peut créer un commit
inverse, mais demande aussi lecture, gestion éventuelle des conflits et preuves ;
ce n'est pas un retour magique des données de production. Voir
[git revert](https://git-scm.com/docs/git-revert). Pour une simple consultation,
préférer `git show` ; `stash` met de côté du travail non committé et ne retire
pas B de l'historique. Ne pas utiliser un effacement de l'arbre pour fabriquer
une référence de test « avant ».

### Exercices et point de sortie

E21 produit un nouveau checkpoint et l'observation fichier/index. E22 fait
relire un changement trop large et qualifier les permissions. Extension :
expliquer comment un diff indexé peut être correct alors que le fichier ouvert
dans l'éditeur contient une nouvelle modification non indexée.

Q11.1 : le fichier est corrigé après `git add` ; le commit contiendra-t-il cette
dernière correction ? Q11.2 : un commit local protège-t-il d'une perte de la machine ?
Q11.3 : `git diff --check` réussi prouve-t-il que Bob ne peut pas clore la demande
d'Alice ? Corrigés dans [CORRIGES](../CORRIGES.md).

Votre point de sortie : vous savez nommer la tâche autorisée, lire sa sélection
Git et distinguer checkpoint, preuve et publication. Vous savez aussi pourquoi
fetch, intégration locale et push sont trois opérations distinctes.
