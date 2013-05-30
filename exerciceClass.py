# _*_ coding:Latin-1 _*_

#########################################
# Programme Python 3.3 type             #
# auteur : P.Berube, Piedmont, 2013     #
# first script Python by DelPi          #
#########################################

# Script pour me pratiquer 

import sys
import os

path = ("//Users//assistant//Desktop//Not_Delete")
qtPath = os.listdir(path)
qtDict = {}
if __name__ == '__main__':
    for qt in qtPath:
        fullQtPath = os.path.join(path, qt)
        if os.path.isdir(fullQtPath):
            continue
        qtShrut = qt.split("_h")[0]
        qtDict[qtShrut] = qt
    print(qtDict)
