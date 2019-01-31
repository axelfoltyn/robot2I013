from robot import *

robot = Robot()
robot.update()
print("Mon accéleration est : ", robot._acceleration)
print("Ma position en x est : ",robot._position[0])
print("Ma position en y est : ", robot._position[1])
print("Ma position en z est : ", robot._position[2])
print("Ma direction actuelle est : " , robot._direction)
print("Ma direction passée est : " , robot._old_direction)


print("tourner")
robot.tourner(50)
robot.update()
print("Mon accéleration est : " , robot._acceleration)
print("Ma position en x est : " , robot._position[0])
print("Ma position en y est : " , robot._position[1])
print("Ma position en z est : " , robot._position[2])
print("Ma direction actuelle est : " , robot._direction)
print("Ma direction passée est : " , robot._old_direction)


print("recup val acc")
print("lacceleration est de", robot.val_accelerometre())
robot.update()
print("Mon accéleration est : " , robot._acceleration)
print("Ma position en x est : " , robot._position[0])
print("Ma position en y est : " , robot._position[1])
print("Ma position en z est : " , robot._position[2])
print("Ma direction actuelle est : " , robot._direction)
print("Ma direction passée est : " , robot._old_direction)


print("tourner")
robot.tourner()
robot.update()
print("Mon accéleration est : " , robot._acceleration)
print("Ma position en x est : " , robot._position[0])
print("Ma position en y est : " , robot._position[1])
print("Ma position en z est : " , robot._position[2])
print("Ma direction actuelle est : " , robot._direction)
print("Ma direction passée est : " , robot._old_direction)


print("accelerer")
robot.acceleration([1,1,1])
robot.update()
print("Mon accéleration est : " , robot._acceleration)
print("Ma position en x est : " , robot._position[0])
print("Ma position en y est : " , robot._position[1])
print("Ma position en z est : " , robot._position[2])
print("Ma direction actuelle est : " , robot._direction)
print("Ma direction passée est : " , robot._old_direction)
