import time
from projet import Strategie_fonce, Strategie_carre
from projet import RobotVirtuel as RobotV
from projet import Adapter as Robot
from projet import lecture
from projet import View
from threading import Thread

robotv = RobotV()

view = View(robotv._arene)
robotv._arene.add_obs(view)
robot = Robot(robotv)

thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
thread_affichage.start()
view.start()


class Strategie_fonce_ameliore:

    di = 0.3
    _i=di

    def __init__(self,robot,vitesse,distance):
        self._robot=robot
        self._vitesse=vitesse
        self._distance=distance

    def start(self):
        pass

    def update(self):
        if self._vitesse > 10:
            if self.dist():
                self._i += self.di
                self._vitesse=self._vitesse/2
        self._robot.avancer(self._vitesse)


    def dist(self):
        print(self._robot.get_distance()/10.0, self._distance*(1+1/self._i))
        return self._robot.get_distance()/10.0<=self._distance*(1+1/self._i)

    def stop(self):
        return self._robot.get_distance()/10.0<=self._distance
#strat = Strategie_fonce(robot, 100, 1)
#strat = Strategie_carre(robot, 100, 10)
strat= Strategie_fonce_ameliore(robot, 300, 40)

strat.start()
while not strat.stop():
    strat.update()
    time.sleep(1/25)
robot.finish()
