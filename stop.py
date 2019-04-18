from robot2I013 import Robot2I013
robot=Robot2I013()
robot.set_motor_dps(3,0)
robot.offset_motor_encoder(robot.MOTOR_LEFT, robot.get_motor_position()[0])
robot.offset_motor_encoder(robot.MOTOR_RIGHT, robot.get_motor_position()[1])
robot.servo_rotate(30)
