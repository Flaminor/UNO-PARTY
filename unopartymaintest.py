import random

# Correction bug changement de sens
# Définir les cartes Uno
couleurs = ["Rouge", "Bleu", "Vert", "Jaune"]
valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Passe", "Inverse", "+2", "+6"]
cartes = []

for couleur in range(len(couleurs)):
    for valeur in range(len(valeurs)):
        carte = couleurs[couleur] + " " + valeurs[valeur]
        cartes.append(carte)

# Mélanger les cartes
random.shuffle(cartes)

# Initialiser les mains des joueurs
joueurs = []
nb_joueurs = int(input("Entrez le nombre de joueurs : "))
for i in range(nb_joueurs):
    nom_joueur = input("Entrez le nom du joueur " + str(i + 1) + " : ")
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
    elif carte.split()[1] == "Inverse":
        return True
    elif carte.split()[1] == "+2" and carte.split()[0] == derniere_carte.split()[0]:
        return True
    elif carte.split()[1] == "+6" and carte.split()[0] == derniere_carte.split()[0]:
        return True
    else:
        return False


# Fonction pour jouer une carte
def jouer_carte(joueur, carte):
    joueur["main"].remove(carte)
    defausse.append(carte)


# Boucle principale du jeu
joueur_courant = 0
sens = 1
while True:
    print("-------------------------------------------------------------------")
    print("La carte actuelle est :", defausse[-1])
    print("C'est au tour de", joueurs[joueur_courant]["nom"])
    print("Votre main est :", joueurs[joueur_courant]["main"])
    carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
    if carte_jouee == "p":
        joueurs[joueur_courant]["main"].append(cartes.pop())
        if sens < 0:
            joueur_courant -= 1
        elif sens > 0:
            joueur_courant += 1

    elif carte_jouable(carte_jouee):
        jouer_carte(joueurs[joueur_courant], carte_jouee)
        if len(joueurs[joueur_courant]["main"]) == 0:
            print(joueurs[joueur_courant]["nom"], "a gagné !")
            break
        if carte_jouee.split()[1] == "Passe":
            if sens < 0:
                joueur_courant -= 2
            elif sens > 0:
                joueur_courant += 2

        elif carte_jouee.split()[1] == "Inverse":
            sens *= -1
            if sens < 0:
                joueur_courant -= 1
            elif sens > 0:
                joueur_courant += 1

        elif carte_jouee.split()[1] == "+2":
            if sens < 0:
                joueur_courant -= 1
            elif sens > 0:
                joueur_courant += 1
            if joueur_courant == -1:
                joueur_courant = len(joueurs) - 1
            elif joueur_courant == -2:
                joueur_courant = len(joueurs) - 2
            elif joueur_courant == len(joueurs):
                joueur_courant = 0
            elif joueur_courant == len(joueurs) + 1:
                joueur_courant = 1
            for i in range(2):
                joueurs[joueur_courant]["main"].append(cartes.pop())
            if sens < 0:
                joueur_courant -= 1
            elif sens > 0:
                joueur_courant += 1
        elif carte_jouee.split()[1] == "+6":
            if sens < 0:
                joueur_courant -= 1
            elif sens > 0:
                joueur_courant += 1

            if joueur_courant == -1:
                joueur_courant = len(joueurs) - 1
            elif joueur_courant == -2:
                joueur_courant = len(joueurs) - 2
            elif joueur_courant == len(joueurs):
                joueur_courant = 0
            elif joueur_courant == len(joueurs) + 1:
                joueur_courant = 1
            for i in range(6):
                joueurs[joueur_courant]["main"].append(cartes.pop())
            if sens < 0:
                joueur_courant -= 1
            elif sens > 0:
                joueur_courant += 1
        else:
            if sens < 0:
                joueur_courant -= 1
            elif sens > 0:
                joueur_courant += 1

    else:
        print("Carte non jouable")
        continue
    if joueur_courant == -1:
        joueur_courant = len(joueurs) - 1
    elif joueur_courant == -2:
        joueur_courant = len(joueurs) - 2
    elif joueur_courant == len(joueurs):
        joueur_courant = 0
    elif joueur_courant == len(joueurs) + 1:
        joueur_courant = 1
