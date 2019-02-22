import time
from random import *
from tkinter import *
from Projet import RobotVirtuel, Arene, Obstacle_carre, Obstacle_rond, lecture, ecriture2

text="resources/fichier_test.txt"
# Test lecture de fichier et initialisation de l'arene
arene = lecture(text)

while (True):
    while (arene.proximite() <= 55 ):
        arene._robot.stop()
        arene._robot.tourner(randint(1, 360))
    if (arene._robot._acceleration==0.0):
        arene._robot.acceleration(20)
    if (random() <= 0.10):
        ecriture2("resources/fichier_test2.txt", arene )
    if (random()<=0.0075) : #utilise pour relire le fichier
        arene = lecture("resources/fichier_test2.txt")
    arene.afficher()
    arene.update(0.40)



