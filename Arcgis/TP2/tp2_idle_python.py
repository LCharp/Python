 ############################
#    TP2 Python sous Arcgis  #
# Espaces de Travail w/ IDLE #
 ############################

# -*- coding: cp1252 -*-
import arcpy
from arcpy import env

arcpy.env.workspace="C:/charpentier/Arcgis_Python/TP3/tp3_gdb.gdb"
gdb = arcpy.env.workspace
mes_classes=arcpy.ListFeatureClasses("*")
nb_classes=len(mes_classes)
print ("Il y a " +str(nb_classes) + " classes dans notre gdb "+ str(gdb))
print ("Voici la liste des classes")

for classe in mes_classes:
    print(classe)

rep = input ("Voulez vous ajouter un champ? ")
while rep.lower == "oui":

    for classe in mes_classes:
        print(classe)

    ma_classe = input("Dans quelle classe veux-tu ajouter le champ?")
    while ma_classe not in mes_classes:
        ma_classe = input("Cette classe n'existe pas. Dans quelle classe veux-tu ajouter le champ?")

    nv_champ = input("Donne le nom du champà rajouter")
    nv_type= input("Quel est le type de ton champs? (STRING, SHORT, TEXT, INT, DOUBLE, FLOAT)")
    arcpy.AddField_management(ma_classe,nv_champ,nv_type)
    remp = input ("Veux tu remplir " + nv_champ + " ? ")

    if remp.lower == "oui":
        formule = input("rentre la formule de la valeur")
        arcpy.CalculateField_management(ma_classe,nv_champ,formule,"PYTHON")
    print ("Le champ" + nv_champ +" à été rajouté dans la classe "+ ma_classe)
    liste_champ = arcpy.ListFields(ma_classe)

    for champ in liste_champ:
        print ("Champ: " + champ.name + " Type: "+ champ.type)

    rep = input ("Veux tu acheter un nouveau champ? ")
