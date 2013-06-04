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

def listingFolder(dirSize = None, nbMax = "mov", extension = None):
    """
    Scrip qui liste un folder et tous les sous folders, retourne une liste de dictionnaire des fichiers avec infos. 
    Ensuite il devra avoir des spécification au recherche, choisir qu'elle extension on veut chercher, la taille des fichier ou non
    le nombre maximal de sous folder à lister
        fichierDict = Dictionnaire comprennant name, extension, size, path, pour chaque fichier 
        listeFichierDict = la liste de dictionnaire
        digitListe = la liste des chiffre qui compose l'image séquence
        dirSize = le poids des fichiers
        pathOriginal = le listing de tous les fichier
        path, dir, files = les path de tout le path original, les folders, les fichiers
        ext = extenssion
        filename = nom du fichier
        filanamrDir = Nom du fichier avec son path
    """
    fichierDict = {}
    listeFichierDict = []
    digit = []
    digitListe = []
    dirSize = 0
    pathOriginal = os.walk("/Users/assistant/Desktop/Not_Delete")
    for path, dir, files in pathOriginal:
        for file in files:
            fileSplit = file.split(".")
            if len(fileSplit) > 2:
                digitSplit = fileSplit[-2]
            ext = fileSplit[-1]
            filename = fileSplit[0]
            filenameDir = os.path.join(path, file)
            dirSize += os.path.getsize(filenameDir)
            fichierDict["name"] = filename
            fichierDict["extension"] = ext
            fichierDict["size"] = dirSize
            fichierDict["path"] = path
            listeFichierDict.append(fichierDict)
    return digit
