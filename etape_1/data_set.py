nom_dataset = "Utilisateur Astro app"
nb_lignes = 342
nb_colonnes = 5

print("Analyse du dataset :")
print("Nom :", nom_dataset)
print("Dimension :", nb_lignes, " lignes, ", nb_colonnes, " nbr de colonnes.")

# estimation du volumes de données si chaque cellules fait 64 octets

nbr_cellules = 342 * 5
volumes_data = nbr_cellules * 64

print("Estimation du volume data :", volumes_data, " octets")

ko = volumes_data / 1024
mo = ko / 1024

print("≈", round(ko, 2), "Ko")
print("≈", round(mo, 2), "Mo")
