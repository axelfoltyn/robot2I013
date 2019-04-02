import time
from projet import RobotVirtuel as RobotV
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore
from projet import lecture
from projet import View
from threading import Thread

robotv = RobotV()

view = View(robotv._arene)
robotv._arene.add_obs(view)
robot = Adapter(robotv)

thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
thread_affichage.start()
view.start()


class StrategieCercle: # a terminer

    def __init__(self, robot, diametre, vitesse):
        self._robot=robot
        self._diametre=diametre
        self._vitesse=vitesse
        self._target=self._distance/self._robot.WHEEL_CIRCUMFERENCE*3600

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
            robotv.set_motor_dps(1,vitesse)
            robotv.set_motor_dps(2,vitesse)

    def stop(self):
        return self._robot.get_motor_position()[0]>=self._target


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

#strat=StrategieCarre(robot, 100, 10)
#strat=StrategieFonce(robot, 100, 1)
strat=Strategie_tourner_droite_ameliore(robot, 360, 100)

strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.finish()
