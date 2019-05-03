# -*- coding: cp1252 -*-
import arcpy
from arcpy import env
arcpy.env.workspace="U:/python/exotig2019/tp1/tp1/tp1.gdb"
ma_bdd=arcpy.env.workspace
mes_classes=arcpy.ListFeatureClasses("*")
nb_classes=len(mes_classes)
liste_type= ("STRING", "TEXT", "SHORT",  "DOUBLE", "FLOAT ")
print("il y a "+str(nb_classes)+ " classes, dans notre base de données "+str(ma_bdd))

rep=input("Veux tu ajouter un champ ?")
while rep.lower()=="oui":
     print("Voici la liste des classes d'entités disponibles")
     for i in mes_classes:
          print(i)
     ma_classe=input("Dans quelle classe veux-tu ajouter le champ ")
     while ma_classe not in mes_classes:
           ma_classe=input("Cette classe n'existe pas. Dans quelle classe veux-tu ajouter le champ ")
     nv_champ=input("Donne le nom du champ à rajouter " )
     liste_champ=arcpy.ListFields(ma_classe)
     tab_champ=[]
     for i in liste_champ:
          tab_champ.append(i.name)
     while nv_champ in tab_champ:
               nv_champ=input("Ce champ existe déjà. Donne le nom du champ à rajouter " )
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
