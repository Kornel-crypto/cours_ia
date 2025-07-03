mdp_correct = "123"
nbr_tentative = 0
max_tentatives = 3

while nbr_tentative < max_tentatives:
    entree = input("Ton mot de passe : ")
    if entree == mdp_correct:
        print("Mot de passe correct, Bienvenue ^^")
        break
    else:
        print("Mot de passe incorrect")
        nbr_tentative += 1

if nbr_tentative == max_tentatives:
    print("Nombre de tentatives dépassées :/ 🔒")
