import math

#a mettre dans la classe robot

def tourner(self, teta=90):
	trad = math.radian(teta)
	dx = self._direction[0]
	dy = self._direction[1]
	self._direction[0] = dx*math.cos(trad) - dy*math.sin(trad)
	self._direction[1] = dx*math.sin(trad) + dy*math.sin(trad)
	return
