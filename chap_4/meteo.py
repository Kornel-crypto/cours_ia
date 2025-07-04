meteo = {
    "temperature": 27,
    "vent": "faible",
    "meteo": "ensoleille"
}

if meteo["temperature"] > 25 and meteo["meteo"] == "ensoleille":
    print("Je recommande une sortie en pic-nic")
elif meteo["vent"] == "fort" or meteo["meteo"] == "pluvieux":
    print("Rester à l'intérieur")
elif meteo["temperature"] < 0 or meteo["meteo"] == "neige":
    print("Habillez vous chaudement")
else:
    print("Bonne journée")