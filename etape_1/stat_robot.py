notes = [12, 15, 9, 17, 10, 18]

somme = sum(notes)
nb_notes = len(notes)
moyenne = somme / nb_notes

print("La moyenne est de :", round(moyenne, 2))
print("La meilleur note est : ", max(notes))
print("La pire note est : ", min(notes))
print("Le nombre de notes est de : ", nb_notes)

if (moyenne >= 15):
    print("Super boulot")
elif (moyenne >= 10):
    print("Peut mieux faire")
else:
    print("Besoin d'aide")