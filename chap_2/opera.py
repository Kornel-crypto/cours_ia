sain = ["pomme", "brocoli", "carotte"]
nbr_reponse = 0

for i in range(2):
    reponse = input("Donne moi le nom d'un aliment : ")

    if reponse in sain:
        nbr_reponse += 1

if nbr_reponse == 2:
    print("\nExcellent choix !")
elif nbr_reponse == 1:
    print("\nPas mal !")
else:
    print("\nPas terrible :/")