from Projet import RobotVirtuel

class AdaptateurVirturel:
    def __init__(self):
        text="resources/fichier_test.txt"
        # Test lecture de fichier et initialisation de l'arene
        self._arene = lecture(text)

    def tourner_droite(self, teta):
        self._arene._robot.tourner(-teta)


    def tourner_gauche(self, teta):
        self._arene._robot.tourner(teta)


    def Avancer(distance):
        self._arene._robot.avancer(distance)


    def stop():
        self._arene._robot.stop()


    def get_proximite():
        return self._arene._robot.proximite_buit(self._arene)


    def get_image():
        pass
