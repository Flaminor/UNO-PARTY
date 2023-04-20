import random
import time


def mode_libre():
    # Définir les cartes Uno
    couleurs = ["Rouge", "Bleu", "Vert", "Jaune", "Blanc", "Noir"]
    valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Inverse", "Passe"]
    cartes = []

    for couleur in range(len(couleurs)):
        for valeur in range(len(valeurs)):
            carte = couleurs[couleur] + " " + valeurs[valeur]
            cartes.append(carte)

    # Mélanger les cartes
    random.shuffle(cartes)
    # Initialiser la pile de défausse
    defausse = [cartes.pop()]
    cartes.append("SWAP")
    for i in range(6):
        cartes.append("Pioche Infernale")
    random.shuffle(cartes)

    # Initialiser les mains des joueurs---------------------------
    joueurs = []
    nb_joueurs = int(input("Entrez le nombre de joueurs : "))
    for i in range(nb_joueurs):
        nom_joueur = input("Entrez le nom du joueur " + str(i + 1) + " : ")
        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": nom_joueur, "main": main_joueur})

    # -----------------------------------------------------------

    # Fonction pour déterminer si une carte est jouable
    def carte_jouable(carte):
        derniere_carte = defausse[-1]
        if carte == "SWAP":
            return True
        elif carte=="Pioche Infernale":
            return True
        elif carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == derniere_carte.split()[1]:
            return True
        elif carte.split()[1] == "Inverse" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == "Passe" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == "+2" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == "+4" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == "+6" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == "+8" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        else:
            return False

    # Fonction pour jouer une carte
    def jouer_carte(joueur, carte):
        joueur["main"].remove(carte)
        if carte != "SWAP" or carte!="Pioche Infernale":
            defausse.append(carte)

    #fonction Evenements test de QI

    def IQ_test():
        rc = 0
        quiz = {
            "Quelle est la capital de la France?": "Paris",
            "Combien y a-t-il de départements en France?": "96",
            "Quelle est la langue officielle de la France?": "Le Français",
            "Quel est le plus grand fleuve de France?": "La Loire",
            "Quel est le plus haut sommet de la France?": "Mont Blanc",
            "Quel est le nom du président actuel de la France?": "Emmanuel Macron",
            "Quel est le nom de la devise nationale de la France?": "Liberté égalité fraternité",
            "Quel est le nom de la tour la plus célèbre de Paris?": "La Tour Eiffel",
            "Quel est le nom de la plus grande île de France?": "Corsica",
            "Combien y a-t-il de régions en France?": "13"
        }
        for i in range(5):
            print(f"Question", i + 1)
            question = random.choice(list(quiz.keys()))
            answer = quiz[question]
            print(question)
            response = input()
            if response.lower() == answer.lower():
                print("Correct!")
                rc += 1
            else:
                print("Incorrect. La réponse était: " + answer)
            print("-------------------------------------------------------------------")
        if rc == 5:
            return True, 5 - rc
        else:
            return False, random.randint(2, 12)

    #Fonction evenement pioche infernale

    def pioche_infernale():
        alea = random.randint(0, 12)
        return alea

    #Fonction évènements combinaisons touches

    def speed_test():
        # Fonction qui donne des touches aléatiores à entrer

        # Les lettres à entrer
        cles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u',
                'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Nombre de lettres à entrer
        num_cles = random.randint(5, 7)
        # Limite de temps
        now = time.time()
        time_limit = now + num_cles + 5

        # Séries de lesttres à entrer
        sequence = []
        for i in range(num_cles):
            sequence.append(random.choice(cles))

        # Ask the player to enter the key sequence within the time limit
        print("Entrez ces", num_cles, "lettres et/ou chiffres en", time_limit, "secondes:")

        for i in range(len(sequence)):
            print(sequence[i], end=" ")
        print()

        for i in range(num_cles):
            clee = input("Lettre : ")
            if clee != sequence[i]:
                print("Mauvaise lettre! Game over.")
                return False
            if time.time() > time_limit:
                print("Temps écoulé! Game over.")
                return False

        if time.time() < time_limit and clee == sequence[i]:
            print("Félicitations! Tu as réussi à faire la bonne combinaison de touches.")
            return True

    # Boucle principale du jeu-------------------------------------------------------------------------------------------------------------------------
    joueur_courant = 0
    sens = 1
    lst_joueurs = []
    for i in range(nb_joueurs):
        lst_joueurs.append(str(i) + " " + "0")

    while True:

        #Condition pour savoir la pioche est vide et la remplir si elle est vide

        if cartes == []:
            while len(defausse) != 1:
                cartes.append(defausse[0])
                defausse.remove(defausse[0])
        random.shuffle(cartes)
        alea = random.randint(1, 15)

        print("-------------------------------------------------------------------")

        #Si le nombre aléatoire est 1 alors déclenchement de l'évènement Test de QI

        if alea == 1:
            print("C'est au tour de", joueurs[joueur_courant]["nom"])
            print("Evènement Test de QI")
            restestqi = IQ_test()
            if restestqi[0] == False:
                print("Vous avez échoué à " + str(restestqi[1]) + " questions donc vous allez piocher " + str(
                    restestqi[1]) + " cartes")
            for i in range(restestqi[1]):
                joueurs[joueur_courant]["main"].append(cartes.pop())

        #Si le nombre aléatoire est 2 alors déclenchement de l'évènement Pioche infernale

        if alea == 2:
            print("C'est au tour de", joueurs[joueur_courant]["nom"])
            print("Evènement pioche infernale")
            roue = pioche_infernale()
            roue2 = random.randint(1, 15)
            if roue2 == 1:
                for i in range(len(joueurs)):
                    for j in range(roue):
                        joueurs[i]["main"].append(cartes.pop())
            else:
                for i in range(roue):
                    joueurs[joueur_courant]["main"].append(cartes.pop())

        #Si le nombre aléatoire est 4 alors déclenchement de l'évènement Combinaiason touche

        if alea == 4:
            print("C'est au tour de", joueurs[joueur_courant]["nom"])
            print("Evènement Combinaison touche")
            combitouche = speed_test()
            if combitouche == False:
                roue_touche = random.randint(2, 12)
                for i in range(roue_touche):
                    joueurs[joueur_courant]["main"].append(cartes.pop())

        #Si le nombre aléatoire est 5 alors déclenchement de l'évènement SWAP

        if alea == 5:
            print("Evènement SWAP")
            regroupement = []
            for i in range(len(joueurs)):
                while joueurs[i]["main"] != []:
                    regroupement.append(joueurs[i]["main"][0])
                    joueurs[i]["main"].remove(joueurs[i]["main"][0])
            random.shuffle(regroupement)
            j = len(joueurs) - 1
            while regroupement != []:
                joueurs[j]["main"].append(regroupement[0])
                regroupement.remove(regroupement[0])
                j -= 1
                if j < 0:
                    j = len(joueurs) - 1

        #Si le nombre aléatoire est 3 alors déclenchement de l'évènement TIME TIME

        if alea == 3:
            print("C'est au tour de", joueurs[joueur_courant]["nom"])
            for i in range(len(lst_joueurs)):
                temp = lst_joueurs[joueur_courant]
                temp = temp.split()
                if temp[1] == "0":
                    temp[1] = "3"
                    temp[0] += " " + str(temp[1])
                    del (temp[1])
                    for j in range(len(temp)):
                        lst_joueurs[joueur_courant] = temp[j]
                    break

        #Ici on vérifie le nombre de tour depuis le déclenchement de l'évènement TIME TIME

        if lst_joueurs[0][2] != "0":
            for i in range(len(lst_joueurs)):
                temp = lst_joueurs[joueur_courant]
                temp = temp.split()
                temp[1] = str(int(temp[1]) - 1)
                temp[0] += " " + str(temp[1])
                del (temp[1])
                for j in range(len(temp)):
                    lst_joueurs[joueur_courant] = temp[j]
                break
            now = time.time()
            max_delay = now + 4

            while True:
                print("Evènement TIME TIME")
                print("La carte actuelle est :", defausse[-1])
                print("Votre main est :", joueurs[joueur_courant]["main"])
                carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                if time.time() > max_delay:
                    print("Temps manqué")
                    carte_jouee = "p"
                    break
                else:
                    break

        #Si le nombre aléatoire est différent alors on joue la partie normalement

        else:
            print("La carte actuelle est :", defausse[-1])
            print("C'est au tour de", joueurs[joueur_courant]["nom"])
            print("Votre main est :", joueurs[joueur_courant]["main"])
            now = time.time()
            max_delay = now + 15
            while True:
                carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                if time.time() > max_delay:
                    print("Temps manqué")
                    carte_jouee = "p"
                    break
                else:
                    break

        #Si la carte posée est la carte SWAP

        if carte_jouee == "SWAP":
            nom_swapp = input("Donnez le nom du joueur : ")
            for i in range(len(joueurs)):
                if joueurs[i]["nom"] == nom_swapp:
                    temp = joueurs[joueur_courant]["main"]
                    joueurs[joueur_courant]["main"] = joueurs[i]["main"]
                    joueurs[i]["main"] = temp
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1
                    break
        elif carte_jouee=="Pioche Infernale":
            nom_pioche_infernale = input("Donnez le nom du joueur : ")
            for i in range(len(joueurs)):
                if joueurs[i]["nom"] == nom_pioche_infernale:
                    roue3=random.randint(2,12)
                    for j in range(roue3):
                        joueurs[i]["main"].append(cartes.pop())
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1
                    break

        #Si le joueur choisit de passer son tour

        elif carte_jouee == "p":
            joueurs[joueur_courant]["main"].append(cartes.pop())
            if sens < 0:
                joueur_courant -= 1
            elif sens > 0:
                joueur_courant += 1

        #Si la carte est jouable alors on regarde s'il s'agit d'une carte spéciale dans chaque conditions

        elif carte_jouable(carte_jouee):
            jouer_carte(joueurs[joueur_courant], carte_jouee)
            if len(joueurs[joueur_courant]["main"]) == 0:
                print(joueurs[joueur_courant]["nom"], "a gagné !")
                return joueurs[joueur_courant]["nom"]

            # Si la carte est la carte Spéciale Inverse

            elif carte_jouee.split()[1] == "Inverse":
                sens *= -1
                if sens < 0:
                    joueur_courant -= 1
                elif sens > 0:
                    joueur_courant += 1

            #Si la carte est la carte Spéciale Passe

            elif carte_jouee.split()[1] == "Passe":
                if sens < 0:
                    joueur_courant -= 2
                elif sens > 0:
                    joueur_courant += 2

            # Si la carte est la carte Spéciale +2

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

            # Si la carte est la carte Spéciale +4

            elif carte_jouee.split()[1] == "+4":
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
                for i in range(4):
                    joueurs[joueur_courant]["main"].append(cartes.pop())
                if sens < 0:
                    joueur_courant -= 1
                elif sens > 0:
                    joueur_courant += 1

            # Si la carte est la carte Spéciale +6

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

            # Si la carte est la carte Spéciale +8

            elif carte_jouee.split()[1] == "+8":
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
                for i in range(8):
                    joueurs[joueur_courant]["main"].append(cartes.pop())
                if sens < 0:
                    joueur_courant -= 1
                elif sens > 0:
                    joueur_courant += 1

            #Si aucune des cartes n'est spéciale alors on passe au joueur suivant

            else:
                if sens < 0:
                    joueur_courant -= 1
                elif sens > 0:
                    joueur_courant += 1

        #Si la carte n'est pas jouable
        else:
            print("Carte non jouable")
            joueurs[joueur_courant]["main"].append(cartes.pop())
            if sens < 0:
                joueur_courant -= 1
            elif sens > 0:
                joueur_courant += 1

        #Si on est en fin ou début de liste selon le sens

        if joueur_courant == -1:
            joueur_courant = len(joueurs) - 1
        elif joueur_courant == -2:
            joueur_courant = len(joueurs) - 2
        elif joueur_courant == len(joueurs):
            joueur_courant = 0
        elif joueur_courant == len(joueurs) + 1:
            joueur_courant = 1


def histoire():
    def explications():
        print("Tu auras un deck de 7 cartes")
        time.sleep(1.3)
        print("Elles peuvent être d'une de ces 7 couleurs :\n-Bleu\n-Rouge\n-Vert\n-Jaune\n-Blanc\n-Noir")
        time.sleep(2)
        print("Ces cartes ont des chiffres allant de 0 à 9")
        time.sleep(1.5)
        print("Ton objectif est donc de te débarasser de tes cartes avant tes adversaires")
        time.sleep(1.3)
        print("Chaque tour est limité à un temps de 15 secondes")
        time.sleep(1.3)
        print("Je t'introduirait à d'autres notions un peu plus poussées plus tard")
        time.sleep(1.5)
        print("Est ce bien clair ?")
        choix3 = "c"
        while (choix3.lower() != "a") or (choix3.lower() != "b"):
            choix3 = input("a)Oui [nom à insérer]    b)Pas vraiment..\nChoix : ")
            if choix3.lower() == "a":
                print("Parfait commençons alors")
                time.sleep(1.3)
                break
            elif choix3.lower() == "b":
                print("Je te réexplique")
                time.sleep(1.3)
                explications()
                break

    nom = input("Entrez votre nom : ")
    print("Bonjour", nom)
    time.sleep(1.5)
    print("Je me présente,")
    time.sleep(1.3)
    print("Je suis Le [nom à insérer], le maitre du jeu")
    time.sleep(1.3)
    choix = "b"
    while choix.lower() != "a":
        choix = input("a)Qu'est ce que je fais là ?\nChoix : ")
    print("Tu es dans la GRANDE GAME ARENA et tu as été choisis pour participer au grand jeux du moment...")
    time.sleep(2.5)
    print("Le GRANDE-UNO !")

    # Introduction du jeux

    choix2 = "c"
    while (choix2.lower() != "a") or (choix2.lower() != "b"):
        choix2 = input("a)Je ne veux pas y participer    b)Le quoi ?\nChoix : ")
        if choix2.lower() == "a":
            break
        elif choix2.lower() == "b":
            time.sleep(1)
            print("C'est le tout nouveau jeux du moment,")
            time.sleep(1)
            print("Il est très apprécié et populaire par tous et toutes")
            break
    time.sleep(1.3)
    print("De toute façons tu n'as pas le choix de participer ou non, tu es coincé dans le batîment")
    time.sleep(1.5)
    # Premier tour
    print("Enfin bref, laisse moi t'expliquer le fonctionnement du jeux")
    time.sleep(1.3)
    # Explications
    explications()
    print("C'est parti")
    chargement = "Chargement en cours"
    for i in range(3):
        print(chargement + ".")
        time.sleep(1)
        print(chargement + "..")
        time.sleep(1)
        print(chargement + "...")
        time.sleep(1)

    def Niveau1(nom):
        # Définir les cartes Uno
        couleurs = ["Rouge", "Bleu", "Vert", "Jaune", "Blanc", "Noir"]
        valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cartes = []

        for couleur in range(len(couleurs)):
            for valeur in range(len(valeurs)):
                carte = couleurs[couleur] + " " + valeurs[valeur]
                cartes.append(carte)

        # Mélanger les cartes
        random.shuffle(cartes)

        # Initialiser les mains des joueurs---------------------------
        joueurs = []
        main_joueur = []

        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": nom, "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot", "main": main_joueur})
        # -----------------------------------------------------------
        # Initialiser la pile de défausse
        defausse = [cartes.pop()]

        # Fonction pour déterminer si une carte est jouable
        def carte_jouable(carte):
            derniere_carte = defausse[-1]
            if carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == derniere_carte.split()[1]:
                return True
            elif carte.split()[1] == "Inverse" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            else:
                return False

        # Fonction pour jouer une carte
        def jouer_carte(joueur, carte):
            joueur["main"].remove(carte)
            defausse.append(carte)

        # Boucle principale du jeu-------------------------------------------------------------------------------------------------------------------------
        joueur_courant = 0
        sens = 1

        while True:
            if cartes == []:
                while len(defausse) != 1:
                    cartes.append(defausse[0])
                    defausse.remove(defausse[0])
            random.shuffle(cartes)
            print("-------------------------------------------------------------------")

            #Condiitons savoir le joueur est un bot ou non

            if joueurs[joueur_courant]["nom"] == "Bot":
                main_debut = len(joueurs[joueur_courant]["main"])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                chargement = "Le bot est en train de réfléchir"
                for i in range(1):
                    print(chargement + ".")
                    time.sleep(1)
                    print(chargement + "..")
                    time.sleep(1)
                    print(chargement + "...")
                    time.sleep(1)
                i = 0
                trouve = False
                taille = len(joueurs[joueur_courant]["main"]) - 1

                #On parcours toutes les cartes pour savoir si l'une d'entre elles est jouables sinon on joue la carte passe

                while i < taille:
                    if trouve == True:
                        break
                    carte_jouee = joueurs[joueur_courant]["main"][i]
                    if carte_jouable(carte_jouee) == True:
                        jouer_carte(joueurs[joueur_courant], carte_jouee)
                        trouve = True
                        taille -= 1
                    i += 1

                if main_debut == len(joueurs[joueur_courant]["main"]):
                    joueurs[joueur_courant]["main"].append(cartes.pop())

                mainbot = "Main du bot : "
                for i in range(len(joueurs[joueur_courant]["main"])):
                    mainbot += "| "
                print(mainbot)
                if len(joueurs[joueur_courant]["main"]) == 0:
                    print(joueurs[joueur_courant]["nom"], "a gagné !")
                    return joueurs[joueur_courant]["nom"]
                elif sens < 0:
                    joueur_courant -= 1
                elif sens > 0:
                    joueur_courant += 1

            #Au tour du joueur

            else:
                print("La carte actuelle est :", defausse[-1])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("Votre main est :", joueurs[joueur_courant]["main"])
                now = time.time()
                max_delay = now + 15
                while True:
                    carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                    if time.time() > max_delay:
                        print("Temps manqué")
                        carte_jouee = "p"
                        break
                    else:
                        break
                #Si le joueur passe son tour

                if carte_jouee == "p":
                    joueurs[joueur_courant]["main"].append(cartes.pop())
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                #Si la carte jouée est jouable

                elif carte_jouable(carte_jouee):
                    jouer_carte(joueurs[joueur_courant], carte_jouee)
                    if len(joueurs[joueur_courant]["main"]) == 0:
                        print(joueurs[joueur_courant]["nom"], "a gagné !")
                        return joueurs[joueur_courant]["nom"]
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                #Si la carte jouée n'est pas jouable

                else:
                    print("Carte non jouable")
                    joueurs[joueur_courant]["main"].append(cartes.pop())
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

    # ---------------------------------------------------------------------------------------------------------------------

    def Niveau2(nom):
        # Définir les cartes Uno
        couleurs = ["Rouge", "Bleu", "Vert", "Jaune","Blanc", "Noir"]
        valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Inverse"]
        cartes = []

        for couleur in range(len(couleurs)):
            for valeur in range(len(valeurs)):
                carte = couleurs[couleur] + " " + valeurs[valeur]
                cartes.append(carte)

        # Mélanger les cartes
        random.shuffle(cartes)

        # Initialiser les mains des joueurs---------------------------
        joueurs = []
        main_joueur = []

        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": nom, "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot1", "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot2", "main": main_joueur})
        # -----------------------------------------------------------
        # Initialiser la pile de défausse
        defausse = [cartes.pop()]

        # Fonction pour déterminer si une carte est jouable
        def carte_jouable(carte):
            derniere_carte = defausse[-1]
            if carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == derniere_carte.split()[1]:
                return True
            elif carte.split()[1] == "Inverse" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            else:
                return False

        # Fonction pour jouer une carte
        def jouer_carte(joueur, carte):
            joueur["main"].remove(carte)
            defausse.append(carte)

        def IQ_test():
            rc = 0
            quiz = {
                "Quelle est la capital de la France?": "Paris",
                "Combien y a-t-il de départements en France?": "96",
                "Quelle est la langue officielle de la France?": "Le Français",
                "Quel est le plus grand fleuve de France?": "La Loire",
                "Quel est le plus haut sommet de la France?": "Mont Blanc",
                "Quel est le nom du président actuel de la France?": "Emmanuel Macron",
                "Quel est le nom de la devise nationale de la France?": "Liberté égalité fraternité",
                "Quel est le nom de la tour la plus célèbre de Paris?": "La Tour Eiffel",
                "Quel est le nom de la plus grande île de France?": "Corsica",
                "Combien y a-t-il de régions en France?": "13"
            }
            for i in range(5):
                print(f"Question", i + 1)
                question = random.choice(list(quiz.keys()))
                answer = quiz[question]
                print(question)
                response = input()
                if response.lower() == answer.lower():
                    print("Correct!")
                    rc += 1
                else:
                    print("Incorrect. La réponse était: " + answer)
                print("-------------------------------------------------------------------")
            if rc == 5:
                return True, 5 - rc
            else:
                return False, random.randint(2, 12)

        # Boucle principale du jeu-------------------------------------------------------------------------------------------------------------------------
        joueur_courant = 0
        sens = 1

        while True:
            if cartes == []:
                while len(defausse) != 1:
                    cartes.append(defausse[0])
                    defausse.remove(defausse[0])
            random.shuffle(cartes)
            alea = random.randint(1, 15)

            print("-------------------------------------------------------------------")

            #Si c'est au tour du bot de jouer

            if joueurs[joueur_courant]["nom"] == "Bot1" or joueurs[joueur_courant]["nom"] == "Bot2":
                main_debut = len(joueurs[joueur_courant]["main"])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("La carte actuelle est :", defausse[-1])
                chargement = "Le bot est en train de réfléchir"
                for i in range(1):
                    print(chargement + ".")
                    time.sleep(1)
                    print(chargement + "..")
                    time.sleep(1)
                    print(chargement + "...")
                    time.sleep(1)
                i = 0
                trouve = False
                taille = len(joueurs[joueur_courant]["main"]) - 1
                while i < taille:
                    if trouve == True:
                        break
                    carte_jouee = joueurs[joueur_courant]["main"][i]
                    if carte_jouable(carte_jouee) == True:
                        jouer_carte(joueurs[joueur_courant], carte_jouee)
                        if carte_jouee.split()[1] == "Inverse":
                            sens *= -1
                        trouve = True
                        taille -= 1

                    i += 1

                if main_debut == len(joueurs[joueur_courant]["main"]):
                    joueurs[joueur_courant]["main"].append(cartes.pop())

                mainbot = "Main du bot : "
                for i in range(len(joueurs[joueur_courant]["main"])):
                    mainbot += "| "
                print(mainbot)
                if len(joueurs[joueur_courant]["main"]) == 0:
                    print(joueurs[joueur_courant]["nom"], "a gagné !")
                    return joueurs[joueur_courant]["nom"]
                else:
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

            else:

                #Déclenchement évènement IQ Test

                if alea == 1:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement Test de QI")
                    restestqi = IQ_test()
                    if restestqi[0] == False:
                        print("Vous allez piocher " + str(
                            restestqi[1]) + " cartes")
                    for i in range(restestqi[1]):
                        joueurs[joueur_courant]["main"].append(cartes.pop())

                print("La carte actuelle est :", defausse[-1])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("Votre main est :", joueurs[joueur_courant]["main"])
                now = time.time()
                max_delay = now + 15
                while True:
                    carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                    if time.time() > max_delay:
                        print("Temps manqué")
                        carte_jouee = "p"
                        break
                    else:
                        break

                #Si le joueur passe son tour

                if carte_jouee == "p":
                    joueurs[joueur_courant]["main"].append(cartes.pop())
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                #Si la carte est jouable

                elif carte_jouable(carte_jouee):
                    jouer_carte(joueurs[joueur_courant], carte_jouee)
                    if len(joueurs[joueur_courant]["main"]) == 0:
                        print(joueurs[joueur_courant]["nom"], "a gagné !")
                        return joueurs[joueur_courant]["nom"]

                    #Si la carte est Inverse

                    elif carte_jouee.split()[1] == "Inverse":
                        sens *= -1
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
                    joueurs[joueur_courant]["main"].append(cartes.pop())
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

    # ----------------------------------------------------------------------------------------------------------------------------
    def Niveau3(nom):
        # Définir les cartes Uno
        couleurs = ["Rouge", "Bleu", "Vert", "Jaune", "Blanc", "Noir"]
        valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Inverse", "Passe"]
        cartes = []

        for couleur in range(len(couleurs)):
            for valeur in range(len(valeurs)):
                carte = couleurs[couleur] + " " + valeurs[valeur]
                cartes.append(carte)

        # Mélanger les cartes
        random.shuffle(cartes)

        # Initialiser les mains des joueurs---------------------------
        joueurs = []
        main_joueur = []

        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": nom, "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot1", "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot2", "main": main_joueur})
        # -----------------------------------------------------------
        # Initialiser la pile de défausse
        defausse = [cartes.pop()]

        # Fonction pour déterminer si une carte est jouable
        def carte_jouable(carte):
            derniere_carte = defausse[-1]
            if carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == derniere_carte.split()[1]:
                return True
            elif carte.split()[1] == "Inverse" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "Passe" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            else:
                return False

        # Fonction pour jouer une carte
        def jouer_carte(joueur, carte):
            joueur["main"].remove(carte)
            defausse.append(carte)

        def IQ_test():
            rc = 0
            quiz = {
                "Quelle est la capital de la France?": "Paris",
                "Combien y a-t-il de départements en France?": "96",
                "Quelle est la langue officielle de la France?": "Le Français",
                "Quel est le plus grand fleuve de France?": "La Loire",
                "Quel est le plus haut sommet de la France?": "Mont Blanc",
                "Quel est le nom du président actuel de la France?": "Emmanuel Macron",
                "Quel est le nom de la devise nationale de la France?": "Liberté égalité fraternité",
                "Quel est le nom de la tour la plus célèbre de Paris?": "La Tour Eiffel",
                "Quel est le nom de la plus grande île de France?": "Corsica",
                "Combien y a-t-il de régions en France?": "13"
            }
            for i in range(5):
                print(f"Question", i + 1)
                question = random.choice(list(quiz.keys()))
                answer = quiz[question]
                print(question)
                response = input()
                if response.lower() == answer.lower():
                    print("Correct!")
                    rc += 1
                else:
                    print("Incorrect. La réponse était: " + answer)
                print("-------------------------------------------------------------------")
            if rc == 5:
                return True, 5 - rc
            else:
                return False, random.randint(2, 12)

        def pioche_infernale():
            alea = random.randint(0, 12)
            return alea

        # Boucle principale du jeu-------------------------------------------------------------------------------------------------------------------------
        joueur_courant = 0
        sens = 1

        while True:
            if cartes == []:
                while len(defausse) != 1:
                    cartes.append(defausse[0])
                    defausse.remove(defausse[0])
            random.shuffle(cartes)
            alea = random.randint(1, 15)

            print("-------------------------------------------------------------------")

            #Si c'est au bot de jouer

            if joueurs[joueur_courant]["nom"] == "Bot1" or joueurs[joueur_courant]["nom"] == "Bot2":
                main_debut = len(joueurs[joueur_courant]["main"])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("La carte actuelle est :", defausse[-1])
                chargement = "Le bot est en train de réfléchir"
                for i in range(1):
                    print(chargement + ".")
                    time.sleep(1)
                    print(chargement + "..")
                    time.sleep(1)
                    print(chargement + "...")
                    time.sleep(1)
                i = 0
                trouve = False
                taille = len(joueurs[joueur_courant]["main"])
                joueur_courant_temp = joueur_courant
                while i < taille:
                    if trouve == True:
                        break
                    carte_jouee = joueurs[joueur_courant]["main"][i]
                    if carte_jouable(carte_jouee) == True:
                        jouer_carte(joueurs[joueur_courant], carte_jouee)
                        if carte_jouee.split()[1] == "Inverse":
                            sens *= -1
                            if sens < 0:
                                joueur_courant -= 1
                            elif sens > 0:
                                joueur_courant += 1
                        elif carte_jouee.split()[1] == "Passe":
                            if sens < 0:
                                joueur_courant -= 2
                            elif sens > 0:
                                joueur_courant += 2
                        else:
                            if sens < 0:
                                joueur_courant -= 1
                            elif sens > 0:
                                joueur_courant += 1
                        trouve = True
                        taille = 1

                    i += 1

                if main_debut == len(joueurs[joueur_courant_temp]["main"]):
                    joueurs[joueur_courant_temp]["main"].append(cartes.pop())
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                mainbot = "Main du bot : "
                for i in range(len(joueurs[joueur_courant_temp]["main"])):
                    mainbot += "| "
                print(mainbot)
                if len(joueurs[joueur_courant_temp]["main"]) == 0:
                    print(joueurs[joueur_courant_temp]["nom"], "a gagné !")
                    return joueurs[joueur_courant_temp]["nom"]

            #Si l'aléatoire est 1 alors évènement IQ_test

            else:
                if alea == 1:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement Test de QI")
                    restestqi = IQ_test()
                    if restestqi[0] == False:
                        print("Vous allez piocher " + str(
                            restestqi[1]) + " cartes")
                    for i in range(restestqi[1]):
                        joueurs[joueur_courant]["main"].append(cartes.pop())

                #Si c'est 2 alors évènement pioche infernale

                if alea == 2:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement pioche infernale")
                    roue = pioche_infernale()
                    roue2 = random.randint(1, 15)
                    if roue2 == 1:
                        for i in range(len(joueurs)):
                            for j in range(roue):
                                joueurs[i]["main"].append(cartes.pop())
                    else:
                        for i in range(roue):
                            joueurs[joueur_courant]["main"].append(cartes.pop())

                #Au tour du joueur

                print("La carte actuelle est :", defausse[-1])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("Votre main est :", joueurs[joueur_courant]["main"])
                now = time.time()
                max_delay = now + 15
                while True:
                    carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                    if time.time() > max_delay:
                        print("Temps manqué")
                        carte_jouee = "p"
                        break
                    else:
                        break

                #Si le joueur passe son tour

                if carte_jouee == "p":
                    joueurs[joueur_courant]["main"].append(cartes.pop())
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                #Si la carte est jouable

                elif carte_jouable(carte_jouee):
                    jouer_carte(joueurs[joueur_courant], carte_jouee)
                    if len(joueurs[joueur_courant]["main"]) == 0:
                        print(joueurs[joueur_courant]["nom"], "a gagné !")
                        return joueurs[joueur_courant]["nom"]

                    #Si c'est inverse

                    elif carte_jouee.split()[1] == "Inverse":
                        sens *= -1
                        if sens < 0:
                            joueur_courant -= 1
                        elif sens > 0:
                            joueur_courant += 1

                    #Si c'est la carte Passe

                    elif carte_jouee.split()[1] == "Passe":
                        if sens < 0:
                            joueur_courant -= 2
                        elif sens > 0:
                            joueur_courant += 2


                    else:
                        if sens < 0:
                            joueur_courant -= 1
                        elif sens > 0:
                            joueur_courant += 1

                else:
                    print("Carte non jouable")
                    joueurs[joueur_courant]["main"].append(cartes.pop())
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

    def Niveau4(nom):
        # Définir les cartes Uno
        couleurs = ["Rouge", "Bleu", "Vert", "Jaune", "Blanc", "Noir"]
        valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Inverse", "Passe"]
        cartes = []

        for couleur in range(len(couleurs)):
            for valeur in range(len(valeurs)):
                carte = couleurs[couleur] + " " + valeurs[valeur]
                cartes.append(carte)

        # Mélanger les cartes
        random.shuffle(cartes)

        # Initialiser les mains des joueurs---------------------------
        joueurs = []
        main_joueur = []

        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": nom, "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot1", "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot2", "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot3", "main": main_joueur})
        # -----------------------------------------------------------
        # Initialiser la pile de défausse
        defausse = [cartes.pop()]

        # Fonction pour déterminer si une carte est jouable
        def carte_jouable(carte):
            derniere_carte = defausse[-1]
            if carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == derniere_carte.split()[1]:
                return True
            elif carte.split()[1] == "Inverse" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "Passe" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+2" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+4" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+6" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+8" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            else:
                return False

        # Fonction pour jouer une carte
        def jouer_carte(joueur, carte):
            joueur["main"].remove(carte)
            defausse.append(carte)

        def IQ_test():
            rc = 0
            quiz = {
                "Quelle est la capital de la France?": "Paris",
                "Combien y a-t-il de départements en France?": "96",
                "Quelle est la langue officielle de la France?": "Le Français",
                "Quel est le plus grand fleuve de France?": "La Loire",
                "Quel est le plus haut sommet de la France?": "Mont Blanc",
                "Quel est le nom du président actuel de la France?": "Emmanuel Macron",
                "Quel est le nom de la devise nationale de la France?": "Liberté égalité fraternité",
                "Quel est le nom de la tour la plus célèbre de Paris?": "La Tour Eiffel",
                "Quel est le nom de la plus grande île de France?": "Corsica",
                "Combien y a-t-il de régions en France?": "13"
            }
            for i in range(5):
                print(f"Question", i + 1)
                question = random.choice(list(quiz.keys()))
                answer = quiz[question]
                print(question)
                response = input()
                if response.lower() == answer.lower():
                    print("Correct!")
                    rc += 1
                else:
                    print("Incorrect. La réponse était: " + answer)
                print("-------------------------------------------------------------------")
            if rc == 5:
                return True, 5 - rc
            else:
                return False, random.randint(2, 12)

        def pioche_infernale():
            alea = random.randint(0, 12)
            return alea

        # Boucle principale du jeu-------------------------------------------------------------------------------------------------------------------------
        joueur_courant = 0
        sens = 1
        lst_joueurs = []
        for i in range(4):
            lst_joueurs.append(str(i) + " " + "0")

        while True:
            if cartes == []:
                while len(defausse) != 1:
                    cartes.append(defausse[0])
                    defausse.remove(defausse[0])
            random.shuffle(cartes)
            alea = random.randint(1, 15)

            print("-------------------------------------------------------------------")
            #Au tour du bot

            if joueurs[joueur_courant]["nom"] == "Bot1" or joueurs[joueur_courant]["nom"] == "Bot2":
                main_debut = len(joueurs[joueur_courant]["main"])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("La carte actuelle est :", defausse[-1])
                chargement = "Le bot est en train de réfléchir"
                for i in range(1):
                    print(chargement + ".")
                    time.sleep(1)
                    print(chargement + "..")
                    time.sleep(1)
                    print(chargement + "...")
                    time.sleep(1)
                i = 0
                trouve = False
                taille = len(joueurs[joueur_courant]["main"])
                joueur_courant_temp = joueur_courant
                while i < taille:
                    if trouve == True:
                        break
                    carte_jouee = joueurs[joueur_courant]["main"][i]
                    if carte_jouable(carte_jouee) == True:
                        jouer_carte(joueurs[joueur_courant], carte_jouee)

                        #Carte jouée inverse

                        if carte_jouee.split()[1] == "Inverse":
                            sens *= -1
                            if sens < 0:
                                joueur_courant -= 1
                            elif sens > 0:
                                joueur_courant += 1

                        #Carte jouée Passe

                        elif carte_jouee.split()[1] == "Passe":
                            if sens < 0:
                                joueur_courant -= 2
                            elif sens > 0:
                                joueur_courant += 2

                        #Carte jouée +2

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

                        #Carte jouée +4

                        elif carte_jouee.split()[1] == "+4":
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
                            for i in range(4):
                                joueurs[joueur_courant]["main"].append(cartes.pop())
                            if sens < 0:
                                joueur_courant -= 1
                            elif sens > 0:
                                joueur_courant += 1

                        #Carte jouée +6

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

                        #Carte jouée +8

                        elif carte_jouee.split()[1] == "+8":
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
                            for i in range(8):
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
                        trouve = True
                        taille = 1

                    i += 1

                if main_debut == len(joueurs[joueur_courant_temp]["main"]):
                    joueurs[joueur_courant_temp]["main"].append(cartes.pop())
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                mainbot = "Main du bot : "
                for i in range(len(joueurs[joueur_courant_temp]["main"])):
                    mainbot += "| "
                print(mainbot)
                if len(joueurs[joueur_courant_temp]["main"]) == 0:
                    print(joueurs[joueur_courant_temp]["nom"], "a gagné !")
                    return joueurs[joueur_courant_temp]["nom"]

            #Au tour du bot (même algorithme)

            elif joueurs[joueur_courant]["nom"] == "Bot3":
                main_debut = len(joueurs[joueur_courant]["main"])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("La carte actuelle est :", defausse[-1])
                chargement = "Le bot est en train de réfléchir"
                for i in range(1):
                    print(chargement + ".")
                    time.sleep(1)
                    print(chargement + "..")
                    time.sleep(1)
                    print(chargement + "...")
                    time.sleep(1)
                i = 0
                trouve = False
                taille = len(joueurs[joueur_courant]["main"])
                joueur_courant_temp = joueur_courant
                while i < taille:
                    if trouve == True:
                        break
                    carte_jouee = joueurs[joueur_courant]["main"][i]
                    if carte_jouable(carte_jouee) == True:
                        jouer_carte(joueurs[joueur_courant], carte_jouee)
                        if carte_jouee.split()[1] == "Inverse":
                            sens *= -1
                            if sens < 0:
                                joueur_courant -= 1
                            elif sens > 0:
                                joueur_courant += 1
                        elif carte_jouee.split()[1] == "Passe":
                            if sens < 0:
                                joueur_courant -= 2
                            elif sens > 0:
                                joueur_courant += 2
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

                        elif carte_jouee.split()[1] == "+4":
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
                            for i in range(4):
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
                        elif carte_jouee.split()[1] == "+8":
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
                            for i in range(8):
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
                        trouve = True
                        taille = 1

                    i += 1
                if main_debut == len(joueurs[joueur_courant_temp]["main"]):
                    joueurs[joueur_courant_temp]["main"].append(cartes.pop())
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                mainbot = "Main du bot : "
                for i in range(len(joueurs[joueur_courant_temp]["main"])):
                    mainbot += "| "
                print(mainbot)
                if len(joueurs[joueur_courant_temp]["main"]) == 0:
                    print(joueurs[joueur_courant_temp]["nom"], "a gagné !")
                    return joueurs[joueur_courant_temp]["nom"]


            #Au tour du joueur

            else:
                if alea == 1:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement Test de QI")
                    restestqi = IQ_test()
                    if restestqi[0] == False:
                        print("Vous allez piocher " + str(
                            restestqi[1]) + " cartes")
                    for i in range(restestqi[1]):
                        joueurs[joueur_courant]["main"].append(cartes.pop())

                if alea == 2:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement pioche infernale")
                    roue = pioche_infernale()
                    roue2 = random.randint(1, 15)
                    if roue2 == 1:
                        for i in range(len(joueurs)):
                            for j in range(roue):
                                joueurs[i]["main"].append(cartes.pop())
                    else:
                        for i in range(roue):
                            joueurs[joueur_courant]["main"].append(cartes.pop())

                if alea == 3:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    for i in range(len(lst_joueurs)):
                        temp = lst_joueurs[joueur_courant]
                        temp = temp.split()
                        if temp[1] == "0":
                            temp[1] = "3"
                            temp[0] += " " + str(temp[1])
                            del (temp[1])
                            for j in range(len(temp)):
                                lst_joueurs[joueur_courant] = temp[j]
                            break
                if lst_joueurs[0][2] != "0":
                    for i in range(len(lst_joueurs)):
                        temp = lst_joueurs[joueur_courant]
                        temp = temp.split()
                        temp[1] = str(int(temp[1]) - 1)
                        temp[0] += " " + str(temp[1])
                        del (temp[1])
                        for j in range(len(temp)):
                            lst_joueurs[joueur_courant] = temp[j]
                        break
                    now = time.time()
                    max_delay = now + 4

                    while True:
                        print("Evènement TIME TIME")
                        print("La carte actuelle est :", defausse[-1])
                        print("Votre main est :", joueurs[joueur_courant]["main"])
                        carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                        if time.time() > max_delay:
                            print("Temps manqué")
                            carte_jouee = "p"
                            break
                        else:
                            break
                else:
                    print("La carte actuelle est :", defausse[-1])
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Votre main est :", joueurs[joueur_courant]["main"])
                    now = time.time()
                    max_delay = now + 15
                    while True:
                        carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                        if time.time() > max_delay:
                            print("Temps manqué")
                            carte_jouee = "p"
                            break
                        else:
                            break

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
                        return joueurs[joueur_courant]["nom"]
                    elif carte_jouee.split()[1] == "Inverse":
                        sens *= -1
                        if sens < 0:
                            joueur_courant -= 1
                        elif sens > 0:
                            joueur_courant += 1

                    elif carte_jouee.split()[1] == "Passe":
                        if sens < 0:
                            joueur_courant -= 2
                        elif sens > 0:
                            joueur_courant += 2

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

                    elif carte_jouee.split()[1] == "+4":
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
                        for i in range(4):
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
                    elif carte_jouee.split()[1] == "+8":
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
                        for i in range(8):
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
                    joueurs[joueur_courant]["main"].append(cartes.pop())
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

    def Niveau5(nom):
        # Définir les cartes Uno
        couleurs = ["Rouge", "Bleu", "Vert", "Jaune", "Blanc", "Noir"]
        valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Inverse", "Passe"]
        cartes = []

        for couleur in range(len(couleurs)):
            for valeur in range(len(valeurs)):
                carte = couleurs[couleur] + " " + valeurs[valeur]
                cartes.append(carte)

        # Mélanger les cartes
        random.shuffle(cartes)

        # Initialiser les mains des joueurs---------------------------
        joueurs = []
        main_joueur = []

        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": nom, "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot1", "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot2", "main": main_joueur})

        # -----------------------------------------------------------
        # Initialiser la pile de défausse
        defausse = [cartes.pop()]

        # Fonction pour déterminer si une carte est jouable
        def carte_jouable(carte):
            derniere_carte = defausse[-1]
            if carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == derniere_carte.split()[1]:
                return True
            elif carte.split()[1] == "Inverse" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "Passe" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+2" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+4" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+6" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+8" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            else:
                return False

        # Fonction pour jouer une carte
        def jouer_carte(joueur, carte):
            joueur["main"].remove(carte)
            defausse.append(carte)

        def IQ_test():
            rc = 0
            quiz = {
                "Quelle est la capital de la France?": "Paris",
                "Combien y a-t-il de départements en France?": "96",
                "Quelle est la langue officielle de la France?": "Le Français",
                "Quel est le plus grand fleuve de France?": "La Loire",
                "Quel est le plus haut sommet de la France?": "Mont Blanc",
                "Quel est le nom du président actuel de la France?": "Emmanuel Macron",
                "Quel est le nom de la devise nationale de la France?": "Liberté égalité fraternité",
                "Quel est le nom de la tour la plus célèbre de Paris?": "La Tour Eiffel",
                "Quel est le nom de la plus grande île de France?": "Corsica",
                "Combien y a-t-il de régions en France?": "13"
            }
            for i in range(5):
                print(f"Question", i + 1)
                question = random.choice(list(quiz.keys()))
                answer = quiz[question]
                print(question)
                response = input()
                if response.lower() == answer.lower():
                    print("Correct!")
                    rc += 1
                else:
                    print("Incorrect. La réponse était: " + answer)
                print("-------------------------------------------------------------------")
            if rc == 5:
                return True, 5 - rc
            else:
                return False, random.randint(2, 12)

        def pioche_infernale():
            alea = random.randint(0, 12)
            return alea

        def speed_test():
            # Fonction qui donne des touches aléatiores à entrer

            # Les lettres à entrer
            cles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

            # Nombre de lettres à entrer
            num_cles = random.randint(5, 7)
            # Limite de temps
            now = time.time()
            time_limit = now + num_cles + 5

            # Séries de lesttres à entrer
            sequence = []
            for i in range(num_cles):
                sequence.append(random.choice(cles))

            # Ask the player to enter the key sequence within the time limit
            print("Entrez ces", num_cles, "lettres et/ou chiffres en", time_limit, "secondes:")

            for i in range(len(sequence)):
                print(sequence[i], end=" ")
            print()

            for i in range(num_cles):
                clee = input("Lettre : ")
                if clee != sequence[i]:
                    print("Mauvaise lettre! Game over.")
                    return False
                if time.time() > time_limit:
                    print("Temps écoulé! Game over.")
                    return False

            if time.time() < time_limit and clee == sequence[i]:
                print("Félicitations! Tu as réussi à faire la bonne combinaison de touches.")
                return True

        # Boucle principale du jeu-------------------------------------------------------------------------------------------------------------------------
        joueur_courant = 0
        sens = 1
        lst_joueurs = []
        for i in range(3):
            lst_joueurs.append(str(i) + " " + "0")

        while True:
            if cartes == []:
                while len(defausse) != 1:
                    cartes.append(defausse[0])
                    defausse.remove(defausse[0])
            random.shuffle(cartes)
            alea = random.randint(1, 15)

            print("-------------------------------------------------------------------")
            if joueurs[joueur_courant]["nom"] == "Bot1" or joueurs[joueur_courant]["nom"] == "Bot2":
                main_debut = len(joueurs[joueur_courant]["main"])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("La carte actuelle est :", defausse[-1])
                chargement = "Le bot est en train de réfléchir"
                for i in range(1):
                    print(chargement + ".")
                    time.sleep(1)
                    print(chargement + "..")
                    time.sleep(1)
                    print(chargement + "...")
                    time.sleep(1)
                i = 0
                trouve = False
                taille = len(joueurs[joueur_courant]["main"])
                joueur_courant_temp = joueur_courant
                while i < taille:
                    if trouve == True:
                        break
                    carte_jouee = joueurs[joueur_courant]["main"][i]
                    if carte_jouable(carte_jouee) == True:
                        jouer_carte(joueurs[joueur_courant], carte_jouee)
                        if carte_jouee.split()[1] == "Inverse":
                            sens *= -1
                            if sens < 0:
                                joueur_courant -= 1
                            elif sens > 0:
                                joueur_courant += 1
                        elif carte_jouee.split()[1] == "Passe":
                            if sens < 0:
                                joueur_courant -= 2
                            elif sens > 0:
                                joueur_courant += 2
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

                        elif carte_jouee.split()[1] == "+4":
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
                            for i in range(4):
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
                        elif carte_jouee.split()[1] == "+8":
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
                            for i in range(8):
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
                        trouve = True
                        taille = 1

                    i += 1

                if main_debut == len(joueurs[joueur_courant_temp]["main"]):
                    joueurs[joueur_courant_temp]["main"].append(cartes.pop())
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                mainbot = "Main du bot : "
                for i in range(len(joueurs[joueur_courant_temp]["main"])):
                    mainbot += "| "
                print(mainbot)
                if len(joueurs[joueur_courant_temp]["main"]) == 0:
                    print(joueurs[joueur_courant_temp]["nom"], "a gagné !")
                    return joueurs[joueur_courant_temp]["nom"]


            else:
                if alea == 1:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement Test de QI")
                    restestqi = IQ_test()
                    if restestqi[0] == False:
                        print("Vous allez piocher " + str(
                            restestqi[1]) + " cartes")
                    for i in range(restestqi[1]):
                        joueurs[joueur_courant]["main"].append(cartes.pop())

                if alea == 2:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement pioche infernale")
                    roue = pioche_infernale()
                    roue2 = random.randint(1, 15)
                    if roue2 == 1:
                        for i in range(len(joueurs)):
                            for j in range(roue):
                                joueurs[i]["main"].append(cartes.pop())
                    else:
                        for i in range(roue):
                            joueurs[joueur_courant]["main"].append(cartes.pop())
                if alea == 4:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement Combinaison touche")
                    combitouche = speed_test()
                    if combitouche == False:
                        roue_touche = random.randint(2, 12)
                        for i in range(roue_touche):
                            joueurs[joueur_courant]["main"].append(cartes.pop())

                if alea == 3:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    for i in range(len(lst_joueurs)):
                        temp = lst_joueurs[joueur_courant]
                        temp = temp.split()
                        if temp[1] == "0":
                            temp[1] = "3"
                            temp[0] += " " + str(temp[1])
                            del (temp[1])
                            for j in range(len(temp)):
                                lst_joueurs[joueur_courant] = temp[j]
                            break
                if lst_joueurs[0][2] != "0":
                    for i in range(len(lst_joueurs)):
                        temp = lst_joueurs[joueur_courant]
                        temp = temp.split()
                        temp[1] = str(int(temp[1]) - 1)
                        temp[0] += " " + str(temp[1])
                        del (temp[1])
                        for j in range(len(temp)):
                            lst_joueurs[joueur_courant] = temp[j]
                        break
                    now = time.time()
                    max_delay = now + 4

                    while True:
                        print("Evènement TIME TIME")
                        print("La carte actuelle est :", defausse[-1])
                        print("Votre main est :", joueurs[joueur_courant]["main"])
                        carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                        if time.time() > max_delay:
                            print("Temps manqué")
                            carte_jouee = "p"
                            break
                        else:
                            break
                else:
                    print("La carte actuelle est :", defausse[-1])
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Votre main est :", joueurs[joueur_courant]["main"])
                    now = time.time()
                    max_delay = now + 15
                    while True:
                        carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                        if time.time() > max_delay:
                            print("Temps manqué")
                            carte_jouee = "p"
                            break
                        else:
                            break

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
                        return joueurs[joueur_courant]["nom"]
                    elif carte_jouee.split()[1] == "Inverse":
                        sens *= -1
                        if sens < 0:
                            joueur_courant -= 1
                        elif sens > 0:
                            joueur_courant += 1

                    elif carte_jouee.split()[1] == "Passe":
                        if sens < 0:
                            joueur_courant -= 2
                        elif sens > 0:
                            joueur_courant += 2

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

                    elif carte_jouee.split()[1] == "+4":
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
                        for i in range(4):
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
                    elif carte_jouee.split()[1] == "+8":
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
                        for i in range(8):
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
                    joueurs[joueur_courant]["main"].append(cartes.pop())
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

    def Niveau6(nom):
        # Définir les cartes Uno
        couleurs = ["Rouge", "Bleu", "Vert", "Jaune", "Blanc", "Noir"]
        valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Inverse", "Passe"]
        cartes = []

        for couleur in range(len(couleurs)):
            for valeur in range(len(valeurs)):
                carte = couleurs[couleur] + " " + valeurs[valeur]
                cartes.append(carte)

        cartes.append("SWAP")
        # Mélanger les cartes
        random.shuffle(cartes)
        # Initialiser la pile de défausse
        defausse = [cartes.pop()]
        cartes.append("SWAP")
        random.shuffle(cartes)

        # Initialiser les mains des joueurs---------------------------
        joueurs = []
        main_joueur = []

        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": nom, "main": main_joueur})

        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": "Bot1", "main": main_joueur})

        # -----------------------------------------------------------

        # Fonction pour déterminer si une carte est jouable
        def carte_jouable(carte):
            derniere_carte = defausse[-1]
            if carte == "SWAP":
                return True
            elif carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == derniere_carte.split()[1]:
                return True
            elif carte.split()[1] == "Inverse" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "Passe" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+2" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+4" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+6" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            elif carte.split()[1] == "+8" and carte.split()[0] == derniere_carte.split()[0]:
                return True
            else:
                return False

        # Fonction pour jouer une carte
        def jouer_carte(joueur, carte):
            joueur["main"].remove(carte)
            if carte != "SWAP":
                defausse.append(carte)

        def IQ_test():
            rc = 0
            quiz = {
                "Quelle est la capital de la France?": "Paris",
                "Combien y a-t-il de départements en France?": "96",
                "Quelle est la langue officielle de la France?": "Le Français",
                "Quel est le plus grand fleuve de France?": "La Loire",
                "Quel est le plus haut sommet de la France?": "Mont Blanc",
                "Quel est le nom du président actuel de la France?": "Emmanuel Macron",
                "Quel est le nom de la devise nationale de la France?": "Liberté égalité fraternité",
                "Quel est le nom de la tour la plus célèbre de Paris?": "La Tour Eiffel",
                "Quel est le nom de la plus grande île de France?": "Corsica",
                "Combien y a-t-il de régions en France?": "13"
            }
            for i in range(5):
                print(f"Question", i + 1)
                question = random.choice(list(quiz.keys()))
                answer = quiz[question]
                print(question)
                response = input()
                if response.lower() == answer.lower():
                    print("Correct!")
                    rc += 1
                else:
                    print("Incorrect. La réponse était: " + answer)
                print("-------------------------------------------------------------------")
            if rc == 5:
                return True, 5 - rc
            else:
                return False, random.randint(2, 12)

        def pioche_infernale():
            alea = random.randint(0, 12)
            return alea

        def speed_test():
            # Fonction qui donne des touches aléatiores à entrer

            # Les lettres à entrer
            cles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

            # Nombre de lettres à entrer
            num_cles = random.randint(5, 7)
            # Limite de temps
            now = time.time()
            time_limit = now + num_cles + 5

            # Séries de lesttres à entrer
            sequence = []
            for i in range(num_cles):
                sequence.append(random.choice(cles))

            # Ask the player to enter the key sequence within the time limit
            print("Entrez ces", num_cles, "lettres et/ou chiffres en", time_limit, "secondes:")

            for i in range(len(sequence)):
                print(sequence[i], end=" ")
            print()

            for i in range(num_cles):
                clee = input("Lettre : ")
                if clee != sequence[i]:
                    print("Mauvaise lettre! Game over.")
                    return False
                if time.time() > time_limit:
                    print("Temps écoulé! Game over.")
                    return False

            if time.time() < time_limit and clee == sequence[i]:
                print("Félicitations! Tu as réussi à faire la bonne combinaison de touches.")
                return True

        # Boucle principale du jeu-------------------------------------------------------------------------------------------------------------------------
        joueur_courant = 0
        sens = 1
        lst_joueurs = []
        for i in range(2):
            lst_joueurs.append(str(i) + " " + "0")

        while True:
            if cartes == []:
                while len(defausse) != 1:
                    cartes.append(defausse[0])
                    defausse.remove(defausse[0])
            random.shuffle(cartes)
            alea = random.randint(1, 15)

            print("-------------------------------------------------------------------")
            if joueurs[joueur_courant]["nom"] == "Bot1":
                main_debut = len(joueurs[joueur_courant]["main"])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("La carte actuelle est :", defausse[-1])
                chargement = "Le bot est en train de réfléchir"
                for i in range(1):
                    print(chargement + ".")
                    time.sleep(1)
                    print(chargement + "..")
                    time.sleep(1)
                    print(chargement + "...")
                    time.sleep(1)
                i = 0
                trouve = False
                taille = len(joueurs[joueur_courant]["main"])
                joueur_courant_temp = joueur_courant
                while i < taille:
                    if trouve == True:
                        break
                    carte_jouee = joueurs[joueur_courant]["main"][i]
                    if carte_jouable(carte_jouee) == True:
                        jouer_carte(joueurs[joueur_courant], carte_jouee)
                        if carte_jouee == "SWAP":
                            nom_swapp = nom
                            for i in range(len(joueurs)):
                                if joueurs[i]["nom"] == nom_swapp:
                                    temp = joueurs[joueur_courant]["main"]
                                    joueurs[joueur_courant]["main"] = joueurs[i]["main"]
                                    joueurs[i]["main"] = temp
                                    if sens < 0:
                                        joueur_courant -= 1
                                    elif sens > 0:
                                        joueur_courant += 1
                                    break
                        elif carte_jouee.split()[1] == "Inverse":
                            sens *= -1
                            if sens < 0:
                                joueur_courant -= 1
                            elif sens > 0:
                                joueur_courant += 1
                        elif carte_jouee.split()[1] == "Passe":
                            if sens < 0:
                                joueur_courant -= 2
                            elif sens > 0:
                                joueur_courant += 2
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

                        elif carte_jouee.split()[1] == "+4":
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
                            for i in range(4):
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
                        elif carte_jouee.split()[1] == "+8":
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
                            for i in range(8):
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
                        trouve = True
                        taille = 1

                    i += 1

                if main_debut == len(joueurs[joueur_courant_temp]["main"]):
                    joueurs[joueur_courant_temp]["main"].append(cartes.pop())
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                mainbot = "Main du bot : "
                for i in range(len(joueurs[joueur_courant_temp]["main"])):
                    mainbot += "| "
                print(mainbot)
                if len(joueurs[joueur_courant_temp]["main"]) == 0:
                    print(joueurs[joueur_courant_temp]["nom"], "a gagné !")
                    return joueurs[joueur_courant_temp]["nom"]


            else:
                if alea == 1:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement Test de QI")
                    restestqi = IQ_test()
                    if restestqi[0] == False:
                        print("Vous allez piocher " + str(
                            restestqi[1]) + " cartes")
                    for i in range(restestqi[1]):
                        joueurs[joueur_courant]["main"].append(cartes.pop())

                if alea == 2:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement pioche infernale")
                    roue = pioche_infernale()
                    roue2 = random.randint(1, 15)
                    if roue2 == 1:
                        for i in range(len(joueurs)):
                            for j in range(roue):
                                joueurs[i]["main"].append(cartes.pop())
                    else:
                        for i in range(roue):
                            joueurs[joueur_courant]["main"].append(cartes.pop())
                if alea == 4:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Evènement Combinaison touche")
                    combitouche = speed_test()
                    if combitouche == False:
                        roue_touche = random.randint(2, 12)
                        for i in range(roue_touche):
                            joueurs[joueur_courant]["main"].append(cartes.pop())

                if alea == 5:
                    print("Evènement SWAP")
                    regroupement = []
                    for i in range(len(joueurs)):
                        while joueurs[i]["main"] != []:
                            regroupement.append(joueurs[i]["main"][0])
                            joueurs[i]["main"].remove(joueurs[i]["main"][0])
                    random.shuffle(regroupement)
                    j = len(joueurs) - 1
                    while regroupement != []:
                        joueurs[j]["main"].append(regroupement[0])
                        regroupement.remove(regroupement[0])
                        j -= 1
                        if j < 0:
                            j = len(joueurs) - 1


                if alea == 3:
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    for i in range(len(lst_joueurs)):
                        temp = lst_joueurs[joueur_courant]
                        temp = temp.split()
                        if temp[1] == "0":
                            temp[1] = "3"
                            temp[0] += " " + str(temp[1])
                            del (temp[1])
                            for j in range(len(temp)):
                                lst_joueurs[joueur_courant] = temp[j]
                            break
                if lst_joueurs[0][2] != "0":
                    for i in range(len(lst_joueurs)):
                        temp = lst_joueurs[joueur_courant]
                        temp = temp.split()
                        temp[1] = str(int(temp[1]) - 1)
                        temp[0] += " " + str(temp[1])
                        del (temp[1])
                        for j in range(len(temp)):
                            lst_joueurs[joueur_courant] = temp[j]
                        break
                    now = time.time()
                    max_delay = now + 4

                    while True:
                        print("Evènement TIME TIME")
                        print("La carte actuelle est :", defausse[-1])
                        print("Votre main est :", joueurs[joueur_courant]["main"])
                        carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                        if time.time() > max_delay:
                            print("Temps manqué")
                            carte_jouee = "p"
                            break
                        else:
                            break
                else:
                    print("La carte actuelle est :", defausse[-1])
                    print("C'est au tour de", joueurs[joueur_courant]["nom"])
                    print("Votre main est :", joueurs[joueur_courant]["main"])
                    now = time.time()
                    max_delay = now + 15
                    while True:
                        carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                        if time.time() > max_delay:
                            print("Temps manqué")
                            carte_jouee = "p"
                            break
                        else:
                            break
                if carte_jouee == "SWAP":
                    nom_swapp = input("Donnez le nom du joueur : ")
                    for i in range(len(joueurs)):
                        if joueurs[i]["nom"] == nom_swapp:
                            temp = joueurs[joueur_courant]["main"]
                            joueurs[joueur_courant]["main"] = joueurs[i]["main"]
                            joueurs[i]["main"] = temp
                            if sens < 0:
                                joueur_courant -= 1
                            elif sens > 0:
                                joueur_courant += 1
                            break
                elif carte_jouee == "p":
                    joueurs[joueur_courant]["main"].append(cartes.pop())
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                elif carte_jouable(carte_jouee):
                    jouer_carte(joueurs[joueur_courant], carte_jouee)
                    if len(joueurs[joueur_courant]["main"]) == 0:
                        print(joueurs[joueur_courant]["nom"], "a gagné !")
                        return joueurs[joueur_courant]["nom"]
                    elif carte_jouee.split()[1] == "Inverse":
                        sens *= -1
                        if sens < 0:
                            joueur_courant -= 1
                        elif sens > 0:
                            joueur_courant += 1

                    elif carte_jouee.split()[1] == "Passe":
                        if sens < 0:
                            joueur_courant -= 2
                        elif sens > 0:
                            joueur_courant += 2

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

                    elif carte_jouee.split()[1] == "+4":
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
                        for i in range(4):
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
                    elif carte_jouee.split()[1] == "+8":
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
                        for i in range(8):
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
                    joueurs[joueur_courant]["main"].append(cartes.pop())
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

    passageniv0 = Niveau1(nom)  # Niveau 1
    if passageniv0 == nom:
        time.sleep(1.3)
        print("Bravo à toi ! Je vois que tu es très fort")
        time.sleep(1.3)
        print("Nous pouvons donc passer à un niveau plus élevé")
        time.sleep(1.3)
        print(
            "Félicitations ! Vous avez débloqué :\n-La Carte Inverse : Celle-ci jouée changera le sens du jeu ainsi le joueur précédent deviendra le suivant et le joueur suivant deviendra le précédent")
        print(
            "-L'évènement Test de QI : Dans lequel vous devrez répondre à 5 questions si vous faîtes une erreur une roue va tourner et vous piocherez entre 2 et 12 cartes")
        time.sleep(5)
        passageniv1 = Niveau2(nom)  # Niveau 2
        if passageniv1 == nom:
            time.sleep(1.3)
            print("Je t'es sous estimés en fait tu es vraiment fort")
            time.sleep(1.3)
            print("Voyons si tu réussiras le niveau 3")
            time.sleep(1.3)
            print("Cette fois c'est 3 adversaires et c'est en 2 parties, une seule erreur et c'est game over")
            time.sleep(1.3)
            print(
                "Félicitations ! Vous avez débloqué :\n-La Carte Passe : Celle-ci jouée empêchera le joueur suivant de jouer pendant 1 tour")
            print(
                "-L'évènement pioche infernale : Dans lequel une roue va être tournée et selon le nombre affiché vous aller piocher le nombre de cartes correspondant au numéro de la roue \nIl y a une faible probabilité que ce soit tout le monde qui pioche")
            time.sleep(5)

            cpt = 0
            while cpt != 2:
                cpt = 0
                for i in range(2):
                    passageniv2 = Niveau3(nom)  # Niveau 3
                    if passageniv2 == nom:
                        cpt += 1
                        print("Partie", i, "gagnée")

            time.sleep(1.3)
            print("Décidément, tu es imbattable cela m'inquiète mais passons...")
            time.sleep(1.3)
            print("Je pense que l'on peut encore augmenter le niveau de difficulté")
            time.sleep(1.3)
            print("Cette fois c'est 3 adversaires et c'est en 3 parties")
            time.sleep(1.3)
            print(
                "Félicitations ! Vous avez débloqué :\n-Les Cartes +2 +4 +6 et +8 : Celles-ci jouées feront piocher au joueur suivant le nombre de cartes inscrits sur celle-ci et passeront son tour")
            print(
                "-L'évènement TIME TIME : Il s'agit d'un des plus dûrs évènements que tu peux rencontrer celui te feras jouer sur 3 tours en moins de 4 secondes")

            cpt = 0
            while cpt != 3:
                cpt = 0
                for i in range(3):
                    passageniv3 = Niveau4(nom)  # Niveau 4
                    if passageniv3 == nom:
                        cpt += 1
                        print("Partie", i, "gagnée")

            time.sleep(1.3)
            print("Tu pourrais peut être ralentir non ?")
            time.sleep(1.3)
            print("Je vais devoir sortir les grands moyens")
            time.sleep(1.3)
            print("Cette fois c'est 2 adversaires et c'est en 4 parties")
            time.sleep(1.3)
            print(
                "Félicitations ! Vous avez débloqué :\n-L'évènement Combinaison Touche : Dans cet évènement vous allez devoir faire une combinaison de touche en un temps limité\nEn cas d'échec vous allez devoir piocher entre 2 et 12 cartes ")
            time.sleep(5)

            cpt = 0
            while cpt != 4:
                cpt = 0
                for i in range(4):
                    passageniv4 = Niveau5(nom)  # Niveau 5
                    if passageniv4 == nom:
                        cpt += 1
                        print("Partie", i, "gagnée")

            time.sleep(1.3)
            print("Comment as-tu ...")
            time.sleep(1.3)
            print("Cette fois je vais devoir t'arrêter")
            time.sleep(1.3)
            print("Maintenant c'est toi contre moi en 5 parties")
            time.sleep(1.3)
            print(
                "Félicitations ! Vous avez débloqué la carte ultime : \n-La carte Swap : Celle-ci va inverser votre jeu avec celui d'un adversaire de votre choix ")

            cpt = 0
            while cpt != 2:
                cpt = 0
                for i in range(2):
                    passageniv5 = Niveau6(nom)  # Niveau 6
                    if passageniv5 == nom:
                        cpt += 1
                        print("Partie", i, "gagnée")

            time.sleep(1.3)
            print("Félicitations ! Vous avez vaincu l'arène")


def mode_libre_bots(nom, nbr_bots):
    # Définir les cartes Uno
    couleurs = ["Rouge", "Bleu", "Vert", "Jaune", "Blanc", "Noir"]
    valeurs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Inverse", "Passe"]
    cartes = []

    for couleur in range(len(couleurs)):
        for valeur in range(len(valeurs)):
            carte = couleurs[couleur] + " " + valeurs[valeur]
            cartes.append(carte)

    # Mélanger les cartes
    # Initialiser la pile de défausse
    defausse = [cartes.pop()]
    cartes.append("SWAP")
    random.shuffle(cartes)

    # Initialiser les mains des joueurs---------------------------
    joueurs = []
    main_joueur = []

    for j in range(7):
        carte = cartes.pop()
        main_joueur.append(carte)
    joueurs.append({"nom": nom, "main": main_joueur})

    bots = "Bot"
    for k in range(nbr_bots):
        main_joueur = []
        for j in range(7):
            carte = cartes.pop()
            main_joueur.append(carte)
        joueurs.append({"nom": bots + str(k), "main": main_joueur})
    nbr_bots+=1

    # -----------------------------------------------------------

    # Fonction pour déterminer si une carte est jouable
    def carte_jouable(carte):
        derniere_carte = defausse[-1]
        if carte == "SWAP":
            return True
        elif carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == derniere_carte.split()[1]:
            return True
        elif carte.split()[1] == "Inverse" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == "Passe" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == "+2" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == "+4" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == "+6" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        elif carte.split()[1] == "+8" and carte.split()[0] == derniere_carte.split()[0]:
            return True
        else:
            return False

    # Fonction pour jouer une carte
    def jouer_carte(joueur, carte):
        joueur["main"].remove(carte)
        if carte != "SWAP":
            defausse.append(carte)

    def IQ_test():
        rc = 0
        quiz = {
            "Quelle est la capital de la France?": "Paris",
            "Combien y a-t-il de départements en France?": "96",
            "Quelle est la langue officielle de la France?": "Le Français",
            "Quel est le plus grand fleuve de France?": "La Loire",
            "Quel est le plus haut sommet de la France?": "Mont Blanc",
            "Quel est le nom du président actuel de la France?": "Emmanuel Macron",
            "Quel est le nom de la devise nationale de la France?": "Liberté égalité fraternité",
            "Quel est le nom de la tour la plus célèbre de Paris?": "La Tour Eiffel",
            "Quel est le nom de la plus grande île de France?": "Corsica",
            "Combien y a-t-il de régions en France?": "13"
        }
        for i in range(5):
            print(f"Question", i + 1)
            question = random.choice(list(quiz.keys()))
            answer = quiz[question]
            print(question)
            response = input()
            if response.lower() == answer.lower():
                print("Correct!")
                rc += 1
            else:
                print("Incorrect. La réponse était: " + answer)
            print("-------------------------------------------------------------------")
        if rc == 5:
            return True, 5 - rc
        else:
            return False, random.randint(2, 12)

    def pioche_infernale():
        alea = random.randint(0, 12)
        return alea

    def speed_test():
        # Fonction qui donne des touches aléatiores à entrer

        # Les lettres à entrer
        cles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u',
                'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Nombre de lettres à entrer
        num_cles = random.randint(5, 7)
        # Limite de temps
        now = time.time()
        time_limit = now + num_cles + 5

        # Séries de lesttres à entrer
        sequence = []
        for i in range(num_cles):
            sequence.append(random.choice(cles))

        # Ask the player to enter the key sequence within the time limit
        print("Entrez ces", num_cles, "lettres et/ou chiffres en", time_limit, "secondes:")

        for i in range(len(sequence)):
            print(sequence[i], end=" ")
        print()

        for i in range(num_cles):
            clee = input("Lettre : ")
            if clee != sequence[i]:
                print("Mauvaise lettre! Game over.")
                return False
            if time.time() > time_limit:
                print("Temps écoulé! Game over.")
                return False

        if time.time() < time_limit and clee == sequence[i]:
            print("Félicitations! Tu as réussi à faire la bonne combinaison de touches.")
            return True

    # Boucle principale du jeu-------------------------------------------------------------------------------------------------------------------------
    joueur_courant = 0
    sens = 1
    lst_joueurs = []
    for i in range(nbr_bots):
        lst_joueurs.append(str(i) + " " + "0")

    while True:
        if cartes == []:
            while len(defausse) != 1:
                cartes.append(defausse[0])
                defausse.remove(defausse[0])
        random.shuffle(cartes)
        alea = random.randint(1, 15)

        print("-------------------------------------------------------------------")
        if joueurs[joueur_courant]["nom"] == "Bot0" or joueurs[joueur_courant]["nom"] == "Bot1":
            main_debut = len(joueurs[joueur_courant]["main"])
            print("C'est au tour de", joueurs[joueur_courant]["nom"])
            print("La carte actuelle est :", defausse[-1])
            chargement = "Le bot est en train de réfléchir"
            for i in range(1):
                print(chargement + ".")
                time.sleep(1)
                print(chargement + "..")
                time.sleep(1)
                print(chargement + "...")
                time.sleep(1)
            i = 0
            trouve = False
            taille = len(joueurs[joueur_courant]["main"])
            joueur_courant_temp = joueur_courant
            while i < taille:
                if trouve == True:
                    break
                carte_jouee = joueurs[joueur_courant]["main"][i]
                if carte_jouable(carte_jouee) == True:
                    jouer_carte(joueurs[joueur_courant], carte_jouee)
                    if carte_jouee == "SWAP":
                        nom_swapp = nom
                        for i in range(len(joueurs)):
                            if joueurs[i]["nom"] == nom_swapp:
                                temp = joueurs[joueur_courant]["main"]
                                joueurs[joueur_courant]["main"] = joueurs[i]["main"]
                                joueurs[i]["main"] = temp
                                if sens < 0:
                                    joueur_courant -= 1
                                elif sens > 0:
                                    joueur_courant += 1
                                break
                    elif carte_jouee.split()[1] == "Inverse":
                        sens *= -1
                        if sens < 0:
                            joueur_courant -= 1
                        elif sens > 0:
                            joueur_courant += 1
                    elif carte_jouee.split()[1] == "Passe":
                        if sens < 0:
                            joueur_courant -= 2
                        elif sens > 0:
                            joueur_courant += 2
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

                    elif carte_jouee.split()[1] == "+4":
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
                        for i in range(4):
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
                    elif carte_jouee.split()[1] == "+8":
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
                        for i in range(8):
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
                    trouve = True
                    taille = 1

                i += 1

            if main_debut == len(joueurs[joueur_courant_temp]["main"]):
                joueurs[joueur_courant_temp]["main"].append(cartes.pop())
                if sens < 0:
                    joueur_courant -= 1
                elif sens > 0:
                    joueur_courant += 1

            mainbot = "Main du bot : "
            for i in range(len(joueurs[joueur_courant_temp]["main"])):
                mainbot += "| "
            print(mainbot)
            if len(joueurs[joueur_courant_temp]["main"]) == 0:
                print(joueurs[joueur_courant_temp]["nom"], "a gagné !")
                return joueurs[joueur_courant_temp]["nom"]

        elif joueurs[joueur_courant]["nom"] == "Bot2" or joueurs[joueur_courant]["nom"] == "Bot3":
            main_debut = len(joueurs[joueur_courant]["main"])
            print("C'est au tour de", joueurs[joueur_courant]["nom"])
            print("La carte actuelle est :", defausse[-1])
            chargement = "Le bot est en train de réfléchir"
            for i in range(1):
                print(chargement + ".")
                time.sleep(1)
                print(chargement + "..")
                time.sleep(1)
                print(chargement + "...")
                time.sleep(1)
            i = 0
            trouve = False
            taille = len(joueurs[joueur_courant]["main"])
            joueur_courant_temp = joueur_courant
            while i < taille:
                if trouve == True:
                    break
                carte_jouee = joueurs[joueur_courant]["main"][i]
                if carte_jouable(carte_jouee) == True:
                    jouer_carte(joueurs[joueur_courant], carte_jouee)
                    if carte_jouee == "SWAP":
                        nom_swapp = nom
                        for i in range(len(joueurs)):
                            if joueurs[i]["nom"] == nom_swapp:
                                temp = joueurs[joueur_courant]["main"]
                                joueurs[joueur_courant]["main"] = joueurs[i]["main"]
                                joueurs[i]["main"] = temp
                                if sens < 0:
                                    joueur_courant -= 1
                                elif sens > 0:
                                    joueur_courant += 1
                                break
                    elif carte_jouee.split()[1] == "Inverse":
                        sens *= -1
                        if sens < 0:
                            joueur_courant -= 1
                        elif sens > 0:
                            joueur_courant += 1
                    elif carte_jouee.split()[1] == "Passe":
                        if sens < 0:
                            joueur_courant -= 2
                        elif sens > 0:
                            joueur_courant += 2
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

                    elif carte_jouee.split()[1] == "+4":
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
                        for i in range(4):
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
                    elif carte_jouee.split()[1] == "+8":
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
                        for i in range(8):
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
                    trouve = True
                    taille = 1

                i += 1

            if main_debut == len(joueurs[joueur_courant_temp]["main"]):
                joueurs[joueur_courant_temp]["main"].append(cartes.pop())
                if sens < 0:
                    joueur_courant -= 1
                elif sens > 0:
                    joueur_courant += 1

            mainbot = "Main du bot : "
            for i in range(len(joueurs[joueur_courant_temp]["main"])):
                mainbot += "| "
            print(mainbot)
            if len(joueurs[joueur_courant_temp]["main"]) == 0:
                print(joueurs[joueur_courant_temp]["nom"], "a gagné !")
                return joueurs[joueur_courant_temp]["nom"]

        else:
            if alea == 1:
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("Evènement Test de QI")
                restestqi = IQ_test()
                if restestqi[0] == False:
                    print("Vous allez piocher " + str(
                        restestqi[1]) + " cartes")
                for i in range(restestqi[1]):
                    joueurs[joueur_courant]["main"].append(cartes.pop())

            if alea == 2:
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("Evènement pioche infernale")
                roue = pioche_infernale()
                roue2 = random.randint(1, 15)
                if roue2 == 1:
                    for i in range(len(joueurs)):
                        for j in range(roue):
                            joueurs[i]["main"].append(cartes.pop())
                else:
                    for i in range(roue):
                        joueurs[joueur_courant]["main"].append(cartes.pop())
            if alea == 4:
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("Evènement Combinaison touche")
                combitouche = speed_test()
                if combitouche == False:
                    roue_touche = random.randint(2, 12)
                    for i in range(roue_touche):
                        joueurs[joueur_courant]["main"].append(cartes.pop())

            if alea==5:
                print("Evènement SWAP")
                regroupement=[]
                for i in range(len(joueurs)):
                    while joueurs[i]["main"]!=[]:
                        regroupement.append(joueurs[i]["main"][0])
                        joueurs[i]["main"].remove(joueurs[i]["main"][0])
                random.shuffle(regroupement)
                j=len(joueurs)-1
                while regroupement!=[]:
                    joueurs[j]["main"].append(regroupement[0])
                    regroupement.remove(regroupement[0])
                    j-=1
                    if j<0:
                        j=len(joueurs)-1


            if alea == 3:
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                for i in range(len(lst_joueurs)):
                    temp = lst_joueurs[joueur_courant]
                    temp = temp.split()
                    if temp[1] == "0":
                        temp[1] = "3"
                        temp[0] += " " + str(temp[1])
                        del (temp[1])
                        for j in range(len(temp)):
                            lst_joueurs[joueur_courant] = temp[j]
                        break
            if lst_joueurs[0][2] != "0":
                for i in range(len(lst_joueurs)):
                    temp = lst_joueurs[joueur_courant]
                    temp = temp.split()
                    temp[1] = str(int(temp[1]) - 1)
                    temp[0] += " " + str(temp[1])
                    del (temp[1])
                    for j in range(len(temp)):
                        lst_joueurs[joueur_courant] = temp[j]
                    break
                now = time.time()
                max_delay = now + 4

                while True:
                    print("Evènement TIME TIME")
                    print("La carte actuelle est :", defausse[-1])
                    print("Votre main est :", joueurs[joueur_courant]["main"])
                    carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                    if time.time() > max_delay:
                        print("Temps manqué")
                        carte_jouee = "p"
                        break
                    else:
                        break
            else:
                print("La carte actuelle est :", defausse[-1])
                print("C'est au tour de", joueurs[joueur_courant]["nom"])
                print("Votre main est :", joueurs[joueur_courant]["main"])
                now = time.time()
                max_delay = now + 15
                while True:
                    carte_jouee = input("Entrez le nom de la carte que vous voulez jouer (ou 'p' pour passer) : ")
                    if time.time() > max_delay:
                        print("Temps manqué")
                        carte_jouee = "p"
                        break
                    else:
                        break
            if carte_jouee == "SWAP":
                nom_swapp = input("Donnez le nom du joueur : ")
                for i in range(len(joueurs)):
                    if joueurs[i]["nom"] == nom_swapp:
                        temp = joueurs[joueur_courant]["main"]
                        joueurs[joueur_courant]["main"] = joueurs[i]["main"]
                        joueurs[i]["main"] = temp
                        if sens < 0:
                            joueur_courant -= 1
                        elif sens > 0:
                            joueur_courant += 1
                        break
            elif carte_jouee == "p":
                joueurs[joueur_courant]["main"].append(cartes.pop())
                if sens < 0:
                    joueur_courant -= 1
                elif sens > 0:
                    joueur_courant += 1

            elif carte_jouable(carte_jouee):
                jouer_carte(joueurs[joueur_courant], carte_jouee)
                if len(joueurs[joueur_courant]["main"]) == 0:
                    print(joueurs[joueur_courant]["nom"], "a gagné !")
                    return joueurs[joueur_courant]["nom"]
                elif carte_jouee.split()[1] == "Inverse":
                    sens *= -1
                    if sens < 0:
                        joueur_courant -= 1
                    elif sens > 0:
                        joueur_courant += 1

                elif carte_jouee.split()[1] == "Passe":
                    if sens < 0:
                        joueur_courant -= 2
                    elif sens > 0:
                        joueur_courant += 2

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

                elif carte_jouee.split()[1] == "+4":
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
                    for i in range(4):
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
                elif carte_jouee.split()[1] == "+8":
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
                    for i in range(8):
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
                joueurs[joueur_courant]["main"].append(cartes.pop())
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

while True:
    print("------------------------------------------------------------------")
    print("Bienvenue sur UNO-PARTY")
    print("------------------------------------------------------------------")
    print("1)JOUER")
    print("2)QUITTER")
    print("------------------------------------------------------------------")
    choix=int(input("Choix : "))
    if choix==1:
        print("------------------------------------------------------------------")
        print("1)MODE HISTOIRE")
        print("2)MODE LIBRE")
        print("------------------------------------------------------------------")
        choix2=int(input("Choix : "))
        if choix2==1:
            histoire()
        elif choix2==2:
            print("------------------------------------------------------------------")
            print("1)Contre bot")
            print("2)Multijoueur")
            print("------------------------------------------------------------------")
            choix3=int(input("Choix : "))
            if choix3==1:
                nbr_bots=int(input("Choisir entre 1 et 4 bots : "))
                if nbr_bots<=0 or nbr_bots>4:
                    break
                else:
                    name=input("Nom joueur : ")
                    mode_libre_bots(name,nbr_bots)
            if choix3==2:
                mode_libre()
        else:
            break
    else:
        break





