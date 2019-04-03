import unittest
import random
import math
from projet import RobotVirtuel, Arene



class RobotTest(unittest.TestCase):

    WHEEL_BASE_WIDTH         = 117                        # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5                       # diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
    MOTOR_RIGHT              = 1
    MOTOR_LEFT               = 2

    def setUp(self):

        self.X = 100
        self.Y = 300
        self.Z = 0.0
        self.A = 0
        self.V = 0
        self.DX = 1.0
        self.DY = 0
        self.DZ = 0.0
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

        self.assertEqual(self.robot._direction[0], self.robot._direction[0]+dx*math.cos(trad) - dy*math.sin(trad))
        self.assertEqual(self.robot._direction[1], self.robot._direction[1]+self.DX*math.sin(trad) + self.DY*math.cos(trad))
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




    def test_set_motor_dps_gauche(self):
        a=random.random()*100
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,a)
        self.assertEqual(self.robot.DPS_Gauche,a)

    def test_set_motor_dps_droit(self):
        a=random.random()*100
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,a)
        self.assertEqual(self.robot.DPS_Droit,a)

    def test_set_motor_dps_deux(self):
        a=random.random()*100
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,a)
        self.assertEqual(self.robot.DPS_Gauche,a)
        self.assertEqual(self.robot.DPS_Droit,a)

    def test_offset_motor_encoder_gauche(self):
        o=self.robot.offset_gauche
        a=random.random()*100
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,a)
        self.assertEqual(self.robot.offset_gauche,o+a)

    def test_offset_motor_encoder_droit(self):
        o=self.robot.offset_droite
        a=random.random()*100
        self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,a)
        self.assertEqual(self.robot.offset_droite,o+a)

    def test_offset_motor_encoder_deux(self):
        o1=self.robot.offset_gauche
        o2=self.robot.offset_droite
        a=random.random()*100
        self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,a)
        self.assertEqual(self.robot.offset_gauche,o1+a)
        self.assertEqual(self.robot.offset_droite,o2+a)

    def test_get_motor_position(self):
        a=[]
        a=self.robot.get_motor_position()
        self.assertEqual(a[0],self.robot.angleg - self.robot.offset_gauche)
        self.assertEqual(a[1],self.robot.angled - self.robot.offset_droite)

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
        l1=len(self.robot._observers)
        self.robot.add_obs(obs)
        l2=len(self.robot._observers)
        self.assertEqual(l1+1,l2)

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
        a=self.robot.get_x()
        b=self.robot.get_y()
        c=self.robot.get_z()
        self.assertEqual(self.robot._position[0],a)
        self.assertEqual(self.robot._position[1],b)
        self.assertEqual(self.robot._position[2],c)

    def test_set_led(self):
        pass

    def test_get_voltage(self):
        pass

    def test_servo_rotate(self):
        pass

    def test_get_image(self):
        pass

    #def test_stop2(self):    pass

    def test_update_acceleration(self):
        self.robot.update_acceleration()
        self.assertEqual(self.robot._vitesse,self.A)
        self.assertEqual(self.robot._position[0],self.X+self.robot._vitesse*self.DX)
        self.assertEqual(self.robot._position[1],self.Y+self.robot._vitesse*self.DY)
        self.assertEqual(self.robot._position[2],self.Z+self.robot._vitesse*self.DZ)


    def test_update_dt(self):
        dt1=self.robot.angled
        dt2=self.robot.angleg
        dt=random.random()*100
        self.robot.update_dt(dt)
        self.assertEqual(self.robot.angled,dt1+dt*self.robot.DPS_Droit)
        self.assertEqual(self.robot.angleg,dt2+dt*self.robot.DPS_Gauche)


    #def test_get_distance(self):
    #    res=self.robot.getdistance()
    #    self.assertLessEqual(res,800)
    #    self.assertLessEqual(0.5,res)

    def test_fin(self):
        pass

    def test_proximite_bruit(self):
        ar=Arene()
        res=self.robot.proximite_bruit(ar)
        self.assertLessEqual(res,ar.proximite()+self.robot._max_bruit_proximite)
        self.assertLessEqual(ar.proximite()+self.robot._min_bruit_proximite,res)


if __name__=="__main__":
    unittest.main()
