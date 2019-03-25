import time
from Projet import Strategie_fonce, Strategie_carre
from robot2I013 import Robot2I013 as RobotV
from Projet import Adapter as Robot
from Projet import lecture
from Projet import View
from threading import Thread

robotv = RobotV()
robot = Robot(robotv)


strat = Strategie_fonce(robot, 100, 1)
#strat = Strategie_carre(robot, 100, 100)


strat.start()
while not strat.stop():
    strat.update()
    time.sleep(1/25)
