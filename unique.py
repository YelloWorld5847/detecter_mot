def supprimer_doublon(chaine):

    for i in range(len(chaine)):  # parcourire chaque caractère de chaine où 'i' est un indice
        caractere_list = []

        unique_boucle = True
        j = 0
        while unique_boucle:
            if i + j <= len(chaine) - 1:  # verifier si il y à la place
                caractere_list.append(chaine[i + j])
                j += 1
                if len(set(caractere_list)) > 1:
                    caractere_list.pop()
                    unique_boucle = False
            else:
                unique_boucle = False


        unique_element = set(caractere_list)
        if len(unique_element) == 1 and len(caractere_list) >= 3:
            for a in range(len(caractere_list) - 2):
                indice = i + 2
                chaine = chaine[:indice] + chaine[indice + 1:]
    print(chaine)
    return chaine