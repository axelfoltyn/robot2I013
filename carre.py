from Projet import RobotVirtuel, Obstacle
from arene import Arene

def carre(self,taille):
    i=0
    while (i<4):
        j=0
        while(j<taille):
            if (arene._robot.proximite_bruite(arene)<taille-j):
                #freine jusqua sarrete
                break
            else:
                arene._robot.avance(j+2)
                arene.update(0.5)
            j=j+2
        arene._robot.tourner()
        arene.update(0.5)
        i=i+1

