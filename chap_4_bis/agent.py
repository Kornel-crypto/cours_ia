from potion_liste import potions, potions_utilisees

def tri_potions(contexte):
    # On filtre d'abord les potions non utilisées
    disponibles = [p for p in potions if p["nom"] not in potions_utilisees]

    if contexte == "guerison":
        # Filtrer les potions peu dangereuses
        filtrées = [p for p in disponibles if p["danger"] <= 5]
        triées = sorted(filtrées, key=lambda p: p["danger"])
        critere = "danger"

    elif contexte == "combat":
        # Pas de filtre, juste tri danger décroissant
        triées = sorted(disponibles, key=lambda p: p["danger"], reverse=True)
        critere = "danger"

    elif contexte == "negotiation":
        # On trie par rareté décroissante
        triées = sorted(disponibles, key=lambda p: p["rarete"], reverse=True)
        critere = "rarete"

    else:
        return "Contexte inconnu."

    # On affiche toute la liste
    resultat = f"--- Potions pour {contexte} ---\n"
    for p in triées:
        resultat += f"{p['nom']} => {critere} : {p[critere]}\n"

    # On affiche la meilleure
    if triées:
        meilleure = triées[0]
        resultat += f"\n✨ Meilleure option : {meilleure['nom']} ({critere} = {meilleure[critere]})\n"
    else:
        resultat += "\n❌ Aucune potion disponible.\n"

    return resultat
