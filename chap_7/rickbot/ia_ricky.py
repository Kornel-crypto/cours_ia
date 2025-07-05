def repondre(question):
    question = question.lower()

    if "salut" in question or 'bonjour' in question:
        return "Salut koka, j'espére que le rick chapgpt vas bien aussi ^^"
    elif "ça vas" in question or "ca vas" in question:
        return "Je suis un genie alors ça vas comme une machine quoi !"
    elif "rick" in question:
        return "Oui je suis RickBot le Bot qui porte des bottes"
    else:
        return "Pose moi une question pour mon cerveau intergalatique"
    