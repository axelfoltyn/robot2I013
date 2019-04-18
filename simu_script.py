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

robot = Adapter(robotv)

thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
thread_affichage.start()
view.start()
view3d.start()


#strat=StrategieAvanceAmeliore(robot, 300, 100)



#strat=StrategieCarre(robot, 50, 20)
#strat=StrategieFonce(robot, 100, 1)
#strat=Strategie_tourner_droite_ameliore(robot, 360, 100)
#strat=StrategieCarreAmeliore(robot, 40, 20)
strat=StrategieArcGauche(robot,50,50,360)

strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)

strat=StrategieArcDroit(robot,50,50,360)
strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.finish()
