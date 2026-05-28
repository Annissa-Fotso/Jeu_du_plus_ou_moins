historique_session = []
def menu_mode ():
    print ("")
    print ("BIENVENU AU JEU DU PLUS OU MOINS")
    print ("")
    print ("1. Nombre mystere")
    print ("2. Annee mystere")
def menu_niveau ():
    print ("1. Facile (tentatives illimitees)")
    print ("2. Moyen (10 tentatives)")
    print ("3. Difficile (5 tentatives)")
    print ("4. Divin (3 tentatives)")
def afficher_historique ():
    print ("")
    print ("Historique de la partie")
    print ("")
    if len (historique_session) == 0 :
        print ("Historique vide")
        return
    else :
        for partie in historique_session:
            print (partie)   
while True :
<<<<<<< HEAD
=======
<<<<<<< HEAD
    menu_niveau()
    choix_menu = input("Choisissez un niveau de 1 à 4 : ")
    if choix_menu == "1":
        niveau = "Facile"
        tentative_max = None
        print ("Vous avez choisi le niveau facile")
        break
    elif choix_menu == "2":
        niveau = "Moyen"
        tentative_max = 10
        print ("Vous avez choisi le niveau Moyen")
        break
    elif choix_menu == "3":
        niveau = "Difficile"
        tentative_max = 5
        print ("Vous avez choisi le niveau difficile")
        break
    elif choix_menu == "4":
        niveau = "Divin"
        tentative_max = 3
        print ("Vous avez choisi le niveau Divin")
        break
    else:
        print ("Entree invalide, choisissez un nombre entre 1 et 4")

if mode == "1":
    nombre_secret = 100
    tentative_utilisee = 0
    print ("")
    print ("Devinez le nombre")
    print ("")
    print ("Le nombre mystère est entre 1 et 100 ")
    while True: 
        if tentative_max is not None:
            restante = tentative_max - tentative_utilisee
            print ("Tentatives restantes : ", restante )
            saisie = input ("Entrez votre réponse : ")
            try:
                reponse = int (saisie)
            except:
                print ("Entree invalide, veuillez saisir un nombre entier . ")
                continue
        tentative_utilisee = tentative_utilisee + 1
        if reponse == nombre_secret :
            print ("")
            print (" BINGO!! Felicitations")
            print ("Vous avez trouvé en ", tentative_utilisee , "tentative(s)" )
            break
        elif  reponse < nombre_secret :
            print ("C'est plus grand")
        else:
            print ("C'est plus petit")

        if tentative_max is not None :
            if tentative_utilisee >= tentative_max :
                print ("")
                print ("Dommage!! vous avez epuise vos", tentative_max , "tentative(s)")
                print ("Vous avez perdu!! la bonne reponse etait : ", nombre_secret )
                break
elif mode == "2":
    annee_secrete = 2022
    tentative_utilisee = 0
    print ("")
    print ("Devinez l'annee")
    print ("")
    print ("l'annee mystere est entre 1990 et 2025")
    while True: 
        if tentative_max is not None:
            restante = tentative_max - tentative_utilisee
            print ("Tentatives restantes : ", restante )
            saisie = input ("Entrez votre réponse : ")
            try:
                reponse = int (saisie)
            except:
                print ("Entree invalide, veuillez saisir un nombre entier . ")
                continue
        tentative_utilisee = tentative_utilisee + 1
        if reponse == annee_secrete:
            print ("")
            print (" BINGO!! Felicitations")
            print ("Vous avez trouvé en ", tentative_utilisee , "tentative(s)" )
            break
        elif  reponse < annee_secrete :
            print ("C'est plus grand")
        else:
            print ("C'est plus petit")

        if tentative_max is not None :
            if tentative_utilisee >= tentative_max :
                print ("")
                print ("Dommage!! vous avez epuise vos", tentative_max , "tentative(s)")
                print ("Vous avez perdu!! la bonne reponse etait : ", annee_secrete )
                break
=======
>>>>>>> feature/resolution_conflit

    while True :
        menu_mode ()
        mode = input ("choisissez votre mode de jeu : " )
        if mode == "1":
            print ("Vous avez choisi le mode Nombre mystère")
            break
        elif mode == "2":
            print ("Vous avez choisi le mode Annee mystere")
            break
        else :
            print ("Entree invalide, entrez 1 ou 2")
       
    while True :
        menu_niveau()
        choix_menu = input("Choisissez un niveau de 1 à 4 : ")
        if choix_menu == "1":
            niveau = "Facile"
            tentative_max = None
            print ("Vous avez choisi le niveau facile")
            break
        elif choix_menu == "2":
            niveau = "Moyen"
            tentative_max = 10
            print ("Vous avez choisi le niveau Moyen")
            break
        elif choix_menu == "3":
            niveau = "Difficile"
            tentative_max = 5
            print ("Vous avez choisi le niveau difficile")
            break
        elif choix_menu == "4":
            niveau = "Divin"
            tentative_max = 3
            print ("Vous avez choisi le niveau Divin")
            break
        else:
            print ("Entree invalide, choisissez un nombre entre 1 et 4")

    if mode == "1":
        nombre_secret = 100
        tentative_utilisee = 0
        print ("")
        print ("Devinez le nombre")
        print ("")
        print ("Le nombre mystère est entre 1 et 100 ")
        while True: 
            if tentative_max is not None:
                restante = tentative_max - tentative_utilisee
                print ("Tentatives restantes : ", restante )
                saisie = input ("Entrez votre réponse : ")
                try:
                    reponse = int (saisie)
                except:
                    print ("Entree invalide, veuillez saisir un nombre entier . ")
                    continue
            tentative_utilisee = tentative_utilisee + 1
            if reponse == nombre_secret :
                print ("")
                print (" BINGO!! Felicitations")
                print ("Vous avez trouvé le nombre mystere en ", tentative_utilisee , "tentative(s)" )
                resultat = "GAGNE"
                partie = {
                "Mode" : mode ,
                "Niveau": niveau,
                "Tentatives": tentative_utilisee,
                "Resultat": resultat,
                }
                historique_session.append(partie)
                afficher_historique ()
                break
            elif  reponse < nombre_secret :
                print ("C'est plus grand")
            else:
                print ("C'est plus petit")

            if tentative_max is not None :
                if tentative_utilisee >= tentative_max :
                    print ("")
                    print ("Dommage!! vous avez epuise vos", tentative_max , "tentative(s)")
                    print ("Vous avez perdu!! la bonne reponse etait : ", nombre_secret )
                    resultat = "PERDU"
                    partie = {
                    "Mode" : mode ,
                    "Niveau": niveau,
                    "Tentatives": tentative_utilisee,
                    "Resultat": resultat,
                    }
                    historique_session.append(partie)
                    afficher_historique ()
                    break
    elif mode == "2":
        annee_secrete = 2022
        tentative_utilisee = 0
        print ("")
        print ("Devinez l'annee")
        print ("")
        print ("l'annee mystere est entre 1990 et 2025")
        while True: 
            if tentative_max is not None:
                restante = tentative_max - tentative_utilisee
                print ("Tentatives restantes : ", restante )
                saisie = input ("Entrez votre réponse : ")
                try:
                    reponse = int (saisie)
                except:
                    print ("Entree invalide, veuillez saisir un nombre entier . ")
                    continue
            tentative_utilisee = tentative_utilisee + 1
            if reponse == annee_secrete:
                print ("")
                print (" BINGO!! Felicitations")
                print ("Vous avez trouvé l'annee mystere en ", tentative_utilisee , "tentative(s)" )
                resultat = "GAGNE"
                partie = {
                "Mode" : mode ,
                "Niveau": niveau,
                "Tentatives": tentative_utilisee,
                "Resultat": resultat,
                }
                historique_session.append(partie)
                afficher_historique ()
                break
            elif  reponse < annee_secrete :
                print ("C'est plus grand")
            else:
                print ("C'est plus petit")

            if tentative_max is not None :
                if tentative_utilisee >= tentative_max :
                    print ("")
                    print ("Dommage!! vous avez epuise vos", tentative_max , "tentative(s)")
                    print ("Vous avez perdu!! la bonne reponse etait : ", annee_secrete )
                    resultat = "PERDU"
                    partie = {
                    "Mode" : mode ,
                    "Niveau": niveau,
                    "Tentatives": tentative_utilisee,
                    "Resultat": resultat,
                    }
                    historique_session.append(partie)
                    afficher_historique ()
                    break
        print ("")
        print("1. Rejouer ")
        print ("2. Quitter")
        print ("")
        while True:
            fin = input("Votre choix : ")
            if fin == "1":
                print("Nouvelle partie !")
                break
            elif fin == "2":
                print("Merci d'avoir joue ! A bientot !")
                exit()      # quitte le programme
            else:
                print("Entree invalide, entrez 1 ou 2.")




<<<<<<< HEAD
=======
>>>>>>> 9ae094d (feat : historique de la partie et option rejouer ou quitter)
>>>>>>> feature/resolution_conflit


   


    