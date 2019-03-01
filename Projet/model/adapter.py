from robot2I013 import Robot2I013

class Adapter(Robot2I013):

    def __init__(self,controler,fps=25,resolution=None,servoPort = "SERVO1",motionPort="AD1"):
        super().__init__(controler,fps,resolution,servoPort,motionPort)

    def action(self, code, vitesse):      # code: -1=tourner_gauche 0=avancer 1=tourner_droite
        dps=(vitesse/WHEEL_CIRCUMFERENCE)*3600
        if code==0:
            Robot2I013.set_motor_dps(Robot2I013.MOTOR_LEFT+Robot2I013.MOTOR_RIGHT, dps)
        else:
            Robot2I013.set_motor_dps(Robot2I013.MOTOR_LEFT, -code*dps)
            Robot2I013.set_motor_dps(Robot2I013.MOTOR_RIGHT, code*dps)

    def tourner_gauche(self,vitesse):       # vitesse en cm/s
        self.action(-1,vitesse)

    def tourner_droite(self,vitesse):       # vitesse en cm/s
        self.action(1,vitesse)

    def avancer(self, vitesse):     # vitesse en cm/s
            self.action(0,vitesse)

    def get_motor_position():
        return Robot2I013.get_motor_position()

    def get_distance():
        return Robot2I013.get_distance()

    def get_image():
        return Robot2I013.get_image()

    def offset_motor_encoder(self, port, offset):
        Robot2I013.offset_motor_encoder(port, offset)

    def stop(self):
        Robot2I013.stop()
