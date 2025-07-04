from agent import analyser_message, compter_mots, verif_email

while True:
    print("\n=== Menu agent IA ===")
    print("1. Analyser un mot dans un message")
    print("2. Compter les mots dans un message")
    print("3. Chercher un Email dans un message")
    print("4. Quitter")

    choix = input("\nChoisi avec un chiffre : ")

    if choix == str(1):
        phrase = input("Donne moi une phrase : ")
        clef = input("Donne le mot à chercher : ")
        reponse = analyser_message(phrase, clef)
        print(reponse)

    elif choix == str(2):
        phrase = input("Donne un phrase que je compte les mots : ")
        reponse = compter_mots(phrase)
        print(reponse)

    elif choix == "3":
        phrase = input("Donne un texte qui peut contenir un Email : ")
        reponse = verif_email(phrase)
        print(reponse)
    
    elif choix == str(4):
        print("Salut et à bientôt ^^")
        break

    else:
        print("Mets un choix valide, un choix chiffré de 1 à 3")