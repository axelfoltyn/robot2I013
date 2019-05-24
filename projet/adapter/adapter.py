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
        """
        Allume une led.

        :led: une des constantes LEDs (ou plusieurs combines avec +) : LED_LEFT_EYE, LED_RIGHT_EYE, LED_LEFT_BLINKER, LED_RIGHT_BLINKER, LED_WIFI.
        :red: composante rouge (0-255)
        :green:  composante verte (0-255)
        :blue: composante bleu (0-255)
        """
        self._robot.set_led(led, red, green, blue)

    def get_voltage(self):
        """ retourne batteri voltage """
        return self._robot.get_voltage()

    def set_motor_dps(self, port, dps):
        self._robot.set_motor_dps(port, dps)

    def avancer(self, vitesse):             # vitesse en cm/s
    """
        Fixe la vitesse d'un moteur en nombre de degres par seconde
        :port: une constante moteur,  MOTOR_LEFT ou MOTOR_RIGHT (ou les deux MOTOR_LEFT+MOTOR_RIGHT).
        :dps: la vitesse cible en nombre de degres par seconde
        """
        dps=(vitesse/self.WHEEL_CIRCUMFERENCE)*3600
        self._robot.set_motor_dps(self.MOTOR_LEFT, dps*self._calibrage)
        self._robot.set_motor_dps(self.MOTOR_RIGHT, dps)

    def tourner_gauche(self,vitesse):       # vitesse en cm/s
        dps=(vitesse/self.WHEEL_CIRCUMFERENCE)*3600
        self._robot.set_motor_dps(self.MOTOR_LEFT, -dps*self._calibrage)
        self._robot.set_motor_dps(self.MOTOR_RIGHT, dps)

    def tourner_droite(self,vitesse):       # vitesse en cm/s
        dps=(vitesse/self.WHEEL_CIRCUMFERENCE)*3600
        self._robot.set_motor_dps(self.MOTOR_LEFT, dps*self._calibrage)
        self._robot.set_motor_dps(self.MOTOR_RIGHT, -dps)

    def get_motor_position(self):
        """
        Lit les etats des moteurs en degre.
        :return: couple du  degre de rotation des moteurs
        """
        offset=self._robot.get_motor_position()
        return (offset[0]/self._calibrage,offset[1])

    def offset_motor_encoder(self, port, offset):
        """
        Fixe l'offset des moteurs (en degres) (permet par exemple de reinitialiser a 0 l'etat
        du moteur gauche avec offset_motor_encode(self.MOTOR_LEFT,self.get_motor_position()[0])

        :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les deux avec +)
        :offset: l'offset de decalage en degre.
        Zero the encoder by offsetting it by the current position
        """
        self._robot.offset_motor_encoder(port, offset)

    def get_distance(self):
        """
        Lit le capteur de distance (en mm).
        :returns: entier distance en millimetre.
            1. L'intervalle est de **5-8,000** millimeters.
            2. Lorsque la valeur est en dehors de l'intervalle, le retour est **8190**.
        """
        return self._robot.get_distance()

    def servo_rotate(self, position):
        """
        Tourne le servo a l'angle en parametre.
        :param int position: Angle de rotation, de **0** a **180** degres, 90 pour le milieu.
        """
        self._robot.servo_rotate(position)

    def stop(self):
         """ Arrete le robot """
        self._robot.stop()

    def get_image(self):
        return self._robot.get_image()

    # methodes supplementaires pour la simulation

    def finish(self):
        """ Arrete le robot lorsque la fonction est terminer"""
        self._robot.stop()
        self._robot.fin()
