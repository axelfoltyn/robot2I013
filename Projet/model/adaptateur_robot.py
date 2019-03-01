from robot2I013 import Robot2I013

class AdaptateurRobot(Robot2I013):

    DPS=360     # vitesse de rotation des roues (en mouvement) fixees a 1 tr/s soit ~ 21 cm/s

    def __init__(self,controler,fps=25,resolution=None,servoPort = "SERVO1",motionPort="AD1"):
        super().__init__(controler,fps,resolution,servoPort,motionPort)
        self._position_moteur=Robot2I013.get_motor_position()

    def tourner_droite(self,teta):
        self._position_moteur=Robot2I013.get_motor_position()
        Robot2I013.offset_motor_encoder(Robot2I013.MOTOR_LEFT, self._position_moteur[0])
        Robot2I013.offset_motor_encoder(Robot2I013.MOTOR_RIGHT, self._position_moteur[1])
        distance=(teta/360)*WHEEL_BASE_CIRCUMFERENCE
        nb_tours=(distance*10)//WHEEL_CIRCUMFERENCE
        reste=(distance*10)%WHEEL_CIRCUMFERENCE
        cpt=0
        Robot2I013.set_motor_dps(Robot2I013.MOTOR_LEFT, DPS)
        while True:
            temp=self._position_moteur[0]
            self._position_moteur=Robot2I013.get_motor_position()
            if temp>self._position_moteur[0]:
                cpt+=1
            delta_position=(self._position_moteur[0]/360)*WHEEL_CIRCUMFERENCE
            if cpt == nb_tours and delta_position >= reste:
                break
        Robot2I013.stop()

    def tourner_gauche(self,teta):
        self._position_moteur=Robot2I013.get_motor_position()
        Robot2I013.offset_motor_encoder(Robot2I013.MOTOR_LEFT, self._position_moteur[0])
        Robot2I013.offset_motor_encoder(Robot2I013.MOTOR_RIGHT, self._position_moteur[1])
        distance=(teta/360)*WHEEL_BASE_CIRCUMFERENCE
        nb_tours=(distance*10)//WHEEL_CIRCUMFERENCE
        reste=(distance*10)%WHEEL_CIRCUMFERENCE
        cpt=0
        Robot2I013.set_motor_dps(Robot2I013.MOTOR_RIGHT, DPS)
        while True:
            temp=self._position_moteur[1]
            self._position_moteur=Robot2I013.get_motor_position()
            if temp>self._position_moteur[1]:
                cpt+=1
            delta_position=(self._position_moteur[1]/360)*WHEEL_CIRCUMFERENCE
            if cpt == nb_tours and delta_position >= reste:
                break
        Robot2I013.stop()

    def avancer(self, distance):        # distance en cm
        self._position_moteur=Robot2I013.get_motor_position()
        Robot2I013.offset_motor_encoder(Robot2I013.MOTOR_LEFT, self._position_moteur[0])
        Robot2I013.offset_motor_encoder(Robot2I013.MOTOR_RIGHT, self._position_moteur[1])
        target=(distance*10)/(WHEEL_CIRCUMFERENCE*360)
        Robot2I013.set_motor_dps(Robot2I013.MOTOR_LEFT+Robot2I013.MOTOR_RIGHT, DPS)
        while self._position_moteur < target:
            self._position_moteur=Robot2I013.get_motor_position()
        Robot2I013.stop()

    def get_proximite():
        """
        Lit le capteur de distance (en mm).
        :returns: entier distance en millimetre.
            1. L'intervalle est de **5-8,000** millimeters.
            2. Lorsque la valeur est en dehors de l'intervalle, le retour est **8190**.
        """
        return Robot2I013.get_distance()

    def get_image():
        return Robot2I013.get_image()
