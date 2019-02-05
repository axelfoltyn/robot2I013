from Robot import *
from View import *
from Arene import *
from Obstacle import *
from lecture import *

text="resources/fichier_test.txt"
# Test lecture de fichier et initialisation de l'arene
arene = lecture(text)

arene._robot.update()
print("Mon accéleration est : ", arene._robot._acceleration)
print("Ma position en x est : ",arene._robot._position[0])
print("Ma position en y est : ", arene._robot._position[1])
print("Ma position en z est : ", arene._robot._position[2])
print("Ma direction actuelle est : " , arene._robot._direction)
arene.afficher()

print("tourner")
arene._robot.tourner(50)
arene._robot.update()
print("Mon accéleration est : " , arene._robot._acceleration)
print("Ma position en x est : " , arene._robot._position[0])
print("Ma position en y est : " , arene._robot._position[1])
print("Ma position en z est : " , arene._robot._position[2])
print("Ma direction actuelle est : " , arene._robot._direction)
arene.afficher()

print("recup val acc")
print("lacceleration est de", arene._robot.val_accelerometre())
arene._robot.update()
print("Mon accéleration est : " , arene._robot._acceleration)
print("Ma position en x est : " , arene._robot._position[0])
print("Ma position en y est : " , arene._robot._position[1])
print("Ma position en z est : " , arene._robot._position[2])
print("Ma direction actuelle est : " , arene._robot._direction)
arene.afficher()

print("tourner")
arene._robot.tourner()
arene._robot.update()
print("Mon accéleration est : " , arene._robot._acceleration)
print("Ma position en x est : " , arene._robot._position[0])
print("Ma position en y est : " , arene._robot._position[1])
print("Ma position en z est : " , arene._robot._position[2])
print("Ma direction actuelle est : " , arene._robot._direction)
arene.afficher()

print("accelerer")
arene._robot.acceleration(1)
arene._robot.update()
print("Mon accéleration est : " , arene._robot._acceleration)
print("Ma position en x est : " , arene._robot._position[0])
print("Ma position en y est : " , arene._robot._position[1])
print("Ma position en z est : " , arene._robot._position[2])
print("Ma direction actuelle est : " , arene._robot._direction)

arene.afficher()

arene._view._endview()









