import time
from Projet import Strategie_fonce, Strategie_carre
from robot2I013 import Robot2I013 as RobotV
from Projet import Adapter as Robot

robotv = RobotV()
robot = Robot(robotv)

class strat_test:
    def __init__(self, robot, distance, vitesse):
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse


    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
            self._robot.avancer(self._vitesse)


#strat = Strategie_fonce(robot, 100, 13)
strat = Strategie_carre(robot, 20, 10)
#strat = strat_test(robot, 90, 5)

while True:
    strat.start()
    while not strat.stop():
        strat.update()
        time.sleep(0)
    print("fin boucle")
