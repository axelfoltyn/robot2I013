import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys
from ..color import color
import threading

#import pdb; pdb.set_trace()

class View3D(threading.Thread):

    red= 'red'
    blue='blue'
    black='black'
    yellow='yellow'
    def __init__(self,arene):
        super(View3D,self).__init__()
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
        self.finish = False


    def run(self):
        self.w = pyglet.window.Window(width = 667, height = 667, caption = ' view_3d ',resizable=False)
        glClearColor(0.5,0.7,1,1)
        self.w.batch = pyglet.graphics.Batch()
        self.w.set_minimum_size(667,667)
        #pyglet.clock.schedule(self.update_arene)
        while not self.finish:
            self.update_arene()


    def afficher_robot(self,robot):
        """
        mettre la cam comme il faut
        : param robot : robot a afficher
        """
        print("afficher_robot")
        glPushMatrix()
        rot = robot._direction
        pos = robot._position
        glRotatef(-rot[0],1,0,0)
        glRotatef(-rot[1],0,1,0)
        glRotatef(-rot[2],0,0,1)
        glTranslatef(-pos[0], -pos[1], -pos[2])
        print("fin_afficher_robot")


    def afficher_obstacle(self,obstacle):
        """
        Cette fonction permet d'afficher les obstacles
        : param obstacle : obstacle a afficher
        """

        #si r est different de 0 alors cest un cercle sinon autre
        #if isinstance(obstacle, ObstacleCarre):
        print("afficher_obstacle")
        if obstacle.name == 'C':
            if (obstacle._lo != 0) and (obstacle._la != 0):
                x1 = obstacle._x
                y1 = obstacle._y
                x2 = x1+obstacle._lo
                y2 = y1-obstacle._la
                z1 = obstacle._z
                z2 = self.arene._z
                couleur = color.trad_str_to_rgb(obstacle.getColor())
                tex_coords = ('c3B', (couleur[0], couleur[1], couleur[2], couleur[0], couleur[1], couleur[2], couleur[0], couleur[1], couleur[2]))
                self._objets.append(self.w.batch.add(4, GL_QUADS, None, ('v3f', (x2, y1, z1,  x1, y1, z1,  x1, y2, z1,  x2, y2, z1)))) # back
                self._objets.append(self.w.batch.add(4, GL_QUADS, None, ('v3f', (x1, y1, z1,  x1, y1, z2,  x2, y2, z2,  x1, y2, z2)))) # front
                self._objets.append(self.w.batch.add(4, GL_QUADS, None, ('v3f', (x1, y1, z1,  x1, y1, z2,  x1, y2, z2,  x1, y2, z1))))  # left
                self._objets.append(self.w.batch.add(4, GL_QUADS, None, ('v3f', (x1, y1, z2,  x2, y1, z1,  x2, y2, z1,  x2, y2, z2))))  # right
                self._objets.append(self.w.batch.add(4, GL_QUADS, None, ('v3f', (x1, y1, z1,  x2, y1, z1,  x2, y1, z2,  x1, y1, z2))))  # bottom
                self._objets.append(self.w.batch.add(4, GL_QUADS, None, ('v3f', (x1, y2, z2,  x2, y2, z2,  x2, y2, z1,  x1, y2, z1))))  # top

            else:
                print("L'obstacle n'existe pas")
        else:
            pass
            x0 = obstacle._x - obstacle._r
            y0 = obstacle._y - obstacle._r
            #r1 = obstacle._r
            #x1=x0+(2*r1)
            #y1=y0+(2*r1)
            #self._objets.append(self._canvas.create_oval(x0, y0, x1, y1,fill = "blue"))
        print("fin_afficher_robot")

    def Projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    def view3d(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def active3d(self):
        self.Projection()
        gluPerspective(70,667/667,0.05,1000)
        self.view3d()

    def update_arene(self,dt=1):
        """
        Affichage de l'arene et de ce que contient l'arène """
        print("update_arene", self.w)
        self.clear()
        self.active3d()

        for i in self.arene._obstacles :              #On procède a l'affichage des obstacles
            self.afficher_obstacle(i)
        self.afficher_robot(self.arene._robot)  #On affiche le robot


        self.update(dt)
        glPopMatrix()
        print("fin_update_arene")






    def clear(self):
        """
        Cette fonction supprime tous les elements affiches sur l'arene
        """
        print("clear")
        for e in self._objets:
                e.delete()
        self._objets = []

        print("fin_clear")




    def arret(self, b=True):
        """
        Cette fonction indique la fin de l'affichage
        : param b: booleen permattant de verifier si nous sommes a la fin du script
        """
        print("arret")
        pass
        if b:
            self._canvas.configure(background = "lime green")
            messagebox.showinfo("Fin du parcours","Le parcours vient de se terminer")
        else:
            self._canvas.configure(background = "red")
            messagebox.showwarning("Fin du parcours","Le robot s'est cogne")
        self._fenetre.mainloop()


    def update(self, dt=1):
        print("update")
        self.w.batch.draw()


