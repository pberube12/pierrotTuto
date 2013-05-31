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
    qtDict = {} 
    originalPath = ("//Users//assistant//Desktop//Not_Delete")
    path = os.listdir(originalPath)
# ici nous allons changer le nom des qt
    for qt in path:
        listShot = []
        listScene = []
        qtPath = os.path.join(originalPath, qt)
        if os.path.isdir(qtPath):
            continue
        shot = qt.split("_")[0][0:3]
        scene = qt.split("_")[1]
        version = qt.split("_")[-1][3:-4]
        ext = qt.split(".")[-1]
        newShot = ("SF" + shot + "_" + scene)
        newScene = ("SF" + shot)
        listShot.append(newShot) # liste des shot ex. SF003_003
        listScene.append(newScene) # liste des scene ex. SF003
# ici c'est la partie qui va chercher dans ByName les bon qt
        pathBn = ("//Volumes//QUICKTIME//Smurf//Sort_By_Name")
        for newQt in listScene:
            pathBn = os.path.join(pathBn, newQt)
            for newQtDeux in listShot:
                pathBn = os.path.join(pathBn, newQtDeux)
                listPathBn = os.listdir(pathBn)
                qtDict[newShot] = listPathBn
                print(qtDict)
