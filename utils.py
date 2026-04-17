import os
import platform
import logging

# Configuration du fichier de log
logging.basicConfig(
    filename='app.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

def log_evenement(message):
    """Enregistre un message dans le fichier app.log"""
    logging.info(message)

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
