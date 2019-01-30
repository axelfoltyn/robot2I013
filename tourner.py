import math

#a mettre dans la classe robot

def tourner(teta=90):
	trad = math.radian(teta)
	dx = self.direction[0]
	dy = self.direction[1]
	self.direction[0] = dx*math.cos(trad) - dy*math.sin(trad)
	self.direction[1] = dx*math.sin(trad) + dy*math.sin(trad)
	self.old_direction[0] = dx
	self.old_direction[1] = dy
	return
