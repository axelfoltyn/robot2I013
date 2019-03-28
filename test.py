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
        print("reset :", self._robot.get_motor_position()[1])
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])
        print("reset :", self._robot.get_motor_position()[1])

    def update(self):
        if(self._vitesse > 50):
            print(self._vitesse)
            if(self.dist()):
                self._vitesse=self._vitesse/2
        if(self.stop()):
            self._robot.avancer(0)
        else:
            self._robot.avancer(self._vitesse)

    def stop(self):
        circonference_cm = self._robot.WHEEL_CIRCUMFERENCE/10
        distance = self._robot.get_motor_position()[1] * circonference_cm / 360
        print(self._distance, distance, self._distance<=distance)
        return self._distance<=distance

    def dist(self):
        circonference_cm = self._robot.WHEEL_CIRCUMFERENCE/10
        distance = self._robot.get_motor_position()[1] * circonference_cm / 360
        if (distance>=self._distance-self._distance/self._i):
            print(distance, self._distance-self._distance/self._i)
            self._i=self._i+1
            return True
        else:
            print('bloblo', distance, self._distance-self._distance/self._i)
            return False
#strat = Strategie_fonce(robot, 100, 1)
#strat = Strategie_carre(robot, 100, 100)
strat= Strategie_avance_ameliore(robot, 300, 3000)

strat.start()
while not strat.stop():
    strat.update()
    time.sleep(1/25)
print("sdqkgqsdjgfrsfhqsiuzfkhjksdf<kglvslgelfhj")
robot.finish()
