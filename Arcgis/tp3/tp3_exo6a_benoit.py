# -*- coding: cp1252 -*-
import arcpy
from arcpy import env

arcpy.env.workspace = "U:/Documents/ArcGIS/tp3.gdb" 
classes=arcpy.ListFeatureClasses("*")
print classes
nb_classes=len(classes)
print(str(nb_classes))

for classe in classes:
    print(classe)


wk_couche=input("Dans quelle couche veux tu travailler ? ")


liste_field = []
liste_field_classe = arcpy.ListFields(classe)

for field in liste_field_classe:
    print(field.name+" "+field.type)

    if field.type not in ("Geometry","OID"):
        liste_field.append(field.name)

print(liste_field)

##for field in liste_field:
##   print(field)


curseur = arcpy.SearchCursor(wk_couche)

nb_tot = 0
for ligne in curseur:
    nb_tot += 1
del curseur

print("La couche contient "+ str(nb_tot)+ " lignes.")
nb_ligne=input("Combien de ligne veux tu afficher ? ")

while nb_ligne > nb_tot:
    nb_ligne=input("Nombre demandé trop élevé, combien de ligne veux tu afficher ? ")

curseur = arcpy.SearchCursor(wk_couche)
cpt=1
for i in range(nb_ligne):
    print("------ Ligne : "+str(cpt)+" ------")
    ligne = curseur.next()

    for field in liste_field:
        print(ligne.getValue(field))

    cpt+=1

del ligne, curseur

