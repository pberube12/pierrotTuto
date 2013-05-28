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

# fonction pour changer le nom du quicktime en lui rajoutant _AVID
# Path des qts voulu en Avid
originalPath = sys.argv[1]
for files in os.listdir(originalPath):
    filename = files.split(".")[0]
    ext = files.split(".")[-1]
    qtAvid = (filename + "_AVID")
    if ext.lower() != "mov":
        continue
    filename = qtAvid + "." + ext
    print files

# Path dans lequel se trouvent les AVID
    avidPath = ("//Volumes//IO01//HyMovieCreator//Quicktime//HD")

# la partie qui va trouver le Qt AVid et le copy au path voulu
    for newFile in os.listdir(avidPath):
        fullPath = os.path.join(avidPath, newFile)
        if os.path.isdir(fullPath):
            continue
        if filename.lower() == newFile.lower():
            print(filename)
            print("Searching")
            shutil.copy2(fullPath, sys.argv[2])
            print("Done")
        else:
            continue