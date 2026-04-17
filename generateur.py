import secrets
import string

def generer_mot_de_passe(longueur=12, inclure_speciaux=True):
    # On définit les "ingrédients" possibles
    caracteres = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    if inclure_speciaux:
        caracteres += string.punctuation  # !, @, #, etc.

    # On génère le mot de passe
    mdp = ''.join(secrets.choice(caracteres) for i in range(longueur))
    return mdp
1