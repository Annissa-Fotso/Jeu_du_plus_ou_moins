def menu_mode ():
    print ("")
    print ("BIENVENU AU JEU DU PLUS OU MOINS")
    print ("")
    print ("1. Nombre mystere")
    print ("2. Annee mystere")
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

def menu_niveau ():
    print ("1. Facile (tentatives illimitees)")
    print ("2. Moyen (10 tentatives)")
    print ("3. Difficile (5 tentatives)")
    print ("4. Divin (3 tentatives)")
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

   


    