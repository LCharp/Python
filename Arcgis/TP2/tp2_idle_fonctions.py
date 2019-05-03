 ############################
#    TP2 Python sous Arcgis  #
# Espaces de Travail w/ IDLE #
 ############################
#      Page des Fonctions    #
 ############################

# -*- coding: cp1252 -*-
import arcpy
from arcpy import env


def verif_classe ():
    arcpy.env.workspace="C:/charpentier/Arcgis_Python/TP3/tp3_gdb.gdb"
    mes_classe = arcpy.ListFeatureClasses("*")
    print("Voici la liste des classes d'entités disponibles")
    for i in mes_classes:
         print(i)
    nom_classe=input("Dans quelle classe veux-tu ajouter le champ ")
    while nom_classe not in mes_classes:
          nom_classe=input("Cette classe n'existe pas. Dans quelle classe veux-tu ajouter le champ ")
    return nom_classe

def verif_champ(ma_classe):
    arcpy.env.workspace="C:/charpentier/Arcgis_Python/TP3/tp3_gdb.gdb"
    liste_champ = arcpy.
