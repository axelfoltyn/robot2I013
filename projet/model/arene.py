from .robot import *
from .obstacle import *

import time

class Arene:
    def __init__(self, x = 42, y = 42, z = 42,robot=None, obstacles=[],observers=[], fps=25):
        """
    int * int * int * Robot * Obstacle[] -> Arene
    L'arene contient le robot et les obstacles
    :param x: longueur de l'arène
    :param y: largeur de l'arène
    :param z: hauteur de l'arène
    """
        #inititialisation des paramètres de l'arene

        self._x = x
        self._y = y
        self._z = z
        self._robot = robot
        self._obstacles = obstacles
        self._observers = []
        self._max_proximite=100


    def add_obs(self,observer):
        self._observers.append(observer)
        pass

    def ajout_Robot(self, robot):
        """
    On peut ajouter un robot dans l'arene
    :param robot: robot a ajouter dans l'arène
    ne retourne rien
    """
        self._robot = robot

    def ajout_Obstacle(self,obstacle):
        """
    Permet d'ajouter un obstacle a notre liste d'obstacle
    :param obstacle: obstacle a ajouter
    """
        self._obstacles.append(obstacle)


    def boucle_actualiser(self, fps = 25):
        while True:
            if self._robot != None:
                self.update(1/fps)
            time.sleep(1/fps)

    #dt en s
    def update(self, dt=0.1):
        """
    Permet de mettre a jour l'arène et ses elements
    :param dt: temps en secondes represente le temps
    ecoule pendant update
    """
        t = 0.04                                #intervalle de temps par defaut (40 ms)
        if(dt <= t):                         #si le temps dt insere est inferieur a 40ms on prendra dt
            self._robot.update(dt)
            #for obs in self._observers:
            #    obs.update_arene(self,dt)
            if self.proximite() == 0:
                for obs in self._observers:
                    obs.arret(False)
        else:
            self._robot.update(t)
            #for obs in self._observers:
            #    obs.update_arene(self,t)
            self.update(dt-t)
            if self.proximite() == 0:
                for obs in self._observers:
                    obs.arret(False)
                       #on rappelle la fonction avec un dt plus petit



    def proximite(self):
        """
    Fonction qui permet au robot de changer de direction de manière aleatoire
    lorsqu'il est trop proche d'un obstacle
    """
        x_p = self._robot.x
        y_p = self._robot.y
        z_p = self._robot.z
        max = self._max_proximite #en cm
        res = 0.0
        while(res < max):
            if (x_p + self._robot._direction[0]*res < 0 or x_p + self._robot._direction[0]*res > self._x or y_p + self._robot._direction[1]*res < 0 or y_p + self._robot._direction[1]*res > self._y):
                return res
            for o in self._obstacles:
                if o.est_dans(x_p + self._robot._direction[0]*res, y_p + self._robot._direction[1]*res, z_p + self._robot._direction[2]*res):
                    return res
            res += 0.1
        return res

    def set_max_proximite(self,valeur):
        self._max_proximite=valeur

    def fin(self):
        print(self._observers)
        for obs in self._observers:
            print("arreta")
            obs.arret(True)
