# _*_ coding:Latin-1 _*_

#########################################
# Programme Python 3.3 type             #
# auteur : P.Berube, Piedmont, 2012     #
# first module Python by DelPi          #
#########################################

import shutil
import os
import sys
import pierrotsModules
from Hybrides_Modules import HyCMySQL

if __name__ == '__main__':
    files = pierrotsModules.renameDnx(sys.argv[1])
    for file in files:
        query = """select * from `2d_tools`.`shots`"""
        sql = HyCMySQL.CMySQL()
        database = sql.connectDb("2d_tools")
        list = sql.sqlFetchAll(query)[0]
        fileSplit = file.split("_")[0]
        for titeListe in list:
            if titeListe[27] == fileSplit:
                if titeListe[63] == 1:
                    dnxPath = ("/Volumes/IO01/HyMovieCreator/Quicktime/HD115")
                elif titeListe[63] == 2:
                    dnxPath = ("/Volumes/IO01/HyMovieCreator/Quicktime/HD")
                else:
                    print("Pas de PixelRatio indiquer")
        fileDnxPath = os.listdir(dnxPath)
        if file in fileDnxPath:
            print("searching", file, "in", dnxPath)
            fullDnxPath = os.path.join(dnxPath, file)
            shutil.copy2(fullDnxPath, sys.argv[2])
            print("______DONE______")
    database.close
