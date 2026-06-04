import random

def afficher_historique (historique_session):
    print ("")
    print ("Historique de la partie")
    print ("")
    if len (historique_session) == 0 :
        print ("Historique vide")
        return
    for partie in historique_session:
        print (partie) 
def jouer_annee(niveau, tentative_max,historique_session):
    annee_secrete = random.randint(1990, 2025)
    tentative_utilisee = 0
    print ("")
    print ("l'annee mystere est entre 1990 et 2025")
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
        if reponse == annee_secrete:
            print ("")
            print (" BINGO!! Felicitations")
            print ("Vous avez trouvé l'annee mystere en ", tentative_utilisee , "tentative(s)" )
            partie = {
                "Mode"      : "Annee mystere",
                "Niveau"    : niveau,
                "Tentatives": tentative_utilisee,
                "Resultat"  : "GAGNE",
            }
            historique_session.append(partie)
            afficher_historique(historique_session)
            return 
        elif  reponse < annee_secrete :
            print ("C'est plus grand")
        else:
            print ("C'est plus petit")

        if tentative_max is not None :
            if tentative_utilisee >= tentative_max :
                print ("")
                print ("Dommage!! vous avez epuise vos", tentative_max , "tentative(s)")
                print ("Vous avez perdu!! la bonne reponse etait : ", annee_secrete )
                partie = {
                "Mode"      : "Annee mystere",
                "Niveau"    : niveau,
                "Tentatives": tentative_utilisee,
                "Resultat"  : "PERDU",
                }
                historique_session.append(partie)
                afficher_historique(historique_session)
                return

