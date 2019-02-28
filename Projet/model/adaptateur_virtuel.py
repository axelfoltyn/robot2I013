from .robot import RobotVirtuel
from .lecture import lecture

class AdaptateurVirtuel:
    def __init__(self, controler, fps=25, resolution=None, servoPort="SERVO1",motionPort="AD1"):
        text="resources/fichier_test.txt"
        # Test lecture de fichier et initialisation de l'arene
        self._arene = lecture(text)
        self._arene._robot.add_obs(self._arene)

    def tourner_droite(self, teta):
        self._arene._robot.tourner(-teta)
        self._arene.update()


    def tourner_gauche(self, teta):
        self._arene._robot.tourner(teta)
        self._arene.update() #a enleve plus tard


    def Avancer(self,distance):
        self._arene._robot.avancer(distance)

    def get_proximite(self):
        max = 80
        self._arene.set_max_proximite(max)
        if (self._arene._robot.proximite_bruit(self._arene)<0.5):
            return 0.5
        elif (self._arene._robot.proximite_bruit(self._arene)>max):
            return max
        else :
            return self._arene._robot.proximite_bruit(self._arene)


    def get_image():
        pass

