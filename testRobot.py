import time
from Projet import Strategie_fonce, Strategie_carre
from robot2I013 import Robot2I013 as RobotV
from Projet import Adapter as Robot

robotv = RobotV()
robot = Robot(robotv)

class strat_test:
    def __init__(self, robot, angle, vitesse,fps=25):
        self._robot=robot
        self._angle=angle
        self._vitesse=vitesse


    def start(self):
        print("reset2.0 :", self._robot.get_motor_position()[1])
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])
        print("reset2.0 :", self._robot.get_motor_position()[1])


    def update(self):
        if(self.stop()):
            self._robot.tourner_droite(0)
        else:
            self._robot.tourner_droite(self._vitesse)


    def stop(self):
        #print(self._robot.get_motor_position()[1])
        #circonference_cm = self._robot.WHEEL_CIRCUMFERENCE
        #distance = 2 * abs(self._robot.get_motor_position()[1]) * circonference_cm / 360
        #deta=distance * 360.0 / self._robot.WHEEL_BASE_CIRCUMFERENCE
        target=self._angle/self._robot.WHEEL_CIRCUMFERENCE*self._robot.WHEEL_BASE_CIRCUMFERENCE
        return target<=abs(self._robot.get_motor_position()[1])


strat = Strategie_fonce(robot, 100, 13)
#strat = Strategie_carre(robot, 50, 10)
#strat = strat_test(robot, 90, 5)


strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0)
robot.stop()
