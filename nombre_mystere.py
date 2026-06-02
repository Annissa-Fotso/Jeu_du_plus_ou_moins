import random

def afficher_historique (historique_session):
    print ("")
    print ("Historique de la partie")
    print ("")
    if len (historique_session) == 0 :
        print ("Historique vide")
        return
    for partie in historique_session:
        print ("Mode :", partie ["Mode"])
        print ("Niveau :", partie ["Niveau"])
        print ("MTentatives :", partie ["Tentatives"])
        print ("Resultat :", partie ["Resultat"]) 
        print ("================================")                
def jouer_nombre (niveau, tentative_max, historique_session):
    nombre_secret = random.randint(1, 100)
    tentative_utilisee = 0
    print ("")
    print ("Nombre Mystere")
    print ("")
    print ("Le nombre mystère est entre 1 et 100 ")
    while True: 
        if tentative_max is not None:
            restante = tentative_max - tentative_utilisee
            print ("Tentatives restantes : ", restante )
            tentative_utilisee = tentative_utilisee + 1
            saisie = input ("Entrez votre réponse : ")
        try:
            reponse = int (saisie)
        except:
            print ("Entree invalide, veuillez saisir un nombre entier . ")
            continue
        if reponse == nombre_secret :
            print ("")
            print (" BINGO!! Felicitations")
            print ("Vous avez trouvé le nombre mystere en ", tentative_utilisee , "tentative(s)" )
            resultat = "GAGNE"
            partie = {
                "Mode"      : "Nombre mystère",
                "Niveau"    : niveau,
                "Tentatives": tentative_utilisee,
                "Resultat"  : resultat,
            }
            historique_session.append(partie)
            afficher_historique(historique_session)
            return
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
                "Mode"      : "Nombre mystère",
                "Niveau"    : niveau,
                "Tentatives": tentative_utilisee,
                "Resultat"  : resultat,
            }
            historique_session.append(partie)
            afficher_historique(historique_session)
            return

