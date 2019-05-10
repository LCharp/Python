# -*- coding: cp1252 -*-
import arcpy
from arcpy import env

def verif_class():
    
     mes_classes=arcpy.ListFeatureClasses("*")
     print("Voici la liste des classes d'entit�s disponibles")
     for i in mes_classes:
          print(i)
     nom_classe=input("Dans quelle classe veux-tu ajouter le champ ")
     while nom_classe not in mes_classes:
           nom_classe=input("Cette classe n'existe pas. Dans quelle classe veux-tu ajouter le champ ")
     return nom_classe           


def verif_champ(ma_classe):
     
     nv_champ=input("Donne le nom du champ � rajouter " )
     liste_champ=arcpy.ListFields(ma_classe)
     tab_champ=[]
     for i in liste_champ:
          tab_champ.append(i.name)
     while nv_champ in tab_champ:
          nv_champ=input("Ce champ existe d�j�. Donne le nom du champ � rajouter " )
     return nv_champ

def verif_champ_existe(ma_classe):
     
     nv_champ=input("Donne le nom du champ � supprimer " )
     liste_champ=arcpy.ListFields(ma_classe)
     tab_champ=[]
     for i in liste_champ:
          tab_champ.append(i.name)
     while nv_champ not in tab_champ:
          nv_champ=input("Ce champ n'existe pas. Donne le nom du champ � supprimer " )
     return nv_champ         
