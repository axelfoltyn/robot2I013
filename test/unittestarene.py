import unittest
import random
import math
from projet import View
from projet import RobotVirtuel
from projet import Obstacle_carre, Obstacle_rond
from projet import Arene

class TestArene(unittest.TestCase):
    def setUp(self):
        self.X = int(random.random()* 10000)
        self.Y = int(random.random()* 10000)
        self.Z = int(random.random()* 10000)
        self.robot = RobotVirtuel([self.X,self.Y,self.Z],self.A,self.V,[self.DX,self.DY,self.DZ])
        self.obstacles = []
        self.view = View(self.X, self.Y)
        self.arene = Arene(self.X, self.Y, self.Z, self.robot, self.obstacles )


    def Test_cree(self):
        self.assertEqual(self.X, self.arene._x)
        self.assertEqual(self.Y, self.arene._y)
        self.assertEqual(self.Z, self.arene._z)

        self.assertEqual(self.X, self.arene._robot._position[0])
        self.assertEqual(self.Y, self.arene._robot._position[1])
        self.assertEqual(self.Z, self.arene._robot._position[2])
        self.assertEqual(self.obstacles, self.arene._obstacles)
        self.assertEqual(self.view_x, self.arene._view_x)
        self.assertEqual(self.view_y, self.arene._view_y)

    def Test_update(self):
        dt = random.random()*100
        self.arene.update(dt)

        self.assertEqual(arene.robot._position[0],  robot.X + dt * robot.V * self.DX)
        self.assertEqual(arene.robot._position[1],  robot.Y + dt * robot.V * self.DY)
        self.assertEqual(arene.robot._position[2],  robot.Z + dt * robot.V * self.DZ)
