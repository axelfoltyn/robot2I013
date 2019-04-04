import unittest
import random
import math
from projet import ObstacleCarre, ObstacleRond, ObstacleBalise


class ObstacleTestCarre(unittest.TestCase):
    def setUp(self):
        self.X = int(random.random()* 10000)
        self.Y = int(random.random()* 10000)
        self.Z = int(random.random()* 10000)
        self.LO = int(random.random()* 10000)
        self.LA = int(random.random()* 10000)
        self.COLOR = 0xff00ff
        self.obstaclec = ObstacleCarre(self.X, self.Y, self.Z, self.LO, self.LA,self.COLOR)

    def test_cree(self):
        self.assertEqual(self.X, self.obstaclec._x)
        self.assertEqual(self.Y, self.obstaclec._y)
        self.assertEqual(self.Z, self.obstaclec._z)
        self.assertEqual(self.LO, self.obstaclec._lo)
        self.assertEqual(self.LA, self.obstaclec._la)
        self.assertEqual(self.COLOR,self.obstaclec.color)

    def test_est_dans(self):
        x = int(random.random()* 10000)
        y = int(random.random()* 10000)
        z = int(random.random()* 10000)
        res = self.obstaclec.est_dans(x, y, z)
        x1=self.X
        x2=self.X+self.LO
        y1=self.Y
        y2=self.Y-self.LA
        self.assertEqual(res, x>=x1 and x<= x2 and y<=y1 and y>=y2 )

    def test_toString(self):
        self.assertEqual(self.obstaclec.__str__(),"C"+" "+str(self.X)+" "+str(self.Y)+" "+str(self.Z)+" "+str(self.LO)+" "+str(self.LA)+" "+str(self.obstaclec.color))


class ObstacleTestRond(unittest.TestCase):
    def setUp(self):
        self.X = int(random.random()* 10000)
        self.Y = int(random.random()* 10000)
        self.Z = int(random.random()* 10000)
        self.R = int(random.random()* 10000)
        self.COLOR = 0xff00ff
        self.obstacler = ObstacleRond(self.X, self.Y, self.Z, self.R,self.COLOR)

    def test_rond(self):
        self.assertEqual(self.X, self.obstacler._x)
        self.assertEqual(self.Y, self.obstacler._y)
        self.assertEqual(self.Z, self.obstacler._z)
        self.assertEqual(self.R, self.obstacler._r)
        self.assertEqual(self.COLOR,self.obstacler.color)

    def test_est_dans(self):
        x = int(random.random()* 10000)
        y = int(random.random()* 10000)
        z = int(random.random()* 10000)
        res = self.obstacler.est_dans(x,y,z)
        self.assertEqual(res,(x-self.X)**2+(y-self.Y)**2 <= self.R**2)

    def test_toSttring(self):
        self.assertEqual(self.obstacler.__str__(),"O"+" "+str(self.X)+" "+str(self.Y)+" "+str(self.Z)+" "+str(self.R)+" "+str(self.obstacler.color))


class ObstacleTestBalise(unittest.TestCase):
    def setUp(self):
        self.X= int(random.random()* 10000)
        self.Y= int(random.random()* 10000)
        self.Z= int(random.random()* 10000)
        self.LO= int(random.random()* 10000)
        self.LA= int(random.random()* 10000)
        self.HAUT= int(random.random()* 10000)
        self.COLOR1='0xff0000'
        self.COLOR2='0x00ff00'
        self.COLOR3='0x0000ff'
        self.COLOR4='0xffff00'
        self.obstacleb=ObstacleBalise(self.X,self.Y,self.Z,self.LO,self.LA,self.HAUT,self.COLOR1,self.COLOR2,self.COLOR3,self.COLOR4)

    def test_cree(self):
        self.assertEqual(self.X,self.obstacleb._x)
        self.assertEqual(self.Y,self.obstacleb._y)
        self.assertEqual(self.Z,self.obstacleb._z)
        self.assertEqual(self.LO,self.obstacleb.lo)
        self.assertEqual(self.LA,self.obstacleb.la)
        self.assertEqual(self.HAUT,self.obstacleb.haut)
        self.assertEqual(self.COLOR1,self.obstacleb.color1)
        self.assertEqual(self.COLOR2,self.obstacleb.color2)
        self.assertEqual(self.COLOR3,self.obstacleb.color3)
        self.assertEqual(self.COLOR4,self.obstacleb.color4)

    def test_est_dans(self):
        x=int(random.random()* 10000)
        y=int(random.random()* 10000)
        z=int(random.random()* 10000)
        x1=self.obstacleb._x
        x2=self.obstacleb._x+self.obstacleb.lo
        y1=self.obstacleb._y
        y2=self.obstacleb._y+self.obstacleb.la
        z1=self.obstacleb._z
        z2=self.obstacleb._z+self.obstacleb.haut
        res=self.obstacleb.est_dans(x,y,z)
        self.assertEqual(res,x>=x1 and x<=x2 and y<=y1 and y>=y2 and z>=z1 and z<=z2)

    def test_toString(self):
        self.assertEqual(self.obstacleb.__str__(),"B"+" "+str(self.X)+" "+str(self.Y)+" "+str(self.Z)+" "+str(self.LO)+" "+str(self.LA)+" "+str(self.COLOR1)+" "+str(self.COLOR2)+" "+str(self.COLOR3)+" "+str(self.COLOR4))

    def test_getColor(self):
        x=int(random.random()* 10000)
        y=int(random.random()* 10000)
        z=int(random.random()* 10000)
        res=self.obstacleb.getColor(x,y,z)


        if (x>self.X) and (x<self.X+self.LO/2):
            if (y>self.Y) and (y<self.Y+self.LA/2):
                self.assertEqual(res,self.COLOR1)
            elif (y>self.Y+self.LA/2) and (y<self.Y+self.LO):
                self.assertEqual(res,self.COLOR3)
            else :
                self.assertEqual(res,1)
        elif(x>self.X+self.LO/2) and (x<self.X+self.LO):
            if (y>self.Y) and (y<self.Y+self.LA/2):
                self.assertEqual(res,self.COLOR2)
            elif (y>self.Y+self.LA/2) and (y<self.Y+self.LO):
                self.assertEqual(res,self.COLOR4)
            else :
                self.assertEqual(res,1)
        else:
            self.assertEqual(res,1)
