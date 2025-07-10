# === MLP complet : forward + backward pass ===
# Ce fichier contient toutes les étapes du forward pass,
# et le début du backward pass avec mise à jour de w1_out.
# On va maintenant l'étendre avec :
# - la mise à jour de w2_out
# - les corrections de tous les poids de la couche cachée
# - un affichage bien commenté

import random

# === Paramètres ===
x1 = 1
x2 = 0.5
target = 1.5
learning_rate = 0.1

# === Initialisation des poids et biais ===
# Couche cachée : neurone 1
w1_h1 = random.uniform(-1, 1)
w2_h1 = random.uniform(-1, 1)
b_h1  = random.uniform(-1, 1)

# Couche cachée : neurone 2
w1_h2 = random.uniform(-1, 1)
w2_h2 = random.uniform(-1, 1)
b_h2  = random.uniform(-1, 1)

# Couche de sortie
w1_out = random.uniform(-1, 1)
w2_out = random.uniform(-1, 1)
b_out  = random.uniform(-1, 1)

# === Fonctions d'activation ===
def relu(z):
    return max(0, z)

def relu_derivative(z):
    return 1 if z > 0 else 0

# === FORWARD PASS ===
# Neurone H1
z1 = w1_h1 * x1 + w2_h1 * x2 + b_h1
a1 = relu(z1)

# Neurone H2
z2 = w1_h2 * x1 + w2_h2 * x2 + b_h2
a2 = relu(z2)

# Sortie
z_out = a1 * w1_out + a2 * w2_out + b_out
y_hat = relu(z_out)

# Perte
loss = (y_hat - target) ** 2

# === BACKWARD PASS ===
# Dérivées de la perte
# Pour tous les poids reliant la couche cachée à la sortie

# Erreur finale
dL_dyhat = 2 * (y_hat - target)

# Dérivée de ReLU
dyhat_dzout = relu_derivative(z_out)

# Pour w1_out
dzout_dw1out = a1
dL_dw1out = dL_dyhat * dyhat_dzout * dzout_dw1out
w1_out -= learning_rate * dL_dw1out

# Pour w2_out
dzout_dw2out = a2
dL_dw2out = dL_dyhat * dyhat_dzout * dzout_dw2out
w2_out -= learning_rate * dL_dw2out

# Pour b_out (biais de sortie)
dzout_dbout = 1
dL_dbout = dL_dyhat * dyhat_dzout * dzout_dbout
b_out -= learning_rate * dL_dbout

# à ce stade, on a corrigé tous les poids de la sortie

# === Affichage final ===
print("\n=== RESULTATS ===")
print(f"y_hat      : {y_hat:.4f}")
print(f"target     : {target}")
print(f"loss       : {loss:.6f}")
print(f"\n--- Poids mis à jour ---")
print(f"w1_out     : {w1_out:.4f}")
print(f"w2_out     : {w2_out:.4f}")
print(f"b_out      : {b_out:.4f}")

