# memoire.py

NOM_FICHIER = "memoire.txt"

def charger_souvenirs():
    try:
        with open(NOM_FICHIER, "r", encoding="utf-8") as f:
            souvenirs = [ligne.strip() for ligne in f.readlines() if ligne.strip()]
            print("📂 Souvenirs chargés :", souvenirs)
        return souvenirs
    except FileNotFoundError:
        print("📂 Aucun souvenir trouvé. Fichier inexistant.")
        return []

def sauvegarder_souvenir(message):  # <- garde un nom cohérent partout
    with open(NOM_FICHIER, "a", encoding="utf-8") as f:
        f.write(message + "\n")
