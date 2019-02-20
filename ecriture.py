from arene import *
from robot import *
from obstacle import *

def ecriture2(fichier, arene):
    """
    Cette fonction écrit dans un fichier l'état actuelle de l'arène
    : param fichier : fichier dans lequel on écrit 
    : param arene : arene à sauvegarder 
    """
    Fichier=open(fichier,"w")                   #ouverture du fichier 
    Fichier.write(str(arene._x)+"\n")           #coordonées de l'arène
    Fichier.write(str(arene._y)+"\n")
    Fichier.write(str(arene._z)+"\n")

    for i in arene._obstacles :                 #sauvegarde des obstacles 
        Fichier.write(i.toString()+"\n")

    Fichier.write(arene._robot.toString()+"\n") #sauvegarde du robot 
    Fichier.close()                             #fermeture du fichier 
