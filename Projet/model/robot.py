import math
import numpy as np
import random
from .lecture import lecture

class RobotVirtuel:

    WHEEL_BASE_WIDTH         = 117                        # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5                       # diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
    MOTOR_RIGHT              = 1
    MOTOR_LEFT               = 2

    def __init__(self, resolution=None, servoPort="SERVO1",motionPort="AD1"):
        text="resources/fichier_test.txt"
        # Test lecture de fichier et initialisation de l'arene


        self.DPS_Gauche              = 0                          # Nombre de tour du moteur gauche
        self.DPS_Droit               = 0                          # Nombre de toursdu moteur droit

        self.dt_gauche               = 0
        self.dt_droite               = 0
        self.offset_gauche           = 0
        self.offset_droite           = 0

        self._min_bruit_acceleration = -0.1
        self._max_bruit_acceleration = 0.1
        self._min_bruit_proximite    = -1.0
        self._max_bruit_proximite    = 1.0
        self._max_distance           = 100
        self._observers              = []

        self._direction = [0,0,0]                                 #initialiser lors de la lecture
        self._position = [0,0,0]                                  #initialiser lors de la lecture
        self._vitesse = 0                                         #initialiser lors de la lecture
        self._acceleration = 0                                    #initialiser lors de la lecture

        self._arene = lecture(text,self)


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
        if   (port == self.MOTOR_LEFT):
            self.DPS_Gauche = dps
        elif (port  == self.MOTOR_RIGHT):
            self.DPS_Droit  = dps
        elif (port == self.MOTOR_RIGHT+self.MOTOR_LEFT):
            self.DPS_Gauche = dps
            self.DPS_Droit  = dps


    def get_motor_position(self):
        """
        Lit les etats des moteurs en degre.
        :return: couple du  degre de rotation des moteurs
        """
        return [(self.dt_gauche * self.DPS_Gauche - self.offset_gauche), (self.dt_droite * self.DPS_Droit - self.offset_droite)]

    def offset_motor_encoder(self, port, offset):
        """
        Fixe l'offset des moteurs (en degres) (permet par exemple de reinitialiser a 0 l'etat
        du moteur gauche avec offset_motor_encode(self.MOTOR_LEFT,self.read_encoders()[0])

        :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les deux avec +)
        :offset: l'offset de decalage en degre.

        Zero the encoder by offsetting it by the current position
        """
        if port == self.MOTOR_LEFT:
            self.offset_gauche += offset
        elif port == self.MOTOR_RIGHT:
            self.offset_droite += offset
        elif port == self.MOTOR_RIGHT + self.MOTOR_LEFT:
            self.offset_gauche += offset
            self.offset_droite += offset


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
        if (self.proximite_bruit(self._arene)<min):
            return min
        elif (self.proximite_bruit(self._arene)>max):
            return max
        else :
            return self.proximite_bruit(self._arene)


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


    def update_dt(self, dt):
        self.dt_droite += dt
        self.dt_gauche += dt

    def update(self, dt):
        dt_max = 0.2
        circonference_cm = self.WHEEL_CIRCUMFERENCE/10
        if dt < dt_max:
            self.update_dt(dt)
            if self.DPS_Gauche == self.DPS_Droit:
                self.avancer(dt * self.DPS_Gauche * circonference_cm / 360)
            elif self.DPS_Gauche == -self.DPS_Droit:
                distance = dt * self.DPS_Gauche * circonference_cm / 360
                self.tourner(distance * 360.0 / self.WHEEL_BASE_CIRCUMFERENCE)
        else:
            self.update_dt(dt_max)
            if DPS_Droit == DPS_Gauche:
                self.avancer(dt_max * DPS_Gauche * self.WHEEL_CIRCUMFERENCE / 360)
            elif DPS_Gauche == -DPS_Droit:
                distance = dt * self.DPS_Gauche * circonference_cm / 360
                self.tourner(distance * 360.0 / self.WHEEL_BASE_CIRCUMFERENCE)
            self.update(dt - dt_max)

    def fin(self):
        self._arene.fin()


    ############################################################################################################################
    ############################# SEPARATION ENTRE LES DEUX CODES ##############################################################
    ############################################################################################################################




    def val_accelerometre(self):
        """Cette  fonction renvoie la valeur de l'accelerometre en prenant en compte
            le bruit eventuelle.
        """
        MIN = self._min_bruit_acceleration
        MAX = self._max_bruit_acceleration
        res = [self._acceleration*self._direction[0], self._acceleration*self._direction[1], self._acceleration * self._direction[2]];
        r= np.random.rand(3)
        res[0] += r[0] * (MAX-MIN) + MIN
        res[1] += r[1] * (MAX-MIN) + MIN
        res[2] += r[2] * (MAX-MIN) + MIN
        return res

    def update_acceleration(self, dt = 1):
        """Cette fonction met a jour la position et la vitesse du robot
           en fonction de sa vitesse et de on acceleration
        """
        self._vitesse += dt * self._acceleration
        self._position[0] += dt * self._vitesse * self._direction[0]
        self._position[1] += dt * self._vitesse * self._direction[1]
        self._position[2] += dt * self._vitesse * self._direction[2]


    def tourner(self, teta=90):
        """
        Cette fonction fait tourner le robot d'un angle teta qui est a 90 degre par defaut
        : param teta : angle de rotation
        """
        # rotation dans le sens trigo
        d_teta = 5
        if teta > d_teta:
            self.tourner(d_teta)
            self.tourner(teta - d_teta)
        elif teta < 0 and teta < -d_teta:
            self.tourner(-d_teta)
            self.tourner(teta + d_teta)
        else:
            trad = math.radians(teta)
            dx = self._direction[0]
            dy = self._direction[1]
            self._direction[0] = dx*math.cos(trad) - dy*math.sin(trad)
            self._direction[1] = dx*math.sin(trad) + dy*math.cos(trad)
            for obs in self._observers:
                obs.update(0.01*abs(teta))



    def avancer(self,distance):
        #target=[distance*self._direction[0]+self._position[0],distance*self._direction[1]+self._position[1],distance*self._direction[2]+self._position[2]]
        #self._acceleration=100
        #while (self._position[0]<=target[0]  if self._direction[0] > 0 \
        #  else self._position[0]>=target[0]) and \
        #  (self._position[1]<=target[1]  if self._direction[1] > 0 \
        #  else self._position[1]>=target[1]):
        #    self.update(0.01)
        #    for obs in self._observers:
        #        obs.update(0.01)


        for i in [0,1,2]:
            self._position[i]=self._position[i]+self._direction[i]*distance
        #self.stop()




    def set_vitesse(self,vitesse):
        dv=vitesse-self._vitesse
        if dv>=0:
            self._acceleration=10
            while self._vitesse<vitesse:
                #self.update()
                for obs in self._observers:
                    obs.update(0.01)
        else:
            self._acceleration=-10
            while self._vitesse>vitesse:
                #self.update()
                for obs in self._observers:
                    obs.update(0.01)
        self._acceleration=0

    def acceleration(self,acceleration):
        """
        Cette fonction fait accelerer le robot
        : param acceleration : valeur de l'acceleration que l'on souhaite ajouter a l'accelaration courante
        """
        self._acceleration += acceleration      # if(self._acceleration <= 60):

    def stop(self):
        """
        Fonction STOP qui met l'acceleration et la vitesse du robot a 0
        """
        self.DPS_Gauche = 0
        self.DPS_Droit = 0
        self._acceleration=0
        self._vitesse=0

    def __str__(self):
        """
        Retourne toutes les donnees du robot sous forme de chaine de caractere
        """
        return "R"+" "+str(self._position[0])+" "+str(self._position[1])+" "+str(self._position[2])+" "+str(self._acceleration)+" "+str(self._vitesse)+" "+str(self._direction[0])+" "+str(self._direction[1])+" "+str(self._direction[2])

    def proximite_bruit(self,arene):
        MIN = self._min_bruit_proximite
        MAX = self._max_bruit_proximite
        bruit = random.random() * (MAX-MIN) + MIN
        return arene.proximite()+bruit

    def set_min_bruit_proximite(self,valeur):
        self._min_bruit_proximite=valeur

    def set_max_bruit_proximite(self,valeur):
        self._max_bruit_proximite=valeur

    def set_max_acceleration(self,valeur):
        self._max_bruit_acceleration =valeur

    def set_min_acceleration(self,valeur):
        self._min_bruit_acceleration=valeur

    def set_distance(self, valeur):
        self._max_distance=valeur

    def add_obs(self,observer):
        self._observers.append(observer)

    def set_position(self,pos1,pos2,pos3):

        """
           Cette fonction nous permet de positionner le robot
           dans l'arene
           : param pos: les parmatres donnant la position du robot
        """
        self._position[0] = pos1
        self._position[1] = pos2
        self._position[2] = pos3

    def set_acceleration(self,acceleration):
        """
            Cette fonction nous permet de donner une accleration au robot

        """
        self._acceleration = acceleration

    def set_vitesse(self,v):
        """
            Cette fonction nous peremet de défnir la vitesse du robot
            : param v : vitesse que l'on souhaite donner au robot
        """
        self._vitesse = v

    def set_direction(self,dirx,diry,dirz):
        """
           Cette fonction nous permet de definir la position du robot
           : params dir : direction dans laquelle se trouve le robot
        """
        self._direction[0] = dirx
        self._direction[1] = diry
        self._direction[2] = dirz

    def get_x(self):
        return self._position[0]

    def get_y(self):
        return self._position[1]

    def get_z(self):
        return self._position[2]

    @property
    def x(self): return self._position[0]

    @property
    def y(self): return self._position[1]

    @property
    def z(self): return self._position[2]
