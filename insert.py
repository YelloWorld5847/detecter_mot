from itertools import combinations


def genere_list_insert(mot, pourcentage):
    def insert_asterisks(word, num_asterisks):
        # Longueur du mot
        length = len(word)

        # Vérification du nombre d'astérisques
        if num_asterisks > length:
            raise ValueError("Le nombre d'astérisques à insérer ne peut pas dépasser la longueur du mot + 1.")

        # Liste pour stocker les résultats
        results = []

        # Positions d'insertion possibles, incluant la fin du mot
        possible_positions = list(range(1, length + 1))  # Du 1er caractère jusqu'à la fin du mot

        # Générer des combinaisons pour les indices d'insertion
        insertion_combinations = combinations(possible_positions, num_asterisks)

        # Parcourir chaque combinaison d'insertion
        for combination in insertion_combinations:
            # Créer une liste de caractères du mot
            chars = list(word)

            # Insérer les astérisques aux positions correspondantes
            for idx, position in enumerate(sorted(combination)):
                chars.insert(position + idx, "*")  # + idx car la liste s'allonge avec les insertions

            # Joindre les caractères pour former la nouvelle chaîne
            new_word = ''.join(chars)

            # Ajouter le résultat à la liste des résultats
            results.append(new_word)

        return results

    # Calculer la marge maximale pour le nombre d'astérisques
    marge = int(pourcentage / 100 * (len(mot) + 1))  # Prendre en compte l'option d'ajout à la fin
    if marge > len(mot):
        marge = len(mot)  # Assurez-vous que le nombre d'astérisques ne dépasse pas la longueur du mot

    # Liste pour stocker toutes les combinaisons
    combination_lists = []
    for j in range(1, marge + 1):  # Commence à 1 pour éviter d'insérer avant le premier caractère
        # Ajouter les combinaisons de chaque nombre d'étoiles à la liste de listes
        combination_lists.extend(insert_asterisks(mot, j))

    return combination_lists

test = genere_list_insert("bon", 100)
test2 = genere_list_insert("b*o*n", 100)

def liste_valide(test2):
    test2 = list(set(test2))
    print(test2)

    new_list = []

    print(test2)
    for chaine in test2:
        #chaine = "geeeeeeeeeeenial"
        #print("\n")
        #print(f"chaine ------------{chaine}--------------------------------------------------")

        caractere_list = []

        garder = True

        for i in range(len(chaine)):  # parcourire chaque caractère de chaine où 'i' est un indice
            caractere_list = []

            unique_boucle = True
            j = 0
            #for j in range(3):
            while unique_boucle:
                if i + j <= len(chaine) - 1:  # verifier si il y à la place
                    caractere_list.append(chaine[i + j])
                    j += 1
                    #print(f"caractere_list append : {caractere_list}")
                    if len(set(caractere_list)) > 1:
                        caractere_list.pop()
                        #print(f"caractere_list supprimer : {caractere_list}")
                        unique_boucle = False
                        #print("fin de la boucle")
                else:
                    unique_boucle = False
                    #print("fin de la boucle")

            #print(f"caractere_list : {caractere_list}")

            unique_element = set(caractere_list)


            if len(unique_element) == 1 and len(caractere_list) >= 3:

                garder = False


        if garder == True:
            new_list.append(chaine)

    print(f"new liste")
    print(new_list)
    return new_list
