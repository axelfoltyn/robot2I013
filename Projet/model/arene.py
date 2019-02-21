from .robot import *
from ..view.view import View

class arene:
    def __init__(self, x = 42, y = 42, z = 42,robot=Robot(), obstacles=[]):
        """int * int * int * Robot * Obstacle[] -> Arene"""
        self._x = x
        self._y = y
        self._z = z
        self._robot = robot
        self._obstacles = obstacles
        self._view = View(x, y)
        
    def ajout_Robot(self, robot):
        self._robot = robot
        
    def ajout_Obstacle(self,obstacle):
        self._obstacles.append(obstacle) 
        
    def afficher(self):
        self._view.clear()
        for i in self._obstacles :
            self._view.afficher_obstacle(i)
        self._view.afficher_robot(self._robot)

    #dt en s
    def update(self, dt = 1):
        t = 0.04
        self.afficher()
        if(dt <= t):
            self._robot.update(dt)
            #for i in self._obstacles :
            #    i.update(dt)
            self._view.update(dt)
        else:
            self._robot.update(t)
            #for i in self._obstacles :
            #    i.update(t)
            self._view.update(t)
            self.update(dt-t)
    
    def proximite(self):
        x_p = self._robot._position[0]
        y_p = self._robot._position[1]
        z_p = self._robot._position[2]
        max = 100.0 #en cm
        res = 0.0
        while(res < max):
            if (x_p + self._robot._direction[0]*res < 0 or x_p + self._robot._direction[0]*res > self._x or y_p + self._robot._direction[1]*res < 0 or y_p + self._robot._direction[1]*res > self._y):
                return res
            for o in self._obstacles:
                if o.est_dans(x_p + self._robot._direction[0]*res, y_p + self._robot._direction[1]*res, z_p + self._robot._direction[2]*res):
                    return res
            res += 0.1
        return res
