from arene import *
from robot import *
from obstacle import *

def ecriture(fichier):
	Fichier=open(fichier,"w")
	Fichier.write(arene._x)
	Fichier.write(arene._y)
	Fichier.write(arene._z)
	for i in arene._obstacles :
		Fichier.write(i.toString())

	Fichier.close()

