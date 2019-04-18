import time
from robot2I013 import Robot2I013
robot=Robot2I013()
while True:
    robot.servo_rotate(0)
    time.sleep(0.5)
    robot.servo_rotate(90)
    time.sleep(0.5)
