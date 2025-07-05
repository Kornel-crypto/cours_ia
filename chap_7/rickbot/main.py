from ia_ricky import repondre

def lancer_rickbot():
    print("🧠 RickBot en action prêt : \n")

    while True:
        question = input("🧠 Que veux tu dire ? : ")

        if question.lower() == "quit":
            print("\n🧠 Bye bye looser ^^")
            break
        else:
            reponse = repondre(question)
            print("🧠 RickBot : ", reponse)


if __name__ == "__main__":
    lancer_rickbot()
