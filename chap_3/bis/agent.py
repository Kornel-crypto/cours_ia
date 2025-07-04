def analyser_message(message, cle):
    message_nettoye = message.lower()
    cherche_mot = cle.lower() in message_nettoye
    nbr_de_caracteres = len(message)

    resultat = {
        "Mot trouve": cherche_mot,
        "Message nettoyé": message_nettoye,
        "Longueur du message": nbr_de_caracteres
    }

    return resultat

def compter_mots (message):
    mots = message.split()
    nbr_de_mots = len(mots)

    return {
        "mots": mots,
        "Nombre de mots": nbr_de_mots
    }

def verif_email(message):
    mots = message.split()
    for mot in mots:
        if "@" in mot and "." in mot:
            return {
                "Email trouvé": True,
                "Email": mot
            }
    return {
        "Email trouvé": False,
        "Email": None
    }
