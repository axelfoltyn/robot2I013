import time
from Projet import Strategie_fonce
from Projet import RobotVirtuel as RobotV
from Projet import Adapter as Robot
from Projet import lecture

robotv = RobotV()

robot = Robot(robotv)


strat = Strategie_fonce(robot, 10, 15)

while not strat.stop():
    dt = strat.update()
    time.sleep(dt)
robot.finish()
