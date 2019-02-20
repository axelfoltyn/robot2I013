import time
from random import *
from tkinter import *
from view import *
from arene import *
from robot import *
from obstacle import *
from lecture import *
from random import *
from ecriture import *

text="resources/fichier_test.txt"
# Test lecture de fichier et initialisation de l'arene
arene = lecture(text)

while (True):                                         #On crée une boucle infinie
  while (arene.proximite() <= 55 ):                   #Tant que le robot est à une distance inférieure à 55 d'un objet
    arene._robot.stop()                         #On met l'acceleration et la vitesse à 0
    arene._robot.tourner(randint(1, 360))             #Le robot tourne ensuite avec un angle qui prend une valeur aléatoire entre 0° et 360°
  if (arene._robot._acceleration==0.0):               #Si l'accélartion a été mise à 0
    arene._robot.acceleration(10)                     #On la remet à 10 l'accéleration pour que le robot reparte
  if (random() <= 0.10):
       ecriture2("resources/fichier_test.txt", arene )
  if (random()<=0.0075) :
        arene = lecture("resources/fichier_test.txt")
  arene.afficher()
  arene.update(0.40)                                  #On update l'arene toute les 40ms
