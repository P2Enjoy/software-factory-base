# DESIGN SYSTEM REFERENCE : P2Enjoy Applications

Référence maîtresse pour l’interface des applications P2Enjoy. Elle dérive de la **charte P2Enjoy SAS** et définit les règles transversales de conception, d’implémentation, d’accessibilité et de validation visuelle.

**Ce fichier se lit intégralement avant toute modification, revue ou commit touchant l’UI ou l’UX**, y compris pour une correction visuelle jugée mineure.

Tout changement d’interface doit être vérifié contre ce document avant commit.

Lorsqu’une règle nouvelle apparaît :

* si elle est applicable à plusieurs applications, elle est ajoutée ici ;
* si elle relève du métier ou d’un produit particulier, elle reste dans la documentation du projet ;
* si une application doit déroger à une règle commune, l’écart est documenté dans sa propre section ou son propre fichier d’extension, avec justification, date et preuve lorsque celle-ci existe.

Le design system définit **comment une information ou une interaction doit être représentée**. Il ne définit pas les règles métier qui décident quelles informations, permissions, transitions ou données existent.

---

# 1. Principes fondamentaux

## 1.1 Une seule source de vérité visuelle

Les couleurs, espacements, tailles, rayons, ombres et comportements communs sont exprimés sous forme de tokens ou de composants partagés.

Une valeur visuelle ne doit pas être réinventée dans un composant métier.

## 1.2 Le design system ne remplace pas le modèle métier

L’interface représente ce que le modèle applicatif autorise ou expose.

Elle ne doit pas créer silencieusement :

* une permission ;
* une contrainte ;
* un statut ;
* une valeur par défaut ;
* une transition ;
* une validation ;
* une relation ;
* un état métier.

Lorsqu’une règle appartient au backend ou à la base de données, l’interface ne doit pas prétendre être sa source d’autorité.

## 1.3 Pas de succès simulé

Une action n’est présentée comme réussie qu’après confirmation du système qui fait autorité.

Une réponse sans modification effective ne doit jamais être traduite visuellement par « Enregistré ».

## 1.4 Pas de commande morte

Une commande n’est pas affichée lorsqu’elle représente une fonctionnalité qui n’existe pas.

Cette règle est distincte du contrôle des permissions.

Si une fonctionnalité existe mais peut être refusée selon le contexte ou les droits, l’application peut laisser l’utilisateur tenter l’action et afficher le refus réel du backend.

## 1.5 Une information ne repose jamais uniquement sur la couleur

Tout état porté par une couleur doit également être identifiable par au moins un élément explicite :

* texte ;
* libellé ;
* icône ;
* forme ;
* attribut ARIA adapté.

## 1.6 Les décisions visuelles se vérifient sur l’application exécutée

Une règle théoriquement correcte peut produire un mauvais résultat une fois rendue.

Les interfaces sont donc validées à partir :

* de captures réelles ;
* de parcours clavier ;
* de mesures de contraste ;
* du comportement réel du navigateur ;
* des réponses réelles du backend lorsque cela est pertinent ;
* des tests E2E.

Un test automatique ne remplace pas l’observation visuelle.

---

# 2. Palette

## 2.1 Couleurs principales P2Enjoy

| Rôle             | Token             | Hex       | Usage                                      |
| ---------------- | ----------------- | --------- | ------------------------------------------ |
| **Bleu P2Enjoy** | `--color-brand`   | `#23468C` | Actions primaires, liens, sélection, focus |
| **Vert**         | `--color-success` | `#238C33` | Succès, confirmation, état positif         |
| **Jaune**        | `--color-accent`  | `#D9CF4A` | Mise en évidence secondaire                |
| **Rouge**        | `--color-danger`  | `#F24141` | Erreurs, refus, actions destructives       |
| **Noir**         | `--color-ink`     | `#0D0D0D` | Titres et texte fort                       |

Aucun hexadécimal ad hoc ne doit apparaître dans un composant.

## 2.2 Déclinaisons

Chaque couleur chromatique peut disposer de déclinaisons calculées :

* `--color-brand-soft`
* `--color-brand-hover`
* `--color-brand-on-soft`
* `--color-success-soft`
* `--color-success-on-soft`
* `--color-accent-soft`
* `--color-accent-on-soft`
* `--color-danger-soft`
* `--color-danger-on-soft`

Les variantes `*-soft` produisent des surfaces colorées légères.

Les variantes `*-on-soft` sont suffisamment assombries pour respecter le contraste AA lorsqu’elles sont utilisées comme texte sur leur propre fond doux.

Le texte d’un badge ne doit pas automatiquement utiliser la couleur pleine du badge.

## 2.3 Voile

`--color-veil` représente l’encre à environ 40 % et constitue le voile standard placé derrière une surface recouvrant l’écran.

Il s’agit d’un token, jamais d’une opacité réécrite localement.

## 2.4 Neutres

| Usage            | Token             | Hex       |
| ---------------- | ----------------- | --------- |
| Fond de page     | `--color-bg`      | `#F7F8FA` |
| Surface          | `--color-surface` | `#FFFFFF` |
| Bordures         | `--color-border`  | `#E5E7EB` |
| Texte secondaire | `--color-text-2`  | `#4B5563` |
| Texte tertiaire  | `--color-text-3`  | `#6B7280` |
| Survol neutre    | `--color-hover`   | `#F3F4F6` |

## 2.5 Thèmes

Le thème clair constitue la référence P2Enjoy.

Un thème sombre n’est ajouté à une application que lorsqu’il est explicitement conçu, documenté et testé. Il ne doit pas être obtenu par inversion automatique des couleurs.

## 2.6 Couleurs portées par les données

Lorsqu’un objet métier possède une couleur configurable, la donnée stocke un **nom de token** et non une valeur hexadécimale.

Valeurs recommandées :

`brand`, `success`, `accent`, `danger`, `neutral`.

Une correspondance unique transforme ensuite cette valeur en tokens visuels.

Une valeur inconnue reçue du backend doit disposer d’un repli documenté, généralement `neutral`.

---

# 3. Typographie

* Police principale : `ui-sans-serif, system-ui, sans-serif`.
* H1 : 26 px, graisse 700, `--color-ink`.
* H2 : 20 px, graisse 700, `--color-ink`.
* H3 : 16 px, graisse 700, `--color-ink`.
* Corps : 15 px, interligne 1,55.
* Texte secondaire : `--color-text-2`.
* Texte tertiaire et aide : `--color-text-3`.
* Texte compact : 13 px.
* Aucun texte visible sous 12 px.

## 3.1 Données techniques

Les données dont la comparaison caractère par caractère est pertinente utilisent :

`ui-monospace, monospace`

avec chiffres tabulaires lorsque nécessaire.

Exemples :

* identifiants ;
* adresses techniques ;
* montants ;
* dates ;
* horodatages ;
* numéros de version ;
* empreintes ;
* codes.

Une donnée technique n’implique pas automatiquement qu’elle doive être affichée. Un identifiant interne sans intérêt utilisateur ne doit pas atteindre l’écran.

---

# 4. Espacement, dimensions et rayons

## 4.1 Échelle d’espacement

Valeurs autorisées :

`0, 4, 8, 12, 16, 24, 32, 48 px`

Aucune valeur intermédiaire ne doit être introduite sans justification spécifique.

`0` fait explicitement partie de l’échelle afin que les classes et propriétés dépendant de l’absence d’espacement puissent être générées.

## 4.2 Rayons

* `--radius-sm` : 8 px, champs et boutons.
* `--radius-md` : 10 px, pastilles d’icône.
* `--radius-lg` : 14 px, cartes et grandes surfaces.
* `rounded-full` : badges, pilules et avatars.

## 4.3 Ombres

Ombre standard d’une carte :

`0 1px 3px rgb(0 0 0 / .06)`

Une élévation supplémentaire peut être utilisée au survol lorsque la carte représente effectivement une surface interactive.

Une surface non interactive ne doit pas simuler une élévation cliquable.

## 4.4 Cible interactive

`--size-target` vaut au minimum 40 px.

La taille visuelle d’une icône ou d’une case peut être inférieure, mais sa cible interactive doit atteindre cette dimension.

---

# 5. Architecture générale des applications

Structure de référence :

```text
┌──────────────┬──────────────────────────────────────────────────────┐
│ Navigation   │ En-tête : contexte · titre · recherche · profil     │
│ principale   ├──────────────────────────────────────────────────────┤
│              │ Navigation contextuelle éventuelle                  │
│ Sections     ├──────────────────────────────────────────────────────┤
│ métier       │                                                      │
│              │ Zone principale                                     │
│ Utilitaires  │                                                      │
│ Réglages     │                                                      │
└──────────────┴──────────────────────────────────────────────────────┘
```

Toutes les applications ne sont pas obligées d’utiliser une barre latérale.

Le patron dépend de la quantité et de la nature de la navigation.

## 5.1 Navigation principale

La navigation principale doit :

* rester identifiable ;
* conserver des libellés accessibles lorsqu’elle devient iconographique ;
* utiliser `aria-current="page"` pour la destination courante ;
* ne pas faire reposer l’état actif sur la couleur seule.

Une barre latérale peut être repliable.

Son état peut être conservé comme préférence de session ou préférence utilisateur lorsque le produit le prévoit.

## 5.2 Navigation contextuelle

Lorsque des éléments changent l’URL ou représentent de véritables destinations, ils sont des **liens**.

Un `tablist` est réservé à des panneaux échangés dans une même vue sans changement de destination.

Ne pas utiliser le patron ARIA `tablist` simplement parce qu’une navigation ressemble visuellement à des onglets.

## 5.3 Priorités sous contrainte de largeur

Quand l’espace manque, les éléments redondants disparaissent avant l’information spécifique à la vue.

Ordre recommandé de sacrifice :

1. marque ou nom du produit lorsque déjà visible ailleurs ;
2. contexte global déjà porté par la navigation ;
3. métadonnées secondaires ;
4. jamais le titre principal de la route sans autre point d’accès.

Un libellé nécessaire aux technologies d’assistance peut devenir `sr-only`, mais ne doit pas être supprimé.

---

# 6. Composants et patterns

## 6.1 Carte d’entité

Une carte standard utilise :

* `--color-surface` ;
* `--radius-lg` ;
* bordure 1 px `--color-border` ;
* titre ;
* métadonnées ;
* états ou catégories ;
* informations secondaires nécessaires.

Une carte peut porter un liseré coloré lorsque la couleur représente une donnée de catégorie ou d’état.

Si la catégorie est `neutral`, utiliser un neutre suffisamment visible, par exemple `--color-text-3`, et non une bordure quasiment invisible sur fond blanc.

Le titre peut être limité à deux lignes dans une vue de cartes.

Les métadonnées ne doivent pas exposer d’identifiant technique lorsqu’une représentation humaine existe.

## 6.2 Board ou Kanban

Un board représente une collection ordonnée de colonnes contenant des éléments.

Chaque colonne possède :

* un titre ;
* éventuellement un compteur ;
* éventuellement une agrégation ;
* une zone de contenu ;
* un état vide explicite.

Une largeur fixe de colonne peut être utilisée lorsqu’elle correspond à la forme attendue du contenu.

Une largeur de référence de **288 px** est recommandée pour les boards P2Enjoy lorsque le produit ne définit pas autre chose.

Cette valeur décrit la forme du composant, elle ne fait pas partie de l’échelle d’espacement.

Lorsque le nombre de colonnes dépasse l’espace disponible :

* les colonnes ne sont pas écrasées ;
* le board défile dans son propre conteneur ;
* la page elle-même ne défile pas horizontalement.

### Glisser-déposer

Le glisser-déposer ne doit jamais constituer l’unique moyen de déplacer un élément.

Une alternative clavier doit exister, par exemple un menu proposant les destinations ou transitions valides.

La zone de dépôt active peut utiliser un liseré `--color-brand` en pointillés.

Ne pas supposer que `dragleave` indique réellement la sortie d’une colonne. Les événements remontant des enfants rendent cette interprétation instable dans les navigateurs.

Préférer un état de cible unique à l’échelle du board, remplacé à l’entrée d’une autre cible et supprimé à la fin du glissement.

## 6.3 Détail d’une entité

Patron de référence sur grand écran :

* colonne principale : identité, métadonnées et édition ;
* colonne secondaire : activité, commentaires, historique ou contexte associé.

Sous 1024 px, les colonnes s’empilent dans l’ordre du document.

L’identité de l’objet doit être présentée avant son formulaire ou son historique.

## 6.4 En-tête d’entité

Un en-tête peut contenir :

* titre ;
* responsable ou acteur associé ;
* montant ou mesure ;
* échéance ;
* états de cycle de vie ;
* adresse ou identifiant lisible ;
* actions contextuelles.

Les paires terme / valeur sont représentées avec une structure sémantique appropriée, notamment `dl`, `dt`, `dd`.

Une donnée absente n’est pas automatiquement représentée par un tiret.

Dans une fiche, une ligne facultative peut simplement ne pas être rendue.

Lorsqu’une absence constitue elle-même une information utile, elle est nommée par une phrase explicite.

Exemples :

« Aucun responsable »

« Adresse indisponible »

## 6.5 Mode lecture et mode édition

Lorsqu’un en-tête contient plusieurs informations éditables, préférer une bascule globale entre lecture et édition à un formulaire permanent.

Avantages :

* lecture plus claire ;
* possibilité d’éditer des valeurs actuellement absentes ;
* réduction du nombre de contrôles visibles ;
* distinction nette entre consultation et modification.

La commande d’ouverture :

* utilise un bouton secondaire ;
* porte un nom accessible précis ;
* indique son état avec `aria-expanded` lorsque pertinent.

À l’ouverture :

* le focus entre dans le premier contrôle.

À la fermeture :

* le focus revient à la commande d’origine.

Une commande « Terminer » peut fermer un mode d’édition sans prétendre enregistrer lorsque les champs sont déjà autosauvegardés.

## 6.6 États de cycle de vie

Les états comme « Archivé », « En sommeil », « Désactivé » ou équivalent sont rendus avec :

* une pilule ;
* un texte explicite ;
* éventuellement une icône ;
* une couleur cohérente.

Plusieurs états indépendants peuvent coexister.

Une pilule ne doit pas remplacer la donnée nécessaire à la compréhension.

Exemple : lorsqu’un état possède une échéance, afficher la date lorsqu’elle constitue une information essentielle.

## 6.7 Boutons

| Variante   | Style                                          |
| ---------- | ---------------------------------------------- |
| Primaire   | `--color-brand`, texte blanc                   |
| Secondaire | surface blanche, bordure `--color-border`      |
| Destructif | `--color-danger`, plein ou contour             |
| Discret    | texte ou icône accompagnée d’un nom accessible |

Tous utilisent `--radius-sm`.

Hauteur minimale : 40 px.

Focus :

* anneau 2 px `--color-brand` ;
* décalage suffisant pour rester visible.

### Tailles

Deux densités sont admises :

**Normale**

* texte principal ;
* rembourrage horizontal 16 px.

**Compacte**

* texte 13 px ;
* rembourrage horizontal 8 px.

La hauteur interactive de 40 px reste identique.

Une action principale ne doit pas utiliser la taille compacte pour réduire artificiellement sa présence.

## 6.8 Badges et pilules

Forme :

`rounded-full`

Un badge coloré utilise :

* un fond `*-soft` ;
* un texte `*-on-soft` ;
* un point, une icône ou un libellé explicite.

Le texte doit respecter AA.

Exemple de correspondance :

| Valeur    | Fond                   | Texte                     |
| --------- | ---------------------- | ------------------------- |
| `brand`   | `--color-brand-soft`   | `--color-brand-on-soft`   |
| `success` | `--color-success-soft` | `--color-success-on-soft` |
| `accent`  | `--color-accent-soft`  | `--color-accent-on-soft`  |
| `danger`  | `--color-danger-soft`  | `--color-danger-on-soft`  |
| `neutral` | `--color-hover`        | `--color-text-2`          |

## 6.9 Champs de formulaire

Structure standard :

1. libellé ;
2. contrôle ;
3. texte d’aide ou état ;
4. erreur éventuelle.

Libellé :

* 13 px ;
* `--color-text-2`.

Contrôle :

* hauteur minimale 40 px ;
* bordure `--color-border` ;
* focus `--color-brand`.

Texte d’aide :

* 13 px ;
* `--color-text-3`.

Erreur :

* `--color-danger` ou couple `danger-soft` / `danger-on-soft` ;
* icône lorsque pertinente ;
* `role="alert"` ;
* association au champ par `aria-describedby`.

Une contrainte temporaire doit expliquer son origine.

Exemple :

« Requis pour effectuer cette action »

plutôt qu’un simple astérisque dépourvu de contexte.

## 6.10 Cases à cocher

La case visible peut mesurer 24 px.

Sa ligne interactive atteint au minimum `--size-target`.

Le libellé associé étend la cible cliquable.

Ne pas introduire une dimension intermédiaire absente de l’échelle de tokens.

## 6.11 Autosauvegarde d’un champ

Lorsqu’un champ s’enregistre individuellement, l’état d’écriture vit près du champ concerné.

États possibles :

* « Enregistrement… »
* « Enregistré »
* message de refus ou d’erreur.

Deux états contradictoires ne sont jamais affichés simultanément.

La confirmation remplace l’état d’envoi.

Le contrôle n’est pas automatiquement désactivé pendant une écriture courte.

Un refus n’efface pas la saisie utilisateur.

Une erreur métier et un avertissement de valeur manquante peuvent coexister lorsqu’ils décrivent des informations différentes.

## 6.12 Mise en évidence d’un champ demandé par une action

Lorsqu’une action globale échoue parce qu’un champ doit être complété :

* utiliser `--color-brand`, pas `--color-danger`, si le champ n’est pas invalide ;
* ajouter un texte expliquant pourquoi le champ est attendu ;
* amener le premier champ pertinent dans la zone visible ;
* déplacer le focus vers ce champ ;
* ne réaliser ce déplacement automatique qu’une fois par arrivée ou contexte ;
* respecter `prefers-reduced-motion`.

Un champ manquant et un champ incorrect ne constituent pas le même état.

## 6.13 États systématiques d’une vue

Toute vue doit explicitement traiter les états pertinents parmi :

* chargement ;
* vide ;
* erreur ;
* absence de droit ;
* absence de sélection ;
* mesure indisponible ;
* résultat partiel.

Le chargement utilise de préférence des squelettes correspondant à la forme du contenu final.

Éviter le spinner plein écran.

Un état vide ne doit proposer une action que lorsqu’une action pertinente existe réellement.

Une vue saine sans donnée, par exemple une corbeille vide, peut n’avoir aucune action.

## 6.14 Tableau de données

Utiliser les éléments HTML natifs :

* `table`
* `thead`
* `tbody`
* `th`
* `td`

Ne pas reconstruire une table avec des `div` lorsque les données sont réellement tabulaires.

### Ligne

Hauteur minimale : `--size-target`.

Une cellule dense utilise une seule ligne de texte avec ellipse si nécessaire.

La valeur complète peut être accessible via une information complémentaire appropriée.

### En-tête

* collant lorsque nécessaire ;
* `--color-bg` ;
* texte 13 px `--color-text-2` ;
* séparateur bas `--color-border`.

### Lignes

* séparateur bas ;
* pas de zébrures par défaut ;
* survol `--color-hover`.

### Interaction

Une ligne entière n’est cliquable que lorsqu’elle représente réellement une seule destination non ambiguë.

Sinon, seul l’élément concerné est un lien ou un bouton.

### Tri

Un `button` vit dans l’en-tête triable.

Le `th` porte `aria-sort`.

L’icône accompagne l’information, elle ne la porte pas seule.

### Alignement

* texte à gauche ;
* données numériques comparables à droite ;
* montants et dates en chiffres tabulaires lorsque pertinent.

### Valeur absente

Dans un tableau, une cellule peut rester vide lorsqu’aucune donnée n’existe.

Ne pas remplir systématiquement les cellules avec « N/A », « non renseigné » ou un tiret.

### Pagination

Les commandes restent présentes aux extrémités et peuvent être désactivées.

Le rang courant est écrit explicitement.

Exemple :

« Page 2 sur 5 »

## 6.15 Commentaires et discussions

Un commentaire est une surface de contenu, pas nécessairement une carte interactive.

Ordre recommandé pour une conversation :

chronologique croissant, du plus ancien au plus récent.

Un commentaire affiche typiquement :

* avatar ;
* nom ;
* date ;
* corps ;
* état éventuel ;
* actions disponibles.

Le corps utilisateur est rendu comme texte brut par défaut.

Ne jamais interpréter du Markdown ou du HTML utilisateur sans décision explicite de sécurité et de produit.

### Suppression

Un contenu supprimé conserve sa place lorsque cette place est nécessaire à la compréhension de la conversation.

Exemple :

« Commentaire supprimé »

Une suppression effectuée par modération peut utiliser un libellé distinct.

### Actions

Les actions réservées à l’auteur peuvent être visibles au survol, mais doivent également apparaître au focus clavier.

Lorsque plusieurs actions accompagnent une métadonnée, une ligne dédiée évite qu’elles recouvrent ou compressent le contenu.

Lorsqu’une commande ouvre une édition :

* le focus entre dans le champ ;
* le curseur se place à un endroit logique, généralement en fin de texte.

## 6.16 Timeline unifiée

Une timeline peut combiner :

* commentaires ;
* changements de données ;
* changements de statut ;
* actions système ;
* événements de cycle de vie.

La différence de nature doit être portée par la forme.

Patron recommandé :

* commentaire : bloc de contenu ;
* événement système : ligne compacte avec pastille d’icône.

Une ligne d’événement contient :

* pastille d’icône ;
* description ;
* acteur lorsqu’il est connu ;
* date.

L’icône est redondante avec le texte.

Aucun filet vertical n’est requis par défaut.

Il ne doit être ajouté que si l’observation montre qu’il améliore effectivement la lecture.

### Filtres

Une barre de filtres n’est affichée que lorsqu’il existe quelque chose à filtrer.

Des boutons `aria-pressed` conviennent aux filtres de vue indépendants d’un formulaire.

Leur état doit être perceptible par :

* couleur ;
* graisse ou forme ;
* attribut `aria-pressed`.

Le compteur d’une catégorie reste indépendant du fait que cette catégorie soit actuellement visible.

## 6.17 Authentification et session

L’écran de connexion est une surface autonome.

Avant authentification, ne pas afficher une navigation applicative inutilisable.

Structure recommandée :

* fond `--color-bg` ;
* carte `--color-surface` ;
* `--radius-lg` ;
* bordure ;
* ombre standard ;
* nom ou marque du produit ;
* titre ;
* phrase explicative ;
* champs ;
* action principale.

Ne pas afficher :

* une création de compte lorsque l’inscription libre n’existe pas ;
* une récupération de mot de passe inerte ;
* une action non implémentée.

L’erreur d’authentification :

* reste près du formulaire ;
* utilise `danger-soft` / `danger-on-soft` ;
* porte `role="alert"`.

Sous 768 px, éviter qu’un centrage vertical masque les contrôles avec le clavier virtuel.

## 6.18 Administration hiérarchique

Une structure parent / enfant utilise de préférence une liste imbriquée lorsque les niveaux ne partagent pas les mêmes colonnes.

Patron :

`ul` / `li`

Le dépliage utilise un bouton avec `aria-expanded`.

Le groupe d’actions reste visible lorsqu’il constitue l’objet principal de l’écran.

Les commandes de déplacement :

* restent à la même position ;
* peuvent être désactivées aux extrémités ;
* ne disparaissent pas simplement parce qu’elles sont momentanément indisponibles.

## 6.19 Administration d’une liste plate

Lorsqu’une collection ne possède qu’un niveau et que ses attributs qualifient chaque objet sans constituer de véritables colonnes comparables, préférer une `ul` structurée plutôt qu’un tableau artificiel.

Les lignes utilisent :

* `--size-target` ;
* séparateurs ;
* survol neutre ;
* groupe d’actions stable.

## 6.20 Graphes et workflows

Ne pas rendre automatiquement un graphe métier sous forme de canevas visuel.

Un diagramme interactif implique :

* disposition ;
* zoom ;
* navigation clavier ;
* équivalent textuel ;
* gestion de focus ;
* responsive spécifique.

Lorsque ces mécanismes ne sont pas nécessaires, une représentation en listes ordonnées peut être préférable.

Exemple générique :

```text
Étape A
  Vers Étape B
  Vers Étape C

Étape B
  Aucune sortie
```

Le sens d’une relation doit être écrit.

Une flèche ne doit pas constituer la seule indication.

## 6.21 Grilles de configuration

Lorsqu’une configuration croise deux dimensions, utiliser une table sémantique.

Exemple :

champ × étape

rôle × permission

module × environnement

Chaque contrôle doit avoir un nom accessible qui identifie les deux dimensions.

Une première colonne peut rester collante pendant le défilement horizontal.

Le tableau défile dans son propre conteneur.

## 6.22 Confirmation intégrée au flux

Une confirmation n’a pas besoin d’être une modale.

Pour de nombreuses actions localisées, préférer un bloc placé :

* sous l’élément concerné ;
* à la place du contenu ;
* sous le contrôle déclencheur.

Cela évite d’introduire inutilement :

* un piège de focus ;
* un voile ;
* une gestion globale d’`Échap` ;
* une surface superposée.

Lorsqu’une confirmation s’ouvre :

* le focus entre dans la confirmation ;
* `Échap` peut refermer un panneau réversible lorsque pertinent ;
* l’annulation rend le focus au déclencheur.

## 6.23 Actions destructives

Une action destructive demande une confirmation explicite lorsqu’elle entraîne une perte ou une modification difficilement réversible.

La confirmation nomme l’objet ou la conséquence.

Le bouton final utilise la variante destructive.

Le bouton qui ouvre la confirmation peut rester secondaire lorsque l’action n’est pas encore engagée.

Ne pas utiliser la couleur `danger` simplement parce qu’une action est importante.

## 6.24 Action réparatrice

Une action de restauration, réveil, réactivation ou récupération n’a généralement pas besoin d’une confirmation lorsqu’elle :

* ne détruit rien ;
* n’a aucun paramètre ;
* est facilement réversible.

Une confirmation systématique banalise les confirmations réellement importantes.

## 6.25 Corbeille

Une corbeille peut utiliser un tableau lorsque toutes les entrées partagent les mêmes propriétés d’événement :

* type ;
* nom ;
* auteur ;
* date ;
* impact ;
* restauration.

Le type doit être écrit en toutes lettres.

Une donnée inconnue constitue parfois un fait et doit être nommée.

Exemple :

« Auteur inconnu »

Une mesure peut distinguer :

* valeur connue ;
* mesure en cours ;
* mesure impossible.

Un blanc ne doit pas être utilisé lorsque son interprétation serait ambiguë.

## 6.26 Guide de démarrage

Un onboarding séquentiel utilise une `ol` lorsque les étapes possèdent un ordre logique.

L’état d’une étape est écrit en toutes lettres.

Exemples :

« Fait »

« À faire »

« Cette étape n’a pas pu être vérifiée »

Une étape accomplie peut conserver son lien lorsque l’action reste utile.

La progression est écrite :

« 3 étapes sur 5 »

Une barre graphique peut l’accompagner, mais ne constitue pas l’unique représentation.

Éviter par défaut les visites guidées flottantes et surimpressions lorsque le même objectif peut être atteint par un écran normal, accessible et persistant.

---

# 7. Interactions

* Retour visuel perceptible immédiatement après une action utilisateur.
* Transitions recommandées : 150 à 250 ms `ease-out`.
* Respect systématique de `prefers-reduced-motion`.
* Une opération longue indique son état réel.
* Une progression connue est représentée comme telle.
* Une opération interruptible propose une interruption.
* Une opération non interruptible ne prétend pas l’être.

## 7.1 Optimisme UI

Une modification optimiste est admise lorsque :

* le retour arrière est déterministe ;
* l’état précédent est conservé ;
* un refus backend peut être représenté clairement.

En cas de refus :

1. restaurer l’état réel ;
2. conserver autant que possible la saisie utilisateur ;
3. afficher la raison du refus près de l’action concernée.

---

# 8. Responsive

Paliers de référence :

| Palier         | Comportement général                                      |
| -------------- | --------------------------------------------------------- |
| ≥ 1280 px      | Navigation complète, vues multi-colonnes                  |
| 1024 à 1279 px | Navigation compacte, densité intermédiaire                |
| 768 à 1023 px  | Navigation en tiroir, colonnes empilées si nécessaire     |
| < 768 px       | Navigation mobile, défilement local des structures larges |

Ces paliers constituent des valeurs par défaut, pas une obligation de mise en page identique pour toutes les applications.

## 8.1 Règles invariantes

* Aucun contenu essentiel n’est masqué sans autre point d’accès.
* La page ne défile jamais horizontalement.
* Les tableaux larges défilent dans leur propre conteneur.
* Les boards larges défilent dans leur propre conteneur.
* Une navigation horizontale longue signale qu’elle peut défiler.
* Une mise en page ne doit pas simplement compresser un composant desktop jusqu’à devenir inutilisable.

## 8.2 Débordement horizontal

Tout conteneur `overflow-x: auto` doit fournir une indication perceptible lorsque du contenu existe hors champ.

Une implémentation CSS commune peut utiliser des ombres de défilement fondées sur :

* `background-attachment: local`;
* `background-attachment: scroll`;
* `--color-bg`;
* `--color-border`.

L’indication doit apparaître uniquement lorsqu’un débordement existe réellement.

Les composants ne réimplémentent pas individuellement cette logique.

---

# 9. Accessibilité

L’accessibilité fait partie du contrat du design system.

## 9.1 Clavier

Toute fonction doit être utilisable sans souris.

Cela inclut notamment :

* navigation ;
* ouverture de menus ;
* formulaires ;
* tableaux interactifs ;
* déplacements d’éléments ;
* confirmations ;
* actions contextuelles.

## 9.2 Structure sémantique

Utiliser les éléments HTML natifs lorsqu’ils existent.

Exemples :

* `nav`
* `main`
* `aside`
* `button`
* `a`
* `table`
* `ol`
* `ul`
* `fieldset`
* `label`
* `dl`

Ne pas reconstruire artificiellement leur comportement avec des `div` et des rôles ARIA sans nécessité.

## 9.3 Titres

La hiérarchie des titres ne saute pas arbitrairement de niveau.

## 9.4 Contraste

Objectif minimal :

AA, soit 4,5:1 pour le texte normal.

Le contraste doit être **mesuré sur les couleurs effectivement rendues**, y compris :

* badges ;
* pilules ;
* texte sur fonds doux ;
* états interactifs.

Une couleur qui semble lisible n’est pas nécessairement conforme.

## 9.5 Focus

`:focus-visible` est perceptible sur tout élément interactif.

Un changement de mode ou de surface ne doit pas laisser le focus sur un élément disparu.

## 9.6 Cibles

Cible interactive minimale : 40 px.

Une petite icône peut rester visuellement compacte à l’intérieur de cette cible.

## 9.7 Changements dynamiques

Les changements significatifs utilisent des régions appropriées.

Exemples :

* `role="status"` pour une confirmation ;
* `role="alert"` pour une erreur ;
* `aria-live="polite"` pour un changement non urgent.

## 9.8 Couleur

La couleur ne constitue jamais le seul porteur d’un état.

## 9.9 État désactivé

Lorsqu’une action existe mais est indisponible dans un état connu, elle peut rester visible et désactivée.

La raison doit rester compréhensible.

Cette règle ne s’applique pas à une fonctionnalité qui n’existe pas.

---

# 10. Icônes

Bibliothèque de référence :

**Lucide**

Caractéristiques :

* trait 2 px ;
* tailles généralement comprises entre 14 et 28 px ;
* `aria-hidden="true"` lorsqu’un libellé visible décrit déjà l’action.

Aucun emoji ne remplace une icône d’interface.

## 10.1 Pastille d’icône

Patron :

* carré `--radius-md` ;
* fond doux de la catégorie ;
* icône à la couleur correspondante ;
* dimension cohérente avec la densité du composant.

## 10.2 Icône sans texte visible

Une icône utilisée seule doit posséder un nom accessible explicite.

Exemple :

`aria-label="Supprimer l’élément"`

et non :

`aria-label="Supprimer"`

lorsque plusieurs éléments sont présents.

## 10.3 Favicon

Chaque application doit fournir explicitement son favicon.

Le favicon :

* doit rester identifiable à 16 px ;
* évite les détails décoratifs ;
* ne dépend pas d’une police distante ;
* est référencé explicitement dans le document HTML.

Une application P2Enjoy peut dériver son favicon de la marque P2Enjoy, tout en conservant une identité produit propre lorsque nécessaire.

---

# 11. Internationalisation

Aucun texte visible destiné à l’utilisateur n’est écrit directement dans un composant lorsqu’un système d’internationalisation est présent.

Tous les textes applicatifs passent par des clés stables.

Langue par défaut recommandée :

français.

Les données métier saisies ou administrées par l’utilisateur restent des données et ne deviennent pas automatiquement des clés de traduction.

Les interfaces doivent tolérer des textes environ 40 % plus longs que leur version française.

## 11.1 Contrôle automatique

Lorsque le projet utilise TypeScript et JSX, la détection de textes écrits en dur doit analyser l’arbre syntaxique plutôt qu’utiliser une expression régulière sur le code source.

Le contrôle doit reconnaître correctement :

* `JsxText` ;
* chaînes littérales utilisées comme enfants JSX ;
* attributs visibles comme `title`, `aria-label`, `placeholder` et `alt`.

Un contrôle qualité ne doit pas imposer une syntaxe artificielle simplement pour satisfaire son propre parseur.

---

# 12. Implémentation

## 12.1 Tokens

Les tokens sont déclarés une seule fois, typiquement sur `:root`.

Les composants consomment les tokens.

Ils ne recopient pas les valeurs.

## 12.2 Tailwind

Lorsqu’une application utilise Tailwind, la configuration doit empêcher l’utilisation accidentelle de valeurs hors design system.

Les espaces de noms concernés peuvent être réinitialisés avant redéclaration :

```css
--color-*: initial;
--spacing-*: initial;
--text-*: initial;
--radius-*: initial;
--shadow-*: initial;
--breakpoint-*: initial;
```

Puis seuls les tokens autorisés sont exposés.

L’objectif est qu’une classe comme `bg-red-500` ou `p-7` n’existe simplement pas lorsqu’elle ne fait pas partie du design system.

## 12.3 Classes non générées

Une classe dépendant d’un token inexistant peut disparaître silencieusement du CSS généré.

Ce cas doit être contrôlé automatiquement.

Le pipeline UI doit pouvoir vérifier que chaque classe utilisée par les composants possède effectivement une règle dans le CSS produit.

Cette vérification est particulièrement importante lorsque les namespaces Tailwind par défaut sont supprimés.

## 12.4 Composants partagés

Les composants fondamentaux vivent dans un espace dédié, par exemple :

```text
src/components/ui/
```

ou :

```text
webapp/src/components/ui/
```

Les composants métier composent ces primitives.

Ils ne redéfinissent pas localement les styles fondamentaux.

## 12.5 Correspondances de tokens

Les correspondances entre une donnée métier comme :

```text
brand
success
accent
danger
neutral
```

et les tokens visuels vivent à un seul endroit.

Même règle pour un catalogue d’icônes.

Un composant ne possède pas sa propre copie de la correspondance.

## 12.6 Commentaires de spécification

Un composant partagé peut porter un commentaire `@spec` renvoyant vers cette référence ou vers une extension locale.

La référence ne doit pas dépendre d’un système de tickets particulier.

---

# 13. Preuves UI et validation

Toute évolution visuelle importante doit pouvoir être inspectée sur l’application réellement exécutée.

Le projet peut conserver :

```text
e2e/output/
e2e/captures/
e2e/videos/
```

ou toute structure équivalente.

## 13.1 Validation attendue

Selon le changement, vérifier :

* desktop ;
* tablette ;
* mobile ;
* état vide ;
* état chargé ;
* état erreur ;
* contenu long ;
* clavier ;
* focus ;
* contraste ;
* défilement ;
* données inhabituelles ;
* permissions ou refus backend ;
* `prefers-reduced-motion`.

## 13.2 Les captures sont une preuve

Certaines catégories de défauts sont difficilement détectables autrement :

* débordement coupé ;
* contraste visuellement faible ;
* métadonnée comprimée ;
* contrôle recouvert ;
* mauvaise densité ;
* espace inutile ;
* hiérarchie visuelle incorrecte ;
* dernière option invisible ;
* composant desktop simplement rétréci.

Une interface qui passe ses tests peut encore être visuellement incorrecte.

## 13.3 Les mesures sont une preuve

Certaines erreurs ne sont pas perceptibles de façon fiable à l’œil.

Exemples :

* contraste 3,8:1 au lieu de 4,5:1 ;
* classe CSS absente du build ;
* comportement d’un événement navigateur ;
* largeur effective ;
* scroll réel ;
* focus perdu ;
* réponse backend sans ligne modifiée.

Dans ces cas, mesurer plutôt que supposer.

---

# 14. Règles issues de comportements réels

Cette section formalise plusieurs enseignements génériques qui doivent être conservés d’une application à l’autre.

## 14.1 Contraste des fonds doux

La couleur principale d’un token n’est pas nécessairement suffisamment contrastée lorsqu’elle est utilisée comme texte sur sa propre déclinaison douce.

Exemple avec la palette P2Enjoy :

| Token     | Couleur pleine sur fond doux | Contraste approximatif |
| --------- | ---------------------------- | ---------------------- |
| `brand`   | conforme                     | 7,64:1                 |
| `success` | insuffisant                  | 3,82:1                 |
| `accent`  | insuffisant                  | 1,45:1                 |
| `danger`  | insuffisant                  | 3,29:1                 |
| `neutral` | conforme                     | 6,87:1                 |

D’où l’existence des tokens `*-on-soft`.

La conformité doit être calculée, pas seulement déclarée.

## 14.2 Débordement horizontal

`overflow-x: auto` ne suffit pas.

Si l’utilisateur ne voit pas qu’il existe du contenu supplémentaire, le contenu est fonctionnellement caché.

Tout débordement horizontal doit donc être signalé.

## 14.3 Focus après disparition d’un contrôle

Lorsqu’un bouton ouvre une autre interface puis disparaît, le focus doit être déplacé vers cette interface.

Lorsqu’elle se ferme, le focus revient au déclencheur logique.

Ne jamais laisser le navigateur gérer ce cas par hasard.

## 14.4 Contrôle sans objet

Une barre de filtres, un bouton ou une option qui ne peut rien affecter crée du bruit.

Lorsqu’un contrôle dépend de l’existence d’un contenu, sa présence peut elle-même dépendre de ce contenu.

Exception : lorsqu’il constitue précisément le moyen de sortir d’un état vide causé par son filtre.

## 14.5 Valeur vide et fait d’absence

Distinguer :

**absence de donnée**

La cellule ou la ligne peut rester vide ou ne pas être rendue.

**information selon laquelle quelque chose n’existe pas**

Elle doit être nommée.

Exemples :

« Auteur inconnu »

« Jamais synchronisé »

« Aucun responsable »

« Aucun résultat »

## 14.6 Mesure indisponible et valeur zéro

Ne jamais confondre :

* zéro ;
* calcul en cours ;
* calcul impossible ;
* donnée inexistante.

Ces états utilisent des textes distincts.

## 14.7 Donnée inconnue

Une valeur technique inconnue reçue du backend ne doit jamais devenir `undefined` dans l’interface.

Prévoir :

* repli neutre ;
* libellé générique ;
* absence contrôlée du détail.

## 14.8 Forme et nature

Deux catégories d’objets de nature différente ne doivent pas être distinguées uniquement par leur couleur.

Utiliser également une différence de structure.

Exemple :

* parole humaine : carte ;
* événement système : ligne.

## 14.9 Backend comme autorité

Ne pas désactiver une action simplement parce que l’interface pense qu’elle sera refusée lorsqu’elle ne possède pas une connaissance fiable de la règle.

À l’inverse, ne pas afficher une action dont la fonctionnalité n’existe réellement pas.

La distinction entre :

**fonction inexistante**

et

**fonction existante mais éventuellement refusée**

est fondamentale.

---

# 15. Contrat d’extension par application

Cette référence reste volontairement générique.

Chaque application peut créer un fichier complémentaire, par exemple :

```text
docs/DESIGN_SYSTEM_APP.md
```

ou :

```text
docs/design-system/APP_REFERENCE.md
```

Ce fichier ne recopie pas la présente référence.

Il contient uniquement ce qui est spécifique au produit.

## 15.1 Informations autorisées dans l’extension

L’extension peut définir :

* architecture particulière de navigation ;
* composants métier ;
* terminologie métier ;
* dimensions justifiées par un composant spécifique ;
* états particuliers ;
* règles de visualisation propres au domaine ;
* choix de responsive particuliers ;
* composants supplémentaires ;
* écarts motivés au socle ;
* liens vers les spécifications du projet ;
* captures de référence ;
* décisions issues de tests réels.

## 15.2 Informations qui restent ici

Une règle doit remonter dans cette référence lorsqu’elle est réutilisable sans connaître le métier de l’application.

Exemples :

* gestion du focus ;
* badges AA ;
* comportement d’un tableau ;
* confirmation dans le flux ;
* squelettes ;
* défilement horizontal signalé ;
* autosauvegarde ;
* gestion d’un refus ;
* navigation par liens ;
* taille des cibles ;
* gestion d’une timeline ;
* règles Tailwind ;
* validation sur captures.

## 15.3 Modèle d’extension

```markdown
# Design System Extension : <Nom de l’application>

Référence complémentaire à `DESIGN_SYSTEM.md`.

Seules les règles propres à cette application sont documentées ici.

## 1. Architecture spécifique

...

## 2. Terminologie métier

...

## 3. Composants métier

...

## 4. Règles de visualisation particulières

...

## 5. Responsive spécifique

...

## 6. Écarts au design system commun

### APP-DS-001 : <titre>

Date :

Règle commune concernée :

Écart :

Justification :

Preuve :

Décision :

## 7. Captures de référence

...
```

---

# 16. Gestion des écarts

Tout écart au design system commun est explicite.

Il comporte au minimum :

* identifiant local ;
* date ;
* règle concernée ;
* comportement retenu ;
* justification.

Lorsqu’une décision provient d’une observation ou d’une mesure, la preuve est indiquée.

Un écart peut ensuite :

* rester spécifique au produit ;
* être refermé ;
* devenir une règle commune et remonter dans cette référence.

Une ancienne décision ne doit pas survivre automatiquement lorsque le motif qui la justifiait a disparu.

Le design system documente les contraintes présentes, pas l’histoire figée du produit.
