import time
from Projet import Strategie_fonce
from Projet import RobotVirtuel as RobotV
from Projet import Adapter as Robot
from Projet import lecture
from Projet import View


robotv = RobotV()

view = View(robotv.x, robotv.y)
robotv._arene.add_obs(view)
robot = Robot(robotv)


strat = Strategie_fonce(robot, 10, 15)

while not strat.stop():
    dt = strat.update()
    time.sleep(dt)
robot.finish()
