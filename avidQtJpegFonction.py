# _*_ coding:Latin-1 _*_

#########################################
# Programme Python 3.3 type             #
# auteur : P.Berube, Piedmont, 2012     #
# first script Python by DelPi          #
#########################################

# Script pour trouver les avid des assistants

import os
import shutil
import sys

# Path dans lequel se trouvent les AVID et Zip
avidPath = ("//Volumes//IO01//HyMovieCreator//Quicktime//HD")
jpegPath = ("//Volumes//IO01//HyMovieCreator//Quicktime//RAR")
# tous les listing directory que j'ai besoin
listAvidPath = os.listdir(avidPath)
listJpegPath = os.listdir(jpegPath)


def renameAvid(originalPath):
    """
    Ceci est la fonction qui renomme le quicktime original en rajoutant _AVID
        listOriginalPath : c'est la liste(path) des quicktimes qu'on veut modifier
        listeQtRecherche : La liste qu'on veut renvoyer des qt renomm�
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
        listeZipRecherche : La liste qu'on veut renvoyer des qt renomm�
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
    Ceci est une fonction qui fait un nouveau folder au path demand�
        destPath : l'argument pass� est le path ou l'on veut cr�er le nouveau folder
    """
    destPath = os.path.join(sys.argv[2], folder)
    if not os.path.exists(destPath):
        os.makedirs(destPath)
    return destPath

# Parti qui copie le _AVID dans le folder voulu
qtAvidRename = renameAvid(sys.argv[1])
for newFile in qtAvidRename:
    newFolder = creationFolder("MXF") # Le folder mxf est maintenant cr��
    fullPath = os.path.join(avidPath, newFile) # le path des qt avid
    if os.path.isdir(fullPath):
        continue
    if os.path.exists(fullPath):
        print("Searching Qt Avid")
        print(newFile)
        shutil.copy2(fullPath, newFolder)
        print("Done")

"""   
# la partie qui va trouver les zip et le copy au path voulu
for newZip in listJpegPath:
    newFolder = creationFolder("JPEG")
    qtJpegRename = renameZip(sys.argv[1])
    fullPathZip = os.path.join(jpegPath, newZip)
    if os.path.isdir(fullPathZip):
        continue
    if qtJpegRename.lower() == newZip.lower():
        print("Searching Zip")
        #print qtJpegRename
        shutil.copy2(fullPathZip, newFolder)
        print("Done")
    else:
        continue
"""