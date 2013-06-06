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
    database = sql.connectDb("2Dtools")
    cursor = database.cursor()
    query = """select * from `2d_tools`.`qt_auto_projects_setup`"""
    lines = cursor.execute(query)
    data = cursor.fetchall()
    dnxPath = ("/Volumes/IO01/HyMovieCreator/Quicktime/HD")
    dnxPathSpherical = ("/Volumes/IO01/HyMovieCreator/Quicktime/HD115")
    fileDnxPath = os.listdir(dnxPath)
    files = pierrotsModules.renameDnx(sys.argv[1])
    for file in files:
        if file in fileDnxPath:
            fullDnxPath = os.path.join(dnxPath, file)
            shutil.copy2(fullDnxPath, sys.argv[2])
            print("______DONE______")
    database.close
