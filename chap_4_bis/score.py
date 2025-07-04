from potion_liste import potions, potions_utilisees

potion_exlution = [p for p in potions if p['nom'] not in potions_utilisees]


for i in potion_exlution:
    score = 0
    if i['danger'] <= 3:
        score += 3
    elif i['danger'] <= 5:
        score += 2
    
    if i['rarete'] >= 4:
        score += 2
    elif i['rarete'] == 5:
        score += 1

    i['score'] = score

meilleurs = sorted(potion_exlution, key=lambda p: p['score'], reverse=True)
meilleurs_choix = meilleurs[0]

print(f"La meilleur potion est {meilleurs_choix['nom']} avec un score de {meilleurs_choix['score']}")