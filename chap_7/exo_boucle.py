nombre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

carre = [x ** 2 for x in nombre if x % 2 == 0 ]

print(carre)

# version classique

au_carre = []
for i in nombre:
    if i % 2 == 0:
        au_carre.append(i ** 2)

print(au_carre)