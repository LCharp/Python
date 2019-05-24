# Memento Python x Arcpy

Memento sur l'utilisation de Python sous Arcgis (Arcpy).

## Commandes principales


|Fonction           | Commande                | Où trouver                     |
|----------------|-------------------------------|-----------------------------|
|         mxd			|`mxd=arcpy.mapping.MapDocument("CURRENT")` |[TP1](https://github.com/LCharp/Python/blob/master/Arcgis/TP1/tp1.py) |
|    Bloc de données	|`blocs=arcpy.mapping.ListDataFrames(mxd)` |[TP1](https://github.com/LCharp/Python/blob/master/Arcgis/TP1/tp1.py) |
|       Couches			|`couches=arcpy.mapping.ListLayers(mxd,"",i)` |[TP1](https://github.com/LCharp/Python/blob/master/Arcgis/TP1/tp1.py) |
| Workspace (gdb / mdb)	|`arcpy.env.workspace="*lien mdb/gdb*"` |[TP2](https://github.com/LCharp/Python/blob/master/Arcgis/TP2/tp2_arcgis_cmd.py) |
|    Couche d'entité	|`arcpy.ListFeatureClasses(*NomClasse*)` |[TP2](https://github.com/LCharp/Python/blob/master/Arcgis/TP2/tp2_arcgis_cmd.py)|
|        Champs			|`arcpy.ListFields(*NomChamp*)` |[TP2](https://github.com/LCharp/Python/blob/master/Arcgis/TP2/tp2_arcgis_cmd.py)|
|   Ajouter un Champ	|`arcpy.AddField_management()` |[TP2](https://github.com/LCharp/Python/blob/master/Arcgis/TP2/tp2_arcgis_cmd.py)|
|  Supprimer un Champ	|`arcpy.DeleteField_management()` |[TP2](https://github.com/LCharp/Python/blob/master/Arcgis/TP2/tp2_arcgis_cmd.py)|
|   Calculer un Champ	|`arcpy.CalculateField_management()` |[TP2](https://github.com/LCharp/Python/blob/master/Arcgis/TP2/tp2_arcgis_cmd.py)|
|     init Curseur		|`arcpy.SearchCursor()` |[TP3](https://github.com/LCharp/Python/blob/master/Arcgis/TP3/tp3.py) |
|    Update Curseur		|`arcpy.UpdateCursor + curseur.updateRow` |[TP3](https://github.com/LCharp/Python/blob/master/Arcgis/TP3/tp3.py)|
|Insert Curseur			|`arcpy.InsertCursor + curseur.insertRow` |[TP3](https://github.com/LCharp/Python/blob/master/Arcgis/TP3/tp3.py)|
|Delete Curseur			|`arcpy.UpdateCursor + curseur.deleteRow` |[TP3](https://github.com/LCharp/Python/blob/master/Arcgis/TP3/tp3.py)|
|Copie temporaire		|`arcpy.MakeFeatureLayer_management` |[TP4](https://github.com/LCharp/Python/blob/master/Arcgis/tp4/tp4_arcmap.py) |
|Selection Attribut		|`arcpy.SelectLayerByAttribute_management` |[TP4](https://github.com/LCharp/Python/blob/master/Arcgis/tp4/tp4_arcmap.py)|
|Selection Emplacement	|`arcpy.SelectLayerByLocation_management` |[TP4](https://github.com/LCharp/Python/blob/master/Arcgis/tp4/tp4_arcmap.py)|
|Créer Couche (de la selection)	|`mxd_tp1=arcpy.mapping.MapDocument("CURRENT")` |[TP4](https://github.com/LCharp/Python/blob/master/Arcgis/tp4/tp4_arcmap.py)|
|Deselectionner	|`arcpy.SelectLayerByAttribute_management("CLEAR_SELECTION")` |[TP4](https://github.com/LCharp/Python/blob/master/Arcgis/tp4/tp4_arcmap.py)|
