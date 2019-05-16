# -*- coding: cp1252 -*-
import arcpy
from arcpy import *
arcpy.env.workspace="U:/P3/Python/données TP1/TP2.gdb"
mes_classes=arcpy.ListFeatureClasses("*")
nb_classes=len(mes_classes)
print(nb_classes, ' classes')
rep=input("Veux tu regarder tes classes ?")

while rep.lower()=="oui":
    print("Voici la liste des classes d'entités disponibles")
    for i in mes_classes:
        print(i)
        
    ma_classe=input("Dans quelle classe voulez-vous vous travailler ?")
    while ma_classe not in mes_classes:
        ma_classe=input("Cette classe n'existe pas. Dans quelle classe voulez-vous travailler ?")
    nb_aff = input("Vous voulez travaillez sur la classe "+ma_classe+", combien de ligne voulez-vous visualiser ?")
    while nb_aff<1:
        nb_aff = input("Ceci n'est pas un nombre, essayez encore")
    
    curseur = arcpy.SearchCursor(ma_classe)
    liste_champ=arcpy.ListFields(ma_classe)
    nb_champ=len(liste_champ)
    tab_champ = []
    for i in liste_champ:
        tab_champ.append(i.name)
    for j in range (nb_aff):
        ligne = curseur.next()
        for k in range(nb_champ):
            champ = tab_champ[k]
            print(ligne.getValue(champ))
    rep = input("Tu veux continuer ?")
        
        
    
