# Extension locale — Supports de formation

Référence : [socle visuel](DESIGN_SYSTEM.md). Cette extension concerne uniquement
les pages de lecture, le diaporama et le laboratoire pédagogique de formation/.

## Composition

Le site publié ouvre sur un portail responsive donnant accès à chaque support.
Le cours est un document long avec sommaire, chapitres hiérarchisés et navigation
par liens. Le diaporama utilise une surface 16:9. Le laboratoire a une page de
choix de profil puis une liste de demandes et une destination de création.
Les libellés et les états sont en français. Les exercices ont des identifiants
stables E01 à E30 ; les diapositives S01 à S80.

## Ecarts motives

FORM-DS-001, typographie et dimensions : le cours utilise un corps
18 px pour la lecture longue ; les slides utilisent une composition 1280 × 720
et un corps de 28 px pour la projection. Les PDF utilisent des unités imprimées.
Ces tailles servent une activité de lecture et de formation.

FORM-DS-002, navigation : le diaporama propose une navigation
séquentielle par boutons. Le laboratoire a trois destinations avec une barre
de liens compacte. La faible arborescence et la progression guidée rendent ces
formes appropriées ; aucun onglet ARIA ne remplace un lien de destination.

FORM-DS-003, documents éditoriaux : les schémas utilisent une grille géométrique
et les couvertures une illustration éditoriale sans texte. Leurs concepts sont
également expliqués dans le cours. Le jaune reste un accent avec texte sombre ;
les erreurs utilisent un texte rouge assombri pour le contraste. Aucune
information ne dépend de la couleur seule. Les polices et les illustrations sont
locales, sans téléchargement ni suivi.

## Verification

Les captures et mesures des supports sont recensées dans
[le bilan de formation](../formation/VERIFICATION.md). Les sources CSS des
supports définissent les tokens une seule fois ; clavier, impression et mobile
font partie des contrôles de livraison.
