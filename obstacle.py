class Obstacle :
	
	def __init__(self,x,y,z,r,lo,la):
		self._x=x
		self._y=y
		self._z=z
		self._r=r				#si r est different de 0 alors cest un cercle sinon autre
		self._lo=lo			
		self._la=la
		
		#si lo et la sont different de 0 et que r est egale a 0 alors cest un rectangle lo: longeur , la: largeur
