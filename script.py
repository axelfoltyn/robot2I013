from Robot import *
from View import *
from Arene import *
from Obstacle import *

robot = Robot()
robot.update()
print("Mon accéleration est : ", robot._acceleration)
print("Ma position en x est : ",robot._position[0])
print("Ma position en y est : ", robot._position[1])
print("Ma position en z est : ", robot._position[2])
print("Ma direction actuelle est : " , robot._direction)


print("tourner")
robot.tourner(50)
robot.update()
print("Mon accéleration est : " , robot._acceleration)
print("Ma position en x est : " , robot._position[0])
print("Ma position en y est : " , robot._position[1])
print("Ma position en z est : " , robot._position[2])
print("Ma direction actuelle est : " , robot._direction)


print("recup val acc")
print("lacceleration est de", robot.val_accelerometre())
robot.update()
print("Mon accéleration est : " , robot._acceleration)
print("Ma position en x est : " , robot._position[0])
print("Ma position en y est : " , robot._position[1])
print("Ma position en z est : " , robot._position[2])
print("Ma direction actuelle est : " , robot._direction)


print("tourner")
robot.tourner()
robot.update()
print("Mon accéleration est : " , robot._acceleration)
print("Ma position en x est : " , robot._position[0])
print("Ma position en y est : " , robot._position[1])
print("Ma position en z est : " , robot._position[2])
print("Ma direction actuelle est : " , robot._direction)


print("accelerer")
robot.acceleration(1)
robot.update()
print("Mon accéleration est : " , robot._acceleration)
print("Ma position en x est : " , robot._position[0])
print("Ma position en y est : " , robot._position[1])
print("Ma position en z est : " , robot._position[2])
print("Ma direction actuelle est : " , robot._direction)

#Test de la classe View:

#initialisation(s) :

view = View(800,600)
view.end_view()

view2 = View(400,400)
view2.endview()

#Test de la classe Arene:

arene = Arene()
arene.endview()






