import time
from Projet import Strategie_fonce, Strategie_carre
from Projet import RobotVirtuel as RobotV
#from Projet import Robot2I013 as RobotV
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

#strat = Strategie_fonce(robot, 10, 15)
strat = Strategie_carre(robot, 10, 15)



while not strat.stop():
    strat.update()
    #robotv._arene.update(1/25)
    time.sleep(1/25)
robot.finish()
