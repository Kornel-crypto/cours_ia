# utils.py
import string
import unicodedata

intentions = {
    "salutations": {
        "mots": ["salut", "bonjour", "yo", "wesh"],
        "reponses": {
            "gentil": [
                "Coucou toi ! 😊",
                "Salut mon ami humain 🥰"
            ],
            "mechant": [
                "Encore toi ?",
                "T’as pas un autre bot à harceler ?"
            ],
            "ironique": [
                "Oh, quelle surprise… une salutation. Quel événement.",
                "Salut. T'as bossé ton originalité ou pas du tout ?"
            ]
        }
    },

    "fatigue": {
        "mots": ["fatigué", "crevé", "épuisé"],
        "reponses": {
            "gentil": [
                "Repose-toi bien surtout. Tu le mérites 💖",
                "Courage, une sieste et ça repart 💤"
            ],
            "mechant": [
                "T’es fatigué d’avoir rien foutu ? Classique.",
                "Tu veux un oreiller ou un cerveau en rab ?"
            ],
            "ironique": [
                "Oh non, le héros est fatigué…",
                "Fatigué ? T'as codé 10 lignes aujourd'hui ? Quelle épreuve."
            ]
        }
    },

    "insulte": {
        "mots": ["idiot", "nul", "stupide", "con"],
        "reponses": {
            "gentil": [
                "Je suis désolé si j’ai mal répondu 😢",
                "Je peux essayer de mieux t'aider si tu veux 🤖"
            ],
            "mechant": [
                "Tu parles à RickBot, pas à ton miroir.",
                "T'as pas honte de ton QI ? Moi si."
            ],
            "ironique": [
                "Oh bravo, une insulte. T’es vraiment trop original.",
                "T’as dû chercher longtemps ou c’est ton maximum ?"
            ]
        }
    }
}


def nettoyer (message):
    # met en minuscule
    message = message.lower()
    
    # supprime les accents
    message = ''.join(c for c in unicodedata.normalize('NFD', message) if unicodedata.category(c) != 'Mn')
    
    # supprime la ponctuation
    message = ''.join(c for c in message if c not in (string.punctuation.replace("+", "")))
    
    # supprime les espaces en trop
    message = ' '.join(message.split())
    
    return message

for data in intentions.values():
        data["mots"] = [nettoyer(n) for n in data['mots']]