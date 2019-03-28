import time



class Strategie_avance:

    def __init__(self, robot, distance, vitesse):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse


    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
            self._robot.avancer(self._vitesse)

    def stop(self):
        circonference_cm = self._robot.WHEEL_CIRCUMFERENCE/10
        distance = self._robot.get_motor_position()[1] * circonference_cm / 360
        return self._distance<=distance





class Strategie_tourner_droite:

    def __init__(self, robot, angle, vitesse):
        self._robot=robot
        self._angle=angle
        self._vitesse=vitesse


    def start(self):
        print("reset2.0 :", self._robot.get_motor_position()[1])
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])
        print("reset2.0 :", self._robot.get_motor_position()[1])


    def update(self):
            self._robot.tourner_droite(self._vitesse)


    def stop(self):
        target=self._angle/self._robot.WHEEL_CIRCUMFERENCE*self._robot.WHEEL_BASE_CIRCUMFERENCE
        return target<=abs(self._robot.get_motor_position()[1])

class Strategie_tourner_gauche:

    def __init__(self, robot, angle, vitesse):
        self._robot=robot
        self._angle=angle
        self._vitesse=vitesse

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])


    def update(self):

            self._robot.tourner_gauche(self._vitesse)

        return 1/fps

    def stop(self):
        circonference_cm = self._robot.WHEEL_CIRCUMFERENCE/10
        distance = self._robot.get_motor_position()[0] * circonference_cm / 360
        deta=distance * 360.0 / self._robot.WHEEL_BASE_CIRCUMFERENCE
        return self._angle<=deta



class Strategie_carre:
    def __init__(self,robot,distance,vitesse):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse
        self._num_strat=0
        self._stratege=[Strategie_avance(robot, distance,vitesse) ,Strategie_tourner_droite(robot, 90, vitesse)]
        self._i=0

    def stop(self):
        return self._i>=4


    def start(self):
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

class Strategie_fonce:
    def __init__(self,robot,vitesse,distance):
        self._robot=robot
        self._vitesse=vitesse
        self._distance=distance

    def start(self):
        self._robot.avancer(0)

    def update(self):
        self._robot.avancer(self._vitesse)

    def stop(self):
        print(self._robot.get_distance()/10.0, self._distance)
        return self._robot.get_distance()/10.0<=self._distance



class Strategie_avance_ameliore:

    _i=2

    def __init__(self, robot, distance, vitesse):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse


    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
        if(self._vitesse > 50):
            if(self.dist()):
                self._vitesse=self._vitesse/2
        if(self.stop()):
            self._robot.avancer(0)
        else:
            self._robot.avancer(self._vitesse)

    def stop(self):
        circonference_cm = self._robot.WHEEL_CIRCUMFERENCE/10
        distance = self._robot.get_motor_position()[1] * circonference_cm / 360
        return self._distance<=distance

    def dist(self):
        circonference_cm = self._robot.WHEEL_CIRCUMFERENCE/10
        distance = self._robot.get_motor_position()[1] * circonference_cm / 360
        if (distance>=self._distance-self._distance/self._i):
            self._i=self._i+1
            return True
        else:
            return False
