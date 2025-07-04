porte_auto = {
    "heure": 22,
    "presence": True,
    "alarme": True
}

if (porte_auto["heure"] > 21 or not porte_auto["presence"]) and porte_auto["alarme"]:
    print("La porte se ferme")
else:
    print("La porte reste ouverte")