# CloudWorker

Prompt de la tâche planifiée « CloudWorker », exécutée automatiquement toutes les
heures sur ce dépôt.

Ce document conserve le texte intégral du prompt, afin qu'une consigne récurrente ne
dépende pas de la seule mémoire de contexte d'un agent.

---

Tu travailles sur le dépôt courant, quel qu'il soit.

Ce document est GÉNÉRIQUE : il décrit la méthode de travail d'une session planifiée, jamais
la pile d'un produit particulier. Chaque fois qu'il renvoie à une commande — démarrage,
seed, preuves —, la commande exacte est celle que le dépôt documente dans son "README.md",
son "Makefile" ou ses scripts. Tu la lis dans le dépôt ; tu ne la supposes pas, et tu ne
reprends aucune commande d'un autre projet.

`CLAUDE.md` définit les règles générales de la MÉTHODE de travail de l'agent ; ce document ajoute
uniquement le cycle propre au worker planifié, et `docs/AUTOMATION.md` décrit ses garde-fous
exécutables. Tous les autres fichiers du dépôt portent le contexte du projet courant. Ces documents
de méthode ne sont modifiés que sur instruction explicite du responsable, et ils s'écrivent d'un seul trait : une
règle y figure une fois, énoncée au présent, sans historique de ses versions ni mention annulant
une règle antérieure. Une règle qui évolue est réécrite sur place ; la trace du changement va au
journal du projet.

## 0. TU DOIS COMMITTER ET POUSSER, SINON TOUT EST PERDU

LIS CECI EN PREMIER, C'EST LA RÈGLE QUI CONDITIONNE TOUTES LES AUTRES.

Cette tâche s'exécute toutes les heures, et CHAQUE EXÉCUTION PART D'UN CHECKOUT NEUF. Ta session n'est pas conservée. Tout ce que tu écris sans le POUSSER sur "origin/main" est définitivement perdu à la fin de ta session, et l'exécution suivante repartira exactement du même point pour refaire exactement le même travail. Une boucle qui ne pousse pas n'avance jamais.

En conséquence, et sans exception :

- Committe et pousse au fil de l'eau, pas seulement à la fin : dès qu'un morceau cohérent tient debout, par exemple une spécification écrite, une migration qui s'applique ou un écran qui rend, tu committes et tu pousses. **Tu n'attends PAS d'avoir prouvé pour pousser.** Ta session peut être interrompue à tout instant.
- Ne termine JAMAIS ta session sur du travail non poussé.
- Ne termine JAMAIS ta session sur une branche autre que "main".
- Ne termine JAMAIS ta session en HEAD détaché.
- Avant de conclure, attends tous les sous-agents éventuels puis exécute obligatoirement
  `scripts/git-hooks/check-session`, selon la procédure du §1.7.
- La session ne peut être considérée comme terminée que lorsque cette garde réussit. Elle exige
  notamment un arbre propre et l'égalité exacte entre `HEAD` et `origin/main`, sans avance, retard
  ni divergence.

Si tu n'as pas le temps de finir une unité, ce n'est pas grave : committe et pousse l'état intermédiaire cohérent, mets à jour "docs/BACKLOG.md" pour dire exactement où tu en es et ce qui reste, et pousse. C'est la seule façon dont l'exécution suivante pourra reprendre là où tu t'es arrêté.

Si "git push" échoue, récupère et rejoue :

```
git fetch origin
git pull --rebase origin main
```

Résous les conflits SUR PLACE, puis pousse.

Ne renonce jamais à pousser, et ne contourne jamais un conflit par une branche.

**L'ORDRE DE LA SESSION, EN UNE LIGNE**, détaillé au §3.2 et au §4.3 :

```
Git → Docker → pile + seed → choisir l'unité → lire et écrire la spéc COMPLÈTE → committer
     → coder → committer et pousser au fil de l'eau → prouver SON unité
     → [fin de session] campagne complète → boucle de correction → committer, pousser
     → journal, backlog, garde Git, compte rendu
```

**La campagne complète de preuves ne s'exécute JAMAIS en ouverture de session.** Elle dure quarante à
soixante-dix minutes ; lancée avant d'avoir choisi une unité, elle consomme la session entière pour
mesurer un dépôt que tu n'as pas encore modifié. Elle est une opération de FIN, suivie d'une boucle
de correction.

### 0.1. ANNONCE D'OUVERTURE, AVANT TOUT AUTRE AFFICHAGE

La toute première chose que tu ÉCRIS, avant tout diagnostic, toute commande et tout
autre message, est cette ligne, seule et telle quelle :

```
A NEW SCHEDULED SESSION HAVE BEEN STARTED
```

suivie immédiatement de l'horodatage courant, relevé sur la machine et non
supposé :

```
date -Is
```

Exemple de ce que tu affiches :

```
A NEW SCHEDULED SESSION HAVE BEEN STARTED
2026-08-20T14:32:07+00:00
```

Motif : ces sessions s'enchaînent automatiquement et leurs sorties se lisent à la
suite. Sans cette borne, on ne sait plus où finit une exécution et où commence la
suivante, ni quand chacune a eu lieu — et deux comptes rendus se confondent.

## 1. BRANCHE : QUEL QUE SOIT L'ÉTAT INITIAL, TU DOIS TRAVAILLER ET FINIR SUR "main"

L'environnement peut démarrer dans n'importe lequel de ces états :

- HEAD détaché ;
- branche "main" ;
- branche temporaire créée par l'infrastructure ;
- branche portant un nom inconnu.

C'est NORMAL.

AUCUN de ces états n'est une raison de t'arrêter.

La branche de démarrage n'est qu'un état technique fourni par l'infrastructure. Elle ne définit jamais la branche sur laquelle tu dois travailler.

Ton objectif Git est invariant :

1. préserver tout éventuel travail local qui ne serait pas encore présent sur "origin/main" ;
2. rattacher le dépôt à la branche locale "main" ;
3. synchroniser "main" avec "origin/main" ;
4. effectuer tout le travail exclusivement sur "main" ;
5. pousser tout travail sur "origin/main" ;
6. terminer obligatoirement avec HEAD attaché à "main".

### 1.1. INITIALISATION GIT OBLIGATOIRE

Ton PREMIER geste dans le dépôt est :

```
git fetch origin main
git branch --show-current
git status --short
git log origin/main..HEAD --oneline
```

Ces commandes servent à DIAGNOSTIQUER l'état initial.

La sortie de :

```
git branch --show-current
```

est informative uniquement.

Une branche différente de "main" ne doit JAMAIS provoquer l'arrêt de la session.

### 1.2. MODIFICATIONS NON COMMITTÉES PRÉSENTES AU DÉMARRAGE

Si :

```
git status --short
```

n'est pas vide, considère ces modifications comme potentiellement importantes.

Ne les détruis JAMAIS avec :

```
git reset --hard
git clean
git checkout -- .
git restore .
```

ou toute autre commande destructrice équivalente.

Préserve-les temporairement avec :

```
git stash push -u -m "sauvegarde-etat-initial-worker"
```

Puis poursuis la procédure de rattachement à "main".

Une fois correctement positionné sur "main", restaure immédiatement :

```
git stash pop
```

En cas de conflit, résous les conflits SUR "main".

Committe ensuite le travail récupéré et pousse-le sur "origin/main".

### 1.3. AUCUN COMMIT LOCAL À SAUVER

Si :

```
git log origin/main..HEAD --oneline
```

est vide, aucun commit spécifique à l'état initial n'a besoin d'être conservé.

Peu importe que tu sois actuellement :

- en HEAD détaché ;
- sur "main" ;
- sur une branche temporaire ;
- sur une branche quelconque créée par l'infrastructure.

Rattache immédiatement le dépôt à "main" :

```
git checkout -B main origin/main
git pull --rebase origin main
```

Puis vérifie :

```
test "$(git branch --show-current)" = "main"
```

Si cette vérification échoue, corrige l'état Git.

Tu ne commences aucune tâche métier tant que :

```
git branch --show-current
```

ne renvoie pas exactement :

```
main
```

### 1.4. DES COMMITS LOCAUX EXISTENT AU-DESSUS DE "origin/main"

Si :

```
git log origin/main..HEAD --oneline
```

n'est PAS vide, ces commits constituent du travail potentiellement réel qu'une exécution précédente ou que l'environnement n'a pas encore poussé.

C'est une urgence.

Tu dois sauver ces commits AVANT :

- de lire le backlog ;
- de démarrer Docker ;
- de modifier un fichier ;
- de commencer une nouvelle unité.

Rattache ces commits à "main" :

```
git checkout -B main HEAD
git pull --rebase origin main
git push -u origin main
```

En cas de conflit pendant le rebase :

1. résous les conflits dans le dépôt courant ;
2. ajoute les fichiers résolus avec "git add" ;
3. poursuis avec :

```
git rebase --continue
```

4. répète jusqu'à la fin du rebase ;
5. pousse sur "origin/main".

Tu ne commences RIEN d'autre tant que :

```
git log origin/main..HEAD --oneline
```

n'est pas vide.

Après récupération, vérifie :

```
git branch --show-current
git status --short
git log origin/main..HEAD --oneline
```

Le résultat attendu est :

```
branche : main
status : vide
commits locaux non poussés : aucun
```

Mentionne dans ton compte rendu final tout travail antérieur que tu as dû récupérer.

### 1.5. RÈGLES ABSOLUES DE BRANCHE

Une fois l'initialisation terminée :

- Travaille EXCLUSIVEMENT sur "main".
- Tout commit est créé sur "main".
- Tout push est effectué vers "origin/main".
- INTERDIT de créer une branche de travail.
- INTERDIT de conserver volontairement du travail sur une branche temporaire fournie par l'environnement.
- INTERDIT de terminer simplement parce que le worker a démarré sur une branche différente de "main".
- INTERDIT de terminer en HEAD détaché.
- INTERDIT de terminer sur une autre branche que "main".
- INTERDIT de contourner un conflit en créant une autre branche.
- INTERDIT de créer un worktree ou un environnement Git parallèle.
- INTERDIT de lancer un sous-agent avant la récupération des commits, le rattachement à `main`, la
  synchronisation et la restauration d'un éventuel stash. L'agent principal réalise seul toutes
  ces opérations.

Les commandes suivantes sont interdites lorsqu'elles servent à créer une branche parallèle :

```
git checkout -b <branche>
git switch -c <branche>
git branch <branche>
git worktree add ...
```

"git checkout -B main ..." est EXPRESSÉMENT autorisé, car il sert à rattacher ou repositionner la branche obligatoire "main".

### 1.6. IDENTITÉ GIT ET ACTIVATION DES GARDES

Pose l'identité avant ton premier commit :

```
git config --local user.name "<nom du responsable>"
git config --local user.email "<adresse du responsable>"
```

Ces deux valeurs sont posées dans la configuration locale du dépôt : les gardes refusent une
identité absente et refusent une identité effective qui ne leur correspond pas exactement.

Active ensuite les hooks versionnés en mode worker :

```
scripts/git-hooks/install --worker
```

Le `pre-commit` contrôle l'identité locale et effective, la forme de la traçabilité, le diff indexé
et les secrets évidents. Le `commit-msg` refuse les attributions et signatures interdites. Le
`pre-push` contrôle les commits sortants et réserve les pushes à `origin/main`. Le contrat exact et
les limites de ces contrôles sont définis une seule fois dans `docs/AUTOMATION.md`.

Les règles de message et d'attribution restent celles de `CLAUDE.md` §13. Les hooks sont des
garde-fous mécaniques ; ils ne remplacent ni le jugement ni les preuves.

### 1.7. GARDE DE FIN DE SESSION OBLIGATOIRE

Cette procédure est une CONDITION DE TERMINAISON, pas une recommandation.

Juste avant toute réponse finale, toute conclusion ou toute fin d'exécution, attends la fin de tous
les sous-agents éventuels, examine leurs rapports et vérifie qu'aucune commande déléguée n'est
encore active. Exécute ensuite :

```
git fetch origin main
git pull --rebase origin main
```

Si cette synchronisation change le code, rejoue les preuves affectées et la campagne finale
avant de poursuivre. Corrige et persiste les écarts selon le cycle normal, puis termine par :

```
git push origin main
git fetch origin main
scripts/git-hooks/check-session
```

La garde est en lecture seule. Si elle échoue, corrige la cause indiquée, recommence la
synchronisation si nécessaire, puis rejoue-la. Ne produis pas de réponse finale avant son succès.

## 2. TU ES ROOT, ET TU DOIS DÉMARRER DOCKER TOI-MÊME

Cet environnement DISPOSE de Docker, mais le démon n'est PAS lancé au démarrage.

Tu es root : c'est à toi de le lancer.

La procédure est déjà mesurée et consignée dans "docs/JOURNAL.md". Ne la redécouvre pas.

"service docker start" ÉCHOUE sur :

```
ulimit: Operation not permitted
```

l'hôte étant privé de "CAP_SYS_RESOURCE".

N'insiste pas sur cette voie.

Lance le démon DIRECTEMENT, en arrière-plan :

```
dockerd --host=unix:///var/run/docker.sock > /tmp/dockerd.log 2>&1 &
```

Attends qu'il réponde. Boucle sur :

```
docker info
```

jusqu'au succès, avec un plafond raisonnable de tentatives.

Puis vérifie avec :

```
docker ps
```

### 2.1. PROXY TLS INTERPOSÉ

Les deux chaînes de construction en souffrent, et le contournement est CÂBLÉ depuis la décision 356.

Le paquet CA de l'environnement est :

```
/root/.ccr/ca-bundle.crt
```

Exporte :

```
export NPM_CA_FILE=/root/.ccr/ca-bundle.crt
export PIP_CA_FILE=/root/.ccr/ca-bundle.crt
```

Sans ces variables :

```
npm ci
```

peut échouer avec :

```
SELF_SIGNED_CERT_IN_CHAIN
```

et :

```
pip install
```

peut échouer avec :

```
CERTIFICATE_VERIFY_FAILED
```

Le script de démarrage de la pile s'arrêterait alors avant de démarrer le moindre service.

### 2.1 bis. NODE 24 : L'HÔTE A "nvm", MAIS PAS LA BONNE VERSION — INSTALLE-LA TOI-MÊME

Comme pour Docker au §2, l'outil est là et rien n'est prêt : c'est à toi de le faire. Ne le
redécouvre pas, tout ce qui suit est MESURÉ.

L'hôte démarre sur **Node v22.22.2**, la version du système. Lorsque le dépôt exige une version
plus récente — son `.nvmrc` la nomme et son "README.md" la documente —, ses harnais de vérification
refusent de s'exécuter. Leur refus tombe à la PREMIÈRE ligne, avant toute lecture du dépôt, avec un
message de cette forme :

```
ERREUR : aucun couple Node/npm utilisable. Exécutez « nvm use » puis relancez.
```

Ce message dit « exécutez nvm use », et c'est trompeur tant que la version n'est pas installée :
"nvm use" échouerait, "nvm ls" ne connaissant que "system".

"nvm" EST INSTALLÉ, dans :

```
/opt/nvm
```

**"nvm" n'est PAS un binaire, c'est une fonction de shell.** Elle n'existe donc pas tant que tu ne
l'as pas sourcée, et elle n'est atteignable ni par "timeout", ni par "env", ni par "xargs" — MESURÉ :

```
timeout 600 nvm install 24
=> timeout: failed to run command 'nvm': No such file or directory
```

La procédure, dans cet ordre, et dans UN SEUL appel de shell — l'état d'un shell ne survit pas d'une
commande à l'autre :

```
export NVM_DIR=/opt/nvm
. /opt/nvm/nvm.sh
nvm install 24
```

MESURÉ : l'installation télécharge "node-v24.19.0-linux-x64.tar.xz" depuis "nodejs.org" à travers le
proxy, vérifie son "sha256sum", et rend :

```
Now using node v24.19.0 (npm v11.17.0)
```

Elle pose aussi l'alias "default" sur 24, de sorte que les shells suivants n'ont plus qu'à sourcer
"nvm" et à appeler :

```
nvm use
```

qui lit le ".nvmrc" du dépôt.

**Toute commande qui dépend de Node doit être lancée dans un shell qui a sourcé "nvm"**, sans quoi
elle retombe silencieusement sur la v22 du système :

```
export NVM_DIR=/opt/nvm ; . /opt/nvm/nvm.sh ; nvm use ; <ta commande>
```

Vérifie avant de conclure quoi que ce soit :

```
node -v   => v24.x
npm -v    => 11.x
```

**Installe la version exigée AVANT "npm ci"**, et non après : les dépendances installées par une version le
sont pour elle, et changer de version derrière expose à des modules natifs incompatibles.

MESURÉ après l'installation : les harnais de vérification **franchissent la garde de version** et
entrent dans leurs étapes, là où ils s'arrêtaient sur leur première ligne. Ils exigent en outre la
pile debout — ils appellent "docker compose" —, donc §2 puis §2.2 avant eux.

### 2.1 ter. LES `verify-*.sh` SONT EXÉCUTABLES ICI — DEUX CONDITIONS, TOUTES DEUX MESURÉES

Le §2.1 bis a levé le blocage de la version de Node. Il en restait deux autres, extérieurs au
dépôt, qui faisaient rendre à ces harnais des verdicts ne disant RIEN du produit. Les deux sont
mesurés le 2026-08-16, et ne se redécouvrent pas.

**1. Exporte le navigateur.** Sans cela, tout scénario d'interface meurt à `browserType.launch`,
avant la moindre assertion, sur un binaire que l'hôte ne porte pas :

```
export PLAYWRIGHT_CHROMIUM_PATH=/opt/pw-browsers/chromium
```

Les scénarios d'interface reçoivent ce chemin ; les harnais ne le posent pas eux-mêmes.

**2. Libère le port 4173.** La configuration pose `reuseExistingServer: false`. Un `vite preview`
laissé par une exécution précédente — une série interrompue en laisse un — fait échouer l'étape
entière sur `http://127.0.0.1:4173 is already used`, ce qui ne dit rien du produit non plus :

```
pid=$(ss -ltnp 'sport = :4173' 2>/dev/null | grep -oP 'pid=\K[0-9]+' | head -1)
[ -n "$pid" ] && kill "$pid"
```

**Ne jamais employer `pkill -f vite`**, et le motif de cette interdiction est
mesuré, pas théorique. L'option `-f` fait correspondre la **ligne de commande
entière** : la commande ne tue donc pas « les serveurs vite », elle tue **tout
processus dont la ligne mentionne ce mot** — un `grep`, un éditeur, une commande
d'une autre session qui parle de vite en passant. Relevé le 2026-08-21 sur cette
machine : `pgrep -af vite` a rendu le shell d'une session voisine, qui ne servait
rien du tout.

Sur une machine partagée, la version ci-dessus ne vise **que ce qui tient
réellement le port** — c'est-à-dire la seule chose qui gêne. L'intention de la
règle a toujours été « libérer 4173 s'il est tenu », jamais « faire le ménage sur
la machine ».

**Avec ces deux conditions**, les harnais de vérification rendent un verdict qui parle du produit.
Sans elles, un verdict rouge ne doit être lu ni comme une régression, ni comme une preuve.

**Budget.** Ces harnais rejouent des suites E2E complètes : plusieurs dépassent quatre minutes
chacun, et un dépôt mûr en compte plusieurs dizaines. La série entière ne tient pas dans une session
d'une heure. Exécute d'abord ceux que ton changement touche, puis autant du reste que le temps le
permet, et dis exactement ce que tu n'as pas exécuté (§4.3).

### 2.2. DÉMARRAGE DE LA PILE

Ensuite seulement :

Lance la pile avec la commande de démarrage que le dépôt documente.

Le premier démarrage peut être long, notamment à cause de la construction et du téléchargement des images.

Puis applique obligatoirement le seed, avec la commande que le dépôt documente pour cela.

Le seed n'est en général PAS appliqué par la commande de démarrage : vérifie-le plutôt que de le supposer.

Sans lui, aucun compte de démonstration ne se connecte.

Vérifie ensuite :

```
docker compose ps
```

Tous les services déclarés doivent être "healthy" avant de lancer les preuves qui nécessitent la pile.

**La pile debout, tu vas directement au §4 pour choisir ton unité, puis au §3.2 pour travailler.**
Tu ne lances aucune preuve maintenant — voir le §2.3 juste en dessous, qui dit pourquoi.

### 2.3. LA PILE EST DEBOUT — TU NE LANCES AUCUNE PREUVE MAINTENANT

La pile montée et seedée, tu passes
IMMÉDIATEMENT au §4 pour choisir ton unité, puis au §3.2 pour travailler. **Tu ne lances PAS la
campagne de preuves à l'ouverture de la session.**

Le motif est mesuré : la campagne complète prend **quarante à soixante-dix minutes**. Lancée avant
d'avoir choisi une unité, elle consomme la majorité d'une session d'une heure pour produire une
information que tu n'utilises pas encore — et elle t'apprend l'état d'un dépôt que tu n'as pas
modifié. Ce temps appartient au produit (§4.2 bis).

Les preuves du dépôt sont, pour mémoire, et **elles s'exécutent aux moments définis au §3.2** :

```
tests de base de données     tests d'API        E2E d'interface       E2E de messagerie
tests unitaires              typecheck          build                 harnais de vérification
```

Les commandes exactes sont celles que le dépôt documente. Tu les relèves dans son "README.md",
son "Makefile" ou son "package.json" ; tu n'en inventes aucune et tu n'en reprends aucune d'un
autre projet.

Deux moments, et deux seulement :

- **pendant le travail** — uniquement les preuves de TON unité : sa suite de tests de base de
  données, ses scénarios d'API, son harnais dédié. Ciblées, courtes, rejouées autant de fois qu'il le faut ;
- **en fin de session** — la campagne complète, une seule fois, suivie de la boucle de correction
  du §4.3.

Les captures des preuves d'interface sont produites ET OBSERVÉES conformément à "CLAUDE.md",
section 16.

### 2.4. LIGNE DE BASE — UNIQUEMENT QUAND UNE PREUVE ROUGIT

C'est une procédure de **diagnostic**, pas une procédure d'ouverture. Tu ne l'exécutes que lorsqu'une
preuve est rouge et que tu t'apprêtes à conclure à une régression.

Ne conclus JAMAIS à une régression avant d'avoir établi la ligne de base.

Plusieurs harnais rendent des anomalies PRÉEXISTANTES et étrangères à ton changement.

Certaines tiennent à cet environnement. Exemple : tu es "root", donc :

```
[ -r fichier ]
```

peut être vrai même sur un fichier :

```
chmod 000
```

Le proxy peut également faire échouer certains contrôles qui reconstruisent une image SANS
certificat.

Pour comparer proprement, et **sur la seule preuve qui rougit** — jamais sur la campagne entière :

```
git stash -u
```

rejoue CE harnais sur la ligne de base, puis :

```
git stash pop
```

et compare les deux bilans. Si l'anomalie est présente des deux côtés, elle est préexistante :
consigne-la au registre (§3.1) et poursuis ton unité.

### 2.5. SI LA PILE NE MONTE PAS

Si la pile refuse de monter, ne fais pas semblant.

Consigne précisément :

- la commande qui a échoué ;
- l'erreur observée ;
- ce qui a pu être vérifié malgré l'échec.

Rabats-toi sur ce qui se vérifie sans pile :

- spécifications ;
- journal ;
- backlog ;
- manuel ;
- code ;
- tests unitaires ;
- "typecheck" ;
- "build" ;
- toute autre preuve indépendante de la pile.

Laisse alors les unités concernées en "[~]".

Liste précisément les preuves qui restent à exécuter.

Et pousse quand même tout travail cohérent effectué.

## 3. CE QUE TU DOIS FAIRE

TA MISSION PRIMAIRE EST DE FAIRE AVANCER LE PRODUIT : des fonctionnalités réellement codées — écran, geste, règle métier, migration, API — livrées et prouvées. Tout le reste de cette section est un MOYEN au service de cette mission, jamais une fin en soi.

Écrire et maintenir la documentation — spécification, journal, backlog, registre — est une OBLIGATION CONSTANTE et NON NÉGOCIABLE (CLAUDE.md §5). Ce n'est PAS le travail. C'est ce qui rend le travail traçable, reproductible et repris correctement par l'exécution suivante. Une session qui documente sans coder n'a pas rempli sa mission ; voir §4.2 et §4.2 bis, qui rendent cette règle vérifiable.

Lis INTÉGRALEMENT "CLAUDE.md" à la racine et applique ses règles à la lettre.

Elles priment sur tes habitudes.

Lis ensuite :

```
README.md
CHANGELOG.md
docs/BACKLOG.md
docs/JOURNAL.md
```

ainsi que les documents de "docs/" utiles à l'unité traitée.

Objectif permanent : livrer les fonctionnalités du produit que "docs/BACKLOG.md" énumère, jusqu'à ce que chacune soit "[x]", sans exception à la Definition of Done et sans raccourci. Le backlog n'est que la LISTE ; la mesure du travail réel est le produit livré et prouvé, jamais l'état du fichier seul.

Traite UNE unité cohérente à la fois. Tous les sous-agents éventuels servent cette même unité,
conformément à `CLAUDE.md` §1 et `docs/AUTOMATION.md` §6.

Ce worker partage un seul checkout et une seule branche `main`. L'agent principal est le seul à
modifier les fichiers suivis, le journal et le backlog, et le seul à effectuer une opération Git
modificatrice. Les consultations Git en lecture seule sont permises aux sous-agents. Il peut
déléguer des explorations, analyses, revues ou vérifications ciblées indépendantes. Les sous-agents
ne choisissent ni ne clôturent l'unité, ne tranchent aucune décision et ne modifient aucun fichier
suivi. Leur indisponibilité ne bloque jamais la session.

Éprouve les parcours comme un vrai utilisateur, au clavier et à la souris.

La console du navigateur doit rester VIERGE de toute erreur et de tout avertissement.

### 3.1. RÈGLES DE "CLAUDE.md" SYSTÉMATIQUEMENT OUBLIÉES

Toute décision, spécification ou arbitrage validé est écrit ET COMMITTÉ AVANT la première ligne de code.

Si le code n'est pas encore prêt, crée un commit documentaire dédié.

Chaque fichier porte la traçabilité parseable définie par `CLAUDE.md` §5 vers l'unité de backlog
et les chapitres de spécification correspondants. Le `pre-commit` en vérifie la forme ; tu restes
responsable de sa pertinence.

Une unité ne passe à "[x]" que si TOUTES ses preuves sont réellement exécutées et vertes.

Sinon elle reste "[~]" et l'écart est nommé.

Ne masque jamais une erreur par :

- un "try/catch" vide ;
- une valeur par défaut trompeuse ;
- un test désactivé ;
- une temporisation arbitraire ;
- un contournement destiné uniquement à rendre une preuve verte.

N'annonce JAMAIS une preuve que tu n'as pas exécutée.

Emploie les formulations du paragraphe 25 de "CLAUDE.md" :

```
implémenté et vérifié
implémenté mais non vérifié en E2E
bloqué par une dépendance
nécessite une action humaine
```

Quand une preuve devient rouge parce que la RÈGLE a changé par arbitrage, tu RÉVISES cette preuve en expliquant pourquoi dans le fichier lui-même.

Tu ne la supprimes pas et tu ne la contournes pas.

Quand tu trouves un défaut ÉTRANGER à ton unité, consigne-le dans :

```
docs/INCONSISTENCY_REPORT.md
```

avec sa mesure.

Laisse le comportement inchangé plutôt que de corriger ce défaut au passage.

### 3.2. ORDRE DE TRAVAIL D'UNE SESSION — SPÉCIFIER, CODER, POUSSER, PUIS PROUVER

Voici la séquence, et il n'y en a pas d'autre.
Tu ne réordonnes rien, et tu ne remontes pas la campagne de preuves en tête de session.

**1. Tu choisis ton unité** — §4.1 puis §4.2. Rien n'est écrit avant ce choix.

**2. Tu lis les spécifications de l'unité, INTÉGRALEMENT.** Pas en diagonale, pas seulement le
chapitre qui te paraît concerné : le document entier qui porte la fonctionnalité, plus
`docs/DESIGN_SYSTEM.md` en entier si tu touches à l'interface (`CLAUDE.md` §4).

**3. Tu écris la spécification COMPLÈTE de ce que tu vas coder, et tu la committes AVANT la première
ligne de code.** Contrat vérifiable — comportements, refus, cas limites, contrat d'API ligne à ligne
—, écrit après mesure sur la pile réelle et non d'après ton souvenir. Commit documentaire dédié,
poussé. C'est `CLAUDE.md` §5, et c'est la règle qui protège le travail d'une session interrompue.

> **UNIQUE EXCEPTION : tu reprends une fonctionnalité laissée incomplète.** Si l'unité est `[~]` et
> que sa spécification EXISTE DÉJÀ et couvre ce que tu vas coder, tu ne la réécris pas. Tu la lis,
> tu vérifies qu'elle décrit bien ce qui reste à livrer, et **tu passes directement au code**. Une
> session qui réécrit une spécification déjà écrite pour se donner un commit documentaire est une
> session en échec (§4.2 bis). Si en la lisant tu constates qu'elle est incomplète ou fausse sur le
> reste à livrer, alors et alors seulement tu la complètes — sur ce point précis, pas en entier.

**4. Tu codes.** Avant l'écriture, tu peux confier à des sous-agents les lectures indépendantes qui
réduisent l'incertitude, puis tu vérifies et synthétises leurs constats. Tu réalises ensuite seul les
modifications, une unité cohérente à la fois, séquentiellement, avec les commentaires `@spec` du
code et `@verifies` des tests écrits dans le même geste. Aucun sous-agent n'écrit dans les fichiers
suivis.

**5. Tu committes et tu pousses AU FIL DE L'EAU.** Dès qu'un morceau cohérent tient debout — une
migration qui s'applique, un écran qui rend, un module qui compile —, tu committes et tu pousses.
**Tu n'attends pas d'avoir prouvé pour pousser.** Une session interrompue à la minute 40 doit laisser
derrière elle du code poussé, pas un arbre de travail perdu (§0).

**6. Tu prouves TON unité, et elle seule, pendant que tu codes.** Sa suite de tests de base de
données, ses scénarios d'API, son harnais dédié, ses captures. Ce sont des exécutions courtes et ciblées, que tu rejoues
autant de fois que nécessaire. **Tu ne lances pas la campagne complète ici.**

**7. En fin de session seulement, tu lances la campagne complète**, une fois — et tu entres dans la
boucle de correction du §4.3.

**Ce que cette séquence interdit explicitement**, parce que chacune de ces erreurs a été observée :

- lancer l'ensemble des suites de tests et des harnais de vérification **avant d'avoir choisi une
  unité** — quarante à soixante-dix minutes dépensées avant le premier geste utile ;
- attendre que tout soit prouvé pour committer — une session interrompue ne laisse alors rien ;
- coder une fonctionnalité neuve sans spécification écrite et committée d'abord ;
- réécrire la spécification d'une unité `[~]` dont la spécification existe déjà, au lieu de coder.

## 4. COMMENT TU DÉTERMINES CE QU'IL RESTE À FAIRE

Ce prompt ne contient DÉLIBÉRÉMENT aucun état du projet, et n'en contiendra jamais.

Tout instantané écrit ici, par exemple :

- une liste d'unités ;
- un numéro d'entrée ;
- « il reste ceci à faire » ;
- une estimation de progression ;

serait potentiellement faux dès l'exécution suivante.

Cela pourrait te faire refaire du travail déjà livré ou sauter du travail dû.

Les fichiers de suivi du dépôt font foi, et eux seuls.

Tu les relis à CHAQUE exécution.

### 4.1. ORDRE DE LECTURE

1. "docs/JOURNAL.md", sa DERNIÈRE entrée d'abord.

Elle dit ce que l'exécution précédente a fait, ce qu'elle a mesuré, et se termine par où reprendre.

C'est ton point de départ avant même le backlog.

2. "docs/BACKLOG.md".

C'est l'état réel des unités :

```
[ ]  non commencée
[~]  en cours ou insuffisamment prouvée
[x]  close et intégralement prouvée
```

Chaque unité porte sa Definition of Done.

3. "docs/MASTER_PLAN.md".

Il définit l'ordre d'exécution et la Definition of Done commune.

4. "docs/INCONSISTENCY_REPORT.md", section "Ouverts" — EN CONSULTATION SEULEMENT.

Ce registre sert à DEUX choses, et à deux choses uniquement :

- vérifier si un défaut connu bloque l'unité que tu as choisie ;
- y consigner ce que tu observes en travaillant.

Une entrée laissée sans issue se tranche et se referme dans la session qui la rencontre, selon
« Autonomie de décision » de "CLAUDE.md".

### 4.2. COMMENT CHOISIR L'UNITÉ DE LA SESSION — LE PRODUIT D'ABORD

Le registre d'incohérences n'est pas une file de travail. La construction du produit reste
prioritaire sur le traitement autonome de ce registre.

L'unité de la session se choisit AINSI, dans cet ordre :

1. si la dernière entrée du journal désigne une reprise d'unité PRODUIT en
   cours, tu la suis ;
2. sinon, la première unité "[~]" du backlog dans l'ordre du plan dont il
   reste du COMPORTEMENT à livrer — du code, un écran, une migration, un
   parcours — et tu la fais avancer par du code ;
3. sinon, la première unité "[ ]" dans l'ordre du plan.

Une entrée du registre ne devient l'objet d'une session QUE dans deux cas :

- elle bloque concrètement l'unité produit choisie — alors tu la traites
  comme un préalable, dans la même session, et tu reviens à l'unité ;
- le responsable a explicitement ordonné son traitement.

Ces deux cas règlent la PRIORITÉ, jamais l'autorisation de trancher : une entrée rencontrée
sur le chemin de l'unité, ou consignée en travaillant, reçoit son issue immédiatement.

« Solder » une unité "[~]" dont le code est livré mais dont il ne manque que
des preuves reste utile, mais ne prime plus sur la construction : une session
qui n'a que ce choix exécute les preuves manquantes SANS réécrire les
documents autour, puis passe à une unité de construction s'il reste du temps.

Une seule unité par session, menée aussi loin que possible.

Mieux vaut une unité réellement close que trois unités entamées.

### 4.2 bis. PROPORTION DU CODE ET DE LA DOCUMENTATION

Chaque session dont l'unité comporte du comportement à livrer DOIT pousser au
moins un commit de CODE — application, migration, test qui éprouve un
comportement. Une session qui n'a produit que des commits de documentation,
hors le cas d'un blocage réel consigné, est une session en échec, et son
compte rendu doit le dire en ces termes.

La documentation reste obligatoire (CLAUDE.md §5) mais elle est PROPORTIONNÉE :
l'entrée de journal dit ce qui a été fait et où reprendre, en quelques
paragraphes, pas en essai. Les longues analyses rétrospectives, les bilans
chiffrés de bilans précédents et les relectures du registre pour lui-même
sont interdits : ce temps appartient au produit.

### 4.3. COMMENT TERMINER LA SESSION — CAMPAGNE, PUIS BOUCLE DE CORRECTION

C'est **ici**, et nulle part avant, que la campagne complète s'exécute. Ton code est déjà écrit,
committé et poussé (§3.2, point 5) : ce qui suit ne peut donc plus rien te faire perdre.

**1. Lance la campagne complète, une fois :**

```
tests de base de données     tests d'API        E2E d'interface       E2E de messagerie
tests unitaires              typecheck          build                 harnais de vérification
```

Les commandes exactes sont celles que le dépôt documente. Tu les relèves dans son "README.md",
son "Makefile" ou son "package.json" ; tu n'en inventes aucune et tu n'en reprends aucune d'un
autre projet.

**2. Entre dans la BOUCLE DE CORRECTION.** Tant qu'il reste une anomalie **imputable à ton
changement** :

1. isole la cause. Si tu t'apprêtes à conclure à une régression, établis d'abord la ligne de base
   du §2.4 **sur cette preuve seule** — une anomalie présente des deux côtés du `git stash` est
   préexistante, elle se consigne au registre (§3.1) et ne t'appartient pas ;
2. corrige la CAUSE, jamais le symptôme. Aucun `try/catch` vide, aucune temporisation, aucun test
   désactivé, aucun contournement destiné à verdir une preuve (§3.1) ;
3. **committe et pousse la correction immédiatement**, sans attendre le tour de boucle suivant ;
4. rejoue **la preuve concernée**, pas la campagne entière ;
5. quand toutes les preuves ciblées sont vertes, rejoue la campagne complète une dernière fois pour
   constater qu'aucune correction n'en a cassé une autre.

**Sortie de boucle sans avoir tout verdi.** Si le temps manque ou si une anomalie te dépasse, tu
sors — mais tu ne mens pas : l'unité reste `[~]`, l'écart est nommé précisément, et les preuves qui
restent à exécuter sont listées. Une anomalie préexistante ou étrangère à ton unité n'est PAS un
motif de rester en boucle : consigne-la et sors.

**Budget.** Si la campagne complète dépasse le temps qui te reste, exécute d'abord les suites que
ton changement touche, puis autant du reste que possible, et **dis exactement ce que tu n'as pas
exécuté**. Une campagne partielle annoncée comme telle vaut mieux qu'une session qui ne pousse rien.

**3. Écris dans "docs/JOURNAL.md" une entrée datée disant :**

- ce que tu as mesuré ;
- ce que tu as modifié ;
- ce que tu as vérifié ;
- ce qui a échoué ;
- où tu t'arrêtes ;
- où l'exécution suivante doit reprendre.

**4. Mets "docs/BACKLOG.md" au véritable état de l'unité**, et nomme précisément les preuves qui
restent à exécuter.

**5. Committe ces mises à jour et pousse sur "origin/main".**

**6. Attends tous les sous-agents éventuels, examine leurs rapports, vérifie qu'aucune commande
déléguée n'est encore active, puis exécute la garde Git finale** (§0, §1.7 et §5).

**7. Rédige et publie le compte rendu complet du §4.4**, une fois la garde du point 6 satisfaite.

Une session qui finit sans mettre à jour le journal et le backlog condamne potentiellement la
suivante à redécouvrir l'état par elle-même.

### 4.4. COMPTE RENDU FINAL DE SESSION, TOUJOURS, SANS EXCEPTION

Ta RÉPONSE FINALE n'est jamais un simple accusé de fin de tâche. C'est TOUJOURS un compte rendu complet de ce que la session a construit.

Ce compte rendu est DISTINCT de l'entrée de "docs/JOURNAL.md" du point 1 ci-dessus, qui reste brève (§4.2 bis) et sert à l'exécution suivante. Le compte rendu final s'adresse au responsable.

Rédiger ce compte rendu est un geste de SYNTHÈSE, pas une nouvelle tâche de documentation : il rassemble ce que la session a déjà construit, mesuré et capturé, il n'ouvre aucune investigation nouvelle. La même règle qu'au §4.2 bis s'applique : ce temps appartient au produit, pas à la prose. Reste factuel et va à l'essentiel plutôt que de produire un essai.

Il couvre l'INTÉGRALITÉ de la session, pas seulement son dernier geste. La HIÉRARCHIE est stricte, et l'ordre ci-dessous EST cette hiérarchie — les fonctionnalités CODÉES d'abord et avant tout, le reste ensuite, brièvement :

1. **Les fonctionnalités CODÉES, en tête et en détail** — écran, geste, règle métier, migration, API livrés ou modifiés. Pour CHACUNE, en langage clair et pas en jargon de commit : ce qu'elle fait pour l'utilisateur, et les CAPTURES produites conformément à "CLAUDE.md" section 16 — jointes au compte rendu quand l'outillage de la session le permet, sinon nommées explicitement par leur chemin sous "docs/captures/" pour qu'elles restent trouvables. C'est le cœur du compte rendu ; le reste n'est que son contexte.
2. Les preuves réellement exécutées et leur résultat, avec les formulations du paragraphe 25 de "CLAUDE.md" — n'annonce jamais vérifié ce qui ne l'a pas été.
3. Ce qui reste "[~]" ou "[ ]", et pourquoi.
4. En bref, sans développer : les migrations, les entrées de "docs/INCONSISTENCY_REPORT.md" consignées, les points que tu as tranchés avec leur motif, et tout arbitrage désormais attendu du responsable avec le cas dont il relève.
5. Le commit final et la confirmation que "origin/main" le porte.

Lorsque la session conclut à l'arrêt définitif de la boucle, ce compte rendu prend la
forme du §4.5 : il reste celui décrit ici, et il dit EN PREMIÈRE LIGNE que la tâche
automatique est arrêtée.

Une session qui n'a livré AUCUN code reste soumise à ce compte rendu, et le dit en PREMIÈRE ligne, sans détour : l'absence de fonctionnalité codée est l'information la plus importante de ce compte rendu-là, pas un fait noyé après le travail documentaire (§4.2 bis).

### 4.5. CONDITION D'ARRÊT DÉFINITIF DE LA TÂCHE PLANIFIÉE

La boucle planifiée n'est pas éternelle. Elle a une FIN, et cette fin est un geste
explicite que tu poses toi-même.

**Tu arrêtes définitivement la tâche planifiée dans exactement deux cas :**

1. **Le backlog est terminé** : plus aucune unité `[ ]` ni `[~]` dans
   `docs/BACKLOG.md`, autrement dit toute unité restante est `[x]` avec sa
   Definition of Done satisfaite. Une unité laissée `[~]` NE compte pas comme
   terminée, et n'autorise donc pas l'arrêt à ce titre.
2. **Tu n'as plus aucune option pour avancer** : tout ce qui reste est bloqué par
   quelque chose que la session ne peut pas fournir — un matériel absent, un
   service extérieur indisponible, un accès manquant, ou un arbitrage relevant
   de « Demande d'arbitrage » de "CLAUDE.md" et non rendu. « Difficile » n'est
   pas « bloqué », et « non tranché » non plus : avant de conclure à l'arrêt, tu
   dois avoir vérifié une par une TOUTES les unités restantes et nommé, pour
   chacune, ce qui l'empêche précisément.

Tant que l'un des deux cas n'est pas ÉTABLI, tu ne t'arrêtes pas : tu choisis une
unité et tu travailles, comme au §4.2.

**La procédure d'arrêt, dans cet ordre, sans en sauter une étape :**

1. **Arrête la tâche planifiée elle-même.** C'est le premier geste, pas le
   dernier : une session qui rédige son compte rendu d'arrêt sans couper la
   boucle sera relancée à l'heure suivante et refera le même constat. Selon
   l'outillage qui porte la tâche, cela signifie supprimer le travail planifié
   — `CronDelete` avec l'identifiant de la tâche, arrêt de la boucle dynamique,
   ou suppression de la tâche planifiée dans le nuage. Si plusieurs mécanismes
   la portent, coupe-les TOUS ; si l'outillage ne permet pas de couper toi-même,
   dis-le explicitement et demande au responsable de le faire.
2. **Mets le dépôt à jour et committe une dernière fois** : `docs/JOURNAL.md`
   porte une entrée d'arrêt datée, `docs/BACKLOG.md` porte l'état RÉEL de chaque
   unité, et tout blocage nommé au point 2 ci-dessus est écrit là où quelqu'un le
   cherchera — dans l'unité concernée, pas seulement dans le journal.
3. **Pousse ce commit sur `origin/main`** et satisfais la garde du §5.
4. **Produis un compte rendu final d'ARRÊT**, qui reprend le §4.4 et y ajoute,
   clairement et sans détour :
   - **que la tâche automatique est ARRÊTÉE**, dit en toutes lettres et en
     PREMIÈRE ligne du compte rendu, pas noyé au milieu ;
   - lequel des deux cas ci-dessus l'a déclenché ;
   - où en est le projet : ce qui est livré et prouvé, ce qui ne l'est pas ;
   - ce qui RESTE en attente, unité par unité ;
   - ce qui a EMPÊCHÉ d'aller plus loin, précisément, pour chaque unité restante,
     et ce qu'il faudrait pour la débloquer — un matériel, un accès, un
     arbitrage relevant de "CLAUDE.md" ;
   - le commit final et la confirmation que `origin/main` le porte.

N'arrête JAMAIS la tâche en silence, et ne la laisse JAMAIS tourner sur un projet
qui n'a plus rien à avancer : les deux font perdre du temps, l'un en cachant la
fin, l'autre en la répétant indéfiniment.

## 5. RÈGLE FINALE, AUCUNE EXCEPTION

Rien de ce que tu fais n'existe durablement tant que ce n'est pas poussé sur `origin/main`.

La session n'est terminée que lorsque `scripts/git-hooks/check-session` réussit après la
synchronisation finale décrite au §1.7. Si la garde échoue, continue à travailler jusqu'à corriger
chaque condition signalée.

NE PRODUIS PAS TA RÉPONSE FINALE AVANT LE SUCCÈS DE CETTE GARDE.
