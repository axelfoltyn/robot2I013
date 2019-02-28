from robot2I013 import Robot2I013

class Adapter(Robot2I013):

    DPS=360     # constante de vitesse de rotation des roues (1 tr/s soit ~ 21 cm/s)

    def __init__(self,controler,fps=25,resolution=None,servoPort = "SERVO1",motionPort="AD1"):
        super().__init__(controler,fps,resolution,servoPort,motionPort)
        self._position_moteur=Robot2I013.get_motor_position()

    def tourner_droite(self,teta): # angle en degres
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

    def tourner_gauche(self,teta): # angle en degres
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

    def Avancer(self, vitesse):     # vitesse en cm/s
        dps=(vitesse*3600)/WHEEL_CIRCUMFERENCE
        Robot2I013.set_motor_dps(Robot2I013.MOTOR_LEFT+Robot2I013.MOTOR_RIGHT, dps)

    def get_distance():
        return Robot2I013.get_distance()

    def get_image():
        return Robot2I013.get_image()
