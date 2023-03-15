def pioche_infernale(joueurs, nb_cartes_max=10, chance_tous_joueurs=0.01):
    # Tirer au sort un joueur
    joueur_selectionne = random.choice(joueurs)
    
    # Faire tourner la roue pour déterminer le nombre de cartes à piocher
    nb_cartes_a_piocher = random.randint(1, nb_cartes_max)
    
    # Il y a une très faible chance que tous les joueurs doivent piocher
    if random.random() < chance_tous_joueurs:
        for joueur in joueurs:
            joueur["main"].extend([cartes.pop() for i in range(nb_cartes_a_piocher)])
        print("Tous les joueurs doivent piocher", nb_cartes_a_piocher, "cartes !")
    else:
        joueur_selectionne["main"].extend([cartes.pop() for i in range(nb_cartes_a_piocher)])
        print(joueur_selectionne["nom"], "doit piocher", nb_cartes_a_piocher, "cartes.")
