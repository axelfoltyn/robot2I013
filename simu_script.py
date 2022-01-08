import time
from projet import RobotVirtuel as RobotV
from projet import Adapter
from projet import StrategieCarreAmeliore, StrategieArcGauche, StrategieArcDroit, StrategieFonceAmeliore
from projet import lecture
from projet import View
#from projet import View3D
from threading import Thread

robotv = RobotV()

view = View(robotv._arene)
#view3d = View3D(robotv._arene)

robotv._arene.add_obs(view)
#robotv._arene.add_obs(view3d)
robot = Adapter(robotv)

thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
thread_affichage.start()
view.start()
#view3d.start()


strat1=StrategieCarreAmeliore(robot, 100, 40)
strat2=StrategieArcGauche(robot,50,50,360)
strat3=StrategieArcDroit(robot,50,50,360)
strat4=StrategieFonceAmeliore(robot, 2, 50)
strats=[strat1,strat2,strat3,strat4]

for strat in strats:
    strat.start()
    while not strat.stop():
        strat.update()
        time.sleep(0.01)
robot.finish()
