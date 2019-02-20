import math
import numpy as np
import random


MIN = -0.1
MAX = 0.1

class Robot:



    def __init__(self,position=[75,60,0],acceleration=0.0,vitesse=0.0,direction=[1.0,0.0,0.0]):
        """Cette fonction inotialise un robot 
        : param position     : position du robot 
        : param acceleration : acceleration du robot 
        : param vitesse      : vitesse du robot 
        : param direction    : direction du robot 
        """
        self._position=position              # initialisation des parametres du robot 
        self._acceleration=acceleration
        self._vitesse=vitesse
        self._direction=direction
        self._min_bruit_acceleration = -0.1
        self._max_bruit_acceleration = 0.1
        self._min_bruit_proximite = -1.0
        self._max_bruit_proximite = 1.0

    def val_accelerometre(self):
        """Cette  fonction renvoie la valeur de l'accelerometre en prenant en compte 
           le bruit éventuelle. 
        """
        MIN = self._min_bruit_acceleration
        MAX = self._max_bruit_acceleration
        res = [self._acceleration*self._direction[0], self._acceleration*self._direction[1], self._acceleration * self._direction[2]];
        r= np.random.rand(3)
        res[0] += r[0] * (MAX-MIN) + MIN
        res[1] += r[1] * (MAX-MIN) + MIN
        res[2] += r[2] * (MAX-MIN) + MIN
        return res

    def update(self, dt = 1):
        """Cette fonction met à jour la position et la vitesse du robot 
           en fonction de sa vitesse et de on acceleration
        """
        self._vitesse += dt * self._acceleration
        self._position[0] += dt * self._vitesse * self._direction[0]
        self._position[1] += dt * self._vitesse * self._direction[1]
        self._position[2] += dt * self._vitesse * self._direction[2]

    def tourner(self, teta=90):
        """
        Cette fonction fait tourner le robot d'un angle teta qui est à 90° par défaut
        : param teta : angle de rotation 
        """
        # rotation dans le sens trigo
        trad = math.radians(teta)
        dx = self._direction[0]
        dy = self._direction[1]
        self._direction[0] = dx*math.cos(trad) - dy*math.sin(trad)
        self._direction[1] = dx*math.sin(trad) + dy*math.cos(trad)

    def acceleration(self,acceleration):
        """
        Cette fonction fait accélérer le robot 
        : param acceleration : valeur de l'acceleration que l'on souhaite ajouter à l'accelaration courante
        """
            self._acceleration += acceleration      # if(self._acceleration <= 60):

    def stop(self):
        """
        Fonction STOP qui met l'acceleration et la vitesse du robot à 0
        """
        self._acceleration=0
        self._vitesse=0

    def toString(self):
        """
        Retourne toutes les données du robot sous forme de chaine de caractere 
        """
        return "R"+" "+str(self._position[0])+" "+str(self._position[1])+" "+str(self._position[2])+" "+str(self._acceleration)+" "+str(self._vitesse)+" "+str(self._direction[0])+" "+str(self._direction[1])+" "+str(self._direction[2])

    def proximite_bruit(self,arene):
        MIN = self._min_bruit_proximite
        MAX = self._max_bruit_proximite
        bruit = random.random() * (MAX-MIN) + MIN
        return arene.proximite()+bruit
