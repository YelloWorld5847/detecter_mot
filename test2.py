# Exemple de chaîne avec des espaces
chaine = "geeeeniallll"

caractere_list = []

for i in range(len(chaine)):  # parcourire chaque caractère de chaine où 'i' est un indice
    caractere_list = []

    unique_boucle = True
    j = 0
    #for j in range(3):
    while unique_boucle:
        if i + j <= len(chaine) - 1:  # verifier si il y à la place
            caractere_list.append(chaine[i + j])
            j += 1
            print(f"caractere_list : {caractere_list}")
            if len(set(caractere_list)) > 1:
                caractere_list.pop()
                print(f"caractere_list : {caractere_list}")
                unique_boucle = False
                print("fin de la boucle")
        else:
            unique_boucle = False

    print(f"caractere_list : {caractere_list}")

    unique_element = set(caractere_list)
    if len(unique_element) == 1 and len(caractere_list) >= 3:
        for a in range(len(caractere_list) - 2):
            indice = i + 2
            chaine = chaine[:indice] + chaine[indice + 1:]
print(chaine)





