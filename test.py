import time
from strategie import Strategie_fonce
from Projet import Adapter as Robot


robot = Robot()
strat = Strategie_fonce(robot, 10, 15)

while not strat.stop():
    dt = strat.update()
    robot.update(dt)
    print(dt)
    time.sleep(dt)
robot.finish()
