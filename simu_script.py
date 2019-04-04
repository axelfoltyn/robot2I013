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

    def __init__(self, robot, rayon, vitesse):
        self._robot=robot
        self._rayon=rayon
        self._vitesse=vitesse
        dps=(vitesse/self.WHEEL_CIRCUMFERENCE)*3600
        self._target=self._rayon*2/self._robot.WHEEL_DIAMETER*3600

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
            self._robot.set_motor_dps(self._robot.MOTOR_LEFT,dps)
            self._robot.set_motor_dps(self._robot.MOTOR_RIGHT,dps+self._rayon*10/self._robot.WHEEL_DIAMETER)

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
