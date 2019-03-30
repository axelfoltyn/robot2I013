import time
from projet import RobotVirtuel as RobotV
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore
from projet import lecture
from projet import View
from threading import Thread

robotv = RobotV()

view = View(robotv._arene)
robotv._arene.add_obs(view)
robot = Adapter(robotv)

thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
thread_affichage.start()
view.start()

#strat=StrategieCarre(robot, 100, 10)
#strat=StrategieFonce(robot, 100, 1)
strat=StrategieFonceAmeliore(robot, 300, 40)

strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.finish()
