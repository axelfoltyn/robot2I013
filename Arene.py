from View import *

class Arene:
    def __init__(self, x = 42, y = 42, z = 42,robot=Robot(), obstacles=[]):
        """intxintxintxRobotxObstacle[] -> Arene"""
        self._x = x
        self._y = y
        self._z = z
        self._robot = robot
        self._obstacles = obstacles
        self._view = View(x, y)
        
    def ajout_Robot(robot):
        self._robot = robot
        
    def ajout_Obstacle(obstacle):
        self._obstacles.append(obstacle) 
        
    def afficher():
        self._view.clear()
        for i in obstacle :
            self._view.affiche_obstacle(i)
        self._view.afficher_robot(self._robot)
