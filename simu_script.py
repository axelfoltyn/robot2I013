import time
from projet import RobotVirtuel as RobotV
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore, StrategieCarreAmeliore
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


class StrategieCercle: # a terminer

    def __init__(self, robot, diametre, vitesse):
        self._robot=robot
        self._diametre=diametre
        self._vitesse=vitesse
        self._target=self._distance/self._robot.WHEEL_CIRCUMFERENCE*3600

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
            robotv.set_motor_dps(1,vitesse)
            robotv.set_motor_dps(2,vitesse)

    def stop(self):
        return self._robot.get_motor_position()[0]>=self._target





#strat=StrategieAvanceAmeliore(robot, 300, 100)



#strat=StrategieCarre(robot, 50, 20)
#strat=StrategieFonce(robot, 100, 1)
#strat=Strategie_tourner_droite_ameliore(robot, 360, 100)
strat=StrategieCarreAmeliore(robot, 40, 20)
strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.finish()
