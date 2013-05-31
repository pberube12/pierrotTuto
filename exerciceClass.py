# _*_ coding:Latin-1 _*_

#########################################
# Programme Python 3.3 type             #
# auteur : P.Berube, Piedmont, 2013     #
# first script Python by DelPi          #
#########################################

# Script pour me pratiquer 

import sys
import os
import pierrotsModules
"""
premier step:
boucle à travers un folder et va print dans un dictionnaire la shot en key et les qt correspondant dans By_Name dans la value
    qtDict : Sera mon dictionnaire plus tard
    originalPath : path des quicktime = Key
    
    """
if __name__ == '__main__':
"""
    qtDict = {} 
    originalPath = ("//Users//assistant//Desktop//Not_Delete")
    path = os.listdir(originalPath)
# ici nous allons changer le nom des qt
    for qt in path:
        dictByName = {}
        qtPath = os.path.join(originalPath, qt)
        if os.path.isdir(qtPath):
            continue
        qtSplitter = qt.split("_")
        erreur = len(qtSplitter)
        if erreur != 3:
            continue 
        shot = qtSplitter[0][0:3]
        scene = qtSplitter[1]
        newShot = ("SF" + shot + "_" + scene)
        newScene = ("SF" + shot)
        dictByName[newScene] = newShot
    """
# ici c'est la partie qui va chercher dans ByName les bon qt
        pathBn = ("//Volumes//QUICKTIME//Smurf//Sort_By_Name")
        for newQt in listScene:
            pathBn = os.path.join(pathBn, newQt)
            for newQtDeux in listShot:
                pathBn = os.path.join(pathBn, newQtDeux)
                listPathBn = os.listdir(pathBn)
                qtDict[newShot] = listPathBn
