from utilis import intentions, nettoyer
import random

memoire = {
    "derniere_intention": None
}

choix_mode = None  # mode actuel : gentil / mechant / ironique


def repondre(question):
    global choix_mode

    # Nettoyage du message utilisateur
    
    print("DEBUG : message reçu →", question)  # 🔍 Suivi du message

    donnees = []
    intention_trouve = None
    choix_possible = ["gentil", "mechant", "ironique"]

    # Commande spéciale : /mode gentil, etc.
    if question.startswith("/mode "):
        nouveau_mode = question.replace("/mode ", "").strip().lower()
        if nouveau_mode in choix_possible:
            choix_mode = nouveau_mode
            print("DEBUG : choix_mode →", choix_mode)
            return f"🧠 RickBot passe en mode : {choix_mode.upper()}"
        else:
            return f"❌ Mode inconnu. Choisis parmi : {', '.join(choix_possible)}"
    
    question = nettoyer(question)

    # Choix du ton : fixe si défini, sinon aléatoire
    if choix_mode:
        choix_effectue = choix_mode
    else:
        choix_effectue = random.choice(choix_possible)
        print(f"DEBUG : ton aléatoire utilisé → {choix_effectue}")

    # Recherche d’intention dans les mots-clés
    for intent, contenu in intentions.items():
        for mot in contenu["mots"]:
            if mot in question:
                # 🔧 Sécurise l'accès au bon ton (ex: 'gentil' vs 'gentil ')
                ton = choix_effectue.strip().lower()
                liste = contenu["reponses"].get(ton)
                if liste:
                    reponse = random.choice(liste)
                    donnees.append(reponse)
                    intention_trouve = intent

    # Si on répète la même intention
    if intention_trouve:
        if intention_trouve == memoire["derniere_intention"]:
            return f"Non mais là tu radotes, mon gars ! Tu répètes : {intention_trouve}"
        else:
            memoire["derniere_intention"] = intention_trouve

    # Si une réponse a été générée
    if donnees:
        return "\n".join(donnees)
    else:
        return f"J'ai rien capté"
