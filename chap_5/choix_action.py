from liste_action import context_weights

def choix_actions (actions, contexte):
    poids = context_weights.get(contexte, {})
    meilleur_choix = None
    meilleur_score = float('-inf')

    for action in actions:
        score = poids.get(action, 0)
        print(f"{action} => score => {score}")
        if score > meilleur_score:
            meilleur_score = score
            meilleur_choix = action
        
    return meilleur_choix

type_actions = ["observer", "fuir", "soigner"]
type_contexte = "négociation"

type_choix = choix_actions(type_actions, type_contexte)

if type_choix == "observer":
    print("L'IA à choisi observer")
else:
    print(type_choix)