Q1.1:
import math
import numpy as np
import random
from .lecture import lecture
from PIL import Image
from ..color import color
from threading import Thread


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
        self.angleg = 0
        self.angled = 0

        self.DPS_Gauche              = 0                          # Nombre de tour du moteur gauche
        self.DPS_Droit               = 0                          # Nombre de toursdu moteur droit
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
        self._acceleration = 0                                    #initialiser lors de la lecture   <==================== changement de couleur
        self._color="pink"

        self._arene = lecture(text,self)

        self.profondeur = 6
        self.pas_pix = 0.1

=========================
pink='pink'
pink_hex='#ff1493'
ajouté dans color.py
=========================
red= 'red'
blue='blue'
black='black'
yellow='yellow'
pink='pink'
ajouté dans color
=========================



Exercice2:
Dans chaque cas j'ai ajouté les strategies aux packages
Q2.1:
class StrategieTriangleEquilateral:
    def __init__(self,robot,distance,vitesse):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse
        self._num=0
        self._strat=[StrategieAvanceAmeliore(robot,distance,vitesse),StrategieTournerDroiteAmeliore(robot,60,vitesse)]
        self._i=0

    def start(self):
        self._i=0
        self._num=0
        self._strat[0].start()

    def update(self):
        if self._strat[self._num].stop() and self._num==0:
            self._robot.avancer(0)
            self._num=1
            self._strat[self._num].start()
            self._strat[self._num].update()
        elif self._strat[self._num].stop() and self._num==1:
            self._robot.avancer(0)
            self._i+=1
            self._num=0
            if not self.stop():
                self._strat[self._num].start()
                self._strat[self._num].update()
        else:
            self._strat[self._num].update()

    def stop(self):
        return self._i>=3

Q2.2:
class StrategiePolygone:
    def __init__(self,robot,vitesse,n):
        self._robot=robot
        self._distance=30/n
        self._vitesse=vitesse
        self._num=0
        self._n=n
        self._angle=((self._n-2)*math.degrees(math.pi))/self._n
        self._strat=[StrategieAvanceAmeliore(robot,self._distance,vitesse),StrategieTournerDroiteAmeliore(robot,self._angle,vitesse)]
        self._i=0

    def start(self):
        self._i=0
        self._num=0
        self._strat[0].start()

    def update(self):
        if self._strat[self._num].stop() and self._num==0:
            self._robot.avancer(0)
            self._num=1
            self._strat[self._num].start()
            self._strat[self._num].update()
        elif self._strat[self._num].stop() and self._num==1:
            self._robot.avancer(0)
            self._i+=1
            self._num=0
            if not self.stop():
                self._strat[self._num].start()
                self._strat[self._num].update()
        else:
            self._strat[self._num].update()

    def stop(self):
        return self._i>=self._n

Q2.3:
class StrategieTour:
    def __init__(self,robot,vitesse,distance):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse
        self._vitessed=vitesse
        self._num=0
        self._strat=[StrategieFonceAmeliore(robot,self._distance,vitesse),StrategieTournerDroiteAmeliore(robot,90,vitesse)]
        self._i=0

    def start(self):
        self._i=0
        self._num=0
        self._strat[0].start()

    def update(self):
        if self._strat[self._num].stop() and self._num==0:
            self._robot.avancer(0)
            self._num=1
            self._strat[self._num].start()
            self._strat[self._num].update()
        elif self._strat[self._num].stop() and self._num==1:
            self._robot.avancer(0)
            self._i+=1
            self._num=0
            if not self.stop():
                self._strat[self._num].start()
                self._strat[self._num].update()
        else:
            self._strat[self._num].update()

    def stop(self):
        return self._i>=5
