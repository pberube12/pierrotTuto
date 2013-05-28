from os import chdir
chdir("/Users/assistant/Desktop/")
o = open('texte.txt', 'r')
r = o.readline(2)
print r
o.close()