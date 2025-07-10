# logique de RickBot
import random # On importe la fonctionnalite random
import memoire
    
commande = [
    "salut / yo / hello",
    "portail",
    "quitte",
    "souviens-toi de ",
    "affiche",
    "efface",
    "aide",
    "secret rick"
]
    
def repondre(message):
    msg = message.lower()
    
    if any(mot in msg for mot in ["salut", "yo", "hey", "hello"]):
        return random.choice([
            "Wubba lubba dub dub ! 🌀",
            "Yo mortel. 🧪",
            "T’as vu mon Morty ?",
            "Tu veux un portail dimensionnel ?"
        ])
    elif "aide" in msg:
        return "Voici la liste des commande :\n" + "\n- ".join(commande)
    elif "secret rick" in msg:
        return "Mon secret et que je suis une ia d'une ia rick qui est le pote de koka"
    elif "portail" in msg:
        return "Je vais chercher le pistolet portail"
    elif "efface" in msg:
        mot = input("Quel souvenir ? ")
        memoire.effacer_souvenir(mot)
    else:
        return "Je suis Rick, pas ton psy"
    
if __name__ == "__main__":
    print("###Test de bot.py###")
    print(repondre("SALUT rick"))
    print(repondre("gaule moi le pistolet portail"))
    print(repondre("comment ça vas"))
    
