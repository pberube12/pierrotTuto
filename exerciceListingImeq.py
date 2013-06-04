# _*_ coding:Latin-1 _*_

#########################################
# Programme Python 3.3 type             #
# auteur : P.Berube, Piedmont, 2013     #
# first script Python by DelPi          #
#########################################

# Exercice Listing 2013_06_03

import sys
import os
import pierrotsModules

def listingFolder(size = False, nbMax = False, extension = False):
    """
    Scrip qui liste un folder et tous les sous folders, retourne une liste de dictionnaire des fichiers avec infos. 
    Ensuite il devra avoir des spécification au recherche, choisir qu'elle extension on veut chercher, la taille des fichier ou non
    le nombre maximal de sous folder à lister
        listeFichierDict = la liste de dictionnaire
        imageDict = dictionnaire pour mes images sequences
        dirSize = le poids des fichiers
        pathOriginal = le listing de tous les fichier
        path, dir, files = les path de tout le path original, les folders, les fichiers
        fichierDict = Dictionnaire comprennant name, extension, size, path, pour chaque fichier 
        ext = extenssion
        filename = nom du fichier
        filanameDir = Nom du fichier avec son path
    """
    listeFichierDict = []
    imageDict = {}
    dirSize = 0
    pathOriginal = os.walk("/Users/assistant/Desktop/Not_Delete")
    a = 0
    for path, dir, files in pathOriginal:
        for file in files:
            fichierDict = {}
            fileSplit = file.split(".") #fichier séparé par les points
            ext = fileSplit[-1]
            filename = fileSplit[0]
            if file.startswith("."): #enlever le .ds_store
                continue
            if size: #premier argument optionnel si il y a une valeur d'entré nous allons avoir le poids dans le dict, sinon rien
                filenameDir = os.path.join(path, file)
                dirSize = os.path.getsize(filenameDir)
                fichierDict["Size"] = dirSize
            if extension: #Si un argument est ecrit, le script va seulement lister les fichier avec les extension indiqué
                if extension == ext:
                    fichierDict["name"] = filename
                    fichierDict["extension"] = ext
                    fichierDict["path"] = path
                continue
            if len(fileSplit) == 3: #pour trouver si c'est une image séquence on rechercher les split de trois partie
                if filename in file:
                    imageDict.setdefault(filename, []).append(file)
                    fichierDict["extension"] = ext
                    fichierDict["path"] = path
                    for key in imageDict: # pour avoir juste le premier frame comme filename
                        fichierDict["name"] = key
                fichierDict["Duration"] = len(imageDict[filename])
            else:
                fichierDict["name"] = filename
                fichierDict["extension"] = ext
                fichierDict["path"] = path
        listeFichierDict.append(fichierDict)
    return listeFichierDict

g = listingFolder()
print g