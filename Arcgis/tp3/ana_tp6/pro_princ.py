import arcpy
from arcpy import env
import sys
sys.path.append(r'W:\p3\python\tp3')
from A import vis
from B import modif
from C import sup
from D import ajout

#workspace
arcpy.env.workspace="W:/p3/python/tp1/tp2.gdb"

couches=arcpy.ListFeatureClasses("*")
#featuresclass
print ("Ton espace de travail contient les couches suivantes:")
for i in couches:
    print (i)

couche_travail=input("Dans quelle couche veux-tu travailler?")
for i in couches:
    if couche_travail != i:
        print ("Cette couche n'existe pas, ou l'écriture est erronée, recommences")
    else :
        rep=input("Si tu souhaites visualiser un certain nombre de lignes de "+couche_travail+" :tape A,si tu veux modifier des données de la couche: tape B, si tu veux supprimer des données tape C, si tu veux ajouter des données: tape D")
        if rep=="A":
            print(vis())
        elif rep=="B":
            print(modif())
        elif rep=="C":
            print(sup())
        elif rep=="D":
            print(ajout())     
        else:
            rep=input("Je ne comprends pas ta réponse, A,B,C ou D?")
           
            
                    
        
