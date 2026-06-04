from nombre_mystere import jouer_nombre
from annee_mystere import jouer_annee
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

while True :

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
        jouer_nombre(niveau, tentative_max, historique_session)
    elif mode == "2":
        jouer_annee(niveau , tentative_max , historique_session)
    
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





   


    