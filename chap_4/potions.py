potions = {
    "nom": "Potion verte",
    "type": "Magique",
    "volume": 5,
    "toxique": True
}

if (potions["type"] == "Magique" or potions["volume"] < 10) and not potions["toxique"]:
    print("Utilisation possible")
else:
    print("A eviter")