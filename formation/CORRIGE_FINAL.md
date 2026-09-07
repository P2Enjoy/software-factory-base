# Corrigé final — DEM-03

À lire après votre remise. Une référence exécutable est produite par :

```bash
python3 formation/atelier/preparer.py ../bureau-finale --version finale
```

Depuis le ZIP complet, conserver le préfixe `formation/`. Le préparateur refuse une
destination existante. Dans le dossier créé : `python3 -m unittest -v`, puis
`python3 app.py --port 8765 --db finale.sqlite3`. Les tests comprennent les sept
contrats initiaux et cinq tests supplémentaires de réouverture.

## Raisonnement et implémentation

La réouverture est une transition inverse, pas une nouvelle demande. Le SQL
met à jour uniquement `status` sur l'identifiant sélectionné. Le titre et le
propriétaire restent identiques. Le rôle responsable vient de la session
serveur. La fonction `can_reopen(actor)` vérifie exactement ce rôle.

```python
def can_reopen(actor):
    return actor["role"] == "responsable"
```

La route accepte le suffixe `/rouvrir`, choisit la règle correspondante et
effectue l'UPDATE seulement après le contrôle. La demande est d'abord lue en
base ; son absence donne 404. Sans session, le traitement s'arrête à 401. Pour
Bob/Eve sur une demande existante, le résultat est 403 et la ligne ne change
pas. Pour Alice, le statut cible est `ouvert`, quelle que soit la valeur
précédente ; la répétition est donc idempotente.

L'interface n'affiche la réouverture qu'à Alice sur une demande fermée.
L'autorisation reste vérifiée à l'API même si l'action est cachée. Le bouton
« Rouvrir la demande 3 » retourne vers la liste après succès. Aucun nouveau
champ ni nouvelle table n'est requis : aucune migration de schéma pour cette
unité. Le DAT doit mentionner cette justification, pas inventer une migration.

## Preuves de référence

| Cas | Attendu | Observation des données |
| --- | --- | --- |
| Alice rouvre 3 | 200 | status ouvert, autres champs identiques |
| Alice répète sur 3 | 200 | même ligne, toujours trois demandes |
| Bob rouvre sa 3 | 403 | status reste ferme |
| Eve rouvre 3 | 403 | aucune mutation |
| Sans session | 401 | aucune mutation |
| Alice vise 999 | 404 | aucune création |
| Alice rouvre puis clôt 3 | deux 200 | retour à ferme, invariants conservés |

Parcours visuel : accueil -> Alice -> demande 3 fermée -> Rouvrir -> état ouvert
et bouton Clore disponible -> Clore -> état fermé. Passer par « Changer de
profil » et entrer Bob puis Eve : la commande de réouverture n'est pas visible.
Rejouer à petite largeur et au clavier. L'appel API de Bob complète ce parcours.

## Exemple de passation

« DEM-03 implémentée : règle can_reopen, route et bouton réservés au responsable.
Le schéma ne change pas. Les cas exécutés sont listés avec la référence de code
et les sorties ci-jointes. Les profils du laboratoire restent simulés. Après
lecture du README et du backlog, reprendre avec la prochaine unité explicitement
choisie ; aucune opération de production n'est autorisée par ce laboratoire. »

Compléter avec vos vrais résultats ; ne recopier aucune réussite non observée.
Dans la version de référence, le backlog dit que le code est fourni mais que
vous devez qualifier vos propres preuves avant de cocher la fin.

## Exemples de notation

Un candidat produit toutes les preuves, explique pourquoi le statut seul change,
et documente la reprise : les points correspondants sont accordés. Un candidat
cache le bouton pour Bob mais laisse la route ouverte perd l'implémentation de
la règle et les preuves de refus ; le critère critique manque, quel que soit
le total. Un candidat annonce honnêtement l'E2E manquant perd les points du
parcours mais respecte l'honnêteté de la preuve. Il reste à consolider cette
compétence avant validation complète.

Une implémentation différente est acceptable si elle satisfait le même contrat,
préserve les données et reste explicable. Le correcteur ne note pas la ressemblance
ligne à ligne avec le générateur de référence.
