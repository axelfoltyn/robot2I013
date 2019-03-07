from adaptateur_virtuel import RobotVirtuel as Robot

class Adapter(Robot):

    def __init__(self,controler,fps=25,resolution=None,servoPort = "SERVO1",motionPort="AD1"):
        super().__init__(controler,fps,resolution,servoPort,motionPort)

    def action(self, code, vitesse):      # code: -1=tourner_gauche 0=avancer 1=tourner_droite
        dps=(vitesse/WHEEL_CIRCUMFERENCE)*3600
        if code==0:
            Robot.set_motor_dps(Robot.MOTOR_LEFT+Robot.MOTOR_RIGHT, dps)
        else:
            Robot.set_motor_dps(Robot.MOTOR_LEFT, -code*dps)
            Robot.set_motor_dps(Robot.MOTOR_RIGHT, code*dps)

    def tourner_gauche(self,vitesse):       # vitesse en cm/s
        self.action(-1,vitesse)

    def tourner_droite(self,vitesse):       # vitesse en cm/s
        self.action(1,vitesse)

    def avancer(self, vitesse):     # vitesse en cm/s
            self.action(0,vitesse)

    def get_motor_position():
        return Robot.get_motor_position()

    def get_distance():
        return Robot.get_distance()

    def get_image():
        return Robot.get_image()

    def offset_motor_encoder(self, port, offset):
        Robot.offset_motor_encoder(port, offset)

    def stop(self):
        Robot.stop()
