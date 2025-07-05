from liste_action import context_weights

def choix_action (actions, contexte, sante):
    poids = context_weights.get(contexte, {})
    meilleur_choix = None
    meilleur_score = float('-inf')
    resumer = []

    for action in actions:
        bonus = 0
        if sante < 30:
            if action == "soigner":
                bonus = 1
            elif action == "fuir":
                bonus = 0.5
        score = poids.get(action, 0) + bonus
        resumer.append((action, poids.get(action, 0), bonus, score))
        if score > meilleur_score:
            meilleur_score = score
            meilleur_choix = action
    return meilleur_choix, resumer

# Initialisation des variables et appel de la fonction
action_dispo = ["attaquer", "fuir", "soigner"]
contexte = "combat"
sante = 20
choix, resumer = choix_action(action_dispo, contexte, sante)

print("\n Résultat des scores :")
for action, base, bonus, total in resumer:
    print(f"=> {action} : base {base} + bonus {bonus} = {total}")

print(f"\nContexte : {contexte} | Santé : {sante}")

if choix == "soigner":
    print("L'IA se soigne, elle est en mauvaise santé")
elif choix == "fuir":
    print("L'IA à choisi de fuir pour éviter le danger")
elif choix == "attaquer":
    print("L'IA à décider d'attaquer, elle se sent assez forte")
elif choix == "observer":
    print("L'IA observe la situation")
elif choix == "négocier":
    print("L'IA tente une négociation")
else:
    print(f"L'IA à choisi : {choix}")

print("\n==== Tour de jeu de l'IA ====")

# liste des contextes possible

print("Contextes disponibles : combat, fuite, guérison, négociation")
contexte_input = input("Quel est le contexte actuelle :").strip().lower()

# Lecture de la santé

try:
    sante_input = int(input("Quel est le nivveau de santé de L'IA de 0 à 100 ? "))
except:
    print("Valeur incorrect, valeur par défaut 100")
    sante_input = 100

# Actions disponible (tu peut les changer plus tard)

action_jeu = ["attaquer", "fuir", "soigner", "observer", "négocier"]

choix_final, recap = choix_action(action_jeu, contexte_input, sante_input)

# resumer

print("\nRésultat du tour :")
for action, base, bonus, total in recap:
    print(f"=> {action} : base {base} + bonus : {bonus} = {total}")

print(f"Contexte : {contexte_input} | sante : {sante_input}")
print(f"L'IA à choisi : ", choix_final)
