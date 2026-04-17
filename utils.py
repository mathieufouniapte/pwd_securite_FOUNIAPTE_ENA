import os
import platform

def effacer_ecran():
    """Nettoie la console selon le système d'exploitation."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Couleurs pour le terminal (Code ANSI)
class Couleurs:
    VERT = '\033[92m'
    ORANGE = '\033[93m'
    ROUGE = '\033[91m'
    BLEU = '\033[94m'
    FIN = '\033[0m'  # Pour arrêter d'écrire en couleur
