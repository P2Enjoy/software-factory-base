# Registre des incohérences

Registre des défauts constatés hors de l'unité en cours, au sens de `CLAUDE.md`
§5. Chaque entrée porte le constat, sa mesure, les fichiers ou règles concernés
et son état. Une entrée quitte le registre lorsqu'elle est corrigée, tranchée
sans changement ou convertie en unité de travail.

Les défauts propres aux supports de formation constatés lors de l'étude du
18 septembre 2026 ne figurent pas ici : ils sont listés dans
`formation/REVISION.md` (section 3.3) et convertis en unités de son plan de
révision.

## INC-01 : `docs/AUTOMATION.md` absent du dépôt mais exigé et cité

Constat : le fichier `docs/AUTOMATION.md` n'a jamais été committé sur aucune
branche (`git log --all -- docs/AUTOMATION.md` ne renvoie rien), alors qu'il est
présent dans `formation/exports/formation-complete.zip` (entrée
`docs/AUTOMATION.md`), listé parmi les fichiers du socle à empaqueter par
`formation/outils/emballer.py` (l. 19), qui s'arrête en erreur s'il manque
(l. 35 à 36), cité comme contrat normatif par `README.md` (sections
« Repository contents » et « docs/AUTOMATION.md, .githooks/ et
scripts/git-hooks/ »), et référencé par les marqueurs `@spec` de
`.github/workflows/pages.yml` (l. 1, ancre `#extension-et-ci`), de
`scripts/git-hooks/*` et des définitions de rôles (`#subagents`).

Mesure : le kit ne peut pas être reconstruit depuis un clone ; les ancres citées
par les marqueurs de traçabilité ne peuvent pas être vérifiées dans le dépôt.

Origine connue : le commit `549d475` a ajouté ce chemin aux exclusions Git avec
d'autres fichiers « générés par la méthode, à ignorer dans le dépôt gabarit »,
puis `ce9aaf2` a déplacé ces exclusions vers la configuration locale du poste du
responsable. L'intention d'exclure ce fichier du gabarit et les usages qui
l'exigent se contredisent.

État : ouverte. Hors périmètre de la révision des supports de formation, par
instruction explicite du responsable (la méthode et ses implémentations ne sont
pas modifiées). Décision attendue du responsable : committer `docs/AUTOMATION.md`
dans le gabarit, ou retirer sa dépendance de `emballer.py` et remplacer les
ancres citées.

## INC-02 : l'arborescence du `README.md` racine cite des fichiers absents

Constat : la section « Repository contents » de `README.md` liste
`CHANGELOG.md`, `docs/AUTOMATION.md` et `docs/JOURNAL.md` ; aucun de ces
fichiers n'existe dans le dépôt ni dans son historique. La table « Global versus
project specific files » et la section « docs/AUTOMATION.md » y renvoient
également.

Mesure : `ls CHANGELOG.md docs/AUTOMATION.md docs/JOURNAL.md` échoue sur les
trois chemins ; `git log --all` ne les connaît pas.

État : ouverte. Hors périmètre de la révision des supports de formation, par
instruction explicite du responsable. Liée à INC-01 : selon la décision prise
pour `docs/AUTOMATION.md`, le README est soit complété par les fichiers, soit
corrigé pour décrire l'arborescence réelle du gabarit.
