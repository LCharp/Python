 ##############################
#     TP2 Python sous Arcgis   #
#  Espaces de Travail w/ IDLE  #
 ##############################
#      Version complète        #
#        Avec Fonctions        #
# tp2_idle_python_fonctions.py #
 ##############################

# -*- coding: cp1252 -*-
import arcpy
from arcpy import env
from tp2_idle_python_fonctions import *

arcpy.env.workspace="C:/charpentier/Arcgis_Python/TP3/tp3_gdb.gdb"
ma_bdd=arcpy.env.workspace
mes_classes=arcpy.ListFeatureClasses("*")
nb_classes=len(mes_classes)
liste_type= ("STRING", "TEXT", "SHORT",  "DOUBLE", "FLOAT ")
print("il y a "+str(nb_classes)+ " classes, dans notre base de donnees "+str(ma_bdd))

rep=input("Veux tu ajouter un champ ?")
while rep.lower()=="oui":
     ma_classe =  verif_classe()
     for i in mes_classes:
          print(i)
     ma_classe=input("Dans quelle classe veux-tu ajouter le champ ")
     while ma_classe not in mes_classes:
           ma_classe=input("Cette classe n'existe pas. Dans quelle classe veux-tu ajouter le champ ")
     nv_champ=input("Donne le nom du champ a rajouter " )
     liste_champ=arcpy.ListFields(ma_classe)
     tab_champ=[]
     for i in liste_champ:
          tab_champ.append(i.name)
     while nv_champ in tab_champ:
               nv_champ=input("Ce champ existe deja. Donne le nom du champ a rajouter " )
     nv_type=input("Quel est le type de ton champ, tu peux choisir entre :  " + str(liste_type))
     while nv_type not in liste_type:
          nv_type=input("Ce type n'existe pas. Quel est le type de ton champ ?")
     arcpy.AddField_management(ma_classe,nv_champ,nv_type)
     remp=input("Souhaites tu remplir le champ  "+nv_champ+" ? ")
     if remp.lower()=="oui":
          formule=input("entre la formule ou la valeur pour ce nouveau champ ")
          print(formule)
          if nv_type in ("STRING","TEXT"):
               arcpy.CalculateField_management(ma_classe,nv_champ,"'"+formule+"'","PYTHON")
          else:
               arcpy.CalculateField_management(ma_classe,nv_champ,formule,"PYTHON")
     print("ton champ a ete rajoute dans la classe d'entite "+ma_classe)
     liste_champ=arcpy.ListFields(ma_classe)
     for i in liste_champ:
          print("voici le nom du champ "+i.name+" voici son type "+i.type)
     rep=input("Veux tu continuer a ajouter un champ ?")
