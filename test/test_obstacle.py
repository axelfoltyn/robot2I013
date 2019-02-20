import unittest
import random
import math
from obstaclec import Obstacle_carre


class ObstacleTestCarre(unittest,TestCase):
    def setUp(self):
        self.X = int(random.random()* 10000)
        self.Y = int(random.random()* 10000)
        self.Z = int(random.random()* 10000)
        self.LO = int(random.random()* 10000)
        self.LA = int(random.random()* 10000)
        self.obstaclec = ObstacleTestCarre(self.X, self.Y, self.Z, self.LO, self.LA)

    def test_cree(self):
        self.assertEqual(self.X, self.obstaclec._x)
        self.assertEqual(self.X, self.obstaclec._y)
        self.assertEqual(self.X, self.obstaclec._z)
        self.assertEqual(self.X, self.obstaclec._lo)
        self.assertEqual(self.X, self.obstaclec._la)

    def test_est_dans(self, x, y, z):
        res = obstaclec.est_dans(x, y, z)
        self.assertEqual(res, self.obstaclec.X<=x and x<=self.obstaclec.X + self.obstaclec.LO and self.obstaclec.Y<=y and y>=self.obstaclec.Y - self.obstaclec.LA )

    def test_toString(self)
        self.assertEqual(self.obstaclec.toString(),"C"+" "+str(self.X)+" "+str(self.Y)+" "+str(self.Z)+" "+str(self.LO)+" "+str(self.LA))

        
class ObstacleTestRond(unittest, TestCase):
    def setUp(self):
        self.X = int(random.random()* 10000)
        self.Y = int(random.random()* 10000)
        self.Z = int(random.random()* 10000)
        self.R = int(random.random()* 10000)
        self.obstacler = ObstacleTestRond(self.X, self.Y, self.Z, self.R)

    def test_rond(self):
        self.assertEqual(self.X, self.obstacler._x)
        self.assertEqual(self.Y, self.obstacler._y)
        self.assertEqual(self.Z, self.obstacler._z)
        self.assertEqual(self.R, self.obstacler._r)

    def test_est_dans(self, x, y, z):
        res = obstacler.est_dans(x,y,z)
        self.assertEqual(res,(x-self.X)**2+(y-self.X)**2 <= self.R**2)

    def test_toSttring(self):
        self.assertEqual(self.obstacler.toString(),"O"+" "+str(self.X)+" "+str(self.Y)+" "+str(self.Z)+" "+str(self.R))

    
