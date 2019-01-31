#tous les attribus sont protected
import str
import math
import numpy as np

class Robot:

    def __init__(self,acceleration=0, x=0, y=0, z=0):  # x et y sont labscisse et lordonné
                """self*int*int*int->none"""
          fichier=open("robot.txt","r")
          f=fichier.readlines()
          f=f.strip() #suppression du retour a la ligne
          self._position =[int(elt) for elt in f.split(";")]
          #self._x=x/2
          #self._y=y/2                                           # initialise le robot au mileu de la map
          self._acceleration=[0.0,0.0,0.0]   #on initialise acceleration a la vitesse max que l'on lui attribue
          self._vitesse=[0.0,0.0,0.0]
          self._direction=[0.0,0.0,0.0]
          self._old_direction=[0.0,0.0,0.0]
          fichier.close()


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
	trad = math.radian(teta)
	dx = self._direction[0]
	dy = self._direction[1]
	self._direction[0] = dx*math.cos(trad) - dy*math.sin(trad)
	self._direction[1] = dx*math.sin(trad) + dy*math.sin(trad)
	vx = self._vitesse[0]
	vy = self._vitesse[1]
	self._vitesse[0] = vx*math.cos(trad) - vy*math.sin(trad)
	self._vitesse[1] = vx*math.sin(trad) + vy*math.sin(trad)
	ax = self._acceleration[0]
	ay = self._acceleration[1]
	self._acceleraion[0] = ax*math.cos(trad) - ay*math.sin(trad)
	self._acceleraion[1] = ax*math.sin(trad) + ay*math.sin(trad)
	return
