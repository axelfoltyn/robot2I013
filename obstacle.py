import math

class Obstacle :
    #les verifications se font par rapport au nom O = Obstacle rond et C = Obstacle Carre
    def __init__(self,x,y,z=0,nom='O',r=1.0,lo=0.0,la=0.0):        #Initialisation des arguments
        self._nom=nom
        self._x=x
        self._y=y
        self._z=z
        self._r=r
        self._lo=lo
        self._la=la

    def est_dans(self,x,y,z):                                       #On vérifie si l'objet de coordonées x,y,z se trouve dans l'obstacle
        if (self._nom=='C'):                                        #Si c'est un rectangle
            x1=self._x                                              #x1 ,x2 , y1 et y2 représentent les quatres points du rcetangle(Carre)
            x2=self._x + self._lo
            y1=self._y
            y2=self._y - self._la
            return x>=x1 and x<= x2 and y<=y1 and y>=y2             #Si les coordonées de l'objet touchent le rectangle ou sont dedans
        if (self._nom=='O'):                                        #Pour un obstacle Rond
            return (x-self._x)**2+(y-self._y)**2 <= self._r**2      #On verifie si les coordonées de l'objet se trouvent dans le cercle

    def toString(self):
        return ""


class Obstacle_carre(Obstacle):

    def __init__(self,x,y,z=0,r=1.0,lo=0.0,la=0.0):        #Initialisation des arguments
        self._x=x
        self._y=y
        self._z=z
        self._lo=lo
        self._la=la

    def est_dans(self,x,y,z):                                       #On vérifie si le point de coordonées x,y,z se trouve dans l'obstacle
        x1=self._x                                              #x1 ,x2 , y1 et y2 représentent les quatres points du rcetangle(Carre) 
        x2=self._x + self._lo
        y1=self._y 
        y2=self._y - self._la
        return x>=x1 and x<= x2 and y<=y1 and y>=y2             #Si les coordonées de l'objet touchent le rectangle ou sont dedans

    def toString(self):
        return "C"+" "+str(self._x)+" "+str(self._y)+" "+str(self._z)+" "+str(self._lo)+" "+str(self._la)

class Obstacle_rond(Obstacle):
    def __init__(self,x,y,z=0,r=1.0):        #Initialisation des arguments
        self._x=x
        self._y=y
        self._z=z
        self._r=r


    def est_dans(self,x,y,z):                                       #On vérifie si l'objet de coordonées x,y,z se trouve dans l'obstacle
        return (x-self._x)**2+(y-self._y)**2 <= self._r**2      #On verifie si les coordonées du point se trouvent dans le cercle
    
    def toString(self):
        return "O"+" "+str(self._x)+" "+str(self._y)+" "+str(self._z)+" "+str(self._r)
