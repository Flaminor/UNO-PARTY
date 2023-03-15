import random
import time

def play_key_sequence():
    #Fonction qui donne des touches aléatiores à entrer
    
    #Les lettres à entrer
    valid_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']

    #Nombre de lettres à entrer
    num_keys = random.randint(5, 7)

    #Limite de temps
    time_limit = num_keys+5

    #Séries de lesttres à entrer
    key_sequence = [random.choice(valid_keys) for _ in range(num_keys)]

    # Ask the player to enter the key sequence within the time limit
    print(f"Entrez ces {num_keys} lettres et/ou chiffres en {time_limit} secondes:")
    print(" ".join(key_sequence))

    start_time = time.time()
    for i in range(num_keys):
        key = input()
        if key != key_sequence[i]:
            print("Mauvaise lettre! Game over.")
            break
        if time.time() - start_time > time_limit:
            print("Temps écoulé! Game over.")
            break
    else:
        print("Félicitations! Tu as réussi à faire la bonne combinaison de touches.")

play_key_sequence()
