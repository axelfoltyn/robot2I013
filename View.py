from tkinter import *
class View:
	def __init__(self,x=800, y=600):
		"""int * int -> View"""
		self._x = x
		self._y = y
		self._fenetre = Tk()
		self._canvas = Canvas(self._fenetre, width = x, height = y, background = "grey")
		self._canvas.pack()
		self._Bouton_Quitter = Button(self._fenetre, text = "Quitter", command = self._fenetre.destroy)
		self._Bouton_Quitter.pack()
		self._objets = []

	def afficher_robot(self,robot):
		x = robot._position[0]
		y = self._y-robot._position[1]
		dx = robot._direction[0]
		dy = robot._direction[1]
		self._objets.append(self._canvas.create_polygon(x+40*dx,y+40*dy,x+10*dy,y-10*dx,x-10*dy,y+10*dx))

	"""
	def afficher_obstacle(self,obstacle):
	### faire attention à coordonnée y qui vaudra self._y - y !!! (pour avoir affichage à l'endroit)
	"""

	def clear(self):
		for e in self._objets:
			self._canvas.delete(e)
		self._objets = []

	def endView(self):
		self._fenetre.mainloop()
