from itertools import combinations

def genere_list(mot, pourcentage):
    # Fonction pour générer des combinaisons avec des indices à remplacer par des `*`
    def generate_combinations(word, num_stars):
        # Obtenir la longueur du mot
        length = len(word)

        # Liste de résultats pour les combinaisons générées
        results = []

        # Générer des indices de toutes les combinaisons possibles
        indices_combinations = combinations(range(length), num_stars)

        # Pour chaque combinaison d'indices
        for indices in indices_combinations:
            # Créer une liste de caractères du mot
            chars = list(word)

            # Remplacer les indices par des `*`
            for i in indices:
                chars[i] = "*"

            # Joindre les caractères ensemble pour obtenir le nouveau mot
            replaced_word = ''.join(chars)

            # Ajouter le résultat à la liste des résultats
            results.append(replaced_word)

        return results


    pourcentage = int(pourcentage)

    marge = int(pourcentage / 100 * len(mot))

    if pourcentage >= 20 and marge == 0:
        marge = 1

    combination_lists = []

    for j in range(marge):
        # Ajouter les combinaisons de chaque nombre d'étoiles à la liste de listes
        combination_lists.extend(generate_combinations(mot, j + 1))

    return combination_lists

print(genere_list("testeeee", 99))