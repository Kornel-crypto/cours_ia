liste_spam = ["gagne", "argent", "gratuit", "crypto", "cadeau", "urgent"]
nbr_spam = 0
spam_detecter = False

message = input("Entre une phrase : ")
mots_du_message = message.lower().split()

for mot in mots_du_message:
    if mot in liste_spam:
        spam_detecter = True
        nbr_spam += 1

if spam_detecter:
    print("Message contenant des spams")
    print("Nombre de mots spam :", nbr_spam)
else:
    print("Message propre")