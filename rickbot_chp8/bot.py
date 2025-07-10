from memoire import charger_souvenirs, sauvegarder_souvenir

souvenirs = charger_souvenirs()

def repondre(message):
    if message in souvenirs:
        return "Je m'en souviens déjà !"
    else:
        souvenirs.append(message)
        sauvegarder_souvenir(message)
        return "Message bien enregistré !"
    