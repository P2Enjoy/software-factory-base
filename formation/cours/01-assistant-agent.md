# M1 — De l'assistant à l'agent

Objectif : comprendre ce qu'un agent sait faire, ce qui guide ses actions et ce
qui reste de votre responsabilité. Durée animée : 150 min. Exercices E01 et E02.
Ce module peut se réaliser sans le laboratoire, avec les exemples fournis.

## Partir de votre pratique

Vous avez déjà décrit une petite application à une IA, attendu le résultat,
cliqué et demandé des corrections. Cette pratique donne rapidement quelque chose
à regarder. Le travail devient plus délicat lorsqu'une correction en casse une
autre ou quand l'agent annonce un succès que vous ne retrouvez pas à l'écran.
La première étape du cours consiste à comprendre les éléments de cette interaction.

Un modèle de langage produit une réponse à partir des informations qui lui sont
accessibles. Il manipule des fragments de texte appelés **tokens**, qui ne
correspondent pas toujours à un mot entier. Le **contexte** regroupe notamment
instructions, conversation, fichiers lus et retours d'outils. Il a une capacité
limitée : une longue conversation peut être résumée, et une information présente
sur votre disque peut ne jamais avoir été lue.

Une réponse convaincante ne garantit pas son exactitude. Le modèle peut produire
une fonction inexistante, oublier une contrainte ou extrapoler un comportement.
Ce type de contenu incorrect est souvent appelé hallucination. L'ingénierie
du travail consiste entre autres à rendre les erreurs observables : contrat,
sources, exécution et comparaison avec l'attendu.

## Quatre niveaux d'interaction

Dans un échange de conseil, vous copiez du code et l'IA propose une réponse.
Avec une assistance dans l'éditeur, elle peut voir certains fichiers et proposer
un diff. Avec un agent outillé, elle peut lire, modifier, lancer et observer.
Avec une exécution planifiée, cette boucle peut démarrer sans votre présence
immédiate. Ce dernier niveau sera étudié en fin de formation.

![L'agent relie mission, modèle, outils et observations sous des limites](../illustrations/11-agent.svg)

Le modèle propose l'action ; un outil l'exécute dans un environnement ; le retour
apporte une nouvelle observation. Un programme qui ne peut pas écrire un fichier
ne l'écrit pas parce que le modèle le souhaite. À l'inverse, un accès puissant
ne dit pas si l'action est pertinente pour votre demande. Il faut articuler
capacité technique, autorisation et intention.

Exemple : vous demandez « explique cette erreur ». Lire le fichier et la sortie
du terminal sert la demande. Modifier les données de production ne découle pas
de cette demande. Vous demandez « corrige ce défaut dans mon laboratoire » :
une petite modification et ses tests locaux font partie du travail, sous les
contraintes annoncées. L'autonomie décrit jusqu'où l'agent peut poursuivre ; elle
ne supprime pas le périmètre.

## Lire une action, pas seulement la phrase finale

Voici un échange fictif : « J'ai réparé la sauvegarde ; tout fonctionne. »
Demandez quelles lignes ont changé, quelle commande a été lancée et ce qu'elle
a obtenu. « Le test existe » signifie que du code de test est présent. « Le test
a réussi » signifie qu'une exécution a donné le résultat attendu dans un contexte.
« Le produit est prêt » exige encore les autres preuves applicables.

Dans le terminal, le **dossier courant** détermine souvent les fichiers utilisés.
Une même commande lancée ailleurs peut tester un autre projet. La sortie d'un
outil doit donc être liée à un dossier et une version. Le **code de sortie**
d'une commande signale habituellement succès (0) ou échec (autre valeur), mais
un succès technique peut porter sur une mauvaise cible. Vous apprendrez à
contrôler la portée autant que la couleur du résultat.

## Construire une demande compréhensible

Un premier message efficace décrit le résultat, les références utiles, les
contraintes et les preuves attendues. Par exemple : « Dans ce dossier, explique
le trajet d'une demande depuis le formulaire jusqu'au stockage. Lis le README
et les fonctions concernées. Ne modifie rien. Cite tes sources et distingue les
hypothèses. » Ce message est court parce que son objet est précis.

Un message tel que « sois le meilleur développeur du monde » ne définit aucun
comportement à vérifier. Une demande trop volumineuse mêle plusieurs décisions
et rend la revue difficile. On peut travailler par échanges : observer,
reformuler, préciser, réaliser une unité, puis vérifier. Les modules suivants
enseignent chacun de ces gestes.

## Vos responsabilités et vos appuis

Vous n'avez pas besoin de mémoriser chaque ligne de code produite. Vous devez
pouvoir expliquer le besoin, reconnaître les données sensibles, comprendre les
modifications essentielles et apprécier les preuves. L'agent peut expliquer un
concept, traduire une erreur et proposer des tests ; vous devez lui demander
des éléments que vous pouvez contrôler. Un collègue ou un formateur peut aider
à cette revue, surtout pour une opération engageante.

Commencez sur des copies locales avec données fictives. Pour une action
destructive ou extérieure, identifiez la cible et l'autorité nécessaire.
L'installation et la fiche de gestes Git minimaux permettent de faire les
premières manipulations ; l'étude complète de Git viendra au module 11.

## Faire et vérifier

E01 distingue conseil, édition et exécution. E02 transforme une promesse de
succès en questions de preuve. Extension : comparer deux réponses au même besoin
sur leurs sources et leurs observations, sans classer les modèles par réputation.

Q1.1 : un fichier présent dans le dépôt est-il nécessairement dans le contexte ?
Q1.2 : quelle différence entre un outil autorisé et une action pertinente ?
Q1.3 : pourquoi un code de sortie 0 ne suffit-il pas à dire « produit terminé » ?
Réponses dans [CORRIGES](../CORRIGES.md).

Point de sortie : vous savez expliquer la boucle mission, action, observation
et les limites de ce qu'une déclaration de l'agent établit.
