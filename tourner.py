import math

#a mettre dans la classe robot

def tourner(teta=90):
	trad = math.radian(teta)
	dx = self.direction[0]
	dy = self.direction[1]
	self.direction[0] = dx*math.cos(trad) - dy*math.sin(trad)
	self.direction[1] = dx*math.sin(trad) + dy*math.sin(trad)
	vx = self.vitesse[0]
	vy = self.vitesse[1]
	self.vitesse[0] = vx*math.cos(trad) - vy*math.sin(trad)
	self.vitesse[1] = vx*math.sin(trad) + vy*math.sin(trad)
	ax = self.acceleration[0]
	ay = self.acceleration[1]
	self.acceleraion[0] = ax*math.cos(trad) - ay*math.sin(trad)
	self.acceleraion[1] = ax*math.sin(trad) + ay*math.sin(trad)
	return
