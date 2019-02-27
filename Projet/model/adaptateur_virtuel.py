from .robot import RobotVirtuel
from .lecture import lecture

class AdaptateurVirtuel:
    def __init__(self, controler, fps=25, resolution=None, servoPort="SERVO1",motionPort="AD1"):
        text="resources/fichier_test.txt"
        # Test lecture de fichier et initialisation de l'arene
        self._arene = lecture(text)

    def tourner_droite(self, teta):
        self._arene._robot.tourner(-teta)
        self._arene.update()


    def tourner_gauche(self, teta):
        self._arene._robot.tourner(teta)
        self._arene.update() #a enleve plus tard


    def Avancer(self,distance):
        self._arene._robot.avancer(distance)

    def get_proximite():
        self._arene.set_max_proximite(8)
        if (self._arene._robot.proximite_buit(self._arene)<0.5):
            return 0.5
        elif (self._arene._robot.proximite_buit(self._arene)>8):
            return 8
        else :
            return self._arene._robot.proximite_buit(self._arene)


    def get_image():
        pass

