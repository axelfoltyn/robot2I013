import time
from projet import RobotVirtuel as RobotV
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore, StrategieCarreAmeliore, StrategieArcGauche, StrategieArcDroit, StrategieTriangleEq10, StrategiePolygone, StrategieContour
from projet import lecture
from projet import View, View3D
from threading import Thread

robotv = RobotV()

view = View(robotv._arene)
robotv._arene.add_obs(view)
robot = Adapter(robotv)

thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
thread_affichage.start()
view.start()


#strat=StrategieAvanceAmeliore(robot, 300, 100)
#strat=StrategieCarre(robot, 50, 20)
#strat=StrategieFonce(robot, 100, 1)
#strat=Strategie_tourner_droite_ameliore(robot, 360, 100)
#strat=StrategieCarreAmeliore(robot, 40, 20)

strat=StrategieTriangleEq10(robot,10, 10) # 1 pixel = 1 cm

#strat=StrategiePolygone(robot, 2, 8)
# des erreurs de précision lors de la rotation sont présentes, celles-ci s'accroissent beaucoup lorsque le nombre de cotés est élevé
#c'est pourquoi il faut nettement baisser la vitesse (surtout pour 20 cotés)

#strat=StrategieContour(robot, 45, 100) # le robot virtuel est un poil plus long que le réel, sa tête frote un peu le mur du coup.
#pour ce qui est du robot réel la stratégie doit sûrement fonctionner à merveille.

strat.start()
while not strat.stop():
    print("position du robot:   ",robotv.x,robotv.y,robotv.z)
    strat.update()
    time.sleep(0.01)
robot.finish()
