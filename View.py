from tkinter import *
from Robot import *

class View:
	def __init__(self,x=800, y=600):
		"""int * int -> View"""
		self._fenetre = Tk()
		self._canvas = Canvas(self._fenetre, width = x, height = y, background = "grey")
		self._canvas.pack()
		self._Bouton_Quitter = Button(self._fenetre, text = "Quitter", command = self._fenetre.destroy)
		self._Bouton_Quitter.pack()

	def afficher_robot(self, x, y, dx, dy):
		self._robot = self._canvas.create_polygon(x+40*dx,y+40*dy,x+10*dy,y-10*dx,x-10*dy,y+10*dx)

	def endView(self):
		self._fenetre.mainloop()
