#tous les attribus sont protected
import str
import numpy as np

class Robot:

    def __init__(self,acceleration, x=0, y=0):  # x et y sont labscisse et lordonné
                """self*int*int*int->none"""
          fichier=open("robot.txt","r")
          f=fichier.readlines()
          f=f.strip() #suppression du retour a la ligne
          self._x, self_y=[int(elt) for elt in f.split(";")]
          #self._x=x/2
          #self._y=y/2                                           # initialise le robot au mileu de la map
          self._acceleration=[0.0,0.0]   #on initialise acceleration a la vitesse max que l'on lui attribue
          self._vitesse=[0.0,0.0]
          self._direction=[0.0,0.0]
          fichier.close()


    #a mettre dans la classe robot
    def val_accelerometre():
        MIN = 0
        MAX = 3
        res = [0,1,2]#self.acceleration;
        r= np.random.rand(3)
        res[0] += r[0] * (MAX-MIN) + MIN
        res[1] += r[1] * (MAX-MIN) + MIN
        res[2] += r[2] * (MAX-MIN) + MIN
        return res
