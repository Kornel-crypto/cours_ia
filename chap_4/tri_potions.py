potions = [
    {"nom": "Potion rouge", "danger": 9, "rarete": 2},
    {"nom": "Potion bleue", "danger": 4, "rarete": 5},
    {"nom": "Potion verte", "danger": 6, "rarete": 3}
]

potions_traite = sorted(potions, key=lambda p: p["danger"], reverse=True)
potions_rarete = sorted(potions, key=lambda p: p["rarete"], reverse=False)

print("\n=== LIste des potions dangeureuses ===\n")
for i in potions_traite:
    print(f"{i["nom"]} => Danger : {i["danger"]}")
print("===================")

print("\n\n=== Liste des potions par rareté ===\n")
for i in potions_rarete:
    print(f"{i['nom']} => Rareté : {i["rarete"]}")
print("===================")