import math

class Obstacle :
	#les verification ce font par rapport au nom O =Obstacle rond C= Obstacle Carré
	def __init__(self,x,y,z=10,nom='O',r=1.0,lo=0.0,la=0.0):
		self._nom=nom
		self._x=x
		self._y=y
		self._z=z
		self._r=r
		self._lo=lo			
		self._la=la
		
	def est_dans_cercle(self,x,y,z,r):
    		""" Retourne True si le point (x,y) est dans le cercle """

    		distance = math.sqrt((self._x-x)^2+(self._y-y)^2+(self._z-z)^2)


    		if(distance<=r):
        		return True

