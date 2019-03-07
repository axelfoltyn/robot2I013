import math
import numpy as np
import random

class RobotVirtuel:



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
        self._max_distance = 100
        self._observers = []

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

    def update(self, dt = 1):
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
        target=[distance*self._direction[0]+self._position[0],distance*self._direction[1]+self._position[1],distance*self._direction[2]+self._position[2]]
        self._acceleration=100
        while (self._position[0]<=target[0]  if self._direction[0] > 0 \
          else self._position[0]>=target[0]) and \
          (self._position[1]<=target[1]  if self._direction[1] > 0 \
          else self._position[1]>=target[1]):
            #self.update(0.01)
            for obs in self._observers:
                obs.update(0.01)
        self.stop()




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
