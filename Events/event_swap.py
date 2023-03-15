def thanos(joueurs, cartes):
    toutes_les_cartes = []
    for joueur in joueurs:
        toutes_les_cartes += joueur["main"]
        joueur["main"] = []
    toutes_les_cartes += cartes
    random.shuffle(toutes_les_cartes)
    nb_joueurs = len(joueurs)
    for i, carte in enumerate(toutes_les_cartes):
        joueurs[i % nb_joueurs]["main"].append(carte)
