import math

class Obstacle :
  #les verifications se font par rapport au nom O =Obstacle rond C= Obstacle Carré
  def __init__(self,x,y,z=10,nom='O',r=1.0,lo=0.0,la=0.0):			 #Initialisation des arguments 
    self._nom=nom
    self._x=x
    self._y=y
    self._z=z
    self._r=r
    self._lo=lo			
    self._la=la
		
  def est_dans(self,x,y,z):   							#On vérifie si l'objet de coordonées x,y,z se trouve dans l'obstacle
    if (self._nom=='C'):      							#Si c'est un rectangle
      x1=self._x              							#x1 ,x2 , y1 et y2 représentent les quatres points du rcetangle(Carre) 
      x2=self._x + self._lo
      y1=self._y 
      y2=self._y - self._la
      print(self._nom,"||", x1,x,x2,"||",y1,y,y2)
      if ( x>=x1 and x<= x2 and y<=y1 and y>=y2) : 				#Si les coordonées de l'objet touchent le rectangle ou sont dedans
        return True
      else:					  			        #Sinon	
        return False
    if (self._nom=='O'):                           				#Pour un obstacle Rond 
      distance = math.sqrt((self._x-x)**2+(self._y-y)**2+(self._z-z)**2)        #On verifie si les coordonées de l'objet se trouvent dans le cercle
      if(distance<=self._r):							
        return True
      else:
        return False
			
