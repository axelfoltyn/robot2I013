import time
from tkinter import *
from projet import lecture

text="resources/fichier_test.txt"
# Test lecture de fichier et initialisation de l'arene
arene = lecture(text)

arene.update()
print("Mon acceleration est : ", arene._robot._acceleration)
print("Ma position en x est : ",arene._robot._position[0])
print("Ma position en y est : ", arene._robot._position[1])
print("Ma position en z est : ", arene._robot._position[2])
print("Ma direction actuelle est : " , arene._robot._direction)
#afficher_arene(arene)

arene.update()

print("tourner")
arene._robot.tourner(50)
arene._robot.update()
print("Mon acceleration est : " , arene._robot._acceleration)
print("Ma position en x est : " , arene._robot._position[0])
print("Ma position en y est : " , arene._robot._position[1])
print("Ma position en z est : " , arene._robot._position[2])
print("Ma direction actuelle est : " , arene._robot._direction)
#afficher_arene(arene)

arene.update()

print("recup val acc")
print("lacceleration est de", arene._robot.val_accelerometre())
arene._robot.update()
print("Mon acceleration est : " , arene._robot._acceleration)
print("Ma position en x est : " , arene._robot._position[0])
print("Ma position en y est : " , arene._robot._position[1])
print("Ma position en z est : " , arene._robot._position[2])
print("Ma direction actuelle est : " , arene._robot._direction)
#afficher_arene(arene)

arene.update()

print("tourner")
arene._robot.tourner()
arene._robot.update()
print("Mon acceleration est : " , arene._robot._acceleration)
print("Ma position en x est : " , arene._robot._position[0])
print("Ma position en y est : " , arene._robot._position[1])
print("Ma position en z est : " , arene._robot._position[2])
print("Ma direction actuelle est : " , arene._robot._direction)
#afficher_arene(arene)

arene.update()

print("accelerer")
arene._robot.acceleration(10)
arene._robot.update(0.1)
print("Mon accéleration est : " , arene._robot._acceleration)
print("Ma position en x est : " , arene._robot._position[0])
print("Ma position en y est : " , arene._robot._position[1])
print("Ma position en z est : " , arene._robot._position[2])
print("Ma direction actuelle est : " , arene._robot._direction)
#afficher_arene(arene)

arene.update(10)

#end_view()
