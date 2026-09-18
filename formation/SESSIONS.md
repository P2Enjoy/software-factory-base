# Ce qui a été enseigné lors des deux premières sessions animées

Compte rendu factuel des deux sessions du cycle « IA usine digitale » animées par
Martino Bettucci (P2Enjoy SAS) les mardis 8 et 15 septembre 2026, établi à partir
des transcriptions et des notes automatiques de visioconférence.

Ce document sert de source à [REVISION.md](REVISION.md). Il décrit ce qui a
réellement été dit et montré, pas ce que les supports prévoyaient. Les deux
participants sont désignés par « premier participant » et « second participant » ;
leurs données personnelles, leurs projets nominatifs et leurs échanges privés ne
sont pas reproduits ici.

## Cadre observé

| | Session 1 | Session 2 |
| --- | --- | --- |
| Date | mardi 8 septembre 2026, après-midi | mardi 15 septembre 2026, après-midi |
| Durée enregistrée | 2 h 47 | 4 h 10 |
| Effectif | un formateur, deux participants | un formateur, deux participants |
| Format | visioconférence, partage d'écran, démonstrations en direct | visioconférence, partage d'écran, manipulations guidées chez les participants |
| Support projeté | un site web publié pour l'occasion, parcouru sur trois écrans | aucun support projeté, uniquement des outils réels |
| Matériel de travail | projets fictifs imposés par le formateur | projets réels des participants |

Durée cumulée : 6 h 57. Une troisième session de deux à trois heures a été
offerte par le formateur en fin de session 2, consacrée exclusivement à la mise
en place pratique d'une usine complète, avec la planification automatique des
agents.

Profil observé des participants : utilisateurs quotidiens et avancés des outils
(terminal, Claude Code, Codex, ChatGPT, skills personnalisés, dépôts et VPS),
sans formation initiale de développeur, l'un se décrivant comme pratiquant le
« vibe coding » et visant une posture de « product builder ». Leur demande est
constante sur les deux séances : industrialiser leurs propres projets, déléguer
sans perdre le contrôle, réduire les coûts d'abonnement, héberger en local.

## Session 1 : cadrer un agent et combattre l'ambiguïté

### Posture et principes

Le fil directeur est énoncé d'emblée : « arrêter de penser à ce qui va le plus
vite, penser à ce qui nous fait perdre le moins de temps », résumé par « slow is
smooth, smooth is fast », répété en milieu de séance. « Diviser pour mieux
régner » est présenté comme « le principe de base de tout le système agentique ».

Autres règles énoncées : parler à un agent en résultat attendu et en limites, les
limites primant sur le résultat ; ne jamais se satisfaire de « les tests
passent » et exiger un rapport de bas niveau (requête, code HTTP, charge utile,
règle appliquée) ; prédire, observer, puis expliquer l'écart ; supposer que
l'agent ne devinera pas la démarche et tout expliciter ; « quand tu conçois, tu
ne codes pas, quand tu codes, tu ne conçois pas » ; itérer en plusieurs boucles
plutôt que chercher le prompt parfait ; prendre le temps des spécifications
(« s'il vous faut deux heures, prenez deux heures ») ; agir à la racine plutôt
que sur les symptômes ; ne pas utiliser un modèle de langage quand une règle
déterministe suffit.

### Vocabulaire enseigné

- **Assistant** : outil qui « fait exactement ce que vous lui dites », qui en
  mode conversation « ne peut pas acter », ce qui en fait l'outil du cadrage et
  de l'introspection.
- **Agent** : se pilote par objectif ; un agent bien fait « répond par une action
  proposée, l'exécute dans sa portée, informe de la suite ».
- **Harnais** : ce qui encadre le modèle, récolte les besoins, produit le code et
  applique les bonnes pratiques. Les harnais de haut niveau sont confortables
  « tant qu'on ne sort pas du sentier battu » ; les harnais de bas niveau
  (terminal) sont à encadrer soi-même.
- **Dérive d'instructions** : « même les meilleurs outils ne retiennent que 68 %
  de vos instructions », proportion qui se dégrade avec le nombre d'interactions
  et la complexité. Oublis typiques cités : le rapport, le démarrage des services
  avant les tests, les tâches intermédiaires.
- **Fiche de goal** (fichier d'objectifs) : document qui décrit un succès, nomme
  l'acteur, le résultat attendu, les changements, les exclusions, les critères
  d'acceptation, les contraintes, et surtout la façon de déterminer que c'est
  fini. Produit avec l'assistant employé comme bloc-notes, puis donné à l'agent.
- **Definition of Done** : « codé, c'est pas fini ; fini, c'est intégré, envoyé,
  testé, fonctionnel dans un parcours utilisateur inscrit dans un cas d'usage ».
- **Definition of Ready** : une tâche « peut être dans le backlog sans être prête
  à être prise » ; l'exploration précède l'inscription au backlog.
- **Few-shot prompting** : « au lieu de donner des instructions très complexes,
  je lui donne des exemples » ; sert à lever l'ambiguïté d'un terme.
- **Métaprompting** : utiliser la description du résultat final avec des exemples,
  puis la capacité d'abstraction du modèle « pour qu'il se prompte correctement
  lui-même ».
- **Faits, hypothèses, décisions** : « les questions posées par l'agent sont des
  hypothèses ; on doit toutes les transformer en décisions » avant l'implémentation.
- **Sous-système** ou **unité d'action** : périmètre minimal d'interaction obtenu
  par décomposition.
- **Orchestrateur** : agent dont le goal est « d'orchestrer ses sous-fifres :
  déterminer quand et comment appeler les phases, si une phase suit l'autre,
  quand et pourquoi ».
- **Consigner** : « ajouter aux choses à faire, dans une pile, au lieu de donner
  une tâche qu'il commence ».
- **Usine** (ou forge) : « le niveau ultime de contrôle », qui « dépêche
  l'orchestrateur dans un environnement maîtrisé, industrialisable, répétable et
  historisé », tournant plusieurs fois par jour à partir de zéro sur une machine
  neuve qui n'est pas la production.
- **Agent pragmatique** : programme sans intelligence, « psychorigide », qui « ne
  dérive pas », par exemple un contrôle qui refuse un commit sans marqueur de
  traçabilité.

Une hiérarchie est énoncée, avec une hésitation dans la transcription sur la
position relative de la boucle et du harnais : agent, harnais, boucle, compétence,
orchestrateur, usine.

### Procédure centrale montrée : cadrer un goal avec l'assistant

1. Ouvrir l'assistant en mode conversation, pas l'outil de code, parce qu'il ne
   peut pas agir et ne partira donc pas produire.
2. Donner un prompt d'ouverture qui impose la chasse à l'ambiguïté, avec des
   exemples : si l'instruction dit « créer tous les dossiers en attente »,
   l'assistant doit demander ce qu'est un dossier en attente ; l'ambiguïté doit
   être levée sur les données d'entrée, les actions, les résultats attendus et la
   façon de les vérifier.
3. Laisser l'assistant poser toutes ses questions.
4. Accélérer la réponse : lui demander de reposer chaque question avec trois
   options, dont une recommandée, avec avantages et inconvénients ; répondre par
   des codes ; écrire sa réponse quand aucune option ne convient ; déclarer
   qu'une question sans réponse vaut option recommandée.
5. Demander de « formuler l'ensemble de toutes nos discussions comme un seul et
   unique goal ».
6. Conserver la conversation dans un projet pour y revenir.

Le formateur observe que les deux outils ne se comportent pas pareil par défaut :
l'un pose spontanément une douzaine de questions, l'autre très peu tant que le
prompt de cadrage n'est pas donné.

### Décomposition et orchestration

La décomposition en sous-systèmes est montrée dans une nouvelle conversation, en
demandant « les périmètres minimaux d'interaction entre sous-systèmes pour les
diviser en unités d'action », avec un exemple few-shot emprunté au bâtiment
(architecte, maître d'œuvre, équipes de gros œuvre, architecte d'intérieur).
Quand la liste obtenue est trop longue, le formateur demande simplement de la
ramener à trois.

Le métaprompting est ensuite appliqué au découpage : le bloc de description de la
pipeline est recollé dans une nouvelle conversation avec la demande de séparer
les objectifs des trois phases en trois fichiers Markdown. Le besoin d'un
orchestrateur apparaît à ce moment : « on découpe, on splitte, il faut un
orchestrateur ». Le curseur du découpage est assumé comme empirique, avec un
critère de correction : on découpe davantage quand on observe des dérives.

### Aperçu de l'usine

Le formateur montre le journal d'exécution d'une usine réelle (clonage, pile,
données synthétiques, migration, unité de développement, preuves, backlog), un
document d'exploration classant les constats en exploratoire, non planifié, non
retenu, réalisation et arbitrage, un backlog de plus de quatre-vingt-dix tâches
numérotées, et une organisation en phases (conception, réalisation, correction,
démonstration, tests, mise en production, contrôles).

Deux rôles particuliers sont décrits : un orchestrateur jouant le Product Owner,
« interdit de coder et d'utiliser l'API », travaillant « clavier et souris
exclusivement », qui ne saute pas de page par l'URL et consigne les défauts ; un
agent de documentation qui relie chaque portion de code aux points du dossier
d'architecture.

Le travail multi-terminaux est montré (une fenêtre par tâche ou par phase, plus
d'une dizaine ouvertes), avec la règle de ne pas gérer la fenêtre de contexte mais
d'isoler les tâches, et de ne pas laisser des agents modifier l'application
pendant qu'on l'observe.

### Exercices réellement conduits

- Exercice oral de classement : pour trois situations, dire si un assistant
  suffit ou s'il faut un harnais. Quatre situations étaient annoncées, trois ont
  été posées ; un second exercice annoncé n'a pas eu lieu.
- Exercice de rédaction : produire un premier goal pour un agent de tri de
  prospects, sujet fictif imposé pour « prendre du recul », avec restitution des
  productions des deux participants et reprise de ce qui manquait.

### Outils manipulés ou montrés

Assistant en mode conversation et mode canevas (applet exécutée chez le
fournisseur, partageable par lien, sans déploiement), pages multi-écrans générées,
harnais complet de développement assisté chez un fournisseur tiers, harnais de
terminal, bascule de modèle dans le terminal entre famille conversationnelle et
famille de code, projets pour ranger les conversations de cadrage, dépôt gabarit
présenté comme support de la méthode.

## Session 2 : de l'agent configuré à l'usine distribuée

### Rappel d'ouverture

« La dernière fois, on a fait un truc sympa. On a vraiment vu comment on crée des
agents de façon efficace et surtout on a essayé de combattre notre pire ennemi
qui est l'ambiguïté. C'était vraiment notre ennemi numéro un. On a vu aussi
comment créer des orchestrateurs. » Le programme annoncé du jour : théoriser la
création d'agents efficaces, expliquer quand fragmenter un agent, définir les
agents orchestrateurs, puis construire une usine d'abord simple puis de plus en
plus complexe.

### Digression matérielle

Environ cinquante-cinq minutes en début de séance portent sur le matériel et la
chaîne d'approvisionnement : prix de la mémoire et des cartes graphiques,
arbitrage entre hébergement local et abonnements, quantisation et architectures
alternatives, monopole de la lithographie, stockage et inférence temps réel. Ce
contenu répond aux projets d'auto-hébergement des participants et ne figure au
programme d'aucune des deux sessions.

### Les trois modes d'un outil et le choix entre eux

Trois modes sont distingués, avec leurs équivalents chez le fournisseur
concurrent : conversation, espace de travail local, outil de code en ligne de
commande. Points enseignés :

- la fenêtre de contexte de la conversation est bridée volontairement (ordre de
  32 000 unités) pour préserver la capacité des serveurs ;
- le mécanisme d'attention n'est pas linéaire : doubler la taille du contexte
  demande environ quatre fois plus de mémoire et seize fois plus de calcul ;
- l'outil de code dispose de fenêtres plus larges parce qu'il sert moins
  d'utilisateurs ;
- la conversation est prioritaire en disponibilité, parce que la grande majorité
  des utilisateurs n'utilise que ce mode ;
- réduire la taille du modèle et de la fenêtre augmente la rétention des
  instructions, ce qui justifie des agents dédiés et segmentés.

L'espace de travail local est présenté comme un assistant administratif : temps
d'exécution très longs, fenêtre nettement plus large, et surtout connecteurs
locaux qui lui donnent accès au système de fichiers de la machine. C'est cet
accès physique à un dossier de travail qui le distingue de la conversation.

### Atelier de configuration guidée

Un agent de veille est construit en direct avec l'un des participants, par
partage d'écran, en appliquant la procédure de cadrage anti-ambiguïté de la
session 1. L'agent pose des questions de clarification, le participant arbitre le
périmètre (sources à surveiller, types d'événements inclus, exclusions), puis
l'agent est rattaché à un dossier physique dédié sur la machine pour y tenir un
journal d'opérations et des rapports.

Éléments de configuration passés en revue : exécution au démarrage, maintien de
la machine éveillée pendant une tâche, enregistrement d'écran pour auditer le
comportement en début d'usage, exigence d'un appareil de confiance pour le
pilotage à distance, dossier racine et liste blanche de dossiers accessibles,
choix entre navigateur du système et navigateur intégré isolé, liste blanche de
sites, instructions globales valables pour toutes les sessions.

Le choix du modèle pour cet agent est explicitement discuté : un modèle lourd
n'est pas nécessaire pour analyser la structure et le contenu d'un site.

### Sécurité et confidentialité

Pour le contrôle complet du clavier et de la souris, le formateur recommande une
machine ou une session utilisateur dédiée, sans mot de passe au démarrage, sans
données confidentielles, programmée pour se relancer après coupure. Deux cas
réels de migration de données sont cités, où cette technique a remplacé des
connecteurs inexistants.

Sur la confidentialité du courrier électronique, la démonstration est faite que
le secret de bout en bout par messagerie ordinaire est illusoire, les messages
transitant par des serveurs publics qui en conservent des traces ; seule une
solution de chiffrement asymétrique avec échange de clés publiques l'assure.

Pour tester une application web ou mobile, le formateur déconseille le contrôle
clavier et souris et préconise des protocoles d'outillage spécialisés, plus
efficients que la vision par ordinateur. Il note au passage que l'outil de code
« triche » volontiers sur les tests d'interface, en déclarant qu'une page
fonctionne alors qu'aucun bouton n'a été implémenté.

### Industrialisation : dépôt, contrôle à distance, planification

Le passage par un dépôt Git hébergé est présenté comme indispensable à
l'industrialisation, et les participants créent un dépôt privé vide ex novo pour
l'exercice. La séquence complète est faite avec eux : autorisation de
l'application sur le dépôt, restriction des droits aux dépôts choisis,
installation de l'outil en ligne de commande de l'hébergeur, authentification,
clonage, approbation du dossier de travail, association du compte, activation du
contrôle à distance.

Le mode de contrôle à distance est ensuite montré sous trois formes : depuis un
téléphone vers un poste laissé allumé, depuis l'interface web, et sur un serveur
distant. Chaque abonnement donne aussi accès à une machine hébergée de
caractéristiques modestes. Le terminal hôte doit rester ouvert pour maintenir le
service.

La planification de routines est montrée dans l'interface de contrôle à distance,
avec une routine horaire de test. Le formateur explique que cette brique permet
d'industrialiser des opérations répétitives : batteries de tests automatisés,
traitements par lot, audits d'interface nocturnes.

### Création d'un agent spécialisé

La procédure est montrée intégralement :

1. Cadrer les objectifs de l'agent dans la conversation, avec le prompt
   anti-ambiguïté, en demandant à l'assistant d'utiliser une fonction de
   questions fermées à choix multiples plutôt que des questions ouvertes, pour
   accélérer les arbitrages.
2. Préciser le périmètre. L'exemple traité est un agent qui collecte et suit le
   développement des fonctionnalités d'une application, avec des états (à faire,
   en cours, en revue, fait), une priorité, et une restitution en tableau de bord.
3. Nommer le rôle avec justesse. L'assistant propose plusieurs qualifications ;
   le formateur retient celle de scribe de backlog en expliquant qu'un Product
   Owner complet valide aussi les livrables en fin de cycle, alors que cet agent
   ne doit que tenir et alimenter le backlog. Il demande ensuite d'aligner le
   fichier d'objectifs sur ce seul besoin.
4. Enregistrer l'agent avec la commande dédiée de l'outil de code, en lui donnant
   un nom de fichier et le contenu. La commande étant limitée en longueur, une
   astuce est donnée : injecter d'abord le fichier complet dans le contexte avec
   un message neutre du type « lis ça, ne fais rien », puis créer l'agent en
   référençant le document du message précédent.
5. Constater le résultat : un dossier caché d'agents contenant un fichier
   Markdown avec en-tête, rôle et instructions.
6. Invoquer l'agent. À sa première instruction (inscrire au backlog les
   définitions de Ready et de Done), il produit une synthèse et propose lui-même
   une structure de fichiers et des conventions. Le formateur souligne le
   changement de nature : « au lieu de demander à l'IA d'exécuter brutalement des
   actions, on s'entretient avec un agent responsabilisé qui formule et applique
   des normes de qualité ».

La distinction entre agent et compétence est posée à la demande d'un participant :
la compétence s'exécute dans le contexte de la conversation courante, l'agent
possède une mémoire et un historique isolés. Cette séparation évite d'engorger la
fenêtre de contexte, qui peut accumuler des centaines de milliers d'unités lors
des modifications de fichiers.

Sur l'écosystème, le formateur signale des répertoires de compétences et d'agents
mais constate un marché naissant, fait d'initiatives essentiellement individuelles.

### L'usine et ses rôles

La vision est énoncée clairement : « on inverse le système, on crée un système
automatique qui build nos logiciels et nous, on se met pratiquement en position
de client. On vient, on dit ce qu'on a besoin, on vérifie ce qui a été fait, et on
a toute une usine derrière de codeur, testeur, industrialisateur, livreur qui font
tout le travail sans qu'on ait besoin de lui dire maintenant build, maintenant
déploie, maintenant corrige tes bugs. » Le diagnostic qui justifie ce
renversement : « l'efficacité du système dépend de votre rigueur à vous rappeler
de faire les tâches », alors que dans une usine, ces tâches sont portées par le
système. L'image retenue : « une usine, c'est une ESN qui nous appartient ».

Principes d'architecture énoncés :

- des rôles strictement séparés (rédaction de backlog, développement, tests,
  déploiement), l'humain se repositionnant en client et concepteur ;
- un agent qui ne corrige que des bugs et ne produit pas de fonctionnalités, avec
  en face un orchestrateur qui impose l'ordre (vider la pile de défauts avant de
  reprendre les nouveautés) ;
- des agents capables de s'envoyer des messages : un agent de backlog qui doute
  de la formulation d'une exigence peut interroger l'agent client pour obtenir
  une clarification métier avant de rédiger ;
- des agents de contrôle qualité dédiés, restreints à une exigence précise
  (conformité au design system, seuil de latence), qui relancent automatiquement
  les agents de développement tant que l'exigence n'est pas satisfaite ;
- des agents de test distincts selon la nature de la preuve : tests d'interface
  de programmation, tests techniques, tests d'interface utilisateur pilotant
  réellement la souris et le clavier ;
- une rigueur qui vient de l'humain et se transmet à l'agent : « c'est à nous de
  nous donner notre propre rigueur, et l'agent va boucler jusqu'à ce qu'il arrive
  à faire une fiche de bug correctement faite ».

Une usine réelle est montrée en fonctionnement : exécution automatique toutes les
quatre heures, traitement d'une unité de backlog par cycle, et production de
captures d'écran de l'interface mise à jour comme preuve de la validité du
travail. La fréquence est limitée volontairement pour préserver le quota
quotidien.

Le formateur propose de bâtir lors de la session suivante une usine reproduisant
l'ensemble des rôles d'une équipe agile (Scrum Master, Product Owner,
développeurs, équipe qualité, sponsors) avec leurs rituels, en précisant que
cette méthode d'orchestration s'applique à n'importe quel processus cyclique
automatisable.

### Choix et coût des modèles

Un développement notable ferme la séance, sur l'économie de l'usine :

- « les bons outils pour le bon usage » plutôt que le modèle le plus intelligent
  systématiquement ; un agent de codage n'a pas besoin d'une grande capacité
  d'abstraction, il doit exécuter des ordres et savoir coder ;
- le modèle le plus puissant sert en amont, pour la conception et l'écriture des
  objectifs ; le développement est confié à des agents moins coûteux ;
- les écarts de tarif entre familles de modèles sont explicités, de même que le
  surcoût d'un mode d'exécution accélérée, et le formateur indique faire tourner
  sa propre usine sans employer le modèle le plus cher ;
- on peut compenser les manques d'un modèle en dotant un agent d'une mémoire
  spécifique : la documentation d'un domaine et l'historique de ses incidents
  connus pour un réviseur de sécurité, le corpus méthodologique pour un agent
  d'animation.

Sur la qualité et la sécurité du code produit, le formateur écarte le procès
d'intention fait au code généré, observe que certains modèles corrigent
spontanément des failles connues mais de façon aléatoire, et pose le calcul qui
justifie les agents de contrôle : si l'agent de codage a une chance sur deux
d'oublier une sécurisation et l'agent qualité une chance sur deux de la manquer,
le défaut passe une fois sur quatre.

### Suite convenue

Une troisième session de deux à trois heures, offerte, consacrée exclusivement à
la construction pratique d'une usine complète et à la planification automatique
des agents. Travail demandé d'ici là : créer ses propres agents, les faire
interagir, documenter les comportements observés et arriver avec des cas d'usage
réels. Une courte séance sur les principes de l'agilité est également prévue pour
préparer la modélisation des rôles.

## Ce que ces sessions disent du public

Les deux participants ne demandent pas un cours d'ingénierie logicielle. Ils
arrivent avec des projets en cours et repartent avec des agents configurés sur
ces projets. Leurs questions récurrentes portent sur la délégation sans perte de
contrôle, la traçabilité de ce que font les agents, la sécurité de ce qui est
produit, le coût d'exploitation, et le choix entre exécution locale et service
hébergé.

Leurs difficultés exprimées sont cohérentes d'une session à l'autre : ne pas
savoir ce qu'on ignore, ne pas savoir spécifier ce que la machine doit vérifier,
perdre la main sur un outil après quelques mois sans pratique, oublier la
sécurité faute de l'avoir spécifiée, craindre de déléguer sans journal
d'exécution, perdre du temps parce que l'outil « oublie régulièrement d'appliquer
cent pour cent des consignes ».

Le formateur constate lui-même en fin de session 2 que les échanges approfondis
ont ralenti le programme initial, et qu'ils n'ont « fait que gratter la surface ».
