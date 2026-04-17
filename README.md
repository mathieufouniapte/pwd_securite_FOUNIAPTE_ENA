# Password Security Tool
Un outil simple en Python pour générer des mots de passe robustes et tester leur force.

## Fonctionnement
- `main.py` affiche un menu en console et demande à l'utilisateur de choisir entre :
  - générer un mot de passe sûr,
  - tester la force d'un mot de passe,
  - quitter.
- Pour la génération, l'utilisateur saisit une longueur minimale de 8 caractères.
- Pour le test de force, le mot de passe est analysé selon : longueur, majuscules, chiffres, symboles, et liste noire.
- Les résultats s'affichent en couleur dans la console grâce à la classe `Couleurs`.

## Choix techniques
- Génération de mot de passe :
  - `generateur.py` utilise `secrets` pour produire des caractères aléatoires sécurisés.
  - `string.ascii_letters`, `string.digits` et `string.punctuation` fournissent l'alphabet utilisé.
- Vérification de force :
  - `checker.py` emploie des expressions régulières (`re`) pour détecter majuscules, chiffres et symboles.
  - Un fichier `liste_noire_pwd.txt` contient les mots de passe trop courants à éviter.
- Utilitaires :
  - `utils.py` gère l'effacement de l'écran, la coloration de la sortie et la journalisation dans `app.log`.
- Interface console :
  - simple et textuelle, sans dépendances externes.
  - la classe `Couleurs` fournit des codes ANSI pour l'affichage coloré.

## Structure des fichiers
- `main.py` : interface principale et boucle du programme.
- `generateur.py` : génération des mots de passe.
- `checker.py` : évaluation de la force et détection des mots de passe communs.
- `utils.py` : fonctions utilitaires et gestion des couleurs.
- `liste_noire_pwd.txt` : dictionnaire de mots de passe faibles.
- `app.log` : fichier de journalisation des événements.

## Remarques
- Le mot de passe au test est analysé en clair pour pouvoir vérifier sa complexité.
- Pour masquer la saisie utilisateur, on peut utiliser `getpass.getpass()` dans `main.py`.
