# _*_ coding:Latin-1 _*_

#########################################
# Programme Python 3.3 type             #
# auteur : P.Berube, Piedmont, 2013     #
# first script Python by DelPi          #
#########################################

# test the walk

import os
import sys

pathOriginal = os.walk("/Users/assistant/Desktop/Not_Delete")
listeFichierDict = []
fichierDict = {}
imageDict = {}
for path, dir, files in pathOriginal:
    fichierDict = {}
    for file in files:
        fileSplit = file.split(".") #fichier séparé par les points
        ext = fileSplit[-1]
        filename = fileSplit[0]
        if len(fileSplit) == 3: #pour trouver si c'est une image séquence on rechercher les split de trois partie
            if filename in file: #On veut seulement se qui est dans l'image séquence pas le reste
                imageDict.setdefault(filename, []).append(file) #On se crée un dict comprenent le nom de la sequence et tous les frames correspondant
                for key in imageDict:
                    fichierDict["extension"] = ext
                    fichierDict["path"] = path
                    fichierDict["name"] = filename
                print key
            continue
