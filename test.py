import time
from Projet import Strategie_fonce, Strategie_carre
from Projet import RobotVirtuel as RobotV
from Projet import Adapter as Robot
from Projet import lecture
from Projet import View
from threading import Thread

robotv = RobotV()

view = View(robotv._arene)
robotv._arene.add_obs(view)
robot = Robot(robotv)

thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
thread_affichage.start()
view.start()


class Strategie_avance_ameliore:

    _i=2

    def __init__(self, robot, distance, vitesse,fps=25):
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
#strat = Strategie_fonce(robot, 100, 1)
#strat = Strategie_carre(robot, 100, 100)
#strat= Strategie_avance_ameliore(robot, 300, 3000)
strat =Strategie_tourner_droite_ameliore(robot,90,20)

strat.start()
while not strat.stop():
    strat.update()
    time.sleep(1/25)
print("sdqkgqsdjgfrsfhqsiuzfkhjksdf<kglvslgelfhj")
robot.finish()
