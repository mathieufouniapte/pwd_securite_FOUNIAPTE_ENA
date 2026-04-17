from generateur import generer_mot_de_passe
from checker import verifier_force
from utils import effacer_ecran, Couleurs
from utils import log_evenement

def main():
    while True:
        effacer_ecran()
        print(f"{Couleurs.BLEU}=== GESTIONNAIRE DE SÉCURITÉ ==={Couleurs.FIN}")
        print("1. Générer un mot de passe sûr")
        print("2. Tester la force d'un mot de passe")
        print("3. Quitter")
        
        choix = input("\nVotre choix : ")

        if choix == "1":
            long = int(input("Longueur souhaitée : "))
            mdp = generer_mot_de_passe(long)
            print(f"\nMot de passe : {Couleurs.VERT}{mdp}{Couleurs.FIN}")
            input("\nAppuyez sur Entrée pour continuer...")
            log_evenement(f"Génération d'un MDP de {long} caractères")

        elif choix == "2":
            mdp_test = input("Entrez le mot de passe : ")
            force, conseils = verifier_force(mdp_test)
            
            # Affichage avec couleur selon le résultat
            c = Couleurs.ROUGE if "Faible" in force else Couleurs.VERT
            print(f"\nRésultat : {c}{force}{Couleurs.FIN}")
            log_evenement(f"Test de force effectué - Résultat : {force}")

            for msg in conseils:
                print(f" - {msg}")
            input("\nAppuyez sur Entrée pour continuer...")

        elif choix == "3":
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()
