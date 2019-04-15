#symbole de robot =R
#symbole obstacle=O
#utiliser with open
#retourne larene
from .arene import Arene
from ..view import View
#from .obstacle import ObstacleRond, ObstacleCarre



def lecture(fichier,robot):
    Fichier=open(fichier,"r")
    txt=Fichier.readline()
    x=int(txt)
    txt=Fichier.readline()
    y=int(txt)
    txt=Fichier.readline()
    z=int(txt)
    a=Arene(x,y,z)                      #creation de arene

    n=0
    for elt in Fichier.readlines():     #parcour le fichier pour cree des obstacles ou robots
        arg=elt.split(" ")
        if 'O'==arg[0] :
            a.ajout_Obstacle(ObstacleRond(float(arg[1]),float(arg[2]),float(arg[3]),float(arg[4]),couleur=str(arg[5])))
        if 'R'==arg[0] :
            a.ajout_Robot(robot)
            robot.set_position(float(arg[1]),float(arg[2]),float(arg[3]))
            robot.set_acceleration(float(arg[4]))
            robot.set_vitesse(float(arg[5]))
            robot.set_direction(float(arg[6]),float(arg[7]),float(arg[8]))
            #robot.set_color(arg[9])

        if 'C'==arg[0] :
            a.ajout_Obstacle(ObstacleCarre(float(arg[1]),float(arg[2]),float(arg[3]),lo=float(arg[4]),la=float(arg[5]),couleur=str(arg[6])))
    Fichier.close()
    return a
