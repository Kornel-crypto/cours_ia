import random

# données d'entrée
x1 = 1
x2 = 0.5
target = 1.5    # ce que l'on veut que le réseau prévoie

# initialistation du poids et du biais
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
b = random.uniform(-1, 1)

# taux d'apprentissage
learning_rate = 0.1

# fonction d'activation ReLU
def relu(x):
    return max(0, x)

# dérivée de ReLU
def relu_derivative(x):
    return 1 if x > 0 else 0

# entrainement des 50 derivations
for epoch in range(50):
    # étape 1 : calcul de la sortie brute (z)
    z = x1 * w1 + x2 * w2 + b
    
    # étape 2 : passage dans ReLU
    y_hat = relu(z)
    
    # étape 3 : calcul de l'erreur quadrilatique
    loss = (y_hat - target) ** 2
    
    # etape 4 : calcul des gradients (decente de gradient)
    d_loss_d_yhat = 2 * (y_hat - target)    # dérivé de MSE
    d_yhat_d_z = relu_derivative(z)         # dérivé de ReLU
    d_z_d_w1 = x1
    d_z_d_w2 = x2
    d_z_d_b = 1
    
    # chainage des dérivées (régle de la chaîne 🔗)
    d_loss_d_w1 = d_loss_d_yhat * d_yhat_d_z * d_z_d_w1
    d_loss_d_w2 = d_loss_d_yhat * d_yhat_d_z * d_z_d_w2
    d_loss_d_b = d_loss_d_yhat * d_yhat_d_z * d_z_d_b
    
    # mise à jour des poids
    w1 = d_loss_d_w1 * learning_rate
    w2 = d_loss_d_w2 * learning_rate
    d = d_loss_d_b * learning_rate
    
    # Affichage de chaque epoch
    print(f"Epoch {epoch+1:02d} → ŷ = {y_hat:.4f}, loss = {loss:.4f}, w1 = {w1:.4f}, w2 = {w2:.4f}, b = {b:.4f}")
    
    
    
    
    
    
    