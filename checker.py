import re

def est_commun(mdp):
    try:
        # On ouvre le fichier en mode lecture ('r')
        with open('common_passwords.txt', 'r') as f:
            # On lit chaque ligne et on enlève les espaces/sauts de ligne
            mots_communs = [ligne.strip() for ligne in f]
            return mdp.lower() in mots_communs
    except FileNotFoundError:
        # Si le fichier n'existe pas, on ignore cette étape
        return False

def verifier_force(mdp):
     
    if est_commun(mdp):
        return "Très Faible", ["Mot de passe trop commun (connu des pirates)"]
     
    score = 0
    remarques = []

    # 1. Vérification de la longueur (min 8 caractères)
    if len(mdp) >= 8:
        score += 1
    else:
        remarques.append("Trop court (min 8 caractères)")

    # 2. Présence de Majuscules
    if re.search(r"[A-Z]", mdp):
        score += 1
    else:
        remarques.append("Ajoutez une majuscule")

    # 3. Présence de Chiffres
    if re.search(r"\d", mdp):
        score += 1
    else:
        remarques.append("Ajoutez un chiffre")

    # 4. Présence de Caractères spéciaux
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", mdp):
        score += 1
    else:
        remarques.append("Ajoutez un symbole spécial")

    # Interprétation du score final
    if score <= 2:
        niveau = "Faible 🔴"
    elif score == 3:
        niveau = "Moyen 🟠"
    else:
        niveau = "Fort 🟢"

    return niveau, remarques
