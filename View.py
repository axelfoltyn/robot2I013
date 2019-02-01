from Arene import *
from tkinter import *

class View:
	def __init__(self,x=800, y=600):
		"""intxint -> View"""
		fenetre = Tk()
		canvas = Canvas(fenetre, width=x, height=y, background='white')
		canvas.pack()

	def end_view():
		fenetre.mainloop()
