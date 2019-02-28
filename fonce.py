from Projet import RobotVirtuel
from random import randint
import sys

def fonce(robot):
    while (True):
        if(robot.get_proximite() == 5):
            break
        robot.Avancer(robot.get_proximite() - 2)

