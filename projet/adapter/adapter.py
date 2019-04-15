class Adapter():

    def __init__(self, robot, calibrage=1):
        self._robot=robot
        self._calibrage=calibrage
        self.WHEEL_DIAMETER=self._robot.WHEEL_DIAMETER
        self.WHEEL_BASE_WIDTH=self._robot.WHEEL_BASE_WIDTH
        self.WHEEL_CIRCUMFERENCE=self._robot.WHEEL_CIRCUMFERENCE
        self.WHEEL_BASE_CIRCUMFERENCE=self._robot.WHEEL_BASE_CIRCUMFERENCE
        self.WHEEL_CIRCUMFERENCE=self._robot.WHEEL_CIRCUMFERENCE
        #self.LED_LEFT_EYE=self._robot.LED_LEFT_EYE
        #self.LED_RIGHT_EYE=self._robot.LED_RIGHT_EYE
        #self.LED_LEFT_BLINKER=self._robot.LED_LEFT_BLINKER
        #self.LED_RIGHT_BLINKER=self._robot.LED_RIGHT_BLINKER
        #self.LED_WIFI=self._robot.LED_WIFI
        self.MOTOR_LEFT=self._robot.MOTOR_LEFT
        self.MOTOR_RIGHT=self._robot.MOTOR_RIGHT


    def set_led(self, led, red=0, green=0, blue=0):
        self._robot.set_led(led, red, green, blue)

    def get_voltage(self):
        return self._robot.get_voltage()

    def set_motor_dps(self, port, dps):
        self._robot.set_motor_dps(port, dps)

    def avancer(self, vitesse):             # vitesse en cm/s
        dps=(vitesse/self.WHEEL_CIRCUMFERENCE)*3600
        self._robot.set_motor_dps(self.MOTOR_LEFT, dps*self._calibrage)
        self._robot.set_motor_dps(self.MOTOR_RIGHT, dps/self._calibrage)

    def tourner_gauche(self,vitesse):       # vitesse en cm/s
        dps=(vitesse/self.WHEEL_CIRCUMFERENCE)*3600
        self._robot.set_motor_dps(self.MOTOR_LEFT, -dps*self._calibrage)
        self._robot.set_motor_dps(self.MOTOR_RIGHT, dps/self._calibrage)

    def tourner_droite(self,vitesse):       # vitesse en cm/s
        dps=(vitesse/self.WHEEL_CIRCUMFERENCE)*3600
        self._robot.set_motor_dps(self.MOTOR_LEFT, dps*self._calibrage)
        self._robot.set_motor_dps(self.MOTOR_RIGHT, -dps/self._calibrage)

    def get_motor_position(self):
        return self._robot.get_motor_position()

    def offset_motor_encoder(self, port, offset):
        self._robot.offset_motor_encoder(port, offset)

    def get_distance(self):
        return self._robot.get_distance()

    def servo_rotate(self, position):
        self._robot.servo_rotate(position)

    def stop(self):
        self._robot.stop()

    def get_image(self):
        return self._robot.get_image()

    # methodes supplementaires pour la simulation

    def finish(self):
        self._robot.stop()
        self._robot.fin()

    def update(self, dt):
        self._robot.update(dt)

    @property
    def pos(self): return self._robot._position
