import time
from strategie import Strategie_fonce
from Projet import Adapter as Robot


robot = Robot()
print("sjdfghsjdgf")
strat = Strategie_fonce(robot, 10, 15)

while not strat.stop():
    dt = strat.update()
    time.sleep(dt)
robot.finish()
