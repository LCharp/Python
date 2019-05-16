# -*- coding: cp1252 -*-
import arcpy
from arcpy import env

arcpy.env.workspace="U:/Documents/LP/P3/python/SEANCE3/tp2.gdb"
ma_bdd=arcpy.env.workspace
mes_classes=arcpy.ListFeatureClasses("*")

rep = input ("Veux tu visualiser des lignes dans une classe d'entité ?")

if rep.lower()=="oui":

    print("Voici les classes disponibles : " + str(mes_classes))

    rep0= input("Quelle classe veux tu ?")
    rep2=input("Combien de lignes veux tu visualiser ?")

    liste_champ = arcpy.ListFields(rep0)

    for i in liste_champ :
        print (i.name)
       
    rep3= "oui"
    champ = ""
    
    while rep3.lower() =="oui":        

        if champ=="":
            rep4=input ("Renseigne un autre champs? ")
            champ = rep4
            rep3=input ("Tu veux renseigner un autre champs ? ")
        else :
            rep4=input ("Renseigne un autre champs? ")
            champ = champ + ";" + rep4
            rep3=input ("Tu veux renseigner un autre champs ? ")

    
    i = 0
    print (champ)

    rep5= input ("Veux renseigner un critère de tri ? ")

    if rep5.lower() == "oui":
        rep6 = input("Renseigne le champ de tri ")
        rep7 = input("Ascendant (A) / Descendant (D) ?")

        critere = rep6 + " "+ rep7
        
    curseur1 = arcpy.SearchCursor(rep0,"",None,champ,critere)   
    
    for i in range (rep2):
        ligne = curseur1.next()
        nom = ligne.NOM
        pop = ligne.POP
        print (nom + " "+ str(pop))
            
        

else :
    print ("Ok bisous!")


rep8 = input("Est ce que tu veux modifier ces données ?")

if rep8.lower() == "oui":
    rep9 = input ("Sur quel champ porte ton critere de sélection ? ")
    rep10 = input ("quel est l'opérateur de comparaison (=/</>/!=)? ")
    rep11 = input ("Quel est le critere de selection ? ")
    rep12 = input ("Sur quel champ portera la modification ?")
    rep13 = input ("Quelle opération veux tu appliquer ? ")

    print ("\""+rep9+rep10+rep11+"\"")
      
    curseur2 = arcpy.UpdateCursor(rep0,"\""+rep9+rep10+rep11+"\"",None,rep12)
    ligne = curseur2.next()
    ligne.rep12 = ligne.rep12 + rep13
    curseur2.updateRow(ligne)
    
