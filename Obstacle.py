class Obstacle :
	
	def __init__(self,x,y,z=10,nom='O',r=1.0,lo=0.0,la=0.0):
		self._nom=nom
		self._x=x
		self._y=y
		self._z=z
		self._r=r		#si r est different de 0 alors cest un cercle sinon autre
		self._lo=lo			
		self._la=la
		
					#si lo et la sont different de 0 et que r est egale a 0 alors cest un rectangle lo: longeur , la: largeur