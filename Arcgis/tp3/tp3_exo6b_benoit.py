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

wk_couche=input("Dans quelle couche veux tu travailler : ? ")

curseur = arcpy.SearchCursor(wk_couche)
nb_tot = 0
for ligne in curseur:
    nb_tot += 1
del curseur



liste_field = []
liste_field_classe = arcpy.ListFields(classe)

for field in liste_field_classe:
    print(field.name+" "+field.type)

    if field.type not in ("Geometry","OID"):
        liste_field.append(field.name)

print(liste_field)


valeur = ""
w_champ=input("Sur quel champ se porte le critère ? (saisir 'AUCUN' si pas de critère) ")

if w_champ.lower()!="aucun":
    curseur = arcpy.SearchCursor(wk_couche,"",None,w_champ)
    for i in range(nb_tot):
        ligne = curseur.next()
        print ligne.getValue(w_champ)
    del ligne, curseur

    w_critere=input("Quel est le critere ? ")
    valeur = w_champ+w_critere
    
curseur = arcpy.SearchCursor(wk_couche,valeur)

res_ligne = "Num"
for field in liste_field:
        res_ligne = res_ligne + " "+ field
print(res_ligne)

cpt=1
for ligne in curseur:
    res_ligne = str(cpt)
    for field in liste_field:
        res_ligne = res_ligne + " "+ str(ligne.getValue(field))
    print(res_ligne)
    cpt+=1
    
del ligne, curseur

