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
script qui print dans un dictionnaire la shot en key et les qt correspondant dans By_Name dans la value
    qtDict : Sera mon dictionnaire plus tard
    qtRename : Dictionnaire des qt renommé
    pathBn : path de Sort_By_Name
    path : path de vision 2D
    listPathBn : la liste de toutes les shots dans le folder Sort_By_Name
    """
if __name__ == '__main__':
    pathBn = ("//Volumes//QUICKTIME//Smurf//Sort_By_Name")
    path = ("//Volumes//QUICKTIME//Smurf//Visionnement//2D")
    listPath = os.listdir(path)
    qtDict = {}
    qtRename = pierrotsModules.renameFrums(path)
    qtRenameShot = qtRename.keys()
    qtRenameScene = qtRename.values()
    for newQt in listPath:
        newQtSplit = newQt.split(".")[-1]
        if newQtSplit != "mov":
            continue
        print newQt
"""
        pathBn = os.path.join(pathBn, newQt)
        listPathBn = os.listdir(pathBn)
        qtDict[newQt] = listPathBn
"""