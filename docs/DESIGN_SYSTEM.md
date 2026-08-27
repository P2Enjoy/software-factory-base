# DESIGN SYSTEM REFERENCE : P2Enjoy Applications

Référence maîtresse pour l’interface des applications P2Enjoy. Elle dérive de la **charte P2Enjoy SAS** et définit les règles transversales de conception, d’implémentation, d’accessibilité et de validation visuelle.

**Ce fichier se lit intégralement avant toute modification, revue ou commit touchant l’UI ou l’UX**, y compris pour une correction visuelle jugée mineure.

Tout changement d’interface doit être vérifié contre ce document avant commit.

## Périmètre impératif : socle global uniquement

**`DESIGN_SYSTEM.md` est GLOBAL à toutes les applications P2Enjoy. Il ne doit contenir AUCUNE trace d’un projet précis.**

Cette interdiction couvre notamment :

* le nom d’un produit, d’un projet ou d’une application ;
* une entité métier propre à un projet ;
* un nom d’écran, d’onglet, de route, de section ou de commande propre à un produit ;
* une architecture fonctionnelle particulière ;
* un état, un quota, une mesure, une valeur, une terminologie ou un comportement propre au métier courant ;
* un identifiant de ticket, de backlog ou de décision ;
* une capture, un chemin de preuve ou un résultat de test propre à un dépôt ;
* une exception décidée pour une seule application ;
* un exemple qui ne peut être compris qu’en connaissant le projet ayant servi à produire la règle.

Le test d’admission est simple : **une règle ou un exemple ne reste ici que s’il peut être compris, appliqué et réutilisé sans connaître le projet courant**. Dans le cas contraire, il appartient au fichier jumelé `docs/DESIGN_SYSTEM_APP.md`.

`DESIGN_SYSTEM_APP.md` est l’extension locale obligatoire dès qu’un projet possède des références, décisions, terminologies, composants, mesures ou exceptions spécifiques. Il référence les sections de ce socle au lieu de les recopier.

Lorsqu’une règle nouvelle apparaît :

* si elle est réutilisable entre plusieurs applications sans connaître leur métier, elle est ajoutée ici ;
* si elle relève du métier, du produit ou de l’implémentation du projet courant, elle est ajoutée à `DESIGN_SYSTEM_APP.md` ;
* si une application doit déroger à une règle commune, l’écart est documenté uniquement dans `DESIGN_SYSTEM_APP.md`, avec justification, date et preuve lorsque celle-ci existe.

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

## 1.5 bis L’écran nomme, le manuel explique

Un écran d’administration affiche des **valeurs** et des **noms**. Il ne porte pas
le raisonnement qui a conduit à les produire.

Ce qui reste à l’écran :

* la valeur, son unité, et ce à quoi elle se rapporte ;
* le nom de ce qui la commande — un réglage, une variable, une source ;
* le mot exact qui la qualifie lorsqu’elle est ambiguë : « plafond », « réservé »,
  « alloué », « non mesuré ».

Ce qui part au manuel :

* **pourquoi** la grandeur existe et ce qui arrive sans elle ;
* le mode de panne qu’elle évite ;
* l’historique de la décision, la mesure qui l’a établie, le compromis retenu.

Motif, et il est double. D’abord, une explication de trois lignes par ligne de
tableau **noie la valeur** : l’écran d’un exploitant se lit en diagonale, sous
pression, pour trouver un chiffre. Ensuite, une explication écrite deux fois — à
l’écran et au manuel — **diverge**. Celle de l’écran est la plus difficile à
maintenir et la plus lue : c’est donc celle qui ment en premier.

Le test : si la phrase reste vraie quand toutes les valeurs de l’écran changent,
elle n’appartient pas à l’écran. Elle appartient au manuel.

Ce n’est pas une invitation à rendre l’interface muette. Une valeur ambiguë est
**qualifiée** par son unité et son référentiel lorsque ceux-ci sont nécessaires à sa compréhension, une absence est
**nommée** (§14.5, §14.6), et un renvoi mène au chapitre du manuel qui explique.
Le renvoi remplace le paragraphe ; il ne remplace pas le mot juste.

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

Ce patron n’est pas un exemple parmi d’autres : c’est la forme par défaut. La
navigation de premier niveau est une barre latérale, celle de second niveau des
onglets, et la modification d’une section passe par une modale. Les trois degrés
sont définis au §5.4 ; la surface qu’ils ouvrent l’est au §6.27.

Une application peut retenir un autre patron — une barre horizontale sur deux ou
trois destinations, par exemple. Ce n’est alors plus une préférence de mise en
page mais un **écart**, documenté comme tel (§16), avec le motif qui le justifie.

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

## 5.4 Les degrés de navigation

Chaque degré a une forme, et cette forme dit à l’utilisateur *ce qui va changer*
quand il clique.

| Degré | Ce qu’il représente | Forme |
|---|---|---|
| 1 | destinations principales du produit | barre latérale |
| 2 | sous-parties d’une même destination | onglets |
| 3 | l’objet ouvert depuis une sous-partie | fenêtre, elle-même découpée en sections — et en onglets lorsque l’objet a plusieurs facettes |
| — | modifier une section, ou lui insérer un élément | modale limitée à cette section (§6.27) |

**Cette hiérarchie est une orientation, pas une loi.** Elle donne la forme par
défaut de chaque niveau ; elle n’interdit pas un niveau de plus lorsqu’il rend
l’écran plus clair. Un niveau supplémentaire est légitime lorsqu’il sépare une
facette réellement distincte d’un objet, sans introduire une navigation redondante.

Ce qui n’est **pas** négociable, en revanche, tient en trois points — et c’est ce
que la hiérarchie sert à obtenir, pas l’inverse :

1. **Ce qu’on affiche et ce qu’on saisit ne partagent pas la même surface.** Une
   fenêtre montre ; une modale recueille. Un écran qui mélange les deux ne dit
   plus ce qui fait foi.
2. **Une surface a un sujet, et un seul.** Une section, un objet, une modale : à
   chaque fois, nommable en une phrase. Une surface qu’on ne peut pas nommer est
   une surface qui en contient deux.
3. **Une action sensible demande toujours une confirmation explicite** (§6.23).
   Aucun degré de navigation n’en dispense.

Un niveau de plus n’est jamais gratuit : chacun ajoute un clic, un état à retenir
et une chose à annoncer. Il se justifie par ce qu’il **sépare**. Un niveau qui ne
contient qu’un seul panneau ne sépare rien : c’est un clic de plus pour arriver
au même endroit.

### Degré 1 — barre latérale

Une liste verticale absorbe une destination de plus sans rien sacrifier. Une
barre horizontale, elle, oblige à arbitrer la largeur dès la cinquième entrée :
on replie, on abrège, on cache derrière un « plus », et la destination courante
finit par ne plus être visible. La barre latérale est donc le défaut, y compris
lorsque le produit n’a encore que deux destinations — c’est précisément le moment
où le choix ne coûte rien.

Elle suit les règles du §5.1 : identifiable, libellés accessibles conservés même
lorsqu’elle devient iconographique, `aria-current="page"` sur la destination
courante, état actif jamais porté par la seule couleur.

Sous 1024 px, elle devient un tiroir ou une barre inférieure. Elle ne devient
jamais un menu iconographique sans libellés : un pictogramme seul n’est pas une
navigation, c’est une devinette.

### Degré 2 — onglets

Les sous-parties d’une destination sont des onglets. Visuellement, ce sont des
onglets dans les deux cas ; la sémantique, elle, dépend de ce qui change
réellement (§5.2) :

* les panneaux sont **échangés dans la même vue**, sans changement d’URL — patron
  ARIA `tablist` / `tab` / `tabpanel`, navigation par flèches, `Home` et `End` ;
* la sous-partie est une **véritable destination** — URL propre, partageable,
  rechargeable — ce sont des **liens** dans un `nav`, avec
  `aria-current="page"`, et surtout **pas** un `tablist`.

Le critère est l’URL, jamais l’apparence.

Un onglet change ce que l’on regarde. Il ne modifie jamais l’état des données, et
ne porte donc aucune action : les actions appartiennent à la section qu’il
révèle. C’est le point 1 ci-dessus, appliqué à la navigation.

Des onglets peuvent apparaître **deux fois** dans une même arborescence — au
second degré pour choisir une sous-partie, puis dans la fenêtre d’un objet pour
choisir une de ses facettes. Ce n’est pas une entorse : ce sont deux sujets
différents, et chacun est nommable. Ce qui serait une faute, c’est deux rangées
d’onglets **côte à côte** pour un même sujet.

### Degré 3 — la fenêtre d’un objet

Ouvrir un élément d’une liste ouvre sa **fenêtre** : la surface où cet objet est
lu, découpée en sections, et découpée en onglets lorsqu’il a plusieurs facettes
(§6.27).

Une fenêtre est une **destination** dès qu’on peut vouloir la rouvrir, la
recharger ou en partager l’adresse. Elle a alors une URL, comme n’importe quelle
destination du §5.2.

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

### Un champ en lecture seule se VOIT

Un contrôle `readonly` qui a l'apparence d'un contrôle modifiable est un piège :
on clique dedans, on tape, et rien ne se passe — sans qu'aucun message
n'explique pourquoi.

Un champ en lecture seule porte donc, en plus de l'attribut :

* un fond `--color-bg`, distinct du blanc des contrôles modifiables ;
* un curseur `default`, jamais le curseur de saisie ;
* un texte d'aide qui dit **d'où vient la valeur**, pas seulement qu'elle est
  figée, par exemple « valeur fournie par une source externe » ou « valeur définie par le système ».

Il reste **focusable** au clavier et sélectionnable à la souris : la valeur doit
pouvoir être lue par une synthèse vocale et copiée. C'est ce qui distingue
`readonly` de `disabled`, lequel sort du parcours de tabulation et ne convient
donc pas à une valeur qu'on veut donner à lire.

Le focus entrant d'une modale ignore ces champs et va au premier contrôle
**modifiable** (§6.27).

## 6.9 bis Curseur ou saisie numérique

Pour une valeur numérique, le **curseur** (`input[type="range"]`) est la forme
préférée. Il montre la plage en même temps que la valeur, il se règle d'un geste,
et il rend une valeur hors bornes impossible à produire.

Ce n'est pas une obligation. Le curseur est retenu lorsque les **trois**
conditions suivantes tiennent ensemble. Dès que l'une manque, la saisie numérique
est le bon contrôle, et ce n'est pas un pis-aller.

1. **Les deux bornes sont connues et stables.** Connues : l'écran sait dire
   jusqu'où va la plage. Stables : la borne ne se périme pas entre l'ouverture de
   l'écran et la soumission. Une borne posée sur une mesure rafraîchissable
   ferait décider le contrôle à la place du serveur, et sur une photographie.
2. **Un pas traverse la plage en un nombre de crans atteignables.** Le contrôle
   mesure au plus 28 rem, soit 448 px : au-delà d'environ **400 crans**, un cran
   devient plus étroit qu'un pixel et cesse d'être visé au pointeur. Au-delà,
   c'est une saisie.
3. **Ce pas ne dégrade pas la granularité que le sens métier exige.** Si le seul
   pas qui ramène la plage sous 400 crans est plus grossier que ce que la valeur
   signifie — au point de rendre une valeur courante inatteignable —, c'est une
   saisie.

Un curseur seul est illisible : la poignée ne dit pas où elle est. Il porte donc
toujours

* sa **valeur en clair**, formatée avec son unité, à côté de la piste ;
* `aria-valuetext` avec cette même chaîne, sans quoi la synthèse peut annoncer
  une valeur nue alors que l’écran affiche une valeur qualifiée par son unité ;
* ses **deux bornes**, écrites sous la piste ;
* une phrase disant **d'où vient la borne haute** lorsque celle-ci n'est pas
  évidente. Une limite sans origine se lit comme un interdit arbitraire.

La borne basse n'est jamais une valeur que le formulaire refusera ensuite : un
curseur ne doit pas pouvoir produire une valeur invalide (§1.4).

**La valeur affichée est EXACTE sur la grille du curseur.** Un format qui arrondit
convient à une mesure qu'on lit — la dernière décimale n'y apprend rien — mais pas
à un réglage qu'on transmet : un curseur qui affiche « 10 unités » pour 10,25 unités
ment sur ce qu'il va envoyer, et l'utilisateur qui déplace la poignée d'un cran
voit un chiffre immobile. Choisir le pas, c'est donc aussi choisir un format
capable de le rendre ; si aucun format ne le peut, c'est le pas qui est mauvais.

Le curseur est nativement utilisable au clavier — flèches, `Origine`, `Fin`,
`Page préc.` et `Page suiv.` — et cet usage ne se remplace pas par un raccourci
maison. Sa hauteur cliquable atteint `--size-target` (§4.4).

Contre-exemple générique : un **identifiant numérique**. Même lorsqu’il est composé
de chiffres et possède des bornes formelles, il ne représente pas une grandeur
continue que l’on approxime. Une valeur voisine n’est pas « presque » correcte.
Un identifiant se saisit ou se recopie ; un curseur n’est donc pas le bon contrôle.

Lorsque les bornes ne sont **pas connues à l'exécution** — la mesure qui les donne
a échoué —, l'écran se rabat sur la saisie et nomme l'absence (§14.6). Il
n'invente pas une borne pour garder le curseur.

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

## 6.23 Actions sensibles et actions destructives

Une action **sensible** demande toujours une confirmation explicite. Est sensible
une action qui :

* détruit une donnée ou en rend la récupération incertaine ;
* est difficilement réversible ;
* produit un effet **au-delà** de ce que la surface courante montre ;
* porte sur un objet que le produit signale comme **protégé**.

Le dernier cas ne se règle pas par une confirmation : lorsqu’un objet est
protégé, la protection se **lève d’abord**, par un geste distinct et explicite.
Une confirmation qui lèverait la protection au passage ne protégerait de rien.

### Une protection ne bloque jamais un geste qui réduit un risque

Il y a une exception, et elle est absolue : une protection est là pour arrêter
l’erreur, jamais pour retenir un geste qui **diminue** l’exposition — révoquer un
accès, retirer une clé, couper une publication, fermer une session.

Refuser un tel geste ferait de la protection une vulnérabilité : un accès qui
devait disparaître survivrait parce que quelqu’un a oublié de désarmer un
interrupteur ailleurs. Le jour où l’on retire l’accès d’une personne partie, ou
d’une clé qui a fuité, on ne veut pas d’un obstacle — on veut savoir ce qu’on
touche.

La protection **informe** alors au lieu de refuser :

* les objets protégés concernés sont **nommés**, pas comptés ;
* l’action demande sa confirmation explicite, portant cette liste ;
* elle aboutit sans qu’aucune protection n’ait à être levée, et sans en lever
  aucune.

Le partage est celui-ci : **ajouter** un accès à un objet protégé se refuse,
**en retirer un** se confirme.

Une action destructive demande une confirmation explicite lorsqu’elle entraîne une perte ou une modification difficilement réversible.

La confirmation nomme l’objet ou la conséquence.

Le bouton final utilise la variante destructive.

Le bouton qui ouvre la confirmation peut rester secondaire lorsque l’action n’est pas encore engagée.

Ne pas utiliser la couleur `danger` simplement parce qu’une action est importante.

### Frapper le nom : quand l'exiger, et quand ne pas l'exiger

Une confirmation ordinaire prouve qu'on a **vu** l'écran. Frapper le nom de
l'objet prouve qu'on a **lu lequel**. Ce n'est pas la même chose, et la
différence n'apparaît que dans le cas qui compte : le mauvais objet sélectionné,
la ligne cliquée trop vite, le script lancé sur le mauvais nom.

**On l'exige quand les trois conditions tiennent ensemble :**

1. l'action est **irréversible** — aucun retour arrière, aucune corbeille ;
2. elle porte sur **un objet parmi d'autres qui se ressemblent**, donc
   confondables ;
3. le nom de l'objet est **court et visible** à l'écran au moment où on le frappe.
   Faire recopier un identifiant long apprend à le coller sans le lire, ce qui
   annule tout le bénéfice.

**On ne l'exige pas** dès qu'une seule manque. En particulier :

* jamais sur une action réversible (§6.24) ;
* jamais sur une action fréquente. Le §6.24 le dit d'une confirmation, et cela
  vaut à plus forte raison ici : une frappe demandée plusieurs fois par jour
  devient un réflexe, et un réflexe ne lit plus.

**Contrat.**

* La confirmation dit **quoi frapper**, en montrant le nom attendu.
* La comparaison est **exacte** : ni espaces de bordure ignorés en silence, ni
  insensibilité à la casse. Un objet dont le nom ne diffère que par la casse
  existe, et l'accepter rendrait la frappe inutile précisément là où elle sert.
* Tant que la frappe ne correspond pas, le bouton d'engagement est **présent et
  désactivé** — pas absent. Le §9.9 s'applique : l'action existe, elle est
  indisponible dans un état connu, et la raison reste lisible.
* Le champ porte son libellé, et l'engagement lui est associé par
  `aria-describedby` : au clavier et à la synthèse vocale, on doit savoir
  pourquoi le bouton ne part pas.
* Une frappe fausse **n'est pas une erreur** et ne prend pas la couleur du refus
  (§6.9). Rien n'a encore été tenté ; c'est un état d'attente, pas un échec.

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

## 6.27 Fenêtre, sections, et modale limitée à une section

C’est le troisième degré du §5.4 : ce que l’on voit une fois qu’on a ouvert un
objet.

### La fenêtre et ses sections

Une **fenêtre** est la surface de lecture d’un objet. Elle porte **plusieurs
sections titrées** — jamais une seule, sans quoi elle n’avait pas besoin d’être
une fenêtre —, rendues en paires terme / valeur (§6.4).

Lorsque l’objet a plusieurs facettes, la fenêtre les répartit en **onglets**, et
chaque onglet porte à son tour ses sections. Une facette regroupe ce qui se lit
ensemble : l’identité et les mesures d’un côté, les paramètres, relations,
activités ou historiques associés de l’autre.

Une fenêtre est en **lecture**. Elle ne porte pas de champ de formulaire
permanent : elle porte des valeurs, et chaque section porte la ou les commandes
qui la concernent.

Motif : une fenêtre entièrement éditable ne distingue plus ce qui est *enregistré*
de ce qui est *en cours de saisie*. Le lecteur ne sait pas ce qui fait foi, et un
« Enregistrer » unique en bas de page ne dit pas ce qu’il couvre.

Les valeurs absentes suivent le §6.4 et le §14.5 : une absence utile est nommée,
elle n’est pas rendue par un tiret muet.

### La modale, limitée à une section

Une commande de section — « Modifier », « Ajouter », « Déclarer », « Importer » —
ouvre une **modale dont le sujet est cette section**, et rien d’autre.

Deux usages, un seul composant :

* **modifier** ce que la section affiche déjà ;
* **insérer** un élément dans ce que la section liste.

Le choix entre les deux ne change pas la surface, seulement son titre et son
bouton d’engagement. Ce qui compte est la **portée** : une modale ouverte depuis
une section ne modifie que le sujet de cette section.

Une modale est chère : elle impose un voile, un piège de focus, une gestion
d’`Échap` et une restitution du focus. Ce prix se paie pour **recueillir une
saisie**, pas pour afficher une information.

Contrat, non négociable :

* `dialog` natif ouvert par `showModal()`, ou à défaut `role="dialog"` avec
  `aria-modal="true"` ;
* le nom accessible de la modale est **le titre de la section** ;
* à l’ouverture, le focus entre dans le premier contrôle ;
* le focus reste dans la modale tant qu’elle est ouverte ;
* `Échap` la ferme, et la fermeture équivaut à une annulation ;
* à la fermeture, le focus revient à la commande qui l’a ouverte ;
* l’arrière-plan est inerte et ne défile pas ;
* une seule modale à la fois : une modale n’en ouvre pas une autre ;
* la modale défile dans son propre conteneur ; sous 768 px elle occupe l’écran
  entier, sans changer de contrat.

Une modale a **un point d’engagement** : un bouton primaire qui nomme l’action.
L’annulation est secondaire.

Un refus du serveur s’affiche **dans la modale**, près du bouton d’engagement, et
n’efface aucune saisie. Une modale qui se referme sur un refus ferait perdre le
travail et cacherait la raison.

Fermer une modale qui contient des modifications non enregistrées demande une
confirmation, rendue **dans le flux de la modale** (§6.22) — pas dans une seconde
modale.

### Une action sensible se confirme, même dans une modale

Une modale n’est pas une confirmation, et l’ouvrir n’en tient pas lieu : elle
recueille une saisie, elle ne démontre pas une intention. Toute action sensible —
au sens du §6.23 — demande donc sa confirmation explicite, y compris lorsqu’elle
est engagée depuis une modale.

Cette confirmation est rendue **dans le flux** de la surface qui l’a déclenchée
(§6.22) : jamais une seconde modale par-dessus la première.

### Ce qui ne prend pas de modale

* un **champ autosauvegardé** (§6.11) — il n’a pas de point d’engagement à isoler ;
* la **création d’un objet de premier plan** lorsqu’elle possède sa propre
  destination : une création qui mérite une URL mérite un écran. Insérer un
  élément **dans** une section reste une modale ;
* l’**affichage** d’une information — si elle mérite d’être lue, elle mérite une
  section de la fenêtre.

### Articulation avec le §6.5

Le §6.5 conserve son domaine : l’**en-tête d’une entité**, dont plusieurs valeurs
s’éditent ensemble, bascule globalement entre lecture et édition sur place.

Le §6.27 vaut pour les **sections** d’une fenêtre : chacune est un sujet distinct,
avec son propre engagement, donc sa propre modale.

Le critère : plusieurs valeurs d’une **même** identité éditées d’un geste → §6.5 ;
une section autonome parmi d’autres → §6.27.

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
* actions contextuelles ;
* onglets — flèches, `Home`, `End` lorsque le patron `tablist` s’applique (§5.4) ;
* modales — focus entrant, focus retenu, `Échap`, focus rendu au déclencheur (§6.27).

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

# 15. Contrat du fichier jumelé `DESIGN_SYSTEM_APP.md`

Cette référence est **strictement globale**. Dès qu’une application possède une règle, une référence, une terminologie, une preuve ou une exception propre au projet, celle-ci vit dans :

```text
docs/DESIGN_SYSTEM_APP.md
```

Ce fichier est le **jumeau local** de `DESIGN_SYSTEM.md`. Il ne recopie pas la présente référence et la présente référence ne recopie pas son contenu.

`DESIGN_SYSTEM.md` ne doit jamais accueillir temporairement une information spécifique sous prétexte qu’elle a servi à découvrir une règle générique. La règle générique peut remonter ici après abstraction ; l’exemple, la mesure, la preuve, le nom métier et l’exception restent dans `DESIGN_SYSTEM_APP.md`.

Tout élément nécessitant de connaître le projet pour être compris appartient à `DESIGN_SYSTEM_APP.md`.

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

Tout écart au design system commun est explicite et documenté dans `DESIGN_SYSTEM_APP.md`.

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
