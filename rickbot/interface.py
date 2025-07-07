# c'est ici que l'on traite les action dans le main

def afficher_message(message):
    message = message.lower()
    print(message)
    
def demander_message(texte="> "):
    return input(texte)

def afficher_erreur(message="Je ne comprend pas"):
    print(f"❌ {message}")
    
if __name__=='__main__':
    print("test de interface.py")
    afficher_message("SALUT JE DOIS ETRE EN MINUSCULE")
    afficher_erreur("Je ne comprend pas")
    afficher_erreur("De quoi tu parles ?")
    