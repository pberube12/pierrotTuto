# _*_ coding:Latin-1 _*_

#########################################
# Programme Python 3.3 type             #
# auteur : P.Berube, Piedmont, 2013     #
# first script Python by DelPi          #
#########################################

# Exercice Listing 2013_06_03

import sys
import os

def listingFolder(size = False, nbMax = 0, extension = False):
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
    """
    dirSize = 0
    pathOriginal = os.walk("/Users/assistant/Desktop/Not_Delete")
    myDict = {}
    for path, dir, files in pathOriginal:
        #pour avoir une recursion differente dans mes qts
        if nbMax:
            pathSplit = path.split("/")[4:]
            if len(pathSplit) <= nbMax:
                files = os.listdir(path)
        for file in files:
            fileNewListePath = os.path.join(path, file)
            if os.path.isdir(fileNewListePath):
                continue
            fichierDict = {}
            #enlever le .ds_store
            if file.startswith("."):
                continue
            #fichier separe par les points
            fileSplit = file.split(".")
            ext = fileSplit[-1]
            filename = fileSplit[0]
            filenameExt = filename+ext #besoin pour savoir si il existe dans le dict avec extension
            #Si un argument est ecrit, le script va seulement lister les fichier avec les extension indique
            if extension:
                if extension != ext:
                    continue
            if not filenameExt in myDict:
                fichierDict["name"] = filename
                fichierDict["extension"] = ext
                fichierDict["path"] = path
                duration = 1
                myDict[filenameExt] = fichierDict
            elif (ext == myDict[filenameExt]["extension"]) and len(fileSplit) == 3:
                duration += 1 #accrementation pour avoir la dur�e total de la sequence d'image
                myDict[filenameExt]["Duration"] = duration
            #premier argument optionnel si il y a une valeur d'entre nous allons avoir le poids dans le dict, sinon rien
            if size:
                filenameDir = os.path.join(path, file)
                dirSize = os.path.getsize(filenameDir)
                fichierDict["Size"] = dirSize
    return myDict.values()

for file in listingFolder(nbMax = 1):
    print file