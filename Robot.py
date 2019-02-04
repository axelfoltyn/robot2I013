import math
import random

class Robot:

    def __init__(self,position=[75.0,60.0,0.0],acceleration=0.0,vitesse=0.0,direction=[1.0,0.0,0.0]):
        self._position=position
        self._acceleration=acceleration
        self._vitesse=vitesse
        self._direction=direction


    def val_accelerometre(self):
        res = self._acceleration
        res += random.random()*0.02-0.01
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
        self._direction[1] = dx*math.sin(trad) + dy*math.sin(trad)
        
    def acceleration(self,acceleration):
        self._acceleration += acceleration

