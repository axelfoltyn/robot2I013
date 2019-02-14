from tkinter import *
import time
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
                dy = -robot._direction[1]
                self._objets.append(self._canvas.create_polygon(x+40*dx,y+40*dy,x+10*dy,y-10*dx,x-10*dy,y+10*dx))

        def afficher_obstacle(self,obstacle):
                x0=obstacle._x
                y0=self._y-obstacle._y
    #si r est different de 0 alors cest un cercle sinon autre
                if obstacle._nom == 'C':
                        if (obstacle._lo != 0) and (obstacle._la != 0):
                                x1 = obstacle._x
                                y1 = self._y-obstacle._y
                                x2 = x1+obstacle._lo
                                y2 = y1+obstacle._la
                                self._objets.append(self._canvas.create_rectangle(x1, y1, x2, y2,fill = "black"))
                        else:
                                print("L'obstacle n'existe pas")
                else:
                        x0 = obstacle._x - obstacle._r
                        y0 = y0 - obstacle._r
                        r1 = obstacle._r
                        x1=x0+(2*r1)
                        y1=y0+(2*r1)
                        self._objets.append(self._canvas.create_oval(x0, y0, x1, y1,fill = "black"))


        ### faire attention à coordonnée y qui vaudra self._y - y !!! (pour avoir affichage à l'endroit)

        def clear(self):
                for e in self._objets:
                        self._canvas.delete(e)
                self._objets = []

        def endView(self):
                self._canvas.configure(background = "lime green")
                messagebox.showinfo("Fin du parcours", "Le parcours vient de se terminer")
                self._fenetre.mainloop()

        #dt en s
        def update(self, dt=1):
                self._canvas.pack()
                time.sleep(dt)
                self._canvas.update()
