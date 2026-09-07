# Bureau des demandes — laboratoire de formation

Application pédagogique locale. Les identités sont simulées par un sélecteur de
profils : ce n'est pas un système d'authentification de production. N'y entrez
aucune donnée personnelle ou confidentielle. Ne déployez pas cette application.

## Demarrer

Prérequis : Python 3.11 ou plus avec SQLite, Git et un navigateur. Aucune
bibliothèque Python supplémentaire n'est nécessaire. Sur Windows, `py -3`
peut remplacer `python3` ; les autres commandes restent identiques.

Depuis ce dossier, dans le terminal de votre éditeur :

```bash
python3 --version
python3 -m unittest -v
python3 app.py --port 8765
```

Ouvrez http://127.0.0.1:8765, choisissez un profil et cliquez sur « Entrer ».
Arrêt : Ctrl+C dans le terminal du serveur. Le lancement crée et initialise
`atelier.sqlite3` seulement si le fichier est absent ; une base existante est
conservée. Pour recommencer sans effacer vos données, arrêtez puis lancez :

```bash
python3 app.py --port 8765 --db autre-session.sqlite3
```

Si le port est occupé, utilisez `--port 8766` et cette même valeur dans le
navigateur. N'arrêtez pas un processus dont vous ne connaissez pas le propriétaire.
Chaque fichier de base est indépendant. Ne lancez pas deux serveurs sur la même
base pendant les exercices. Il n'y a ni cloud, ni variable secrète, ni build
frontend. La vérification de syntaxe est `python3 -m compileall -q .`.

## Profils et donnees

Alice, responsable : lit, crée et clôt toute demande. Bob, contributeur : lit,
crée et clôt ses propres demandes. Eve, lectrice : lit seulement.
Seed initial : demande 1 « Préparer la salle » ouverte, propriétaire Alice ;
demande 2 « Vérifier le vidéoprojecteur » ouverte, propriétaire Bob ; demande 3
« Ranger les câbles » fermée, propriétaire Bob.

Le prototype de départ contient exactement deux défauts intentionnels : titre
trop court accepté et clôture d'une demande tierce autorisée au contributeur.
La suite exprime le contrat attendu : quatre tests échouent au départ,
un unitaire et un test API pour chacun des deux défauts.
Les tests passent sur la version de référence. Un rouge annoncé ne doit pas être
supprimé : il permet de mesurer la correction.

## Contrat

Le titre contient entre 3 et 80 caractères après suppression des espaces aux
extrémités. Une demande est `ouvert` ou `ferme`. Une seconde clôture autorisée
reste sans effet supplémentaire. Les règles s'appliquent côté serveur même
si l'interface ne présente pas l'action. Une erreur conserve les données et
explique ce qui est refusé. L'affichage échappe les textes saisis.

API locale avec cookie de session obtenu par le sélecteur :

| Opération | Résultat |
| --- | --- |
| GET /api/demandes | 200 et liste des demandes ; 401 sans session |
| POST /api/demandes avec JSON {"title":"Installer le réseau"} | 201 ; 400 invalide ; 403 pour Eve |
| POST /api/demandes/1/fermer avec JSON {} | 200 autorisé ; 403 interdit ; 404 absent |

Pour un test direct, utilisez le script Python de tests fourni : il démarre un
vrai serveur sur un port libre et utilise une base temporaire. Aucun compte réel
n'est nécessaire. Les tests directs complètent le parcours dans le navigateur.

## Structure

`app.py` : serveur, session de démonstration, routes et SQL.
`domain.py` : validation et autorisation à corriger.
`style.css` : présentation locale.
`test_contract.py` : tests unitaires et intégration HTTP/SQLite.
`SCENARIO_VISUEL.md` : parcours E2E manuel.
`BACKLOG.md` et `DAT.md` : références stables de l'atelier.

## Git du laboratoire

Le préparateur n'initialise pas Git. Depuis CE dossier d'exercice neuf :

```bash
git init
git status --short
git add README.md BACKLOG.md DAT.md app.py domain.py style.css test_contract.py SCENARIO_VISUEL.md .gitignore
git diff --cached --stat
git commit -m "Initialiser le laboratoire de formation"
```

Conservez votre identité Git habituelle. Si elle manque, configurez vos propres
nom et adresse après lecture du message Git, jamais l'identité P2Enjoy copiée
du socle. Aucun remote n'est nécessaire aux exercices de code. Le module 11
explique la sauvegarde distante et distingue commit local et push.

## Limites techniques

Le serveur de la bibliothèque standard et les identités de démonstration sont
réservés à cette formation locale. La production exigerait une authentification
réelle, TLS, une gestion de sessions durable, la protection des opérations et une
revue de sécurité adaptée. Les exercices n'attestent aucune aptitude de ce
laboratoire à la production. Les commandes ont une forme multiplateforme ; le
bilan de formation indique les systèmes effectivement testés.
