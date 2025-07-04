def analyser_message (mot, secret):
    mot_nettoye = mot.lower()
    cherche_mot = secret.lower() in mot_nettoye
    longeur_phrase = len(mot)

    resultat = {
        "Mot trouvé :": cherche_mot,
        "Longueur du message :": longeur_phrase,
        "Message nettoyé :": mot_nettoye
    }

    return resultat