import unittest
import random
import math
from Projet import Robot

class RobotVirtuelTest(unittest.TestCase):
    def setUp(self):

        self.X = int(random.random()* 10000)
        self.Y = int(random.random()* 10000)
        self.Z = int(random.random()* 10000)
        self.A = random.random()* 10000
        self.V = random.random()* 10000
        self.DX = random.random()* 1
        self.DY = random.random()*math.sqrt(1-self.DX**2)
        self.DZ = math.sqrt(1-self.DX**2 - self.DY**2)
        self.robot = Robot([self.X,self.Y,self.Z],self.A,self.V,[self.DX,self.DY,self.DZ])
        self.DPS_Gauche=random.random()*(360/60)
        self.DPS_Droit=random.random()*(360/60)
        self.offset_gauche=0
        self.offset_droit=0

    def soso(self):
        pass





