from view import *
from robot import *
from obstacle import *

class Arene:
	def __init__(self, x = 42, y = 42, z = 42,robot=Robot(), obstacles=[]):
		"""
		   int * int * int * Robot * Obstacle[] -> Arene
		   L'arene contient le robot et les obstacles 
		   :param x: longueur de l'arène 
		   :param y: largeur de l'arène 
		   :param z: hauteur de l'arène 
		"""
		#inititialisation des paramètres de l'arene 
		
		self._x = x
		self._y = y
		self._z = z
		self._robot = robot
		self._obstacles = obstacles
		self._view = View(x, y)
		
	def ajout_Robot(self, robot):
		"""
			On peut ajouter un robot dans l'arene 
			:param robot: robot à ajouter dans l'arène
			ne retourne rien 
		"""
		self._robot = robot

	def ajout_Obstacle(self,obstacle):
		"""
			Permet d'ajouter un obstacle à notre liste d'obstacle
			:param obstacle: obstacle à ajouter  
		"""
		self._obstacles.append(obstacle) 

	def afficher(self):
		"""
			Affichage de l'arene et de ce que contient l'arène
		"""
		self._view.clear()                      #On efface d'abord ce qui était affiché précedemment
		for i in self._obstacles :              #On procède à l'affichage des obstacles
			self._view.afficher_obstacle(i)     
		self._view.afficher_robot(self._robot)  #On affiche le robot 

	#dt en s
	def update(self, dt = 1):
		"""
			Permet de mettre à jour l'arène et ses éléments
			:param dt: temps en secondes représente le temps 
			écoulé pendant update
		"""
		t = 0.04                                #intervalle de temps par défaut (40 ms) 
		self.afficher()                         #affichage de l'arène
		if(dt <= t):                            #si le temps dt inséré est inférieur à 40ms on prendra dt             
			self._robot.update(dt)  
			#for i in self._obstacles :
			#    i.update(dt)
			self._view.update(dt)              #il n'y a qu'un seul affichage    
		else:
			self._robot.update(t)                
			#for i in self._obstacles :
			#    i.update(t)
			self._view.update(t)
			self.update(dt-t)                   #on rappelle la fonction avec un dt plus petit 

	def proximite(self):
		"""
		Fonction qui permet au robot de changer de direction de manière aléatoire
		lorsqu'il est trop proche d'un obstacle
		"""
		x_p = self._robot._position[0]
		y_p = self._robot._position[1]
		z_p = self._robot._position[2]
		max = 100.0 #en cm
		res = 0.0
		while(res < max):
			if (x_p + self._robot._direction[0]*res < 0 or x_p + self._robot._direction[0]*res > self._x or y_p + self._robot._direction[1]*res < 0 or y_p + self._robot._direction[1]*res > self._y):
				return res
			for o in self._obstacles:
				if o.est_dans(x_p + self._robot._direction[0]*res, y_p + self._robot._direction[1]*res, z_p + self._robot._direction[2]*res):
					return res
			res += 0.1
		return res
