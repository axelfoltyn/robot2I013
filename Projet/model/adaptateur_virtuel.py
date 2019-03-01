from .robot import RobotVirtuel
from .lecture import lecture

class AdaptateurVirtuel:
    #def __init__(self, controler, fps=25, resolution=None, servoPort="SERVO1",motionPort="AD1"):
    #    text="resources/fichier_test.txt"
    #    # Test lecture de fichier et initialisation de l'arene
    #    self._arene = lecture(text)
    #    self._arene._robot.add_obs(self._arene)
#
#    #def tourner_droite(self, teta):
#    #    self._arene._robot.tourner(-teta)
#    #    self._arene.update()
#
#
#    #def tourner_gauche(self, teta):
#    #    self._arene._robot.tourner(teta)
#    #    self._arene.update() #a enleve plus tard
#
#
#    #def Avancer(self,distance):
#    #    self._arene._robot.avancer(distance)
#
#
#
#    #def get_image():
    #    pass
    WHEEL_BASE_WIDTH         = 117                        # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5                       # diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
    MOTOR_RIGHT              = 1
    MOTOR_LEFT               = 2

    def __init__(self, controler, fps=25, resolution=None, servoPort="SERVO1",motionPort="AD1"):
        text="resources/fichier_test.txt"
        # Test lecture de fichier et initialisation de l'arene
        self._arene = lecture(text)
        self._arene._robot.add_obs(self._arene)
        self.DPS_Gauche          = 0                          # Nombre de tour du moteur gauche
        self.DPS_Droit           = 0                          # Nombre de toursdu moteur droit
        self.dt_gauche = 0
        self.dt_droite = 0
        self.offset_gauche = 0
        self.offset_droite = 0


    def set_led(self, led, red = 0, green = 0, blue = 0):
        """
        Allume une led.

        :led: une des constantes LEDs (ou plusieurs combines avec +) : LED_LEFT_EYE, LED_RIGHT_EYE, LED_LEFT_BLINKER, LED_RIGHT_BLINKER, LED_WIFI.
        :red: composante rouge (0-255)
        :green:  composante verte (0-255)
        :blue: composante bleu (0-255)
        """
        pass

    def get_voltage(self):
        """ get the battery voltage """
        pass


    def set_motor_dps(self, port, dps):
        """
        Fixe la vitesse d'un moteur en nombre de degres par seconde

        :port: une constante moteur,  MOTOR_LEFT ou MOTOR_RIGHT (ou les deux MOTOR_LEFT+MOTOR_RIGHT).
        :dps: la vitesse cible en nombre de degres par seconde
        """
        if   (port == MOTOR_LEFT):
            DPS_Gauche = dps
        elif (port  == MOTOR_RIGHT):
            DPS_Droit  = dps
        elif (port == MOTOR_RIGHT+MOTOR_LEFT):
            DPS_Gauche = dps
            DPS_Droit  = dps


    def get_motor_position(self):
        """
        Lit les etats des moteurs en degre.
        :return: couple du  degre de rotation des moteurs
        """
        return [(dt * DPS_Gauche - offset_gauche), (dt * DPS_Droit - offset_droite)]

    def offset_motor_encoder(self, port, offset):
        """
        Fixe l'offset des moteurs (en degres) (permet par exemple de reinitialiser a 0 l'etat
        du moteur gauche avec offset_motor_encode(self.MOTOR_LEFT,self.read_encoders()[0])

        :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les deux avec +)
        :offset: l'offset de decalage en degre.

        Zero the encoder by offsetting it by the current position
        """
        if port == MOTOR_LEFT:
            self.offset_gauche = offset
        elif port == MOTOR_RIGHT:
            self.offset_droite = offset
        elif port == MOTOR_RIGHT + MOTOR_LEFT:
            self.offset_gauche = offset
            self.offset_droite = offset


    def get_distance(self):
        """
        Lit le capteur de distance (en mm).
        :returns: entier distance en millimetre.
            1. L'intervalle est de **5-8,000** millimeters.
            2. Lorsque la valeur est en dehors de l'intervalle, le retour est **8190**.
        """
        min = 0.5
        max = 800
        self._arene.set_max_proximite(max)
        if (self._arene._robot.proximite_bruit(self._arene)<min):
            return min
        elif (self._arene._robot.proximite_bruit(self._arene)>max):
            return max
        else :
            return self._arene._robot.proximite_bruit(self._arene)


    def servo_rotate(self,position):
        """
        Tourne le servo a l'angle en parametre.
        :param int position: Angle de rotation, de **0** a **180** degres, 90 pour le milieu.
        """
        pass

    def stop(self):
        """ Arrete le robot """
        self.set_motor_dps(self.MOTOR_LEFT+self.MOTOR_RIGHT,0)
        self.set_led(self.LED_LEFT_BLINKER+self.LED_LEFT_EYE+self.LED_LEFT_BLINKER+self.LED_RIGHT_EYE+self.LED_WIFI,0,0,0)

    def get_image(self):
        pass


    def update(self, dt):
        dt_max = 0.2
        if dt < dt_max:
            if DPS_Droit == DPS_Gauche:
                self._arene._robot.avancer(dt * DPS_Gauche * WHEEL_CIRCUMFERENCE / 360)
            elif DPS_Gauche == -DPS_Droit:
                circonference_cm = WHEEL_CIRCUMFERENCE/10
                distance = self.get_motor_position()[1] * circonference_cm / 360
                self._arene._robot.tourner(distance * 360 / WHEEL_BASE_CIRCUMFERENCE)
                pass
        else:
            if DPS_Droit == DPS_Gauche:
                self._arene._robot.avancer(dt_max * DPS_Gauche * WHEEL_CIRCUMFERENCE / 360)
            elif DPS_Gauche == -DPS_Droit:
                circonference_cm = WHEEL_CIRCUMFERENCE/10
                distance = self.get_motor_position()[1] * circonference_cm / 360
                self._arene._robot.tourner(distance * 360 / WHEEL_BASE_CIRCUMFERENCE)
            self.update(dt - dt_max)
