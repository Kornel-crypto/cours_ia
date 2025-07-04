from agent import analyser_message

msg = input("Quel est ton message : ")
mot = input("Quel mot veux tu chercher : ")

resultat = analyser_message(msg, mot)
print(resultat)