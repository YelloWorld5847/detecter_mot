from mot_variation_def import genere_list
from insert import genere_list_insert, liste_valide
from unique import supprimer_doublon

def main():

    def detection(mot_liste, mot_detecter2, texte):

        for i in range(len(texte)):  # parcourire le numéro de position de chaque lettre
            for mot in mot_liste:
                #if texte[i] == mot[0]:  # si lettre en question = première lettre de mot
                test_lettre = 0
                for p in range(len(mot)):  # parcourire chaque position de mot
                    if len(texte) - 1 >= i + p:
                        if mot[p] == "*":
                            if texte[i + p] in variation:
                                test_lettre += 1
                            else:
                                break

                        else:

                            if texte[i + p] == mot[p]:  # tester pour chaque caractère si ils sont égaux ex : bon et bébé b == b ; o == é ; n == b  ect...
                                test_lettre += 1
                            else:
                                break
                if len(mot) == test_lettre:  # si à chaque fois ont à ajouter 1 le mot est trouver
                    mot_detecter2 += 1
                    break
        return mot_detecter2


    mots = input("mot à détécter (ex film, image) :")
    texte = input("texte :")
    texte = texte.lower()
    mots = mots.lower()
    print(f"texte : {texte}")
    chaine_sans_espaces = mots.replace(" ", "")
    mot_liste1 = chaine_sans_espaces.split(",")
    print(f"mot liste = {mot_liste1}")

    texte2 = supprimer_doublon(texte)

    sortir = False
    while not sortir:
        pourcentage = input("Marge de détection par remplacement (en %) :")

        if pourcentage == "":
            print("100%")
            pourcentage = 99
            sortir = True
        else:
            valide = True
            if len(pourcentage) >= 3:
                print("Il ne doit pas avoir plus de 3 caractères")
                valide = False

            for caractere in pourcentage:
                if caractere not in "1234567890":
                    print("Veuillez entrer uniquement des chiffres ")
                    valide = False

            if valide == True:
                sortir = True
            else:
                sortir = False

    sortir = False
    while not sortir:
        pourcentage_insert = input("Marge de détéction par insertion (en %) :")

        if pourcentage_insert == "":
            print("100%")
            pourcentage_insert = 100
            sortir = True
        else:

            valide = True
            chiffre = True
            for caractere in pourcentage_insert:
                if caractere not in "1234567890":
                    print("Veuillez entrer uniquement des chiffres ")
                    valide = False
                    chiffre = False
            if chiffre:
                pourcentage_insert = int(pourcentage_insert)
                if pourcentage_insert > 100:
                    print("Veuillez entrer un pourcentage inférieur ou égal à 100")
                    valide = False

            if valide == True:
                sortir = True
            else:
                sortir = False

    for mot1 in mot_liste1:
        mot_liste_remplace = genere_list(mot1, pourcentage)

        mot_liste_insert1 = genere_list_insert(mot1, pourcentage_insert)

        #mot_liste_insert = []
        #mot_liste_insert.extend(mot_liste_insert1)
        #new_liste_insert = liste_valide(mot_liste_insert)

        #mot_liste = []
        #mot_liste.extend(mot_liste_remplace)
        #mot_liste.extend(mot_liste_insert1)
        mot_liste_insert1.append(mot1)
        #print(mot_liste)

        variation = ("azertyuiopqsdfghjklmwxcvbn1234567890"
                    ",;:!?./§&é(-è_çà)=+°]@^|[{}€><²*%ùµ¨£$¤ ")


        # le petit chat         i = 3
        #    petit              p = 0

        mot_detecter = 0

        # pour insert
        mot_detecter = detection(mot_liste_insert1, mot_detecter, texte2)

        variation = ("1234567890,;:!?./§&(-_)=+°]@^|[{}€><²*%µ¨£$¤ ")
        mot_detecter = detection(mot_liste_remplace, mot_detecter, texte)


        if mot_detecter == 0:
            if len(mot_liste1) == 1:
                print(f"{mots} n'est pas dans ce texte")
            else:
                print(f"{mots} ne sont pas dans ce texte")
        else:
            if len(mot_liste1) == 1:
                print(f"{mots} est dans ce texte {mot_detecter}")
            else:
                print(f"{mots} sont dans ce texte {mot_detecter}")




if "__main__":
    main()