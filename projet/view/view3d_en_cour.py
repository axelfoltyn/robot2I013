import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys
from ..color import color


class View3D(threading.Thread, pyglet.window.Window):

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
        self.batch = pyglet.graphics.Batch()
        self.set_minimum_size(667,667)
        pyglet.clock.schedule(self.update)

    def afficher_robot(self,robot):
        """
        mettre la cam comme il faut
        : param robot : robot a afficher
        """
        glPushMatrix()
        rot = self.robot._direction
        pos = self.robot._position
        glRotatef(-rot[0],1,0,0)
        glRotatef(-rot[1],0,1,0)
        glRotatef(-rot[2],0,0,1)
        glTranslatef(-pos[0], -pos[1], -pos[2])


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
                y1 = obstacle._y
                x2 = x1+obstacle._lo
                y2 = y1-obstacle._la
                z1 = obstacle._z
                z2 = self.arene._z
                couleur = color.trad_str_to_rgb(obstacle.getColor())
                tex_coords = ('c3B', (couleur[0], couleur[1], couleur[2], couleur[0], couleur[1], couleur[2], couleur[0], couleur[1], couleur[2]))
                self.batch.add(4, GL_QUADS, None, ('v3f', (X, y, z,  x, y, z,  x, Y, z,  X, Y, z)),tex_coords) # back
                self.batch.add(4, GL_QUADS, None, ('v3f', (x, y, Z,  X, y, Z,  X, Y, Z,  x, Y, Z)),tex_coords) # front
                self.batch.add(4, GL_QUADS, None, ('v3f', (x, y, z,  x, y, Z,  x, Y, Z,  x, Y, z)),tex_coords)  # left
                self.batch.add(4, GL_QUADS, None, ('v3f', (X, y, Z,  X, y, z,  X, Y, z,  X, Y, Z)),tex_coords)  # right
                self.batch.add(4, GL_QUADS, None, ('v3f', (x, y, z,  X, y, z,  X, y, Z,  x, y, Z)),tex_coords)  # bottom
                self.batch.add(4, GL_QUADS, None, ('v3f', (x, Y, Z,  X, Y, Z,  X, Y, z,  x, Y, z)),tex_coords)  # top

            else:
                print("L'obstacle n'existe pas")
        else:
            pass
            x0 = obstacle._x - obstacle._r
            y0 = y0 - obstacle._r
            r1 = obstacle._r
            x1=x0+(2*r1)
            y1=y0+(2*r1)
            self._objets.append(self._canvas.create_oval(x0, y0, x1, y1,fill = "blue"))


    def update_arene(self,dt=1):
        """
        Affichage de l'arene et de ce que contient l'arène """
        self.clear()
        self.active3d()

        for i in self.arene._obstacles :              #On procède a l'affichage des obstacles
            self.afficher_obstacle(i)
        self.afficher_robot(self.robot)


        self.update(dt)
        glPopMatrix()






    def clear(self):
                """
                Cette fonction supprime tous les elements affiches sur l'arene
                """
                for e in self._objets:
                        e.delete()
                self._objets = []




    def arret(self, b=True):
        """
        Cette fonction indique la fin de l'affichage
        : param b: booleen permattant de verifier si nous sommes a la fin du script
        """
        pass
        if b:
            self._canvas.configure(background = "lime green")
            messagebox.showinfo("Fin du parcours","Le parcours vient de se terminer")
        else:
            self._canvas.configure(background = "red")
            messagebox.showwarning("Fin du parcours","Le robot s'est cogne")
        self._fenetre.mainloop()


    def update(self, dt=1):
        self.batch.draw()


