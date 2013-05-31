# _*_ coding:Latin-1 _*_

#########################################
# Programme Python 3.3 type             #
# auteur : P.Berube, Piedmont, 2012     #
# first module Python by DelPi          #
#########################################

import os
import sys

def renameAvid(originalPath):
    """
    Ceci est la fonction qui renomme le quicktime original en rajoutant _AVID
        listOriginalPath : c'est la liste(path) des quicktimes qu'on veut modifier
        listeQtRecherche : La liste qu'on veut renvoyer des qt renommé
        filename : filename sans l'extension
        ext : l'extension split 
        qtAvid : le nouveau que l'on veut avec _AVID 
    """
    listOriginalPath = os.listdir(originalPath)
    listeQtRecherche = []
    for files in listOriginalPath:
        filename = files.split(".")[0]
        ext = files.split(".")[-1]
        filenameAvid = (filename + "_AVID") # nom temporaire pour rajouter le _AVID au nom
        if ext.lower() != "mov":
            continue
        qtAvid = filenameAvid + "." + ext
        listeQtRecherche.append(qtAvid)
    return listeQtRecherche

def renameZip(originalPath):
    """
    Ceci est la fonction qui renomme le quicktime original en ramplacant le .mov par .zip
        listOriginalPath : c'est la liste(path) des quicktimes qu'on veut modifier
        listeZipRecherche : La liste qu'on veut renvoyer des qt renommé
        filename : filename sans l'extension
        ext : l'extension split 
        qtJpeg : le nouveau que l'on veut en zip  
    """
    
    listOriginalPath = os.listdir(originalPath)
    listeZipRecherche = []
    for files in listOriginalPath:
        filename = files.split(".")[0]
        qtJpeg = (filename + ".zip")
        ext = files.split(".")[-1]
        if ext.lower() != "mov":
            continue
        listeZipRecherche.append(qtJpeg)
    return listeZipRecherche

def creationFolder(folder):
    """
    Ceci est une fonction qui fait un nouveau folder au path demandé
        destPath : l'argument passé est le path ou l'on veut créer le nouveau folder
    """
    destPath = os.path.join(sys.argv[2], folder)
    if not os.path.exists(destPath):
        os.makedirs(destPath)
    return destPath

def renameFrums(originalPath):
    """
    Ceci est une fonction qui renomme les quicktime dans le bon format et retourne un dictionnaire Scene:shot
        path = le path dess qt qu'on veut renommer
        dictByName = dictionnaire des Scene = key et des Shot = Value
        qtSplitter = tous les quicktimes splitter en trois partie
    """
    path = os.listdir(originalPath)
    for qt in path:
        dictByName = {}
        qtPath = os.path.join(originalPath, qt)
        if os.path.isdir(qtPath): # ignorer les folder
            continue
        qtSplitter = qt.split("_")
        erreur = len(qtSplitter)
        if erreur != 3: # ignorer les qt qui n'ont pas la nomenclature du projet
            continue 
        shot = qtSplitter[0][0:3]
        scene = qtSplitter[1]
        newShot = ("SF" + shot + "_" + scene)
        newScene = ("SF" + shot)
        dictByName[newScene] = newShot
        return dictByName
