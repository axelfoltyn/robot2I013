from View import *
from Robot import *
from Obstacle import *

class Arene:
    def __init__(self, x = 42, y = 42, z = 42,robot=Robot(), obstacles=[]):
        """intxintxintxRobotxObstacle[] -> Arene"""
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
            #    i.update(0.45)
            self._view.update(t)
            self.update(dt-t)
            
