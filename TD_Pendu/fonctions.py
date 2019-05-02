def verif_joue(joue):
        while joue.lower() !=  "o" and joue != "n":
                joue = input("(O = Oui| N = Non)")
        return joue  

def verif_nouveau(nouveau):
        while nouveau.lower() !=  "o" and nouveau != "n":
                nouveau = input("(O = Oui | N = Non)")
        return nouveau

def verif_taille_pseudo(pseudo):
        while len(pseudo) <= 8:
                print("La longueur du pseudo doit être d'au moins 8 caractères! ")
                pseudo = input("Ressaisir votre pseudo ")
        return pseudo

def verif_dispo_pseudo(valide_pseudo):
        while valide_pseudo == True:
                print("Pseudo déja utilisé, veuillez un pseudo différent ")
                pseudo = input("Choisir un pseudo: ")
                
                if pseudo in liste_joueurs :
                    valide_pseudo = True
                else:
                    valide_pseudo = False
        return valide_pseudo


def verif_choix_niv(niveau):
        while niveau != "1" and niveau != "2" and niveau !="3":
                niveau = input("Veuillez selectionner un niveau entre 1 et 3 !")
        return niveau
