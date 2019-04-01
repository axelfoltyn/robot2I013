import time


class StrategieAvance:

    def __init__(self, robot, distance, vitesse):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse
        self._target=self._distance/self._robot.WHEEL_CIRCUMFERENCE*3600

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
            self._robot.avancer(self._vitesse)

    def stop(self):
        return self._robot.get_motor_position()[0]>=self._target


class StrategieTournerDroite:

    def __init__(self, robot, angle, vitesse):
        self._robot=robot
        self._angle=angle
        self._vitesse=vitesse
        self._target=self._angle*self._robot.WHEEL_BASE_CIRCUMFERENCE/self._robot.WHEEL_CIRCUMFERENCE

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
            self._robot.tourner_droite(self._vitesse)

    def stop(self):
        return self._robot.get_motor_position()[0]>=self._target


class StrategieTournerGauche:

    def __init__(self, robot, angle, vitesse):
        self._robot=robot
        self._angle=angle
        self._vitesse=vitesse
        self._target=self._angle*self._robot.WHEEL_BASE_CIRCUMFERENCE/self._robot.WHEEL_CIRCUMFERENCE

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])

    def update(self):
        self._robot.tourner_gauche(self._vitesse)

    def stop(self):
        return self._robot.get_motor_position()[1]>=self._target


class StrategieCarre:

    def __init__(self, robot, distance, vitesse):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse
        self._num_strat=0
        self._strategie=[StrategieAvance(robot, distance,vitesse), StrategieTournerDroite(robot, 90, vitesse)]
        self._i=0

    def start(self):
        self._i=0
        self._num_strat=0
        self._strategie[0].start()

    def update(self):
        if self._strategie[self._num_strat].stop() and self._num_strat==0:
            self._robot.avancer(0)
            self._num_strat=1
            self._strategie[self._num_strat].start()
            self._strategie[self._num_strat].update()
        elif self._strategie[self._num_strat].stop() and self._num_strat==1:
            self._robot.avancer(0)
            self._i+=1
            self._num_strat=0
            if not self.stop():
                self._strategie[self._num_strat].start()
                self._strategie[self._num_strat].update()
        else:
            self._strategie[self._num_strat].update()

    def stop(self):
        return self._i>=4


class StrategieFonce:

    def __init__(self, robot, distance, vitesse):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse

    def start(self):
        pass

    def update(self):
        self._robot.avancer(self._vitesse)

    def stop(self):
        return self._robot.get_distance()/10.0<=self._distance


class StrategieAvanceAmeliore:

    _i=2

    def __init__(self, robot, distance, vitesse):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse
        self._target=self._distance/self._robot.WHEEL_CIRCUMFERENCE*3600

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
        if(self._vitesse > 10):
            if(self.dist()):
                self._vitesse=self._vitesse/2
        else:
            self._robot.avancer(self._vitesse)

    def stop(self):
        return self._robot.get_motor_position()[0]>=self._target

    def dist(self):
        if self._robot.get_motor_position()[0]>=self._target/(1-self._i):
            self._i=self._i+1
            return True
        else:
            return False

class Strategie_tourner_droite_ameliore:

    _i=2

    def __init__(self, robot, angle, vitesse):
        self._robot=robot
        self._angle=angle
        self._vitesse=vitesse


    def start(self):
        print("reset2.0 :", self._robot.get_motor_position()[1])
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])
        print("reset2.0 :", self._robot.get_motor_position()[1])


    def update(self):
        print("v=", self._vitesse)
        if(self._vitesse>10):
            if(self.dist()):
                self._vitesse = self._vitesse / 2
        self._robot.tourner_droite(self._vitesse)


    def stop(self):

        target=self._angle/self._robot.WHEEL_CIRCUMFERENCE*self._robot.WHEEL_BASE_CIRCUMFERENCE
        print("tfvtftftftftftf", target, abs(self._robot.get_motor_position()[1]))
        return target<=abs(self._robot.get_motor_position()[1])


    def dist(self):
        target=self._angle/self._robot.WHEEL_CIRCUMFERENCE*self._robot.WHEEL_BASE_CIRCUMFERENCE
        print("uhyfhdygxcjfh", abs(self._robot.get_motor_position()[1]),target*(1-1/self._i))
        if (abs(self._robot.get_motor_position()[1])>=target*(1-1/self._i)):
            self._i=self._i*2
            return True
        else:
            return False


class Strategie_carre:
    def __init__(self,robot,distance,vitesse):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse
        self._num_strat=0
        self._stratege=[Strategie_avance(robot, distance,vitesse) ,Strategie_tourner_droite_ameliore(robot, 90, vitesse)]
        self._i=0

    def stop(self):
        return self._i>=4


    def start(self):
        self._i = 0
        self._num_strat=0
        self._stratege[0].start()



    def update(self):
        if self._stratege[self._num_strat].stop() and self._num_strat==0:
            self._robot.avancer(0)
            self._num_strat=1
            self._stratege[self._num_strat].start()
            self._stratege[self._num_strat].update()
        elif self._stratege[self._num_strat].stop() and self._num_strat==1:
            self._robot.avancer(0)
            self._i+=1
            self._num_strat=0
            if not self.stop():
                self._stratege[self._num_strat].start()
                self._stratege[self._num_strat].update()
        else:
            self._stratege[self._num_strat].update()


class StrategieFonceAmeliore:

    di=0.7
    _i=di

    def __init__(self, robot, vitesse, distance): # !!!probleme quand on inverse distance et vitesse
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse

    def start(self):
        pass

    def update(self):
        if self._vitesse>10:
            if self.dist():
                self._i+=self.di
                self._vitesse=self._vitesse/2
        self._robot.avancer(self._vitesse)

    def dist(self):
        print(self._robot.get_distance()/10.0, self._distance*(1+1/self._i))
        return self._robot.get_distance()/10.0<=self._distance*(1+1/self._i)

    def stop(self):
        return self._robot.get_distance()/10.0<=self._distance
