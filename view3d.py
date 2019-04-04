#import pyglet
#from pyglet.gl import *
#from pyglet.window import key
import OpenGL
import math
import sys


class View3D:

    def get_tex(self,file):
        tex = pyglet.image.load(file).texture
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)


    def afficher_obstacle_cube(self,obstacle):
        """
        Cette fonction peremet d'afficher un cube
        : param obstacle : cube a afficher

        """
        if obstacle.name == 'C':

            color = ('c3f',(1,667,45))
            x,y,z = obstacle._x,obstacle._y,obstacle_z
            X,Y,Z = x+1,y+1,z+1
            #x,y,z = obstacle._x, obstacle._y, obstacle._z
            #X,Y,Z = x+obstacle._lo ,y+obstacle._lo, z+obstacle._lo

            self.batch.add(4, GL_QUADS, self.side, ('v3f', (X, y, z,  x, y, z,  x, Y, z,  X, Y, z)),tex_coords) # back
            self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, y, Z,  X, y, Z,  X, Y, Z,  x, Y, Z)),tex_coords) # front

            self.batch.add(4, GL_QUADS, self.sid2, ('v3f', (x, y, z,  x, y, Z,  x, Y, Z,  x, Y, z)),tex_coords)  # left
            self.batch.add(4, GL_QUADS, self.side2, ('v3f', (X, y, Z,  X, y, z,  X, Y, z,  X, Y, Z)),tex_coords)  # right

            self.batch.add(4, GL_QUADS, self.bottom, ('v3f', (x, y, z,  X, y, z,  X, y, Z,  x, y, Z)),tex_coords)  # bottom
            self.batch.add(4, GL_QUADS, self.top,    ('v3f', (x, Y, Z,  X, Y, Z,  X, Y, z,  x, Y, z)),tex_coords)  # top


    def __init__(self):

        tex_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1))

        self.top = self.get_tex('p.png')
        self.side = self.get_tex('t.png')
        self.side2 = self.get_tex('dirt.png')
        self.bottom = self.get_tex('n.png')

        self.batch = pyglet.graphics.Batch()

    #    for i in self.arene._obstacles :
    #        self.afficher_obstacle_cube(i)
        x,y,z = 0,0,-1
        X,Y,Z = x+1,y+1,z+1


        self.batch.add(4, GL_QUADS, self.side, ('v3f', (X, y, z,  x, y, z,  x, Y, z,  X, Y, z)),tex_coords) # back
        self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, y, Z,  X, y, Z,  X, Y, Z,  x, Y, Z)),tex_coords) # front

        self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, y, z,  x, y, Z,  x, Y, Z,  x, Y, z)),tex_coords)  # left
        self.batch.add(4, GL_QUADS, self.side, ('v3f', (X, y, Z,  X, y, z,  X, Y, z,  X, Y, Z)),tex_coords)  # right

        self.batch.add(4, GL_QUADS, self.bottom, ('v3f', (x, y, z,  X, y, z,  X, y, Z,  x, y, Z)),tex_coords)  # bottom
        self.batch.add(4, GL_QUADS, self.top, ('v3f', (x, Y, Z,  X, Y, Z,  X, Y, z,  x, Y, z)),tex_coords)  # top


    def draw(self):
        self.batch.draw()


class Robot:

    def __init__(self, pos=(0, 0, 0), rot=(0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def mouse_motion(self, dx, dy):
        dx/= 8
        dy/= 8
        self.rot[0] += dy
        self.rot[1] -= dx
        if self.rot[0]>90:
            self.rot[0] = 90
        elif self.rot[0] < -90:
            self.rot[0] = -90

    def update(self,dt,keys):
        sens = 0.1
        s = dt*10
        rotY = -self.rot[1]/180*math.pi
        dx, dz = s*math.sin(rotY), math.cos(rotY)
        if keys[key.Z]:
            self.pos[0] += dx*sens
            self.pos[2] -= dz*sens
        if keys[key.S]:
            self.pos[0] -= dx*sens
            self.pos[2] += dz*sens
        if keys[key.Q]:
            self.pos[0] -= dz*sens
            self.pos[2] -= dx*sens
        if keys[key.D]:
            self.pos[0] += dz*sens
            self.pos[2] += dx*sens
        if keys[key.SPACE]:
            self.pos[1] += s
        if keys[key.LSHIFT]:
            self.pos[1] -= s


#class Window(pyglet.window.Window):
#
#
#    def push(self,pos,rot):
#        glPushMatrix()
#        rot = self.robot.rot
#        pos = self.robot.pos
#        glRotatef(-rot[0],1,0,0)
#        glRotatef(-rot[1],0,1,0)
#        glTranslatef(-pos[0], -pos[1], -pos[2])
#
#    def Projection(self):
#        glMatrixMode(GL_PROJECTION)
#        glLoadIdentity()
#
#    def View3D(self):
#        glMatrixMode(GL_MODELVIEW)
#        glLoadIdentity()
#
#    def active3d(self):
#        self.Projection()
#        gluPerspective(70,self.width/self.height,0.05,1000)
#        self.View3D()
#
#    def __init__(self,*args,**kwargs):
#        super().__init__(*args,**kwargs)
#        self.set_minimum_size(667,667)
#
#        self.keys = key.KeyStateHandler()
#        self.push_handlers(self.keys)
#
#        self.model = View3D()
#        pyglet.clock.schedule(self.update)
#
#        self.robot = Robot((0.5,1.5,1.5),(-30,0))
#
#        #self.robot = Robot((robot_pos[0],robot_pos[1],robot_pos[2]),(0,0))
#
#    def setLock(self, state):
#        self.lock = state
#        self.set_exclusive_mouse(state)
#
#    lock = False
#    mouse_lock = property(lambda self:self.lock, setLock)
#
#
#    def quitter(self,KEY,MOD):
#        if KEY == key.ESCAPE :
#            self.close()
#        elif KEY == key.E:
#            self.mouse_lock = not self.mouse_lock
#
#    def update(self, dt):
#        self.robot.update(dt, self.keys)
#
#    def on_draw(self):
#        self.clear()
#        self.active3d()
#
#        self.push(self.robot.pos,self.robot.rot)
#        self.model.draw()
#        glPopMatrix()



if __name__ == '__main__':
    window = Window(width = 667, height = 667, caption = ' >:D ',resizable=True)
    glClearColor(0.5,0.7,1,1)
    glEnable(GL_DEPTH_TEST)
    pyglet.app.run()

