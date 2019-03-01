import time

class Strategie_avance:

    def __init__(self, robot, distance, vitesse,fps=25):
        self._robot=robot
        self._distance=distance
        self._t=time.time()
        self._vitesse=vitesse

    def update(self):
        if(self.stop())
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
        if(self.stop())
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
        if(self.stop())
            self._robot.tourner_gauche(0)
        else:
            self._robot.tourner_gauche(self._vitesse)

        return 1/fps

    def stop(self):
        dt=(time.time()-self._t)
        return self._angle<=dt*self._vitesse
