# données d'entrée
x1 = 1
x2 = 0.5

# cible (valeur attendu)
target = 1.5

# on veut que le reseau donne 1.5 quand on lui donne 1 et 0.5

# neurone caché 1 (w = weight, h = hidden, b = biais)
w1_h1 = 0.8
w2_h1 = 0.4
b_h1 = 0.1

# neurone caché 2
w1_h2 = 0.3
w2_h2 = 0.9
b_h2 = 0.2

# neurone de sortie en gros il ne change rien ici
w_h1_out = 1
w_h2_out = 1
b_out = 0.0

# fonction relu pour retourne 0 si -float ou zero sinon on renvoie le chiffre positif
def relu(x):
    return max(0, x)

# calcule des valeurs des neurones
# neurone h1
z_h1 = (x1 * w1_h1) + (x2 * w2_h1) + b_h1
a_h1 = relu(z_h1)

# neurone h2
z_h2 = (x1 * w1_h2) + (x2 * w2_h2) + b_h2
a_h2 = relu(z_h2)

# calcul de la sortie 
z_out = (w_h1_out * a_h1) + (w_h2_out * a_h1) + b_out
y_hat = z_out

# on compare avec la cible (taux de l'erreur)
loss = (y_hat - target) ** 2

# affichage des résultats
print("\n===Calcul des neurones===\n")
print(f"Neurone 1 => {a_h1}")
print(f"Neurone 2 => {a_h2}")
print("\n===Calcul de la sortie===\n")
print(f"sortie y => {y_hat}")
print("\n===Calcul de l'erreur===\n")
print(f"Erreur quadrilatique => {loss}\n")
