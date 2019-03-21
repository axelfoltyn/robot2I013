class Adapter():

    def __init__(self, Robot):
        self._Robot=Robot

    def action(self, code, vitesse):      # code: -1=tourner_gauche 0=avancer 1=tourner_droite
        dps=(vitesse/self._Robot.WHEEL_CIRCUMFERENCE)*3600
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

    def get_motor_position(self):
        return self._Robot.get_motor_position()

    def get_distance(self):
        return self._Robot.get_distance()

    def get_image(self):
        return self._Robot.get_image()

    def offset_motor_encoder(self, port, offset):
        self._Robot.offset_motor_encoder(port, offset)

    def stop(self):
        self._Robot.stop()

    def finish(self):
        self._Robot.stop()
        self._Robot.fin()

    def update(self, dt):
        self._Robot.update(dt)

    @property
    def WHEEL_CIRCUMFERENCE(self): return self._Robot.WHEEL_CIRCUMFERENCE

    @property
    def WHEEL_BASE_CIRCUMFERENCE(self): return self._Robot.WHEEL_BASE_CIRCUMFERENCE

    @property
    def MOTOR_LEFT(self): return self._Robot.MOTOR_LEFT

    @property
    def MOTOR_RIGHT(self): return self._Robot.MOTOR_RIGHT
