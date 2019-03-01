from robot2I013 import Robot2I013

class AdaptateurRobot(Robot2I013):

    DPS=360     # vitesse de rotation des roues (en mouvement) fixees a 1 tr/s soit ~ 21 cm/s

    def __init__(self,controler,fps=25,resolution=None,servoPort = "SERVO1",motionPort="AD1"):
        super().__init__(controler,fps,resolution,servoPort,motionPort)
        self._position_moteur=Robot2I013.get_motor_position()

    def tourner_droite(self,teta): # teta en degree
        self._position_moteur=Robot2I013.get_motor_position()
        Robot2I013.offset_motor_encoder(Robot2I013.MOTOR_LEFT, self._position_moteur[0])
        target=teta*(WHEEL_BASE_CIRCUMFERENCE/WHEEL_CIRCUMFERENCE)
        Robot2I013.set_motor_dps(Robot2I013.MOTOR_LEFT, DPS)
        Robot2I013.set_motor_dps(Robot2I013.MOTOR_RIGHT, -DPS)
        while self._position_moteur[0] < target:
            self._position_moteur=Robot2I013.get_motor_position()
        Robot2I013.stop()

    def tourner_gauche(self,teta): # teta en degree
        self._position_moteur=Robot2I013.get_motor_position()
        Robot2I013.offset_motor_encoder(Robot2I013.MOTOR_LEFT, self._position_moteur[1])
        target=teta*(WHEEL_BASE_CIRCUMFERENCE/WHEEL_CIRCUMFERENCE)
        Robot2I013.set_motor_dps(Robot2I013.MOTOR_LEFT, -DPS)
        Robot2I013.set_motor_dps(Robot2I013.MOTOR_RIGHT, +DPS)
        while self._position_moteur[1] < target:
            self._position_moteur=Robot2I013.get_motor_position()
        Robot2I013.stop()

    def avancer(self, distance):        # distance en cm
        self._position_moteur=Robot2I013.get_motor_position()
        Robot2I013.offset_motor_encoder(Robot2I013.MOTOR_LEFT, self._position_moteur[0])
        target=(distance/WHEEL_CIRCUMFERENCE)*3600
        Robot2I013.set_motor_dps(Robot2I013.MOTOR_LEFT+Robot2I013.MOTOR_RIGHT, DPS)
        while self._position_moteur[0] < target:
            self._position_moteur=Robot2I013.get_motor_position()
        Robot2I013.stop()
