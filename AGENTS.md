# Instructions Codex

L'agent principal lit intégralement `CLAUDE.md` avant toute modification et
l'applique comme contrat général. Lorsqu'une session est déclenchée par
`docs/.routine`, il lit aussi intégralement `docs/CloudWorker.md`, qui définit le
cycle propre au worker planifié. Il lit `CLAUDE_PROJECT.md` lorsqu'il existe.

Un sous-agent ne recharge pas automatiquement tous ces documents. Il lit son
fichier d'agent et uniquement les contrats ou sources que l'agent principal
nomme dans sa mission. L'agent principal lui transmet les contraintes utiles.

## Orchestration

L'agent principal reste l'unique responsable de l'unité en cours, l'unique
éditeur des fichiers suivis et le seul autorisé à modifier l'état Git.

Utilise les agents spécialisés de `.codex/agents/` seulement pour une mission
indépendante et bornée :

- `factory_explorer` lorsque le périmètre, les dépendances ou le flux réel sont
  incertains ;
- `factory_reviewer` lorsqu'un changement cohérent et non trivial peut être
  relu contre ses contrats ;
- `factory_verifier` lorsque l'arbre est stabilisé et qu'une preuve ciblée ou
  ses résultats doivent être analysés.

Ne délègue pas une tâche triviale. Chaque délégation précise l'objectif, le
périmètre, les sources à lire et le livrable attendu. N'utilise pas de
sous-agents imbriqués.

Les sous-agents ne prennent aucune décision produit ou architecturale, ne
modifient aucun fichier suivi et n'effectuent aucune opération Git modificatrice.
Les consultations Git en lecture seule sont permises. Attends les
résultats utiles, vérifie leurs constats dans le dépôt, puis synthétise-les avant
de décider ou de modifier quoi que ce soit.

`factory_verifier` peut produire uniquement les artefacts temporaires générés
par les commandes de preuve autorisées. Lance-le sans écriture concurrente,
compare l'état Git avant et après son travail et traite tout écart comme une
anomalie.
