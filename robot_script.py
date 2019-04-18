import time
from robot2I013 import Robot2I013 as Robot
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore, StrategieCarreAmeliore, StrategieArcGauche, StrategieArcDroit

calibrage=1.007 # defaut=1 , augmenter legerement pour devier vers la droite

robot=Adapter(Robot(), calibrage)

#VITESSE MAX = 20.9

#strat=StrategieFonceAmeliore(robot, 2, 20)
#strat=StrategieFonce(robot, 5, 20)
#strat=StrategieFonceAmeliore(robot, 300, 40)
strat=StrategieArcGauche(robot,10,10,360*2)
strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.stop()
