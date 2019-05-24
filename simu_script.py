import time
from projet import RobotVirtuel as RobotV
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore, StrategieCarreAmeliore, StrategieArcGauche, StrategieArcDroit
from projet import lecture
from projet import View, View3D
from threading import Thread

robotv = RobotV()

view = View(robotv._arene)
view3d = View3D(robotv._arene)

robotv._arene.add_obs(view)
robotv._arene.add_obs(view3d)
robot = Adapter(robotv)

thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
thread_affichage.start()
view.start()
view3d.start()


#strat=StrategieCarre(robot, 50, 10)
#strat=StrategieCarreAmeliore(robot, 50, 40)
#strat=StrategieFonce(robot, 1, 100)
#strat=StrategieFonceAmeliore(robot, 2, 20)
strat=StrategieArcDroit(robot,40,50,360)

strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.finish()
