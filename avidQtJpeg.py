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
# Path des qts voulu en Avid
originalPath = sys.argv[1]
for files in os.listdir(originalPath):
    filename = files.split(".")[0]
    ext = files.split(".")[-1]
    qtAvid = (filename + "_AVID")
    qtJpeg = (filename + ".zip")
    if ext.lower() != "mov":
        continue
    filenameAvid = qtAvid + "." + ext
    print files

# la partie qui va trouver le Qt AVid et le copy au path voulu
    for newFile in listAvidPath:
        fullPath = os.path.join(avidPath, newFile)
        destPathMxf = os.path.join(sys.argv[2], "MXF")
        if not os.path.exists(destPathMxf):
            os.makedirs(destPathMxf)
        if os.path.isdir(fullPath):
            continue
        if filenameAvid.lower() == newFile.lower():
            print(filenameAvid)
            print("Searching Qt Avid")
            shutil.copy2(fullPath, destPathMxf)
            print("Done")
        else:
            continue
        
    for newZip in listJpegPath:
        fullPathZip = os.path.join(jpegPath, newZip)
        destPathZip = os.path.join(sys.argv[2], "JPEG")
        if not os.path.exists(destPathZip):
            os.makedirs(destPathZip)
        if os.path.isdir(fullPathZip):
            continue
        if qtJpeg.lower() == newZip.lower():
            print(qtJpeg)
            print("Searching Zip")
            shutil.copy2(fullPathZip, destPathZip)
            print("Done")
        else:
            continue