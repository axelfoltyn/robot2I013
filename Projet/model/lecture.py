#symbole de robot =R
#symbole obstacle=O
#utiliser with open
#retourne larene
from .arene import Arene
from .robot import RobotVirtuel
from .obstacle import Obstacle_rond, Obstacle_carre
from ..view import View


def lecture(fichier,robot):
    Fichier=open(fichier,"r")
    txt=Fichier.readline()
    x=int(txt)
    txt=Fichier.readline()
    y=int(txt)
    txt=Fichier.readline()
    z=int(txt)
    a=Arene(x,y,z)                      #creation de arene
    a.add_obs(View(x,y))
    n=0
    for elt in Fichier.readlines():     #parcour le fichier pour cree des obstacles ou robots
        arg=elt.split(" ")
        if 'O'==arg[0] :
            a.ajout_Obstacle(Obstacle_rond(float(arg[1]),float(arg[2]),float(arg[3]),float(arg[4])))
        if 'R'==arg[0] :
            a.ajout_Robot(robot)
            robot.set_position(float(arg[1]),float(arg[2]),float(arg[3]))
            robot.set_acceleration(float(arg[4]))
            robot.set_vitesse(float(arg[5]))
            robot.set_direction(float(arg[6]),float(arg[7]),float(arg[8]))
        if 'C'==arg[0] :
            a.ajout_Obstacle(Obstacle_carre(float(arg[1]),float(arg[2]),float(arg[3]),lo=float(arg[4]),la=float(arg[5])))
    Fichier.close()
    return a
