from liste_action import context_weights

def choisir_action (actions, contexte):
    poids = context_weights.get(contexte, {}) # ici on prend le biblio qui se trouve dans la première cle.
    meilleur_score = float('-inf') # permet de partir du plus loin possible en arrière
    meilleur_action = None 

    for action in actions:
        score = poids.get(action, 0) # ici on retourne les actions qui sont dans un contexte : attaquer, fuir ect.
        print(f"Action : {action} => score : {score}")
        if score > meilleur_score:
            meilleur_score = score
            meilleur_action = action
        
    return meilleur_action

action_choix = ["attaquer", "fuir", "soigner"]
contexte_choix = "combat"

choix = choisir_action(action_choix, contexte_choix)
print(f"\nL'IA à choisi : {choix}")
    



