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
import pierrotsModules

if __name__ == '__main__':
    # Path dans lequel se trouvent les AVID et Zip
    avidPath = ("//Volumes//IO01//HyMovieCreator//Quicktime//HD")
    jpegPath = ("//Volumes//IO01//HyMovieCreator//Quicktime//RAR")
    # tous les listing directory que j'ai besoin
    listAvidPath = os.listdir(avidPath)
    listJpegPath = os.listdir(jpegPath)
    qtAvidRename = pierrotsModules.renameAvid(sys.argv[1]) # Ma liste de qt renommé
    qtJpegRename = pierrotsModules.renameZip(sys.argv[1]) # Ma liste de zip renommé

    # Parti qui copie le _AVID dans le folder voulu
    for newFile in qtAvidRename:
        newFolder = pierrotsModules.creationFolder("MXF") # Le folder mxf est maintenant créé
        fullPath = os.path.join(avidPath, newFile) # le path des qt avid qu'on va vouloir
        if os.path.isdir(fullPath): # on ne veut pas les folder
            continue
        if os.path.exists(fullPath):
            print("Searching Qt Avid")
            print(newFile)
            shutil.copy2(fullPath, newFolder) #LA copie
            print("Done")

    # la partie qui va trouver les zip et le copy au path voulu
    for newZip in qtJpegRename:
        newFolder = pierrotsModules.creationFolder("JPEG") # Le folder JPEG est maintenant créé
        fullPathZip = os.path.join(jpegPath, newZip) # le path des zip qu'on va vouloir
        if os.path.isdir(fullPathZip): # on ne veut pas les folder
            continue
        if os.path.exists(fullPathZip):
            print("Searching Zip")
            print(newZip)
            shutil.copy2(fullPathZip, newFolder) # La copie
            print("Done")
