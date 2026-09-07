# Fiches à réutiliser

Les champs entre crochets sont à remplir avec des faits du projet. Ces modèles
servent une rédaction courte ; ils ne dispensent pas de vérifier leurs références.

## F1 — Mission bornée

```text
Résultat attendu : [un comportement observable].
Sources à lire : [contrat, unité, fichiers utiles].
État initial connu : [référence de code, données, défaut reproduit].
Périmètre : [ce qui doit changer pour ce résultat].
Pouvoirs : [lecture/édition/tests locaux] ; [opérations non autorisées].
Critères : [succès, limites, refus, absence de mutation sur refus].
Preuves : [commandes existantes et parcours].
Livrable : diff, références, résultats réellement obtenus, limites et reprise.
```

Exemple DEM-01 : refuser 2 caractères et 81 caractères après trim, conserver la
saisie, ne rien créer en base. Corriger domain.py et les références nécessaires.
Exécuter les tests ciblés puis parcourir la création depuis l'accueil.

## F2 — Fiche de reproduction

```text
Contexte : OS, navigateur, version de code, profil et données.
Préparation : comment obtenir l'état initial sans altérer des données partagées.
Gestes : 1… 2… 3…
Observé : résultat exact, erreur utile et capture si pertinente.
Attendu : contrat ou décision qui le définit.
Fréquence : reproduit [nombre] fois dans [contexte].
Hypothèses : séparées des observations.
```

Exemple : Bob, base neuve, trois espaces dans la création ; quatrième ligne au
titre vide alors que le contrat exige un refus. Cause à rechercher dans la
normalisation et la validation, sans la prétendre déjà établie.

## F3 — Unite et preuves

```text
Identifiant stable : [DEM-XX].
Acteur, action et état initial : […].
Résultat et données préservées : […].
Refus et cas limites : […].
Hors périmètre : […].
Spécification : [chemin#ancre].
Tests unitaires : [cas et commande].
Intégration/API : [cas et commande].
E2E/visuel : [parcours canonique et observations].
Documentation : [sources affectées].
Statut : [ ] / [~] / [x], avec preuves ou manques nommés.
```

## F4 — Relecture du diff

1. Relire le résultat demandé et les critères.
2. Vérifier chaque fichier ajouté, modifié ou supprimé.
3. Relier les changements aux critères ; expliquer les écarts de périmètre.
4. Vérifier données, refus, erreurs et droits au niveau d'autorité.
5. Lire les assertions : peuvent-elles détecter le défaut initial ?
6. Rechercher une documentation devenue fausse et contrôler la sélection Git.

## F5 — Contrat d'agent pour le laboratoire

Exemple de petit `AGENTS.md` pour Codex, dans le dossier d'exercice :

```markdown
# Travail sur ce laboratoire
Lis CLAUDE.md puis CLAUDE_PROJECT.md lorsqu'il existe.
Reste dans la mission courante et cite les références utilisées.
```

Exemple de `CLAUDE.md` pédagogique réutilisable :

```markdown
# Méthode de travail
Lis le README et le contrat de l'unité avant de modifier.
Lis explicitement CLAUDE_PROJECT.md lorsqu'il existe.
Préserve le travail existant. Un agent principal édite les sources.
Écris les décisions et critères avant l'implémentation correspondante.
Corrige une cause avec des preuves qui détectent le défaut.
Ne déclare jamais une vérification que tu n'as pas exécutée.
Relis le diff et actualise les documents rendus faux par le changement.
Les opérations de production et les dépenses demandent une autorité explicite.
```

Ce petit exemple est un échafaudage d'apprentissage ; il ne remplace pas le
contrat complet du socle lors de son adoption. Exemple de compagnon local :

```markdown
# Contexte du laboratoire
Python 3.11 ou plus, SQLite, serveur local à identités simulées.
Lancement : python3 app.py --port 8765
Tests : python3 -m unittest -v
Référence : BACKLOG.md et DAT.md.
Seed : créé à l'absence du fichier de base ; jamais réinitialisé au redémarrage.
Ne pas déployer ce laboratoire et ne pas utiliser de données réelles.
```

## F6 — Mission de revue ou de verification

```text
Rôle : [revue en lecture seule / preuve ciblée].
Question unique : […].
Sources : [liste précise].
Arbre stabilisé : [référence, état connu].
Pouvoirs : pas d'édition des sources, pas d'opération Git modificatrice.
Pour une preuve : commande autorisée, durée attendue, artefacts temporaires.
Retour : constat sourcé, impact, résultat, incertitude et preuve manquante.
Le principal vérifie les constats et prend les décisions.
```

## F7 — Passation et clôture

```text
Unité et référence de code : […].
Comportement implémenté : […].
Commandes et preuves exécutées : […].
Résultats et artefacts observés : […].
Ce qui reste non vérifié : […].
Documents actualisés : […].
État Git : fichiers, commit réel, push réel ou non réalisé.
Prochaine action exécutable : […].
Opérations externes nécessaires : [aucune ou cible/autorité explicites].
```

## F8 — Avant un worker réel

Décrire la machine et son caractère éphémère, les dépendances réellement disponibles,
les commandes du projet, le stockage durable, les accès, la destination des
pushes et leur effet éventuel de déploiement. Fixer la sélection d'une unité,
les checkpoints, les preuves, le budget, la reprise et l'arrêt. Tester une
interruption locale et lire la passation. L'ordonnanceur est installé séparément
sur un service autorisé ; aucun fichier de prompt ne crée ce service.
