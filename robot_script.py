import time
from robot2I013 import Robot2I013 as Robot
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore

calibrage=0.999 # defaut=1 , augmenter legerement pour devier vers la droite

robot=Adapter(Robot(), calibrage)

#VITESSE MAX = 20.9

#strat=StrategieCarre(robot, 20, 10)
strat=StrategieFonce(robot, 10, 20)
#strat=StrategieFonceAmeliore(robot, 300, 40)

strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.stop()
