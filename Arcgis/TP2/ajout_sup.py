# -*- coding: cp1252 -*-
import arcpy
from arcpy import env
from paquet_ajout import *
arcpy.env.workspace="U:/python/exotig2019/tp1/tp1/tp1.gdb"
ma_bdd=arcpy.env.workspace
mes_classes=arcpy.ListFeatureClasses("*")
nb_classes=len(mes_classes)
liste_type= ("STRING", "TEXT", "SHORT",  "DOUBLE", "FLOAT ")
print("il y a "+str(nb_classes)+ " classes, dans notre base de données "+str(ma_bdd))

rep=input("Veux tu ajouter un champ ?")
while rep.lower()=="oui":
     ma_classe=verif_class()
     nv_champ=verif_champ(ma_classe)
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
     print("ton champ a été rajouté dans la classe d'entité "+ma_classe)
     liste_champ=arcpy.ListFields(ma_classe)
     for i in liste_champ:
          print("voici le nom du champ "+i.name+" voici son type "+i.type)
     rep=input("Veux tu continuer à ajouter un champ ?")
rep=input("Veux tu supprimer un champ ?")
while rep.lower()=="oui":
     ma_classe=verif_class()
     champ_sup=verif_champ_existe(ma_classe)
     arcpy.DeleteField_management(ma_classe,champ_sup)
     rep=input("Veux tu continuer à supprimer un champ ?")
