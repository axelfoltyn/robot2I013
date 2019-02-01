from robot import *

class Arene:
    def __init__(self, x = 42, y = 42, z=42,robot=Robot(), obstacles=[]):
        """intxintxintxRobotxObstacle[] -> Arene"""
        self._x = x
        self._y = y
        self._z = z
        self._robot = robot
        self._obstacles = obstacles
        
