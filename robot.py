#tous les attribus sont protected
import math
import numpy as np

class Robot:

    def __init__(self,position=[0.0,0.0,0.0],acceleration=[0.0,0.0,0.0],vitesse=[0.0,0.0,0.0],direction[1.0,0.0,0.0]):
        self._position=position
        self._acceleration=acceleration
        self._vistesse=vitesse
        self._direction=direction
        self._old_direction=direction


    #a mettre dans la classe robot
    def val_accelerometre(self):
        MIN = 0
        MAX = 3
        res = [0,1,2]#self.acceleration;
        r= np.random.rand(3)
        res[0] += r[0] * (MAX-MIN) + MIN
        res[1] += r[1] * (MAX-MIN) + MIN
        res[2] += r[2] * (MAX-MIN) + MIN
        return res

    def update(self, dt = 1):
        self._acceleration[0] = self._acceleration[0] * self._direction[0]
        self._acceleration[1] = self._acceleration[1] * self._direction[1]
        self._acceleration[2] = self._acceleration[2] * self._direction[2]
        self._vitesse[0] = self._vitesse[0] * self._direction[0] + dt * self._acceleration[0]
        self._vitesse[1] = self._vitesse[1] * self._direction[1] + dt * self._acceleration[1]
        self._vitesse[2] = self._vitesse[2] * self._direction[2] + dt * self._acceleration[2]
        self._position[0] = self._position[0] * self._direction[0] + dt * self._vitesse[0]
        self._position[1] = self._position[1] * self._direction[1] + dt * self._vitesse[1]
        self._position[2] = self._position[2] * self._direction[2] + dt * self._vitesse[2]
    


    #a mettre dans la classe robot

    def tourner(self, teta=90):
        # la rotation s'effectue vers la gauche
        trad = math.radians(teta)
        dx = self._direction[0]
        dy = self._direction[1]
        self._direction[0] = dx*math.cos(trad) - dy*math.sin(trad)
        self._direction[1] = dx*math.sin(trad) + dy*math.sin(trad)
        
    def acceleratioon(acceleration):
        self._acceleration[0]+=acceleration[0]*direction[0]
        self._acceleration[1]+=acceleration[1]*direction[1]
        self._acceleration[2]+=acceleration[2]*direction[2]

