 ####################################
#       TP3 Python sous Arcgis       #
# Question 6 - Curseurs & fonctions  #
 ####################################
# -*- coding: cp1252 -*-


import arcpy
from arcpy import env
arcpy.env.workspace="C:/charpentier/Arcgis_Python/TP3/tp3_gdb.gdb"

choix_crud = input("Choisir entre : A = Read, B = Update, C = Delete, D = Insert | Votre choix = ")
while choix_crud == "A":
    mes_classes = arcpy.ListFeatureClasses("*")
    nb_classes = len(mes_classes)
    print("Il y a "+str(nb_classes) +" classes.")
    for i in mes_classes:
        print(i)
    choix_classe = input("Quelle classe voulez vous voir?")
    while choix_classe not in mes_classes:
        choix_classe = input("La classe n'existe pas, choisissez en un autre")
    curseur = arcpy.SearchCursor(choix_classe)
    affichage_ligne = input("Combien voulez vous voir de lignes? ")
    for i in range(affichage_ligne):
        ligne = curseur.next()
        nom = ligne.getValue("NOM")
        pop = ligne.POP
        print ("La commune ",nom," possede ",pop," habitants")
    continuer = input("Voulez vous choisir un autre champ?")
    if continuer == "oui":
        choix_crud == "A"
    else :
        choix_crud = input("Choisir entre : A = Read, B = Update, C = Delete, D = Insert | Votre choix = ")

while choix_crud == "B":
    mes_classes = arcpy.ListFeatureClasses("*")
    nb_classes = len(mes_classes)
    print("Il y a "+str(nb_classes) +" classes.")
    for i in mes_classes:
        print(i)
    choix_classe = input("Quelle classe voulez vous voir?")
    while choix_classe not in mes_classes:choix
        choix_classe = input("La classe n'existe pas, choisissez en un autre")
    curseur = arcpy.SearchCursor(choix_classe)
    liste_champs = arcpy.ListFields(choix_classe)
    for champ in liste_champs:
        print champ.name
    choix_champ = input("Quel champ voulez vous modifier? ")
    curseur = arcpy.searchCursor(choix_classe,"",None,choix_champ)
     for ligne in curseur:
         print ligne.getValue(choix_champ)
    continuer = input("Voulez vous choisir une autre classe?")
    if continuer == "oui":
        choix_crud == "B"
    else :
        choix_crud = input("Choisir entre : A = Read, B = Update, C = Delete, D = Insert | Votre choix = ")








while choix_crud == "C":
    mes_classes = arcpy.ListFeatureClasses("*")
    nb_classes = len(mes_classes)
    print("Il y a "+str(nb_classes) +" classes.")
    for i in mes_classes:
        print(i)
    choix_classe = input("Quelle classe voulez vous voir?")
    while choix_classe not in mes_classes:
        choix_classe = input("La classe n'existe pas, choisissez en un autre")
    choix_critere = input("Voulez vous ajouter un critère de selection?")






    continuer = input("Voulez vous choisir un autre champ?")
    if continuer == "oui":
        choix_crud == "A"
    else :
        choix_crud = input("Choisir entre : A = Read, B = Update, C = Delete, D = Insert | Votre choix = ")


















while choix_crud == "D":
    print ("choix D")
    continuer = input("Voulez vous choisir un autre champ?")
    if continuer == "oui":
        choix_crud == "A"
    else :
        choix_crud = input("Choisir entre : A = Read, B = Update, C = Delete, D = Insert | Votre choix = ")
