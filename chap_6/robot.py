import json
import os
import random

# au début du code on vérifie si le fichier memoire.json existe sinon on créer une reponse vide
fichier_memoire = "memoire.json"

if os.path.exists(fichier_memoire):
    with open(fichier_memoire, "r", encoding="utf-8") as f:
        reponse = json.load(f)
else:
    print("Aucun fichier memoire detecté, création d'une base vide\n")
    reponse = {}

# On met en place un systéme d'ajout de donnée pour réponse que l'on enregistera dans memoire.json

while True:
    question = input("Posez votre question (ou tapez 'exit' pour quitter) : ").lower()
    if question == "exit":
        break
    elif question == "liste":
        print("RickBot : Voici la liste des mots que je connais")
        for i in sorted(reponse.keys()):
            print(f"\n- {i}\n")
            print(f"{reponse[i]}")
    elif question == "apprendre":
        mot = input("quel mot voulez_vous apprendre ? ").lower()
        if mot not in reponse:
            reponse[mot] = []
        while True:
            reponse_ajouter = input("Quelle definition veux-tu ajouter (tape fin pour terminer) ? ").lower()
            if reponse_ajouter == "fin":
                print(f"Fin de l'ajout pour le mot : {mot}")
                break
            else:
                reponse[mot].append(reponse_ajouter)
                print(f"Réponse ajoutée pour le mot {mot} !")
                
       
# Enregistement des réponses dans le fichier memoire.json
        with open(fichier_memoire, "w", encoding="utf-8") as f:
            json.dump(reponse, f, ensure_ascii=False, indent=4)
            print(f"Mot enregister avec succés ^^")

    else:
        trouve = False
        for key in reponse:
            if key in question:
                print("RickBot :", random.choice(reponse[key]))
                trouve = True
                break
        if not trouve:
            print("RickBot : Je ne comprend pas cette question !")



