from robot import *
from view import *
from arene import *
from obstacle import *
from lecture import *
from tkinter import *
import time
from random import *

text="resources/fichier_test.txt"
# Test lecture de fichier et initialisation de l'arene
arene = lecture(text)

while (True):
    while (arene.proximite() <= 55 ):
        arene._robot.stop()
        arene._robot.tourner(randint(1, 360))
    if (arene._robot._acceleration==0.0):
        arene._robot.acceleration(100)
    arene.afficher()
    arene.update(0.40)
