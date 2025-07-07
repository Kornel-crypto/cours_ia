# memoire de rick

memoire = []

# fonction pour ajouter un souvenir
def ajouter_souvenir(texte):
    memoire.append(texte)

# fonction pour afficher un souvenir
def afficher_souvenir():
    if memoire:
        for i, souvenir in enumerate(memoire, 1):
            print(f"{i}. {souvenir}")
    else:
        print("Je n'est pas de souvenir")
        
def effacer_souvenir(mot_souvenir):
    if mot_souvenir in memoire:
        memoire.remove(mot_souvenir)
        print(f"Souvenir : {mot_souvenir} effacé")
    else:
        print("Je ne trouve pas ce souvenir :/")

if __name__ == "__main__":
    print("Memoire.py en test local")
    ajouter_souvenir("Rick adore les cornichons")
    afficher_souvenir()