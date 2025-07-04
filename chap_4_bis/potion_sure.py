from potion_liste import potions, potions_utilisees

try_potions = [p for p in potions if p['danger'] <= 5 and not p['nom'] in potions_utilisees]
organisation_potions = sorted(try_potions, key=lambda p: p['danger'])
potion_sur = organisation_potions[0]

print(f"La potion la plus sur est : {potion_sur['nom']} niveau de danger => {potion_sur['danger']}")

# try_potion = []
# for i in potions:
#     if i['danger'] <= 5 and not i['nom'] in potions_utilisees:
#         try_potion.append(i)