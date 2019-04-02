import unittest
import random
import math
from projet import RobotVirtuel



class RobotTest(unittest.TestCase):
    def setUp(self):

        self.X = 0
        self.Y = 0
        self.Z = 0
        self.A = 0
        self.V = 0
        self.DX = 0
        self.DY = 0
        self.DZ = 0
        self.robot = RobotVirtuel()


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
        trad = math.radians(angle)
        self.robot.tourner(angle)
        dx = self.DX
        dy = self.DY

        self.assertEqual(self.robot._direction[0],  dx*math.cos(trad) - dy*math.sin(trad))
        self.assertEqual(self.robot._direction[1],  self.DX*math.sin(trad) + self.DY*math.cos(trad))
        self.assertEqual(self.robot._direction[2],  self.DZ)

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
        self.assertEqual(str(self.robot) , "R"+" "+str(self.X)+" "+str(self.Y)+" "+str(self.Z)+" "+str(self.A)+" "+str(self.V)+" "+str(self.DX)+" "+str(self.DY)+" "+str(self.DZ))


    def test_set_motor_dps_gauche(self):
        a=random.random()*100
        self.robot.set_motor_dps(MOTOR_LEFT,a)
        self.assertEqual(self.robot.DPS_Gauche,a)

    def test_set_motor_dps_droit(self):
        a=random.random()*100
        self.robot.set_motor_dps(MOTOR_RIGHT,a)
        self.assertEqual(self.robot.DPS_Droit,a)

    def test_set_motor_dps_deux(self):
        a=random.random()*100
        self.robot.set_motor_dps(MOTOR_LEFT+MOTOR_RIGHT,a)
        self.assertEqual(self.robot.DPS_Gauche,a)
        self.assertEqual(self.robot.DPS_Droit,a)

    def test_offset_motor_encoder_gauche(self):
        a=random.random()*100
        self.robot.offset_motor_encoder(MOTOR_LEFT,a)
        self.assertEqual(self.robot.offset_gauche,self.offset_gauche+a)

    def test_offset_motor_encoder_droit(self):
        a=random.random()*100
        self.robot.offset_motor_encoder(MOTOR_RIGHT,a)
        self.assertEqual(self.robot.offset_droit,self.offset_droit+a)

    def test_offset_motor_encoder_deux(self):
        a=random.random()*100
        self.robot.offset_motor_encoder(MOTOR_LEFT+MOTOR_RIGHT,a)
        self.assertEqual(self.robot.offset_gauche,self.offset_gauche+a)
        self.assertEqual(self.robot.offset_droit,self.offset_droit+a)

    def test_get_motor_position(self):
        a=self.robot.get_motor_position()
        self.assertEqual(a[0],self.robot.dt_gauche * self.robot.DPS_Gauche - self.robot.offset_gauche)
        self.assertEqual(a[1],self.robot.dt_droit * self.robot.DPS_Droit - self.robot.offset_droit)

    def test_avancer(self):
        b=random.random()*100
        self.robot.avancer(b)
        self.assertEqual(self.robot._position[0],self.X+self.DX*b)
        self.assertEqual(self.robot._position[1],self.Y+self.DY*b)
        self.assertEqual(self.robot._position[2],self.Z+self.DZ*b)

    def test_set_min_bruit_proximite(self):
        val=random.random()*100
        self.robot.set_min_bruit_proximite(val)
        self.assertEqual(self.robot._min_bruit_proximite,val)

    def test_set_max_bruit_proximite(self):
        val=random.random()*100
        self.robot.set_max_bruit_proximite(val)
        self.assertEqual(self.robot._max_bruit_proximite,val)

    def test_set_max_acceleration(self):
        acc=random.random()*100
        self.robot.set_max_acceleration(acc)
        self.assertEqual(self.robot._max_bruit_acceleration,acc)

    def test_set_min_acceleration(self):
        acc=random.random()*100
        self.robot.set_min_acceleration(acc)
        self.assertEqual(self.robot._min_bruit_acceleration,acc)

    def test_set_distance(self):
        dist=random.random()*100
        self.robot.set_distance(dist)
        self.assertEqual(self.robot._max_distance,dist)

    def test_add_obs(self):
        class test_obs:
            def __init__(self):
                arreter = False
        obs=test_obs()
        self.robot.add_obs(obs)
        l=len(self.robot._observers)
        self.assertFalse(self.robot._observers[l-1].arreter)

    def test_set_position(self):
        pos1=random.random()*100
        pos2=random.random()*100
        pos3=random.random()*100
        self.robot.set_position(pos1,pos2,pos3)
        self.assertEqual(self.robot._position[0],pos1)
        self.assertEqual(self.robot._position[1],pos2)
        self.assertEqual(self.robot._position[2],pos3)

    def test_set_acceleration(self):
        val=random.random()*100
        self.robot.set_acceleration(val)
        self.assertEqual(self.robot._acceleration,val)

    def test_set_vitesse(self):
        val=random.random()*100
        self.robot.set_vitesse(val)
        self.assertEqual(self.robot._vitesse,val)

    def test_set_direction(self):
        dir1=random.random()*100
        dir2=random.random()*100
        dir3=random.random()*100
        self.robot.set_direction(dir1,dir2,dir3)
        self.assertEqual(self.robot._direction[0],dir1)
        self.assertEqual(self.robot._direction[1],dir2)
        self.assertEqual(self.robot._direction[2],dir3)


    def test_get(self):
        a=self.robot.get_x
        b=self.robot.get_y
        c=self.robot.get_z
        self.assertEqual(self.robot._position[0],a)
        self.assertEqual(self.robot._position[1],b)
        self.assertEqual(self.robot._position[2],c)


if __name__=="__main__":
    unittest.main()
