#############################
#   TP1 Python sous Arcgis  #
#       TP1 Document.doc    #
#############################

mxdtp1  = arcpy.mapping.MapDocument("CURRENT")
print(mxdtp1)
#<geoprocessing Map object object at 0x32EC85E0>

blocs_tp1 = arcpy.mapping.ListDataFrames(mxdtp1)
nb = len(blocs_tp1)
nb
#3

for i in blocs_tp1:
    print i.name," ",i.spatialReference.name
#France   NTF_Lambert_II_Carto
#Languedoc   NTF_Lambert_II_Carto
#Aude   NTF_Lambert_II

vue = mxd.activeView
print vue
#Aude

# -> Pour passer le projet en mise en page #
mxdtp1.activeView="PAGE_LAYOUT"

# -> Pour passer sur une couche en mode donnée #
mxdtp1.activeView="FRANCE" #FRANCE = nom du bloc

# -> Afficher les couches de tous les blocs du .mxd #
couches = arcpy.mapping.ListLayers(mxdtp1)
for couche in couches:
    descr = arcpy.Describe(couche)
    print couche.name," ",descr.spatialReference.name
#VILLE_10   NTF_Lambert_II_Carto
#REGIONS   NTF_Lambert_II_Carto
#DEPARTMT   NTF_Lambert_II_Carto
#LANGDEP   NTF_Lambert_II_Carto
#autor11l2p   NTF_Lambert_II
#can11l2p   NTF_Lambert_II
#com11l2p   NTF_Lambert_II
#Narbplage.png   NTF_Lambert_Conformal_Conic

# -> Récupérer les layers d'une couche précise #
couche_france = arcpy.mapping.ListLayers(mxdtp1,"",blocs_tp1[0])
for couche in couche_france:
    print couche.name
#VILLE_10
#REGIONS
#DEPARTMT

# -> Afficher le nom des blocs et des couches #
for bloc in blocs_tp1:
    print ("Le bloc est : "+ bloc.name)
    for couche in bloc:
        print ("Il y a la couche : " + couche.name)
#Le bloc est : France
#Il y a la couche : VILLE_10
#Il y a la couche : REGIONS
#Il y a la couche : DEPARTMT
#Le bloc est : Languedoc
#Il y a la couche : LANGDEP
#Le bloc est : Aude
#Il y a la couche : autor11l2p
#Il y a la couche : can11l2p
#Il y a la couche : com11l2p
#Il y a la couche : Narbplage.png

# -> Retrouver une couche raster #
for couche in couches1:
    if couche.isRasterLayer:
        print (couche.datasetName + " est un raster")
#Narbplage.png est un raster

# -> Selectionner les tables présentes #
tables = arcpy.mapping.ListTableViews(mxdtp1)
for table in tables:
    print table.name, table.datasetName
#Table_des_régions Table_des_régions

# -> Selectionner les éléments graphiques #
elmt = arcpy.mapping.ListLayoutElements(mxdtp1)
for elem in elmt:
    print elem.name, elem.type
#TEXT_ELEMENT
#GRAPHIC_ELEMENT
#TEXT_ELEMENT
#TEXT_ELEMENT
#TEXT_ELEMENT
#TEXT_ELEMENT
#North Arrow MAPSURROUND_ELEMENT
#Aude DATAFRAME_ELEMENT
#Languedoc DATAFRAME_ELEMENT
#France DATAFRAME_ELEMENT
