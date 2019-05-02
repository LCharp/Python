import os
import sys
import csv
import random
from random import choice
import fonctions
from fonctions import *

pseudo = ""
joue = ""
nouveau = ""
nb_erreur_tot = 5
nb_erreur_cpt = 0
niveau = "0"
mot= "test"
liste_jeu = []
lettre = ""
lettre_joue = []
statut = False
replace = 0
indice_pseudo = 0


print("               ___________")
print(" _____________| Bienvenue |_____________")
joue = input("Voulez vous jouer? (O/N) ")

joue = verif_joue(joue)



if joue.lower() == "n":
    print('\n A Bientôt')
    
while joue.lower()== "o" :
    
    liste_jeu.clear()
    lettre_joue.clear()
    longueur_mot = 0
    score_partie = 0
    statut=False

    fic_joueur_r = open("joueur.txt","r")
    data_joueur = fic_joueur_r.read()
    fic_joueur_r.close()
    liste_joueurs = data_joueur.split('\n')
    
    fic_score_r = open("score.txt","r")
    data_score = fic_score_r.read()
    fic_score_r.close()
    liste_score = data_score.split('\n')
    
    if pseudo == "":
        
        print("\n")
        print("               ___________")
        print(" _____________| Connexion |_____________")
        nouveau = input ("Est-tu un nouveau joueur? (O/N) ")
        nouveau = verif_nouveau(nouveau)
        if nouveau.lower() == "o":
            print("\n Bienvenue dans le jeu du pendu !")
            pseudo = input("Veuillez choisir un pseudo pour l'inscription (Min. 8 carat.) ")
            pseudo = verif_taille_pseudo(pseudo)
            valide_pseudo=False
            if pseudo in liste_joueurs :
                valide_pseudo = True
            valide_pseudo = verif_dispo_pseudo(valide_pseudo)
            fic_joueur=open("joueur.txt","a")
            fic_joueur.write(pseudo+"\n")
            fic_joueur.close()
            score = 0
            print(' Votre pseudo est ' + pseudo+' et vous avez un score de '+ str(score))
      
        elif nouveau.lower() == "n":
            pseudo = input("Saisir votre pseudo : ")
            pseudo = verif_taille_pseudo(pseudo)
            trouve_pseudo=False
            if pseudo in liste_joueurs :
                trouve_pseudo = False
            else:
                trouve_pseudo = True
            while trouve_pseudo == True:
                print("Pseudo non trouvé! ")
                pseudo = input("Ressaisir votre pseudo ")
                if pseudo in liste_joueurs :
                    trouve_pseudo = False
                else:
                    trouve_pseudo = True               
            while (pseudo != liste_joueurs[indice_pseudo]) and (indice_pseudo< len(liste_joueurs)-1):
                            indice_pseudo+=1  
    if pseudo == liste_joueurs[indice_pseudo]:
        score=int(liste_score[indice_pseudo])
    print ("\n Votre pseudo est : " + pseudo + " et votre Score est de %s" % score)

    print("\n       ____________________________")
    print(" _____| Selection de la difficulté |____")
    niveau=input("| Facile = 1 | Normal = 2 | Difficile = 3 | ")
    niveau = verif_choix_niv(niveau)
    print("Le niveau choisi est : " + niveau)

    words = [mot.strip() for mot in open("niveau"+niveau+".txt","r")]
    mot = choice(words)
    liste_mot = list(mot)
    longueur_mot = len(mot)
    print("Le mot est long de %s" % longueur_mot + " Caractères")


    print("\n")
    print("                  _____")
    print(" ________________| Jeu |_________________")
    i=0
    while i < longueur_mot :
        liste_jeu.append("*")
        i = i + 1
    print(liste_jeu)
    lettre_joue.clear()
    
    while statut is False :
        print("______________________ \n")
        lettre = input("Donne une lettre : ")
        print("\n")
        while len(lettre) != 1 or not lettre.isalpha():
                print("Veuillez saisir qu'une seule lettre")
                lettre = input("Donne une lettre : ")
        while lettre in lettre_joue :
            print("Vous avez déjà joué cette lettre")
            lettre = input("Choisir une nouvelle lettre: ")          
             
        lettre_joue.append(lettre)

        if lettre in liste_mot :
            print("La lettre est présente dans le mot !")
            replace = liste_mot.index(lettre)
            liste_jeu[replace] = lettre
            score_partie = score_partie+1
            print(liste_jeu)
        else :
            print("Cette lettre n'est pas présente dans le mot")
            nb_erreur_cpt = nb_erreur_cpt + 1

        print("\n")
        print("Les lettres déjà utilisées sont : ")
        print(lettre_joue)
        nb_erreur = nb_erreur_tot - nb_erreur_cpt
        print("Vous avez fait %s" %nb_erreur_cpt + " erreurs.\nVous pouvez encore faire %s" % nb_erreur + " erreurs.")

 
        while score_partie == longueur_mot :
            statut = True
            
            if score == 0:
                    score = score + 1
                    fic_joueur=open("score.txt","a")
                    fic_joueur.write(str(score))
                    fic_joueur.close()
                    score_partie = 0
            else:
                fic_score1=open("score.txt","r")
                data_score1=fic_score1.read()
                fic_score1.close()
                lst_score=data_score1.split('\n')
                lst_score[indice_pseudo] = int(lst_score[indice_pseudo])+1
                fic_score2=open("score.txt","w")
                i=0
                score = score + 1
                while i < len(lst_score):
                    fic_score2.write(str(lst_score[i])+"\n")
                    i = i+1
                fic_score2.close()
                score_partie = 0
            print("\n")
            print("              ____________")
            print(" ____________| Victoire ! |_____________")
            print("Vous avez gagné !!!")
            print("Le mot était : "+mot)
            print("Vous avez gagné 1 point, votre score total : %s" % score)

            
        while nb_erreur_cpt == nb_erreur_tot :
            statut = True
            print("\n")
            print("              ____________")
            print(" ____________| Défaite !! |_____________")
            print("Vous avez perdu !!!")
            print("Le mot était : "+mot)
            print("Vous n'avez pas gagné de point, votre score total : %s" % score)      
            nb_erreur_cpt = 0

    print("\n")
    print("              ____________")
    print(" ____________| On rejoue? |_____________")
    joue = input("Voulez vous rejouer? (O/N) ")
    while joue.lower() !=  "o" and joue != "n":
        joue = input("(O = Oui| N = Non)")
    if joue == "o":
        print('\n*************** Restart ***************')
    elif joue == "n":
        print('\n A Bientôt')
