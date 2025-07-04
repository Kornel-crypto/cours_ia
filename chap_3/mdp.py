def verifier_mot_de_passe():
    nbr_tentative = 0
    while True:
        arg = input("Choisi ton mot de passe : ")
        nbr_tentative += 1
        if nbr_tentative == 3:
            print("Nbr de tentative dépassée !")
            break
        elif len(arg) < 6:
            print(f"Mot de passe trop court :/, il te reste {3 - nbr_tentative} tentative(s)")
        elif len(arg) <= 10:
            print("Mot de passe acceptable")
            break
        else:
            print("Mot de passe correct")
            break
    

verifier_mot_de_passe()