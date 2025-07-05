from liste import reponses
import random

def choix_reponse (question):
    question = question.lower()

    base_response = []

    for key in reponses:
        if key in question:
            base_response.append(random.choice(reponses[key]))
    if not base_response:
        return "Je ne comprend pas la question (apprendre)"

    return "\n".join(base_response)

while True:
    mot = input("Quel est ta question ? (ou quit) ").lower()
    if mot == "quit":
        print("Fin de connexion, bye bye !")
        break
    elif mot == "apprendre":
        key = input("Quel mot apprendre ? ").lower()
        if key not in reponses:
            reponses[key] = []
        while True:
            phrase = input("Quel est la description (ou fin) ? ")
            if phrase.lower() == "fin":
                print("Fin des entrées descriptives")
                break
            else:
                reponses[key].append(phrase)
    else:
        print(choix_reponse(mot))
