import time
import getpass
from generateur import generer_mot_de_passe
from checker import verifier_force
from utils import effacer_ecran, Couleurs, log_evenement

def recuperer_longueur():
    """Demande une longueur à l'utilisateur jusqu'à ce qu'elle soit >= 8."""
    while True:
        try:
            valeur = input("\nLongueur souhaitée (minimum 8) : ")
            # Permet de revenir au menu si l'utilisateur change d'avis
            if valeur.lower() == 'retour': 
                return None
                
            longueur = int(valeur)
            if longueur >= 8:
                return longueur
            else:
                print(f"{Couleurs.ROUGE}Erreur : Le mot de passe doit faire au moins 8 caractères.{Couleurs.FIN}")
        except ValueError:
            print(f"{Couleurs.ROUGE}Erreur : Veuillez entrer un nombre entier valide.{Couleurs.FIN}")

def main():
    while True:
        effacer_ecran()
        print(f"{Couleurs.BLEU}=== GESTIONNAIRE DE SÉCURITÉ ==={Couleurs.FIN}")
        print("1. Générer un mot de passe sûr")
        print("2. Tester la force d'un mot de passe")
        print("3. Quitter")
        
        choix = input("\nVotre choix : ")

        if choix == "1":
            # Utilisation de la fonction de contrôle de longueur
            long = recuperer_longueur()
            
            if long:
                mdp = generer_mot_de_passe(long)
                print(f"\nMot de passe généré : {Couleurs.VERT}{mdp}{Couleurs.FIN}")
                log_evenement(f"Génération d'un MDP de {long} caractères")
            
            input("\nAppuyez sur Entrée pour continuer...")

        elif choix == "2":
            mdp_test = getpass.getpass("\nEntrez le mot de passe à tester : ")
            force, conseils = verifier_force(mdp_test)
            
            # Détermination de la couleur selon la force
            if "Faible" in force:
                c = Couleurs.ROUGE
            elif "Moyenne" in force:
                c = Couleurs.JAUNE
            else:
                c = Couleurs.VERT
                
            print(f"\nForce du mot de passe : {c}{force}{Couleurs.FIN}")
            
            if conseils:
                print("Conseils d'amélioration :")
                for msg in conseils:
                    print(f" - {msg}")
            
            log_evenement(f"Test de force effectué - Résultat : {force}")
            input("\nAppuyez sur Entrée pour continuer...")

        elif choix == "3":
            print(f"{Couleurs.ORANGE}Fermeture du gestionnaire. Au revoir !{Couleurs.FIN}")
            break
        
        else:
            print(f"{Couleurs.ROUGE}Choix invalide, réessayez.{Couleurs.FIN}")
            time.sleep(1) # Petit délai pour lire l'erreur

if __name__ == "__main__":
    main()
