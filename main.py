def afficher_menu ():
    print ("")
    print (" JEU DU PLUS OU MOINS")
    print ("")
    print ("Choisissez votre mode de jeu")
    print ("1. Nombre mystere")
    print ("2. Annee mystere")
afficher_menu ()
choix_mode = input ("Entrez votre choix (1 ou 2) :  ")
if choix_mode == "1":
    print ("Vous avez choisi le mode Nombre mystere")
elif choix_mode == "2":
    print ("Vous avez choisi le mode Annee mystere")
else:
    print ("Choix invalide, veuillez relancer le programme et taper 1 ou 2 ")
