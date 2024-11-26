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


# Exemple de test
test = genere_list_insert("genial", 100)
print(test)
