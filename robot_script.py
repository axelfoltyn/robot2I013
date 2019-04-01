import time
from robot2I013 import Robot2I013 as Robot
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore

calibrage=1 # augmenter legerement pour devier vers la droite

robot=Adapter(Robot(), calibrage)

strat=StrategieCarre(robot, 20, 10)
#strat=StrategieFonce(robot, 100, 13)
#strat=StrategieFonceAmeliore(robot, 300, 40)

strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.stop()
