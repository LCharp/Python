# -*- coding: cp1252 -*-
import arcpy
from arcpy import env

arcpy.env.workspace="C:/charpentier/Arcgis_Python/TP4/tp4.gdb"

ville = input("Choisir une ville : ")
print ville

nom_couche = input("Comment voulez vous appeler votre couche?")
print nom_couche
mes_couches = arcpy.ListFeatureClasses("*")
while nom_couche in mes_classes:
    choix_couche = input ("Le nom de cette couche est déjà utilisée, voulez vous la re-créer?")
    if nom_couche == "O":
        arcpy.env.overwriteOutput="TRUE"
    else:
        nom_couche =
    

nom_couche_temp = "temp_"+nom_couche
print nom_couche_temp
curseur = arcpy.SearchCursor("Commune_41","NOM_COMM='"+ville+"'",None,"NOM_COMM ; CODE_ARR","CODE_ARR D")
ligne = curseur.next()
code_arr = ligne.getValue("CODE_ARR")
print code_arr
critere = "CODE_ARR='"+code_arr+"'"
print critere

arcpy.MakeFeatureLayer_management("Commune_41",nom_couche_temp)

arcpy.SelectLayerByAttribute_management(nom_couche_temp,"NEW_SELECTION","CODE_ARR='"+code_arr+"'")

arcpy.CopyFeatures_management(nom_couche_temp,nom_couche)

arcpy.SelectLayerByAttribute_management(nom_couche_temp,"CLEAR_SELECTION")

print "fini"
