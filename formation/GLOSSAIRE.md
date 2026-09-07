# Glossaire pratique

| Terme | Sens dans le cours | Exemple |
| --- | --- | --- |
| Agent | Système capable d'enchaîner des outils pour une mission | lire, modifier, tester, rendre compte |
| Contexte | Informations accessibles pour décider | conversation et fichiers lus |
| Hypothèse | Explication encore à vérifier | la route oublie la validation |
| Contrat | Comportement attendu explicite | refuser 2 caractères sans créer |
| Oracle | Référence qui détermine l'attendu d'un test | table des bornes de titre |
| Backend | Code exécuté côté serveur | route de clôture |
| Frontend | Partie présentée par le navigateur | formulaire et liste |
| API | Interface d'échange entre programmes | POST /api/demandes |
| HTTP | Protocole de requête/réponse du Web | statut 403 sur un refus |
| Route | Traitement associé à une adresse et une méthode | POST /nouvelle |
| Domaine | Règles propres au produit | qui peut clore une demande |
| Diff | Comparaison de deux états de fichiers | lignes ajoutées et supprimées |
| Index Git | Sélection du prochain commit | contenu capturé par git add |
| Commit | Instantané identifié dans l'historique local | checkpoint de DEM-01 |
| Push | Transfert de commits vers un dépôt distant | conserver le checkpoint ailleurs |
| Remote | Dépôt distant configuré | origin |
| Baseline | État de référence d'une comparaison | version avant correction |
| Regression | Comportement auparavant correct devenu incorrect | refus d'accès perdu après refactor |
| Test unitaire | Preuve ciblée d'une petite règle | longueur du titre |
| Integration | Vérification de plusieurs éléments ensemble | HTTP, validation et SQLite |
| E2E | Parcours de bout en bout du système | accueil jusqu'à la demande créée |
| Mock | Composant simulé pour un test | fournisseur extérieur indisponible |
| Seed | Données initiales reproductibles | demandes 1, 2 et 3 |
| Bootstrap | Préparation reproductible de l'environnement | installer, lancer, initialiser |
| Authentification | Établir qui agit | connexion réelle dans un produit |
| Autorisation | Décider si cet acteur peut agir sur cet objet | Bob ne clôt pas la demande d'Alice |
| Transaction | Ensemble d'opérations engagé ou abandonné de façon cohérente | modification de données |
| Idempotence | Répéter sans effet supplémentaire | clore à nouveau une demande fermée |
| Migration | Transformation versionnée du schéma ou des données | ajouter une colonne documentée |
| Hook | Programme déclenché par un événement | précommit Git |
| CI | Exécution automatisée de contrôles d'intégration | tests distants sur un changement |
| Sandbox | Limite technique d'accès de l'environnement | dossier accessible en écriture |
| Worker | Exécutant qui prend et traite une unité | session planifiée |
| Ephemere | Qui ne conserve pas son état local après sa fin | checkout neuf à la prochaine session |
| Definition of Done | Conditions de fin d'une unité | comportement, preuves, documents et Git |
| Traçabilité | Lien entre besoin, code et preuve | @spec et @verifies |
| DAT | Dossier d'architecture technique | composants, flux, données et compromis |

Les termes ont ici un sens opérationnel pour les exercices. Certains possèdent
des définitions plus larges dans d'autres disciplines ; référez-vous toujours
au contrat du système concerné.
