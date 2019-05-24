# Memento Python x Arcpy

Memento sur l'utilisation de Python sous Arcgis (Arcpy).

## Commandes principales


|Fonction           | Commande                | Où trouver                     |
|----------------|-------------------------------|-----------------------------|
|         mxd			|`mxd=arcpy.mapping.MapDocument("CURRENT")` |TP1 |
|    Bloc de données	|`blocs=arcpy.mapping.ListDataFrames(mxd)` |TP1 |
|       Couches			|`couches=arcpy.mapping.ListLayers(mxd,"",i)` |TP1 |
| Workspace (gdb / mdb)	|`arcpy.env.workspace="*lien mdb/gdb*"` |TP2 |
|    Couche d'entité	|`arcpy.ListFeatureClasses(*NomClasse*)` |TP2 |
|        Champs			|`arcpy.ListFields(*NomChamp*)` |TP2 |
|   Ajouter un Champ	|`arcpy.AddField_management()` |TP2 |
|  Supprimer un Champ	|`arcpy.DeleteField_management()` |TP2 |
|   Calculer un Champ	|`arcpy.CalculateField_management()` |TP2 |
|     init Curseur		|`arcpy.SearchCursor()` |TP3 |
|    Update Curseur		|`arcpy.UpdateCursor + curseur.updateRow` |TP3 |
|Insert Curseur			|`arcpy.InsertCursor + curseur.insertRow` |TP3 |
|Delete Curseur			|`arcpy.UpdateCursor + curseur.deleteRow` |TP3 |
|Copie temporaire		|`arcpy.MakeFeatureLayer_management` |TP4 |
|Selection Attribut		|`arcpy.SelectLayerByAttribute_management` |TP4 |
|Selection Emplacement	|`arcpy.SelectLayerByLocation_management` |TP4 |
|Créer Couche (de la selection)	|`mxd_tp1=arcpy.mapping.MapDocument("CURRENT")` |TP4 |
|Deselectionner	|`arcpy.SelectLayerByAttribute_management("CLEAR_SELECTION")` |TP4 |
