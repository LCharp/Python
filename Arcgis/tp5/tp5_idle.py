#############################
#   TP3 Python sous Arcgis  #
#       TP5 Outil.doc       #
#############################

# => IDLE Python: Fichier Lignes.py

# -> Outil permettant de dupliquer une classe polygon en une classe polyligne
import arcpy
source = arcpy.GetParameterAsText(0) # Classe de polygones
spatialref = arcpy.Describe(source).SpatialReference
cible = arcpy.GetParameterAsText(1) # Classe des polylignes
curseur = arcpy.SearchCursor(source)
featureList = []
for ligne in curseur:
    polygone = ligne.Shape
    tableau = polygone.getPart(0)
    polyligne = arcpy.Polyline(tableau,spatialref)
    featureList.append(polyligne)
arcpy.CopyFeatures_management(featureList,cible)
del curseur, featureList,ligne,polygone,tableau,polyligne

# => Fenêtre Python de ArcMap

# ->Importer Boite à Outil
arcpy.ImportToolbox("C:/charpentier/Arcgis_Python/tp5","TP5")
