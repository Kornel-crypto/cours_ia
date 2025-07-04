def analyser_message():
    message = input("Que veut tu faire : ")
    message_nettoyer = message.lower()
    code = "code"
    longueur_message = len(message)
    cherche_code = code.lower() in message_nettoyer

    rapport = {
        "mot_trouve": cherche_code,
        "longueur": longueur_message,
        "nettoye": message_nettoyer
    }

    return rapport

resultat = analyser_message()
print(resultat)