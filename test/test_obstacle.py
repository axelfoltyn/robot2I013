import unittest
import random
import math
from projet import ObstacleCarre, ObstacleRond


class ObstacleTestCarre(unittest.TestCase):
    def setUp(self):
        self.X = int(random.random()* 10000)
        self.Y = int(random.random()* 10000)
        self.Z = int(random.random()* 10000)
        self.LO = int(random.random()* 10000)
        self.LA = int(random.random()* 10000)
        self.obstaclec = ObstacleCarre(self.X, self.Y, self.Z, self.LO, self.LA)

    def test_cree(self):
        self.assertEqual(self.X, self.obstaclec._x)
        self.assertEqual(self.Y, self.obstaclec._y)
        self.assertEqual(self.Z, self.obstaclec._z)
        self.assertEqual(self.LO, self.obstaclec._lo)
        self.assertEqual(self.LA, self.obstaclec._la)

    def test_est_dans(self):
        x = int(random.random()* 10000)
        y = int(random.random()* 10000)
        z = int(random.random()* 10000)
        res = self.obstaclec.est_dans(x, y, z)
        self.assertEqual(res, self.X<=x and x<=self.X + self.LO and self.Y<=y and y>=self.Y - self.LA )

    def test_toString(self):
        self.assertEqual(self.obstaclec.__str__(),"C"+" "+str(self.X)+" "+str(self.Y)+" "+str(self.Z)+" "+str(self.LO)+" "+str(self.LA))


class ObstacleTestRond(unittest.TestCase):
    def setUp(self):
        self.X = int(random.random()* 10000)
        self.Y = int(random.random()* 10000)
        self.Z = int(random.random()* 10000)
        self.R = int(random.random()* 10000)
        self.obstacler = ObstacleRond(self.X, self.Y, self.Z, self.R)

    def test_rond(self):
        self.assertEqual(self.X, self.obstacler._x)
        self.assertEqual(self.Y, self.obstacler._y)
        self.assertEqual(self.Z, self.obstacler._z)
        self.assertEqual(self.R, self.obstacler._r)

    def test_est_dans(self):
        x = int(random.random()* 10000)
        y = int(random.random()* 10000)
        z = int(random.random()* 10000)
        res = self.obstacler.est_dans(x,y,z)
        self.assertEqual(res,(x-self.X)**2+(y-self.Y)**2 <= self.R**2)

    def test_toSttring(self):
        self.assertEqual(self.obstacler.__str__(),"O"+" "+str(self.X)+" "+str(self.Y)+" "+str(self.Z)+" "+str(self.R))


