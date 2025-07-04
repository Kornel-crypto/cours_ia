from potion_liste import potions, potions_utilisees

potion_util = [p for p in potions if not p['nom'] in potions_utilisees]
potion_filtre = [p for p in potion_util if (p['danger'] <= 5 and p['danger'] >= 3) or (p['rarete'] == 5 and p['danger'] >= 5) ]
potion_tri = sorted(potion_filtre, key=lambda p: p['rarete'], reverse=True)

if potion_tri:
    meilleur = potion_tri[0]
    print(f"Meilleur choix : {meilleur['nom']} => rarete : {meilleur['rarete']} => danger : {meilleur['danger']}")
else:
    print("Aucune potion valide :/")


