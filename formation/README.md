# Coder avec un agent : les bases, la méthode, puis l'usine

**Formation au codage agentique · P2Enjoy**

Vous savez déjà lancer Codex ou Claude Code et obtenir une petite application.
Ce parcours vous apprend à comprendre ce que l'agent change, exprimer ce que vous
attendez, produire des preuves et reprendre le projet dans la durée.

Le cours s'utilise seul. L'animation premium ajoute des démonstrations commentées,
du travail en binôme et un retour individualisé sur vos productions. Aucune
connaissance préalable de l'architecture, de la CI ou des tests n'est supposée.

## Commencer

1. Lire le [syllabus](SYLLABUS.md) et préparer le laboratoire selon
   [le guide d'installation](INSTALLATION.md).
2. Ouvrir [le cours autonome](exports/cours.html), ou son
   [PDF](exports/cours.pdf), puis suivre les modules dans l'ordre.
3. Réaliser les [30 exercices](EXERCICES.md). Consulter les
   [corrigés](CORRIGES.md) après avoir produit votre réponse.
4. Réaliser [l'évaluation finale](EVALUATION.md), puis comparer au
   [corrigé et au barème](CORRIGE_FINAL.md).

Pour animer : [slides HTML](exports/slides.html), [PowerPoint éditable](exports/slides.pptx),
[PDF des slides](exports/slides.pdf), [guide d'animation](ANIMATION.md) et
[notes par diapositive](exports/notes-slides.md).
Pour imprimer séparément : [cahier d'exercices](exports/cahier-exercices.pdf),
[corrigés](exports/corriges.pdf) et [guide d'animation avec notes](exports/guide-animation.pdf).
Le [kit complet ZIP](exports/formation-complete.zip) permet de transmettre une
copie comprenant les sources, les supports et le laboratoire.

## Contenu et rythme

Les quinze modules du syllabus, de 150 minutes chacun, et une évaluation
de 270 minutes représentent 42 heures animées hors pauses. Chaque module comprend
une situation de départ, des notions
expliquées, un exemple commenté, deux exercices, un quiz et un point de reprise.
En autonomie, interrompez-vous après chaque exercice et conservez vos preuves.
La durée de lecture ou de travail personnel varie ; le minutage est un scénario
d'animation, pas un délai imposé à l'apprenant.

| Module | Lecture | Exercices |
| --- | --- | --- |
| 1. De l'assistant à l'agent | [Chapitre 1](cours/01-assistant-agent.md) | E01, E02 |
| 2. Transformer une demande en unité | [Chapitre 2](cours/02-unite.md) | E03, E04 |
| 3. Construire le contexte | [Chapitre 3](cours/03-contexte.md) | E05, E06 |
| 4. Externaliser la mémoire | [Chapitre 4](cours/04-memoire.md) | E07, E08 |
| 5. Séparer global et local | [Chapitre 5](cours/05-global-local.md) | E09, E10 |
| 6. Spécifier avant d'implémenter | [Chapitre 6](cours/06-specifier.md) | E11, E12 |
| 7. Concevoir la boucle d'exécution | [Chapitre 7](cours/07-boucle.md) | E13, E14 |
| 8. Rendre l'environnement reproductible | [Chapitre 8](cours/08-environnement.md) | E15, E16 |
| 9. Construire la preuve | [Chapitre 9](cours/09-preuves.md) | E17, E18 |
| 10. Encadrer sécurité et production | [Chapitre 10](cours/10-securite.md) | E19, E20 |
| 11. Utiliser Git comme mémoire durable | [Chapitre 11](cours/11-git.md) | E21, E22 |
| 12. Orchestrer plusieurs agents | [Chapitre 12](cours/12-agents.md) | E23, E24 |
| 13. Automatiser les invariants | [Chapitre 13](cours/13-invariants.md) | E25, E26 |
| 14. Passer au worker autonome | [Chapitre 14](cours/14-worker.md) | E27, E28 |
| 15. Assembler la software factory | [Chapitre 15](cours/15-factory.md) | E29, E30 |

Compléments : [fiches pratiques](FICHES.md), [glossaire](GLOSSAIRE.md),
[sources](SOURCES.md), [guide des illustrations](ILLUSTRATIONS.md),
[bilan de vérification](VERIFICATION.md).

## Portée du support

Le cours explique la méthode du dépôt dans son état disponible. Il distingue
les principes réutilisables, les conventions P2Enjoy et les capacités actuelles
des outils. La publication de recherche antérieure mentionnée lors du cadrage
n'était pas disponible ; aucune conclusion ne lui est attribuée. Sa révision,
après stabilisation définitive du socle, appartient à une publication ultérieure.

Les exemples et figures sont originaux. Les sources externes sont citées sans
en reproduire de longs extraits. La licence du dépôt s'applique aux fichiers
distribués ; voir [LICENSE](../LICENSE). Les noms d'outils ne constituent pas une
certification de la formation par leurs éditeurs.

## Modifier puis régénérer les supports

Les fichiers Markdown sont les sources du cours ; `slides.json` contient le
texte et les notes du diaporama. Les SVG sont des figures éditables. Les exports
sont produits par les scripts documentés dans [PRODUCTION.md](PRODUCTION.md).

Ne pas modifier directement un fichier dans `exports/` pour conserver un
changement : ce dossier est généré et sera remplacé. Reporter la modification
dans le fichier source correspondant, puis lancer depuis la racine du dépôt :

```bash
python3 formation/outils/construire.py
node formation/outils/exporter.cjs
python3 formation/outils/emballer.py
```

La première commande reconstruit les HTML, les schémas et les notes. La deuxième
recrée les PDF et le PowerPoint. La dernière remet à jour le ZIP et son
inventaire. Sur un nouveau poste, effectuer auparavant l'installation décrite
dans [PRODUCTION.md](PRODUCTION.md#installer-les-outils-dédition). Pour une
publication formellement vérifiée, suivre ensuite toute la séquence de contrôles
de [PRODUCTION.md](PRODUCTION.md#construire-et-vérifier).

## Consulter la formation depuis GitHub

GitHub affiche directement les fichiers Markdown et propose un aperçu des PDF.
Le [cours en PDF](exports/cours.pdf), les [slides en PDF](exports/slides.pdf) et
les autres supports peuvent donc être consultés depuis le dépôt ou téléchargés.

Les fichiers HTML interactifs ne sont pas exécutés dans l'interface standard de
GitHub : GitHub en montre le code ou le fichier brut. Le workflow
`.github/workflows/pages.yml` publie donc `formation/exports/` comme un site
GitHub Pages à chaque mise à jour des exports sur `main`. Il peut aussi être
lancé manuellement depuis l'onglet Actions.

Lors de la première publication, choisir **GitHub Actions** comme source dans
**Settings → Pages** si le dépôt ne l'utilise pas encore. L'adresse publique est
ensuite affichée dans l'environnement `github-pages` et dans le résumé du
workflow. Le [kit complet](exports/formation-complete.zip) reste disponible pour
une consultation entièrement hors ligne.
