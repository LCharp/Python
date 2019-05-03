 ###########################
#   TP2 Python sous Arcgis  #
#     Espaces de Travail    #
 ###########################
#      Suivi du fichier     #
#  TP_Espace_de_travail.doc #
 ###########################

# -> Définir un espace de travail #
arcpy.env.workspace="C:/charpentier/Arcgis_Python/TP2/tp2.mdb"

# -> Liste des classes #
mes_classes=arcpy.ListFeatureClasses("*")
mes_classes
#[u'VILLE_10', u'REGIONS', u'DEPARTMT', u'LANGDEP', u'autor11l2p', u'can11l2p', u'com11l2p']

# -> Liste des classes polygon #
mes_classes_polygon = arcpy.ListFeatureClasses("*","polygon")
mes_classes_polygon
#[u'REGIONS', u'DEPARTMT', u'LANGDEP', u'can11l2p', u'com11l2p']

# -> Contenu d'une classe #
liste_champ_autoroute = arcpy.ListFields("autor11l2p")
for i in liste_champ_autoroute:
    print ("Champ: " + i.name + " Type: "+ i.type)
#Champ: OBJECTID Type: OID
#Champ: Shape Type: Geometry
#Champ: CATEGORIE Type: String
#Champ: NIVEAU Type: Double
#Champ: NOM_LOCAL Type: String
#Champ: INTERNAT_1 Type: String
#Champ: INTERNAT_2 Type: String
#Champ: VraiX Type: Double
#Champ: VraiY Type: Double
#Champ: MonX Type: Double
#Champ: Shape_Length Type: Double

#-> Ajouter un champ (km) dans une classe (autor11l2p) #
arcpy.AddField_management("autor11l2p","km","SHORT")

# -> Calculer un champ #
arcpy.CalculateField_management("autor11l2p","km","!Shape_Length!/1000","PYTHON")
#  ____________________
# | Shape_Length | km |
# |______________|____|
# |  9187,55485  |  9 |
# |______________|____|

# -> Supprimer un champ #
arcpy.DeleteField_management("autor11l2p","km")
