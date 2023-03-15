import random

# Définir les cartes Uno
couleurs = ["Rouge", "Bleu", "Vert", "Jaune"]
valeurs = [str(i) for i in range(0, 10)]
valeurs += ["Passe", "Recommence", "Inverse"]
cartes = []

for couleur in couleurs:
    for valeur in valeurs:
        carte = couleur + " " + valeur
        cartes.append(carte)

# Mélanger les cartes
random.shuffle(cartes)

# Initialiser les mains des joueurs
joueurs = []
nb_joueurs = int(input("Entrez le nombre de joueurs : "))
for i in range(nb_joueurs):
    nom_joueur = input("Entrez le nom du joueur " + str(i+1) + " : ")
    main_joueur = []
    for j in range(7):
        carte = cartes.pop()
        main_joueur.append(carte)
    joueurs.append({"nom": nom_joueur, "main": main_joueur})

# Initialiser la pile de défausse
defausse = [cartes.pop()]

# Fonction pour déterminer si une carte est jouable
def carte_jouable(carte):
    derniere_carte = defausse[-1]
    if carte.split()[0] == derniere_carte.split()[0]:
        return True
    elif carte.split()[1] == derniere_carte.split()[1]:
        return True
    elif carte.split()[1] == "Passe":
        return True
    elif carte.split()[1] == "Recommence":
        return True
    elif carte.split()[1] == "Inverse":
        return True
    else:
        return False

# Fonction pour jouer une carte
def jouer_carte(joueur, carte):
    joueur["main"].remove(carte)
    defausse.append(carte)

# Boucle principale du jeu
joueur_courant = 0
tour_suivant = 1
sens = 1
while True:
    print("La carte actuelle est :", defausse[-1])
    print("C'est au tour de", joueurs[joueur_courant]["nom"])
    print("Votre main est :", joueurs[joueur_courant]["main"])
    carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
    if carte_jouee == "p":
        joueurs[joueur_courant]["main"].append(cartes.pop())
        tour_suivant += sens
    elif carte_jouable(carte_jouee):
        jouer_carte(joueurs[joueur_courant], carte_jouee)
        if len(joueurs[joueur_courant]["main"]) == 0:
            print(joueurs[joueur_courant]["nom"], "a gagné !")
            break
        if carte_jouee.split()[1] == "Passe":
            tour_suivant += sens*2
        elif carte_jouee.split()[1] == "Recommence":
            tour_suivant = joueur_courant
        elif carte_jouee.split()[1] == "Inverse":
            sens *= -1
            tour_suivant += sens*2
        else:
            tour_suivant += sens
    else:
        print("Vous ne pouvez pas jouer cette carte.")
        continue
    joueur_courant = (joueur_courant + tour_suivant) % nb_joueurs
