#############################
#   TP3 Python sous Arcgis  #
#       TP3 Curseur.doc    #
#############################

 # -> Question 1 : Dénombrer les communes et la population dans l'Aude
arcpy.env.workspace = "C:\charpentier\Arcgis_Python\TP3\tp3_gdb.gdb"
curseur = arcpy.SearchCursor("com11l2p")
nb, pop = 0,0
for ligne in curseur:
     nb += 1
     pop += ligne.POP
print "Nombre de communes dans l'Aude :" ,nb
 # Nombre de communes dans l'AUde : 438
print "Population de l'Aude :" ,pop,"habitants"
 # Population de l'Aude : 298898.0 habitants


 # -> Question 2 : Commune la plus peuplée + sa population
curseur = arcpy.SearchCursor("com11l2p","",None,"NOM ; POP", "POP D")
ligne = curseur.next()
nom = ligne.getValue("NOM")
population = ligne.POP
print "Commune la plus peuplée de l'Aude :",nom,population,"hbts"
 # Commune la plus peuplée de l'Aude : NARBONNE 45866.0 hbts


 # -> Question 3 : 5 communes les plus peuplées + pop (indiv) + pop (total)
curseur = arcpy.SearchCursor("com11l2p","",None,"NOM ; POP", "POP D")
poptot = 0
for i in range(5):
    ligne = curseur.next()
    poptot += ligne.POP
    print ("La commune numero "+str(i+1)+" est "+ligne.NOM +" sa population est de "+str(ligne.POP))
print ("La population totale de s5 plus grandes villes de l'aude est " + str(poptot))
 # La commune numero 1 est CARCASSONNE sa population est de 43511.0
 # La commune numero 2 est CASTELNAUDARY sa population est de 10973.0
 # La commune numero 3 est LIMOUX sa population est de 9665.0
 # La commune numero 4 est LEZIGNAN-CORBIERES sa population est de 7881.0
 # La commune numero 5 est TREBES sa population est de 5576.0
 # La population totale de s5 plus grandes villes de l'aude est 123472.0


 # -> Question 4 : Ajouter + 100 à un champ et - 100
 curseur = arcpy.UpdateCursor("com11l2p","\"NOM\" = 'CARCASSONNE'",None,"POP")
 ligne = curseur.next()

 # ADDITION
 ligne.POP += 100
 #  _______
 # |  pop |
 # |______|
 # | 43511|
 # |______|

 # SOUSTRACTION
 ligne.POP -= 100
  #  _______
  # |  pop |
  # |______|
  # | 43411|
  # |______|
 curseur.updateRow(ligne)


 # -> Question 5a : Ajouter une ligne (nom et pop)
 curseur = arcpy.InsertCursor("communes")
 ligne = curseur.newRow()
 ligne.Nom = "GAUJAC"
 ligne.POP = 500
 curseur.insertRow(ligne)
#  __________________
# |   nom    |  pop |
# |__________|______|
# |  GAUJAC  |  500 |
# |__________|______|

 # -> Question 5b : Supprimer une ligne (nom et pop)
 curseur = arcpy.UpdateCursor("communes", "\"Nom\" = 'GAUJAC'")
 ligne = curseur.next()
 curseur.deleteRow(ligne)
