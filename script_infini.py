import time
from random import *
from tkinter import *
from view import *
from arene import *
from robot import *
from obstacle import *
from lecture import *
from ecriture import *

text="resources/test.txt"
# Test lecture de fichier et initialisation de l'arene
arene = lecture(text)

while (True):
    while (arene.proximite() <= 55 ):
        arene._robot.stop()
        arene._robot.tourner(randint(1, 360))
    if (arene._robot._acceleration==0.0):
        arene._robot.acceleration(20)
    #if (random() <= 0.10):
    #   ecriture2("resources/test.txt", arene )
    arene.afficher()
    arene.update(0.40)
