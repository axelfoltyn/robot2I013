import unittest
import random
import math
<<<<<<< HEAD
from robot import Robot
=======
from Projet import RobotVirtuel
>>>>>>> dev



class RobotTest(unittest.TestCase):
    def setUp(self):

        self.X = int(random.random()* 10000)
        self.Y = int(random.random()* 10000)
        self.Z = int(random.random()* 10000)
        self.A = random.random()* 10000
        self.V = random.random()* 10000
        self.DX = random.random()* 1
        self.DY = random.random()*math.sqrt(1-self.DX**2)
        self.DZ = math.sqrt(1-self.DX**2 - self.DY**2)
<<<<<<< HEAD
        self.robot = Robot([self.X,self.Y,self.Z],self.A,self.V,[self.DX,self.DY,self.DZ])
=======
        self.robot = RobotVirtuel([self.X,self.Y,self.Z],self.A,self.V,[self.DX,self.DY,self.DZ])
>>>>>>> dev


    def test_create(self):
        self.assertEqual(self.X, self.robot._position[0])
        self.assertEqual(self.Y, self.robot._position[1])
        self.assertEqual(self.Z, self.robot._position[2])

        self.assertEqual(self.A, self.robot._acceleration)
        self.assertEqual(self.V, self.robot._vitesse)
        self.assertEqual(self.DX, self.robot._direction[0])
        self.assertEqual(self.DY, self.robot._direction[1])
        self.assertEqual(self.DZ, self.robot._direction[2])

    def test_val_accelerometre(self):
        res = self.robot.val_accelerometre()
        self.assertLessEqual(res[0], self.A * self.DX + self.robot._max_bruit_acceleration)
        self.assertLessEqual(self.A * self.DX + self.robot._min_bruit_acceleration, res[0])
        self.assertLessEqual(res[1], self.A * self.DY + self.robot._max_bruit_acceleration)
        self.assertLessEqual(self.A * self.DY + self.robot._min_bruit_acceleration, res[1])
        self.assertLessEqual(res[2], self.A * self.DZ + self.robot._max_bruit_acceleration)
        self.assertLessEqual(self.A * self.DZ + self.robot._min_bruit_acceleration, res[2])

    def test_update(self):
        dt = random.random()*100
        self.robot.update(dt)
        self.V = self.V + dt * self.A
        self.assertEqual(self.robot._position[0],  self.X + dt * self.V * self.DX)
        self.assertEqual(self.robot._position[1],  self.Y + dt * self.V * self.DY)
        self.assertEqual(self.robot._position[2],  self.Z + dt * self.V * self.DZ)

    def test_tourner(self):
        angle = random.random()*360
<<<<<<< HEAD
        self.robot.tourner(angle)
        trad = math.radians(angle)
        dx = self.DX
        dy = self.DY

        self.assertEqual(self.robot._position[0],  dx*math.cos(trad) - dy*math.sin(trad))
        self.assertEqual(self.robot._position[1],  self.DX*math.sin(trad) + self.DY*math.cos(trad))
        self.assertEqual(self.robot._position[2],  self.DZ)
=======
        trad = math.radians(angle)
        self.robot.tourner(angle)
        dx = self.DX
        dy = self.DY

        self.assertEqual(self.robot._direction[0],  dx*math.cos(trad) - dy*math.sin(trad))
        self.assertEqual(self.robot._direction[1],  self.DX*math.sin(trad) + self.DY*math.cos(trad))
        self.assertEqual(self.robot._direction[2],  self.DZ)
>>>>>>> dev

    def test_acceleration(self):
        a = random.random() * 100
        self.robot.acceleration(a)
        self.assertEqual(self.robot._acceleration, self.A + a)

    def test_stop(self):
        self.setUp()
        self.robot.stop()
        self.assertEqual(self.robot._acceleration, 0)
        self.assertEqual(self.robot._vitesse, 0)

    def test_toString(self):
<<<<<<< HEAD
        self.assertEqual(self.robot.toString() , "R"+" "+str(self.X)+" "+str(self.Y)+" "+str(self.Z)+" "+str(self.A)+" "+str(self.V)+" "+str(self.DX)+" "+str(self.DY)+" "+str(self.DZ))
=======
        self.assertEqual(str(self.robot) , "R"+" "+str(self.X)+" "+str(self.Y)+" "+str(self.Z)+" "+str(self.A)+" "+str(self.V)+" "+str(self.DX)+" "+str(self.DY)+" "+str(self.DZ))
>>>>>>> dev


if __name__=="__main__":
    unittest.main()
