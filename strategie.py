import time
from Projet import RobotVirtuel as Robot
from Projet import Arene as arene


class Strategie_avance:

    def __init__(self, robot, distance, vitesse,fps=25,):
        self._robot=robot
        self._distance=distance
        self._t=time.time()
        self._vitesse=vitesse
        self._

    def update(self):
        if(self.stop()):
            self._robot.avancer(0)
        else:
            self._robot.avancer(self._vitesse)
        return 1/fps

    def stop(self):
        dt=(time.time()-self._t)
        return self._distance<=dt*self._vitesse





class Strategie_tourner_droite:

    def __init__(self, robot, angle, vitesse,fps=25):
        self._robot=robot
        self._angle=angle
        self._t=time.time()
        self._vitesse=vitesse

    def update(self):
        if(self.stop()):
            self._robot.tourner_droite(0)
        else:
            self._robot.tourner_droite(self._vitesse)

        return 1/fps


    def stop(self):
        dt=(time.time()-self._t)
        return self._angle<=dt*self._vitesse



class Strategie_tourner_gauche:

    def __init__(self, robot, angle, vitesse,fps=25):
        self._robot=robot
        self._angle=angle
        self._t=time.time()
        self._vitesse=vitesse

    def update(self):
        if(self.stop()):
            self._robot.tourner_gauche(0)
        else:
            self._robot.tourner_gauche(self._vitesse)

        return 1/fps

    def stop(self):
        dt=(time.time()-self._t)
        return self._angle<=dt*self._vitesse



class Strategie_carre:
    def __init__(self,robot,distance,vitesse,fps=25):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse
        self._num_strat=0
        self._stratege=[Strategie_avancer(robot, distance,vitesse) ,Strategie_tourner_droite(robot, 90, vitesse)]
        self._i=0

    def stop(self):
        return self._i>=4


    def update(self):
        dt=1/fps
        if self.stop():
            return dt
        if self._stratege[self._num_strat].stop() and self._num_strat==0:
            self._num_strat=1
            self._stratege[self._num_strat].update()
        elif self._stratege[self._num_strat].stop() and self._num_strat==1:
            self._i+=1
            self._num_strat=0
            if not self.stop():
                self._stratege[self._num_strat].update()
        return dt

class Strategie_fonce:
    def __init__(self,robot,vitesse,distance,fps=25):
        self._robot=robot
        self._vitesse=vitesse
        self._distance=distance
        self.fps = fps

    def update(self):
        if(self.stop()):
            self._robot.avancer(0)
        else:
            self._robot.avancer(self._vitesse)
        return 1/self.fps


    def stop(self):
        return self._robot.get_distance()<=self._distance

