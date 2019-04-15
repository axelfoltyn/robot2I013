import sys
import time
from tkinter import *
from tkinter import messagebox
import threading
from ..color import color

class View(threading.Thread):

    red= 'red'
    blue='blue'
    black='black'
    yellow='yellow'
    def __init__(self,arene):
        super(View,self).__init__()
        """
        int * int -> View
        Cette fonction initialise la fenetre sur laquelle le robot va s'afficher
        : param x: largeur de la fenetre
        : param y: heuteur de la fenetre
        """
        #initialisation des parametres
        self._x = arene._x
        self._y = arene._y
        self._objets = []
        self.arene = arene

    def run(self):
        self._fenetre = Tk()
        self._canvas = Canvas(self._fenetre, width = self._x, height = self._y, background = "grey")
        self._canvas.pack()
        self._Bouton_Quitter = Button(self._fenetre, text = "Quitter", command = self._fenetre.destroy) #creation du boutton quitter
        self._Bouton_Quitter.pack()
        self._fenetre.after(1,self.update_arene)
        self._fenetre.mainloop()
    def afficher_robot(self,robot):
        """
        Cette fonction affiche le robot sur le canevas
        : param robot : robot a afficher
        """
        x = robot._position[0]
        y = self._y-robot._position[1]
        dx = robot._direction[0]
        dy = -robot._direction[1]
        self._objets.append(self._canvas.create_polygon(x+40*dx,y+40*dy,x+10*dy,y-10*dx,x-10*dy,y+10*dx,fill=robot._color))

    def afficher_obstacle(self,obstacle):
        """
        Cette fonction permet d'afficher les obstacles
        : param obstacle : obstacle a afficher
        """
        x0=obstacle._x
        y0=self._y-obstacle._y
        #si r est different de 0 alors cest un cercle sinon autre
        #if isinstance(obstacle, ObstacleCarre):
        if obstacle.name == 'C':
            if (obstacle._lo != 0) and (obstacle._la != 0):
                x1 = obstacle._x
                y1 = self._y-obstacle._y
                x2 = x1+obstacle._lo
                y2 = y1+obstacle._la
                if obstacle.getColor()==self.yellow:
                    self._objets.append(self._canvas.create_rectangle(x1, y1, x2, y2,fill = "yellow"))
                else:
                    self._objets.append(self._canvas.create_rectangle(x1, y1, x2, y2,fill = "red"))
            else:
                print("L'obstacle n'existe pas")
        else:
            x0 = obstacle._x - obstacle._r
            y0 = y0 - obstacle._r
            r1 = obstacle._r
            x1=x0+(2*r1)
            y1=y0+(2*r1)
            self._objets.append(self._canvas.create_oval(x0, y0, x1, y1,fill = "blue"))


        ### faire attention a coordonnee y qui vaudra self._y - y !!! (pour avoir affichage a l'endroit)

    def update_arene(self,dt=1):
        """
        Affichage de l'arene et de ce que contient l'arène """
        self.clear()                   #On efface d'abord ce qui etait affiche precedemment
        for i in self.arene._obstacles :              #On procède a l'affichage des obstacles
            self.afficher_obstacle(i)
        self.afficher_robot(self.arene._robot)  #On affiche le robot
        self.update(dt)
        self._fenetre.after(5,self.update_arene)



    def clear(self):
                """
                Cette fonction supprime tous les elements affiches sur l'arene
                """
                for e in self._objets:
                        self._canvas.delete(e)
                self._objets = []




    def arret(self, b=True):
        """
        Cette fonction indique la fin de l'affichage
        : param b: booleen permattant de verifier si nous sommes a la fin du script
        """
        if b:
            self._canvas.configure(background = "lime green")
            messagebox.showinfo("Fin du parcours","Le parcours vient de se terminer")
        else:
            self._canvas.configure(background = "red")
            messagebox.showwarning("Fin du parcours","Le robot s'est cogne")
        self._fenetre.mainloop()

    #dt en s
    def update(self, dt=1):
        self._canvas.pack()
        #time.sleep(dt)
        self._canvas.update()




