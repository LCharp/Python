# -*- coding: cp1252 -*-
import arcpy
from arcpy import env
arcpy.env.workspace="U:/Documents/python/données TP1/TP2.gdb"
ma_bdd=arcpy.env.workspace
mes_classes=arcpy.ListFeatureClasses("*")
nb_classes=len(mes_classes)
liste_type= ("STRING", "TEXT", "SHORT",  "DOUBLE", "FLOAT ")
print("Il y a "+str(nb_classes)+ " classes, dans notre base de donnees ")

rep=input("Veux tu visualiser des lignes ? ")
while rep.lower()=="oui":
     print("Voici la liste des classes d'entités disponibles")
     for i in mes_classes:
          print(i)
     ma_classe=input("De quelle classe veux-tu voir les lignes ? ")
     while ma_classe not in mes_classes:
           ma_classe=input("Cette classe n'existe pas. De quelle classe veux-tu voir les lignes ")
     nb_lignes=input("Combien de lignes veux tu voir ? ")

     curseur = arcpy.SearchCursor(ma_classe)
     liste_champ=arcpy.ListFields(ma_classe)
     nb_champ=len(liste_champ)
     tab_champ=[]
     for l in liste_champ:
              tab_champ.append(l.name)
     for i in range(nb_lignes):
          ligne = curseur.next()
          print("Ligne numero " + str(i+1))
          for j in range(nb_champ):
              champ = tab_champ[j]
              print(champ+":")
              print(ligne.getValue(champ))
     rep=input("Veux tu continuer à visualer un champ ?")
