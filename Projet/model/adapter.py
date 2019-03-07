from adaptateur_virtuel import RobotVirtuel as Robot

class Adapter():

    def __init__(self):
        self._Robot=Robot()

    def action(self, code, vitesse):      # code: -1=tourner_gauche 0=avancer 1=tourner_droite
        dps=(vitesse/WHEEL_CIRCUMFERENCE)*3600
        if code==0:
            self._Robot.set_motor_dps(self._Robot.MOTOR_LEFT+self._Robot.MOTOR_RIGHT, dps)
        else:
            self._Robot.set_motor_dps(self._Robot.MOTOR_LEFT, -code*dps)
            self._Robot.set_motor_dps(self._Robot.MOTOR_RIGHT, code*dps)

    def tourner_gauche(self,vitesse):       # vitesse en cm/s
        self.action(-1,vitesse)

    def tourner_droite(self,vitesse):       # vitesse en cm/s
        self.action(1,vitesse)

    def avancer(self, vitesse):     # vitesse en cm/s
            self.action(0,vitesse)

    def get_motor_position():
        return self._Robot.get_motor_position()

    def get_distance():
        return self._Robot.get_distance()

    def get_image():
        return self._Robot.get_image()

    def offset_motor_encoder(self, port, offset):
        self._Robot.offset_motor_encoder(port, offset)

    def stop(self):
        self._Robot.stop()

    def finish(self):
        self._Robot.fin()
