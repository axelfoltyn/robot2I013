from Projet import RobotVirtuel, Obstacle, Arene
from random import randint
import sys

def fonce(self):
    while(True):
        if arene.proximite()<=100 :
            while (arene.proximite()<=100):
                arene._robot.tourner(random.randint(1, 360))
                arene.update()
        arene._robot.aceleration(10)
        arene.afficher()
        arene.update(0.05)
        if (arene._robot._positio[0]>arene._x or arene._robot._positio[0]<0 or arene._robot._positio[1]>arene._y or arene._robot._positio[1]<0 ):
            sys.exit(0)
