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

#strat = Strategie_fonce(robot, 100, 1)
strat = Strategie_carre(robot, 100, 100)


strat.start()
while not strat.stop():
    strat.update()
    time.sleep(1/25)
