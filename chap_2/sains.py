sain = ["pomme", "brocoli", "carotte"]
neutre = ["pain", "riz", "pâtes"]
sante_global = 0

for i in range(3):
    reponse = input("Donne moi un aliment : ")
    if reponse.lower() in sain:
        print("Aliment sain ^^")
        sante_global += 2
    elif reponse.lower() in neutre:
        print("Aliment neutre")
    else:
        print("Aliment Gras :/")
        sante_global -= 3

print("\n ton score de santé global est de : ", sante_global)