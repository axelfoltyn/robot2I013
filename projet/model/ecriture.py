from .arene import *
from .robot import *
from .obstacle import *

def ecriture2(fichier, arene):
    Fichier=open(fichier,"w")
    Fichier.write(str(arene._x)+"\n")                   #Nous ouvrons un fichier pour le quel nous lui
    Fichier.write(str(arene._y)+"\n")                   #donnons en premier la valeur de x=abscisse
    Fichier.write(str(arene._z)+"\n")                   #puis la valeur y=ordonne et la valeur z=hauteur
                                                        #Nous ajoutons ensuite les obstacles qui viennent de arene
    for i in arene._obstacles :                         #Pas besoin decrire parametre par parametre, on ecrit tout directement avec un cast en string
        Fichier.write(str(i)+"\n")                      #On fait de meme avec le robot qui vient de arene puis nous fermons le fichier que nous avons ouvert

    Fichier.write(str(arene._robot)+"\n")
    Fichier.close()
