# je vais essayer de faire un MLP à la main

x = 2
y = 1
b = 0.5

target = 1

# la je met la sortie
z_w1_out = 1
z_w2_out = 0.5
z_b_out = 0

# là je vais crée 2 réseau neuronaux MLP

x_w1 = 0.25
y_w1 = 1
b_w1 = 0.25

x_w2 = 1
y_w2 = 0.25
b_w2 = 0.35

# je configuer le ReLU

def relu(x):
    return max(0, x)

# calcul des somme factorielle et ensuite on les passe dans le déclencheur relu
z_w1 = (1 * 0.25) + (0.5 * 1) + 0.25
a_z_w1 = relu(z_w1)

z_w2 = (1 * 1) + (0.5 * 0.25) + 0.35
a_z_w2 = relu(z_w2)

# calcul de z_out et z_hat et le ReLU de z_out
z_out = (a_z_w1 * z_w1_out) + (a_z_w2 * z_w2_out) + z_b_out
y_hat = relu(z_out)

# et maintenant la perte
loss = (y_hat - target) ** 2

# maintenant on affiche les résultats
print(f"z_w1 => {z_w1}")
print(f"a_z_w1 = {a_z_w1}")
print(f"z_w2 => {z_w2}")
print(f"a_z_w2 => {a_z_w2}")
print(f"z_out => {z_out}")
print(f"y_hat la verité => {y_hat}")
print(f"La perte ou la differnce previsionnel => {loss}")
print(f"\nOn as une erreur de prediction de : {loss * 100} %, car on as en réel : {y_hat} par rapport au target : {target}")
