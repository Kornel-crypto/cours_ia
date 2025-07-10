from bot import repondre

def lancer_rickbot():
    print("\nSalut je suis RickBot, parle moi ou tape 'quit' pour arrêter !\n")
    
    while True:
        message = input("Toi < ")
        if message.lower() == "quit":
            print("\n🧠 RickBot : Bon ben, saaaaaaalut !\n")
            break
        
        reponse = repondre(message)
        print("\n🧠 RickBot : ", reponse + "\n")
        