# M10 — Encadrer sécurité et production

Objectif : mettre une règle à l'endroit où elle fait autorité et prouver ses effets.
Durée animée : 150 min. Exercices E19 et E20.

## Une architecture que l'on peut expliquer

L'**architecture** décrit les éléments d'un système, leurs responsabilités et
leurs échanges. Elle permet de répondre à « où dois-je intervenir ? ». Une
architecture adaptée au petit laboratoire tient en quatre éléments : présentation
HTML, routes HTTP, fonctions de domaine et stockage SQLite. Ajouter une couche
n'est utile que si elle clarifie une responsabilité ou répond à un besoin réel.

La route traduit HTTP en action. La fonction `can_close` décide du droit. La
requête SQL change le statut. Le navigateur présente le résultat. Une règle
copiée séparément dans trois boutons et deux routes peut diverger. Centraliser
la décision réduit ce risque ; cela n'enlève pas la nécessité de la faire appeler
par toutes les entrées pertinentes.

## Identité, rôle, propriété

L'**authentification** établit qui agit. L'**autorisation** décide ce que cette
personne peut faire. La **propriété** relie une ressource à une personne. Le
profil contributeur ne donne pas automatiquement accès à toutes les ressources.
Il faut examiner la demande précise. Dans notre atelier, l'identité est simulée
par le sélecteur, tandis que la règle d'autorisation s'exécute réellement.

![Le serveur décide avec le profil et la propriété de la demande](../illustrations/05-droits.svg)

Pour DEM-02, écrire : responsable, ou contributeur ET propriétaire. Les
parenthèses traduisent le contrat :

```python
return actor["role"] == "responsable" or (
    actor["role"] == "contributeur" and actor["id"] == request["owner"]
)
```

Demandez-vous ce que reçoit la fonction. Le rôle vient-il du serveur ou d'un
champ envoyé par le client ? Le propriétaire est-il lu dans la base ou envoyé
avec la requête ? Une vérification fondée uniquement sur deux valeurs que le
client choisit ne protège pas l'objet réel. Ici, la route lit la demande en
base et utilise le profil issu de la session côté serveur.

Le principe d'un contrôle d'autorisation à chaque accès et du refus par défaut
est également expliqué par [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).
Le cours l'applique sur un laboratoire local ; il ne constitue pas un audit de
sécurité complet d'une application de production.

## Le refus doit préserver l'état

Le scénario critique est celui de Bob visant la demande 1 d'Alice. Il faut obtenir
403 et conserver `ouvert`. Le serveur doit donc vérifier le droit avant l'UPDATE.
Une réponse d'erreur après modification ne remplit pas le contrat. Dans le
laboratoire, lecture, contrôle et écriture se déroulent dans la même action avec
SQLite. Pour un produit concurrent, examinez aussi les transactions et les
changements de droits pendant l'opération.

Une **transaction** regroupe des opérations de données avec un engagement ou
un abandon cohérent. Une opération **idempotente** peut être répétée sans effet
supplémentaire après le premier résultat. Clore une demande déjà fermée laisse
ici son statut fermé ; aucune ligne supplémentaire n'est créée. L'autorisation
reste vérifiée à chaque tentative, même quand l'état cible est déjà atteint.

## L'interface accompagne le contrat

La liste appelle `can_close` pour présenter les actions utiles. Après correction,
Bob ne voit plus de clôture sur la demande d'Alice. C'est une aide d'interface.
L'appel direct avec la session de Bob doit encore être refusé. Eve lit les
demandes ; aucune écriture n'est permise. Testez aussi l'absence de session
(401) et l'absence de ressource (404) selon le contrat local.

Un contrôle caché ne résume pas l'expérience utilisateur. Après une création,
la liste doit montrer la vraie demande. Une erreur de titre doit rester près
du formulaire et conserver la saisie. Au clavier, le focus est visible. Sur petit
écran, les titres longs reviennent à la ligne. Le design system formalise ces
règles de présentation ; il ne crée pas les permissions métier.

## Évoluer sans tout reconstruire

Si une future unité ajoute une échéance, elle touche le schéma, les données, la
validation, l'affichage et les tests. Une **migration** décrit une transformation
versionnée du schéma ou des données. Elle est rejouée localement sur un état connu
avant de viser un environnement partagé. Une sauvegarde et une procédure de
retour arrière sont considérées avant une opération difficilement réversible.

N'ajoutez pas une dépendance simplement parce que l'agent la propose. Demandez
quel besoin elle remplit, si un élément existant suffit, quelle maintenance et
quelles contraintes elle apporte. Pour notre fil rouge, la bibliothèque standard
suffit. Le choix réduit le temps de préparation, sans prétendre convenir à toute
application.

## Préparer une opération sensible

Une opération de production exige une instruction humaine explicite dans cette
méthode. Avant une migration, nommer l'environnement, la cible, les données
affectées, la sauvegarde disponible, l'ordre d'exécution et le retour arrière.
Une sauvegarde non restaurée en test n'établit pas à elle seule qu'une reprise
fonctionnera. Les secrets de production ne sont pas des fixtures de tests.

Exemple sur table : ajout d'une colonne obligatoire aux demandes existantes.
Il faut décider comment remplir les lignes déjà présentes, rejouer la migration
sur une copie locale représentative, vérifier la compatibilité du code ancien
et nouveau et prévoir le retour arrière ou expliquer son impossibilité. Aucune
migration de production n'est effectuée dans ce cours.

Un contrat de déploiement précise ce que l'humain autorisé doit faire et ce
qui a été réellement appliqué. Le changelog ne marque publié qu'un changement
effectivement déployé et vérifié. Les logs et captures utiles au diagnostic
restent exempts de secrets et de données personnelles inutiles. Le stockage
client n'est ajouté que pour un besoin explicite, avec les validations requises
par le projet ; ce cours ne prétend pas fournir un avis juridique.

## Faire et vérifier

E19 localise les responsabilités et analyse un mauvais contrôle client. E20
corrige DEM-02 et prouve le refus sans mutation. Après cette étape, les sept
tests doivent réussir. Exécutez aussi les parcours Alice, Bob et Eve du scénario
visuel. Extension : définir le test d'une modification concurrente du propriétaire.

Q10.1 : authentification et autorisation répondent-elles à la même question ?
Q10.2 : pourquoi vérifier l'état après 403 ? Q10.3 : une clôture répétée doit-elle
court-circuiter le contrôle du profil ? Voir les corrigés.

Point de sortie : vous pouvez expliquer la règle, la localiser et démontrer un
succès ainsi qu'un refus réel.
