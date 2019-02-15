from arene import *
from robot import *
from obstacle import *

def ecriture2(fichier, arene):
	Fichier=open(fichier,"w")
	Fichier.write(str(arene._x)+"\n")
	Fichier.write(str(arene._y)+"\n")
	Fichier.write(str(arene._z)+"\n")
	for i in arene._obstacles :
		Fichier.write(i.toString()+"\n")

	Fichier.close()

