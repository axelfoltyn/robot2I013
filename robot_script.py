import time
from robot2I013 import Robot2I013 as Robot
from projet import Adapter
from projet import Strategie_fonce, Strategie_carre, Strategie_fonce_ameliore

calibrage=1 # augmenter legerement pour devier vers la droite

robot=Adapter(Robot(), calibrage)

strat=Strategie_carre(robot, 20, 10)
#strat=Strategie_fonce(robot, 100, 13)
#strat=Strategie_fonce_ameliore(robot, 300, 40)

strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.stop()
