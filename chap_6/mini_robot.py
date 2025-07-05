from liste import reponses
import random

def repondre(question): 
    question = question.lower()
    
    base_reponse = [] 

    for cle in reponses:
        if cle in question:
            base_reponse.append(random.choice(reponses[cle]))

    if base_reponse:
        return "\n".join(base_reponse)
    else:
        return "Je ne comprend pas la question"

while True:
    question_utilisateur = input("👓 Toi : ")
    if question_utilisateur == "quit":
        print("🤖 RickBot : Au revoir !")
        break
    elif question_utilisateur == "apprendre":
        mot = input("🫡  mot à apprendre : ")
        mot_cle = mot.lower()
        if mot_cle not in reponses:
            reponses[mot_cle] = []
        while True:
            reponse = input("🧠 Réponse associé (ou fin) : ")
            if reponse.lower() == "fin":
                break
            else:
                reponses[mot_cle].append(reponse)
                print(f"Réponse ajoutée pour {mot} !")
        print(f"Mot {mot} appris !")
    else:
         print("🤖 RickBot : ", repondre(question_utilisateur))




