from itertools import combinations

# Fonction pour générer des combinaisons avec des indices à remplacer par des `*`
def generate_combinations(word, num_stars, v):
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
            chars[i] = v

        # Joindre les caractères ensemble pour obtenir le nouveau mot
        replaced_word = ''.join(chars)

        # Ajouter le résultat à la liste des résultats
        results.append(replaced_word)

    return results


variation = ("1234567890AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn"
             ",;:!?./§&é(-è_çà)=+°]@^|[{}€><²*%ùµ¨£$¤ ")

mot = input("mot à détécter :")
sortir = False
while not sortir:
    pourcentage = input("marge de detection (en %) :")

    valide = True
    if len(pourcentage) >= 3:
        print("Il ne doit pas avoir plus de 3 caractères")
        valide = False

    for caractère in pourcentage:
        if caractère not in "1234567890":
            print("Veuillez entrer uniquement des chiffres ")
            valide = False

    if valide == True:
        sortir = True
    else:
        sortir = False

pourcentage = int(pourcentage)

marge = int(pourcentage / 100 * len(mot))
print(f"marge = {marge}")
if pourcentage >= 20 and marge == 0:
    marge = 1
    print(f"marge = {marge}")
else:
    print("c'est bon pour marge")

combination_lists = []
for j in range(marge):
    print("marge =", j + 1)
    for v in variation:
        # Ajouter les combinaisons de chaque nombre d'étoiles à la liste de listes
        combination_lists.extend(generate_combinations(mot, j + 1, v))

combination_lists.append(mot)
print(combination_lists)

for mot_de_liste in combination_lists:
    if mot_de_liste in "bonjours le 1uck":
        print("oui")
        print(f"mot de liste = {mot_de_liste}")

