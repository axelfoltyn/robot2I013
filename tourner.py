import math

#a mettre dans la classe robot

def tourner(self, teta=90):
	trad = math.radian(teta)
	dx = self._direction[0]
	dy = self._direction[1]
	self._direction[0] = dx*math.cos(trad) - dy*math.sin(trad)
	self._direction[1] = dx*math.sin(trad) + dy*math.sin(trad)
	vx = self._vitesse[0]
	vy = self._vitesse[1]
	self._vitesse[0] = vx*math.cos(trad) - vy*math.sin(trad)
	self._vitesse[1] = vx*math.sin(trad) + vy*math.sin(trad)
	ax = self._acceleration[0]
	ay = self._acceleration[1]
	self._acceleraion[0] = ax*math.cos(trad) - ay*math.sin(trad)
	self._acceleraion[1] = ax*math.sin(trad) + ay*math.sin(trad)
	return
