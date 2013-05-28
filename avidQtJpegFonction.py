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


# fonction pour changer le nom du quicktime en lui rajoutant _AVID
def renameAvid(originalPath):
    listOriginalPath = os.listdir(originalPath)
    for files in listOriginalPath:
        filename = files.split(".")[0]
        ext = files.split(".")[-1]
        filenameAvid = (filename + "_AVID") # nom temporaire pour rajouter le _AVID au nom
        if ext.lower() != "mov":
            continue
        qtAvid = filenameAvid + "." + ext
        return qtAvid

# fonction pour changer le nom des quicktime en remplacant le mov en zip
def renameZip(originalPath):
    listOriginalPath = os.listdir(originalPath)
    for files in listOriginalPath:
        filename = files.split(".")[0]
        qtJpeg = (filename + ".zip")
        ext = files.split(".")[-1]
        if ext.lower() != "mov":
            continue
        return qtJpeg

# fonction pour la creation de folder
def creationFolder(folder):
    destPath = os.path.join(sys.argv[2], folder)
    if not os.path.exists(destPath):
        os.makedirs(destPath)
    return destPath

# la partie qui va trouver le Qt Avid et le copy au path voulu
for newFile in listAvidPath:
    newFolder = creationFolder("MXF")
    fullPath = os.path.join(avidPath, newFile)
    if os.path.isdir(fullPath):
        continue
    if renameAvid(sys.argv[1]) == newFile.lower():
        print("")
        print("Searching Qt Avid")
        shutil.copy2(fullPath, newFolder)
        print("Done")
    else:
        continue

# la partie qui va trouver les zip et le copy au path voulu
for newZip in listJpegPath:
    newFolder = creationFolder("JPEG")
    fullPathZip = os.path.join(jpegPath, newZip)
    if os.path.isdir(fullPathZip):
        continue
    if renameZip(sys.argv[1]) == newZip.lower():
        print("")
        print("Searching Zip")
        shutil.copy2(fullPathZip, newFolder)
        print("Done")
    else:
        continue