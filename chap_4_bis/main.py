from agent import tri_potions

# construction du menu

while True:
    print("====Choix d'un action====")
    print("1. Je veux un tri pour guerison")
    print("2. Je veux un tri pour le combat")
    print("3. Je veux un tri pour des negociation")
    print("4. Quittez")

    choix = input("Ton choix : ")

    if choix == "1":
        resultat = tri_potions("guerison")
        print(resultat)
    elif choix == "2":
        resultat = tri_potions("combat")
        print(resultat)
    elif choix == "3":
        resultat = tri_potions("negotiation")
        print(resultat)
    else:
        print("Fin du tri des potions")
        break

