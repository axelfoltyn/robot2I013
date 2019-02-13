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
		
  def est_dans(self,x,y,z):
    if (self._nom=='C'):
      x1=self._x
      x2=self._x + self._lo
      y1=self._y 
      y2=self._y - self._la
      print(self._nom,"||", x1,x,x2,"||",y1,y,y2)
      if ( x>=x1 and x<= x2 and y<=y1 and y>=y2) :
        return True
      else:
        return False
    if (self._nom=='O'):
      distance = math.sqrt((self._x-x)**2+(self._y-y)**2+(self._z-z)**2)
      if(distance<=self._r):
        return True
      else:
        return False
			
