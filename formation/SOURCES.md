# Sources et portée des affirmations

Consultations documentaires : période récente. Les contenus pédagogiques, scénarios
et schémas sont originaux. Les liens ci-dessous permettent de vérifier les points
propres aux outils ; aucune disponibilité, tarification ou performance d'un
modèle n'est présumée. Les commandes du laboratoire sont définies et testées
dans cette édition ; le bilan indique les résultats effectifs.

## Méthode du depot

| Source | Usage dans le cours | Limite |
| --- | --- | --- |
| [CLAUDE.md](../CLAUDE.md) | principes, documentation, preuves, Git, sécurité, DoD | conventions de la méthode P2Enjoy |
| [README](../README.md) | architecture du socle et séparation global/local | socle encore en évolution |
| [AGENTS.md](../AGENTS.md) | responsabilité du principal et délégation | routage propre à ce dépôt |
| [AUTOMATION](../docs/AUTOMATION.md) | contrôles mécaniques, limites, absence de CI distante | lire les scripts pour leur comportement réel |
| [CloudWorker](../docs/CloudWorker.md) | reprise, checkpoints, cycle et arrêt | hypothèses d'hôte non universelles ; prompt ≠ ordonnanceur |
| [Design system](../docs/DESIGN_SYSTEM.md) | lisibilité, états, clavier et preuve visuelle | conventions visuelles P2Enjoy |

Les scripts de hooks examinent notamment une forme de traçabilité ; ils ne
résolvent pas la pertinence des spécifications. La garde finale compare une
référence locale actualisée par un fetch distinct. Une comparaison par stash
ne remonte pas avant une correction déjà committée. Ces limites sont enseignées
explicitement ; le cours ne prétend pas que le dépôt est déjà sa version définitive.

## Sources primaires des outils

| Source officielle | Point étayé | Module |
| --- | --- | --- |
| [OpenAI — AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | découverte et hiérarchie des instructions Codex | M5 |
| [OpenAI — sécurité](https://learn.chatgpt.com/docs/security) | accès aux documents de permissions et sécurité | M11, M5 |
| [Claude Code — mémoire](https://code.claude.com/docs/en/memory) | CLAUDE.md, contexte et différence avec AGENTS.md | M5 |
| [Claude Code — permissions](https://code.claude.com/docs/en/permissions) | configuration des actions autorisées | M11 |
| [Git — diff](https://git-scm.com/docs/git-diff) | comparaison du travail, de l'index et des commits | M11 |
| [Git — fetch](https://git-scm.com/docs/git-fetch) | récupération et références de suivi distant | M11 |
| [Git — merge](https://git-scm.com/docs/git-merge) | avance rapide, divergence et conflits | M11 |
| [Git — revert](https://git-scm.com/docs/git-revert) | correction conservant une histoire partagée | M11 |
| [Git — hooks](https://git-scm.com/docs/githooks) | événements Git et contexte d'exécution | M13 |
| [Python — unittest](https://docs.python.org/3/library/unittest.html) | tests, assertions et lancement de suites | M9 |
| [Playwright — écrire des tests](https://playwright.dev/python/docs/writing-tests) | actions et assertions navigateur | M9 |
| [OWASP — autorisation](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | contrôle serveur, accès par ressource, refus par défaut | M10 |

La compétence OpenAI Docs a orienté la vérification des points propres à Codex
vers les sources officielles. Les extraits de prompts sont des exemples de
formation, pas des options de configuration garanties par tous les outils.

## Publication antérieure

La pièce jointe de recherche évoquée lors du cadrage n'a pas été reçue dans le
contexte accessible. Aucune affirmation de validation scientifique, aucun résumé
et aucune citation ne lui sont attribués. Le support présent est complet pour
son parcours ; la confrontation à cette publication et sa révision finale
constituent une étape éditoriale ultérieure quand le document sera disponible.

## Maintenance éditoriale

Avant une nouvelle édition : vérifier les liens des éditeurs, rejouer le
laboratoire, comparer les contrats du socle, reconstruire les exports et vérifier
leurs rendus. Conserver un bilan avec date et environnement. Une évolution de
version d'outil n'autorise pas à modifier silencieusement le comportement produit
attendu dans les exercices.
