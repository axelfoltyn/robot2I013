import time
from projet import RobotVirtuel as RobotV
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore, StrategieCarreAmeliore
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


class StrategieCercle: # a terminer

    def __init__(self, robot, rayon, vitesse, angle):
        self._robot=robot
        self._rayon=rayon
        self._vitesse=vitesse
        self._distance=self._rayon*20/self._robot.WHEEL_DIAMETER*angle
        self._target=(self._rayon*20-self._robot.WHEEL_BASE_WIDTH)/self._robot.WHEEL_DIAMETER*angle
        self._dps=(vitesse*10/self._robot.WHEEL_CIRCUMFERENCE)*360

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
            self._robot.set_motor_dps(self._robot.MOTOR_LEFT,self._dps)
            self._robot.set_motor_dps(self._robot.MOTOR_RIGHT,self._dps*(self._distance/self._target))

    def stop(self):
        return self._robot.get_motor_position()[0]>=self._target





#strat=StrategieAvanceAmeliore(robot, 300, 100)



#strat=StrategieCarre(robot, 50, 20)
#strat=StrategieFonce(robot, 100, 1)
#strat=Strategie_tourner_droite_ameliore(robot, 360, 100)
#strat=StrategieCarreAmeliore(robot, 40, 20)
strat=StrategieCercle(robot,80,100,1440)
strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.finish()
