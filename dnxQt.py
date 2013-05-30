# _*_ coding:Latin-1 _*_

#########################################
# Programme Python 3.3 type             #
# auteur : P.Berube, Piedmont, 2013     #
# first script Python by DelPi          #
#########################################

# Script pour trouver le DNX 

import os
import sys
import shutil
import pierrotsModules

def copieDnx(originalPath):
    """
    Ceci est la fonction qui renomme le quicktime original en enlevant _vfx 
        listOriginalPath : c'est la liste(path) des quicktimes qu'on veut modifier
        listeDnxRecherche : La liste qu'on veut renvoyer des qt renommé
        filename : filename sans l'extension
        ext : l'extension spliter
        vfx : le _vfx seul
        qtDnx : le nouveau que l'on veut sans _vfx 
    """
    pathDnx = ("//Volumes//IO01//HyMovieCreator//Quicktime//HD")
    pathDnxCentQuinze = ("//Volumes//IO01//HyMovieCreator//Quicktime//HD115")
    listOriginalPath = os.listdir(originalPath)
    listeDnxRecherche = []
    for files in listOriginalPath:
        filename = files.split("_vfx")[0] # retire le nom du qt
        ext = files.split(".")[-1] # retire l'extension
        if ext.lower() != "mov":
            continue
        qtDnx = filename + "." + ext
        fullPath = os.path.join(pathDnx, qtDnx)
        if os.path.exists(fullPath):
            print("Searching Qt DNX")
            print(qtDnx)
            shutil.copy2(fullPath, newFolder) #LA copie
            print("Done")
    return