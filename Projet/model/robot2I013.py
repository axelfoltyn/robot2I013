import time
import math

class Robot2I013(object):
    """
    Classe d'encapsulation du robot et des senseurs.
    Constantes disponibles :
    LED (controle des LEDs) :  LED_LEFT_EYE, LED_RIGHT_EYE, LED_LEFT_BLINKER, LED_RIGHT_BLINKER, LED_WIFI
    MOTEURS (gauche et droit) : MOTOR_LEFT, MOTOR_RIGHT
    et les constantes ci-dessous qui definissent les elements physiques du robot
    """

    WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)

    def __init__(self,controler,fps=25,resolution=None,servoPort = "SERVO1",motionPort="AD1"):
        """
            Initialise le robot

            :controler: le controler du robot, muni d'une fonction update et d'une fonction stop qui
                        rend in booleen (vrai a la fin du controle, faux sinon)
            :fps: nombre d'appel a controler.update() par seconde (approximatif!)
            :resolution: resolution de la camera
            :servoPort: port du servo (SERVO1 ou SERVO2)
            :motionPort: port pour l'accelerometre (AD1 ou AD2)
        """

        text="resources/fichier_test.txt"
        # Test lecture de fichier et initialisation de l'arene
        self.arene = lecture(text)

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
        self._gpg.set_motor_dps(port,dps)
        self.set_motor_limits(port,dps)


    def get_motor_position(self):
        """
        Lit les etats des moteurs en degre.
        :return: couple du  degre de rotation des moteurs
        """
        pass

    def offset_motor_encoder(self, port, offset):
        """
        Fixe l'offset des moteurs (en degres) (permet par exemple de reinitialiser a 0 l'etat
        du moteur gauche avec offset_motor_encode(self.MOTOR_LEFT,self.read_encoders()[0])

        :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les deux avec +)
        :offset: l'offset de decalage en degre.

        Zero the encoder by offsetting it by the current position
        """
        pass

    def get_distance(self):
        """
        Lit le capteur de distance (en mm).
        :returns: entier distance en millimetre.
            1. L'intervalle est de **5-8,000** millimeters.
            2. Lorsque la valeur est en dehors de l'intervalle, le retour est **8190**.
        """
        return self.arene._robot.proximite_bruit(self.arene)


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


