from potion_liste import potions

def triage_potion ():
    resultat = ""
    tri_potion = [p for p in potions if p["danger"] <= 5]
    return tri_potion
    # for i in tri_potion:
    #     resultat += f"\n{i['nom']} niveau de danger {i['danger']}"
    
    # return resultat

print(triage_potion())

