#############################
#   TP3 Python sous Arcgis  #
#     TP4 Extraction.doc    #
#############################

## => SUR ARCMAP

arcpy.env.workspace="C:/charpentier/Arcgis_Python/tp4/tp4.gdb"

# -> Selection par attribut sur une couche
arcpy.SelectLayerByAttribute_management("Commune_41","NEW_SELECTION","STATUT='Chef-lieu de pseudo-canton'")
#<Result 'Commune_41'>

# -> Déselectionner la selection
arcpy.SelectLayerByAttribute_management("Commune_41","CLEAR_SELECTION")

# -> Créer une couche temporaire
arcpy.MakeFeatureLayer_management("Commune_41","temp_com41")

# -> Selection sur la couche temporaire
arcpy.SelectLayerByAttribute_management("temp_com41","NEW_SELECTION","STATUT='Chef-lieu de pseudo-canton'")

# -> Créer une couche à partir d'une selection
arcpy.CopyFeatures_management("temp_com41","comm41_chef_lieu")

# -> Créer une table des ville > 5000hab (avec variables)
critere = "POPULATION>5"
source = "temp_com41"
destination = "com41_5"

arcpy.SelectLayerByAttribute_management(source,"NEW_SELECTION",critere)
arcpy.CopyFeatures_management(source,destination)

arcpy.SelectLayerByAttribute_management(source,"CLEAR_SELECTION")

# -> Selection par emplacement
# 1°) Créer une table temporaire
arcpy.MakeFeatureLayer_management("comm41_chef_lieu","temp_chl_41")
# 2°) SelectLayerByLocation_management
arcpy.SelectLayerByLocation_management("temp_chl_41","WITHIN","com41_5")
# 3°) Créer la couche de la séléction
arcpy.CopyFeatures_management("temp_chl_41","com41_chef_lieu_5")
# 4°) Deselectionner la couche source
arcpy.SelectLayerByAttribute_management("temp_chl_41","CLEAR_SELECTION")
