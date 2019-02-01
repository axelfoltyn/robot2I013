from Arene import *
from tkinter import *

class View:
	def __init__(self,arene=Arene()):
		"""Arene -> View"""
		self._arene = arene

	def afficher():
		fenetre = Tk()
		canvas = Canvas(fenetre, width=800, height=600, background='white')
		canvas.pack()
		fenetre.mainloop()