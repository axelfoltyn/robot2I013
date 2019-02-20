import math
import numpy as np
import random


class Robot:

    self._min_bruit_acceleration = -0.1
    self._max_bruit_acceleration = 0.1
    self._min_bruit_proximite = -1.0
    self._max_bruit_proximite = 1.0

    def __init__(self,position=[75,60,0],acceleration=0.0,vitesse=0.0,direction=[1.0,0.0,0.0]):
        self._position=position
        self._acceleration=acceleration
        self._vitesse=vitesse
        self._direction=direction

    def val_accelerometre(self):
        MIN = self._min_bruit_acceleration
        MAX = self._max_bruit_acceleration
        res = [self._acceleration*self._direction[0], self._acceleration*self._direction[1], self._acceleration * self._direction[2]];
        r= np.random.rand(3)
        res[0] += r[0] * (MAX-MIN) + MIN
        res[1] += r[1] * (MAX-MIN) + MIN
        res[2] += r[2] * (MAX-MIN) + MIN
        return res

    def update(self, dt = 1):
        self._vitesse += dt * self._acceleration
        self._position[0] += dt * self._vitesse * self._direction[0]
        self._position[1] += dt * self._vitesse * self._direction[1]
        self._position[2] += dt * self._vitesse * self._direction[2]

    def tourner(self, teta=90):
        # rotation dans le sens trigo
        trad = math.radians(teta)
        dx = self._direction[0]
        dy = self._direction[1]
        self._direction[0] = dx*math.cos(trad) - dy*math.sin(trad)
        self._direction[1] = dx*math.sin(trad) + dy*math.cos(trad)

    def acceleration(self,acceleration):
            self._acceleration += acceleration      # if(self._acceleration <= 60):

    def stop(self):
        self._acceleration=0
        self._vitesse=0

    def toString(self):
        return "R"+" "+str(self._position[0])+" "+str(self._position[1])+" "+str(self._position[2])+" "+str(self._acceleration)+" "+str(self._vitesse)+" "+str(self._direction[0])+" "+str(self._direction[1])+" "+str(self._direction[2])

    def proximite_bruit(self,arene):
        MIN = self._min_bruit_proximite
        MAX = self._max_bruit_proximite
        bruit = random.random() * (MAX-MIN) + MIN
        return arene.proximite()+bruit
