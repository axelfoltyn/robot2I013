class Obstacle :
	
	def __init__(self,type,x,y,z,r,lo,la):
		self._type=type
		if self._type == 'O':
			self._x=x
			self._y=y
			self._z=z
			self._r=r		#si r est different de 0 alors cest un cercle sinon autre
		
		if self._type == 'C' :
			self._x=x
			self._y=y
			self._z=z
			self._r=r
			self._lo=lo			
			self._la=la
		
					#si lo et la sont different de 0 et que r est egale a 0 alors cest un rectangle lo: longeur , la: largeur
