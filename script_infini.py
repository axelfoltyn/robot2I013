from Robot import *
from View import *
from Arene import *
from Obstacle import *
from lecture import *
from tkinter import *
import time
from random import *

text="resources/fichier_test.txt"
# Test lecture de fichier et initialisation de l'arene
arene = lecture(text)

while (True):
  print("Ma distance est : " , arene.proximite())
  while (arene.proximite() <= 55 ):
    arene._robot._vitesse=0.0
    arene._robot._acceleration=0.0
    print("tourne")
    arene._robot.tourner(randint(1, 360))
    print("lalala")
    #arene.update(0.40)
    print("Ma distance est : " , arene.proximite())
  if (arene._robot._acceleration==0.0):
    arene._robot.acceleration(10)
    print("lblblb")
  arene.afficher()
  arene.update(0.40)
