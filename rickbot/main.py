import memoire # on importe le fichier memoire
import bot # import du fichier bot
import interface

interface.afficher_message("Salut je suis RickBOt dis moi quelque chose ou tape une commande.")
interface.afficher_message("Commande: 'souviens-toi de ....', 'affiche', 'quitte'")

while True:
    message = interface.demander_message()


    if message == "quitte":
        interface.afficher_message("Coucou fermeture du la conversation")
        break
    elif message.startswith("souviens-toi de "):
        souvenir = message.replace("souviens-toi de ", "", 1)
        memoire.ajouter_souvenir(souvenir)
        interface.afficher_message("Ok, je m'en souviendrais")
    else:
        reponse = bot.repondre(message)
        interface.afficher_message(reponse)
