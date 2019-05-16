# -*- coding: cp1252 -*-
import os
import arcpy
from arcpy import env
arcpy.env.workspace="U:/Documents/P3/ufarte/python/tp1/données TP1/tp2.gdb"


def watch():
    # TODO
    # Affiche le nom de toutes les classes
    classes=arcpy.ListFeatureClasses("*")
    
    nb_classes=len(classes)

    print("il y a "+str(nb_classes)+ " classes,dans notre base de donnes ")
    for i in classes:
        print(i)

    #Selection d'une classe pour afficher les données
    ma_classe = input("\nVeuillez choisir une classe à afficher les données\n")
    while ma_classe not in classes:
           ma_classe=input("Cette classe n'existe pas. Dans quelle classe veux-tu voir les lignes ")

    nb_lignes = input("\n choisi ton nb de lignes \n")
    
    liste_champ = arcpy.ListFields(ma_classe)
    #Curseur
    tab_champ=[]
    nb_champ = len(liste_champ)
    curseur = arcpy.SearchCursor(ma_classe,"",None)
    for i in liste_champ:
        tab_champ.append(i.name)
        for j in range(nb_lignes):
            ligne = curseur.next()
            print("Ligne n° : " + str(j+1))
            for l in range (nb_champ):
                champ = tab_champ[l]
                print(champ+ " Valeur : ")
                print(0ligne.getValue(champ))
    raw_input("Press [Enter] to continue...")

def modif():
    # TODO
    
    raw_input("Press [Enter] to continue...")

def suppr():
    # TODO
    raw_input("Press [Enter] to continue...")

def add():
    # TODO
    raw_input("Press [Enter] to continue...")    

menuItems = [
    { "Visualisation classe d'entite": watch },
    { "Modif données": modif },
    { "Supprimer": suppr },
    { "Ajouter": add },
    { "Quitter": exit },
]

def main():
    while True:
        os.system('clear')
        for item in menuItems:
            print (str(menuItems.index(item)) + " " + item.keys()[0])
        choice = raw_input(">> ")
        try:
            if int(choice) < 0 : raise ValueError
            # Call the matching function
            menuItems[int(choice)].values()[0]()
        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
