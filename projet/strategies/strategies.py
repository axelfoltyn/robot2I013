import time


class StrategieAvance:

    def __init__(self, robot, distance, vitesse):
        self._robot=robot
        self._distance=distance                                                                             #on initialise avec le robot et on lui donne une distance a parcourir
        self._vitesse=vitesse                                                                               #avec une vitesse donner. Pour cela on donne un angle a faire aux roues
        self._target=self._distance/self._robot.WHEEL_CIRCUMFERENCE*3600                                    #puis elle met a zero les roues a la fin.#puis elle met a zero les roues a la fin.

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
            self._robot.avancer(self._vitesse)

    def stop(self):
        return self._robot.get_motor_position()[0]>=self._target


class StrategieTournerDroite:

    def __init__(self, robot, angle, vitesse):
        self._robot=robot                                                                                    #on initialise avec le robot et on lui donne un angle a tourne vers la droite
        self._angle=angle                                                                                    #avec une vitesse donner.on donne a la roue droite un angle negatif et on donne
        self._vitesse=vitesse                                                                                #a la roue gauche un angle positif a tourner. ainsi le robot tourne sur place vers la droite.
        self._target=self._angle*self._robot.WHEEL_BASE_CIRCUMFERENCE/self._robot.WHEEL_CIRCUMFERENCE

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
            self._robot.tourner_droite(self._vitesse)

    def stop(self):
        return self._robot.get_motor_position()[0]>=self._target


class StrategieTournerGauche:

    def __init__(self, robot, angle, vitesse):
        self._robot=robot                                                                                         # cette strategie realise la meme chose que StraegieTournerDroite sauf que
        self._angle=angle                                                                                         # la roue gauche prend un agle negatif a realiser et la roue droite un angle
        self._vitesse=vitesse                                                                                     # positif a realise.
        self._target=self._angle*self._robot.WHEEL_BASE_CIRCUMFERENCE/self._robot.WHEEL_CIRCUMFERENCE

    def start(self):
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])

    def update(self):
        self._robot.tourner_gauche(self._vitesse)

    def stop(self):
        return self._robot.get_motor_position()[1]>=self._target


class StrategieCarre:

    def __init__(self, robot, distance, vitesse):
        self._robot=robot
        self._distance=distance                                                                                     #on initialise avec le robot et une distance a parcourir.
        self._vitesse=vitesse                                                                                       #il realise 4 fois la distance donner a une vitesse canstante donner.
        self._num_strat=0
        self._strategie=[StrategieAvance(robot, distance,vitesse), StrategieTournerDroite(robot, 90, vitesse)]
        self._i=0

    def start(self):
        self._i=0
        self._num_strat=0
        self._strategie[0].start()

    def update(self):                                                                                               #elle parcoure une distance a une vitesse donner.
        if self._strategie[self._num_strat].stop() and self._num_strat==0:                                          #elle s'arrete lorsque la distance est atteint.
            self._robot.avancer(0)
            self._num_strat=1
            self._strategie[self._num_strat].start()
            self._strategie[self._num_strat].update()
        elif self._strategie[self._num_strat].stop() and self._num_strat==1:
            self._robot.avancer(0)
            self._i+=1
            self._num_strat=0
            if not self.stop():
                self._strategie[self._num_strat].start()
                self._strategie[self._num_strat].update()
        else:
            self._strategie[self._num_strat].update()

    def stop(self):
        return self._i>=4


class StrategieFonce:

    def __init__(self, robot, distance, vitesse):
        self._robot=robot                                                                                               #elle realise une distance a une vitesse donner.
        self._distance=distance                                                                                         #au fur et a mesure que la distance est parcouru la vitesse diminue egalement.
        self._vitesse=vitesse

    def start(self):
        pass

    def update(self):
        self._robot.avancer(self._vitesse)

    def stop(self):
        return self._robot.get_distance()/10.0<=self._distance


class StrategieAvanceAmeliore:

    _i=2

    def __init__(self, robot, distance, vitesse):
        self._robot=robot                                                                                                 #le robot parcour la distance et une vitesse donner.
        self._distance=distance                                                                                           #au fur et a mesure que la distance diminu la vitesse diminue egalement.
        self._vitesse=vitesse
        self._target=self._distance/self._robot.WHEEL_CIRCUMFERENCE*3600
        self._vitessed=vitesse

    def start(self):
        self._vitesse=self._vitessed
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):
        if self._vitesse>10:
            if self.dist():
                self._vitesse=self._vitesse/2
        self._robot.avancer(self._vitesse)

    def stop(self):
        return self._robot.get_motor_position()[0]>=self._target

    def dist(self):
        if self._robot.get_motor_position()[0]>=self._target*(1-1/self._i):
            self._i=self._i+1
            return True
        else:
            return False


class StrategieFonceAmeliore:

    di=0.3
    _i=di

    def __init__(self, robot, distance, vitesse): # !!!probleme quand on inverse distance et vitesse
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse
        self._vitessed=vitesse

    def start(self):
        self._vitesse=self._vitessed

    def update(self):
        if self._vitesse>10:
            if self.dist():
                self._i+=self.di
                self._vitesse=self._vitesse/2
        self._robot.avancer(self._vitesse)

    def dist(self):
        return self._robot.get_distance()/10.0<=self._distance*(1+1/self._i)

    def stop(self):
        return self._robot.get_distance()/10.0<=self._distance


class StrategieTournerDroiteAmeliore:

    _i=2

    def __init__(self, robot, angle, vitesse):              #On initialise le robot en lui donnant un angle et une vitesse
        self._robot=robot
        self._angle=angle
        self._vitesse=vitesse
        self._vitessed=vitesse


    def start(self):                                           # On attribue aux roues du robot l'angle de rotation
        self._i=2
        self._vitesse=self._vitessed
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])



    def update(self):                   #Tant que la vitesse est supérieure à 3 on diminue la _vitesse
        if(self._vitesse>3):            #Jusqu'à obtenir une vitesse suffisemment petite pour ne pas rencontrer de problèmes
            if(self.dist()):
                self._vitesse = self._vitesse / 2
        self._robot.tourner_droite(self._vitesse)


    def stop(self):

        target=self._angle/self._robot.WHEEL_CIRCUMFERENCE*self._robot.WHEEL_BASE_CIRCUMFERENCE
        return target<=abs(self._robot.get_motor_position()[1])


    def dist(self):
        target=self._angle/self._robot.WHEEL_CIRCUMFERENCE*self._robot.WHEEL_BASE_CIRCUMFERENCE
        if (abs(self._robot.get_motor_position()[1])>=target*(1-1/self._i)):
            self._i=self._i*2
            return True
        else:
            return False


class StrategieCarreAmeliore:

    def __init__(self, robot, distance, vitesse):       #On initialise la classe avec un robot une distance (coté du carré) et une _vitesse
        self._robot=robot
        self._distance=distance
        self._vitesse=vitesse
        self._num_strat=0
        self._strategie=[StrategieAvanceAmeliore(robot, distance,vitesse), StrategieTournerDroiteAmeliore(robot, 90, vitesse)]
        self._i=0

    def start(self):                                #On indique petit à petit à quelle étape nous nous trouvons
        self._i=0                                   #Cela nous permet alors de savoir combien de coté il nous reste à faire
        self._num_strat=0
        self._strategie[0].start()

    def update(self):
        if self._strategie[self._num_strat].stop() and self._num_strat==0:
            self._robot.avancer(0)
            self._num_strat=1
            self._strategie[self._num_strat].start()
            self._strategie[self._num_strat].update()
        elif self._strategie[self._num_strat].stop() and self._num_strat==1:
            self._robot.avancer(0)
            self._i+=1
            self._num_strat=0
            if not self.stop():
                self._strategie[self._num_strat].start()
                self._strategie[self._num_strat].update()
        else:
            self._strategie[self._num_strat].update()

    def stop(self):
        return self._i>=4

class StrategieArcGauche:

    def __init__(self, robot, rayon, vitesse, angle):           #On initialise la classe avec un robot, un rayon, une vitesse, et un angle de rotation
        self._robot=robot
        self._diametre=rayon*20
        self._dps=(vitesse*10/self._robot.WHEEL_CIRCUMFERENCE)*360
        self._target=(self._diametre+self._robot.WHEEL_BASE_WIDTH)/self._robot.WHEEL_DIAMETER*angle
        self._coeff=(self._diametre+self._robot.WHEEL_BASE_WIDTH)/(self._diametre-self._robot.WHEEL_BASE_WIDTH)

    def start(self):                                            #On attribue aux roues du robot l'angle de rotation
        self._robot.offset_motor_encoder(self._robot.MOTOR_RIGHT, self._robot.get_motor_position()[1])

    def update(self):                                           #On fait évoluer la roue droite plus vite que la roue gauche
            self._robot.set_motor_dps(self._robot.MOTOR_LEFT,self._dps/self._coeff)
            self._robot.set_motor_dps(self._robot.MOTOR_RIGHT,self._dps)

    def stop(self):
        return self._robot.get_motor_position()[1]>=self._target
  

class StrategieArcDroit:

    def __init__(self, robot, rayon, vitesse, angle):       #On initialise la classe avec un robot, un rayon, une vitesse, et un angle de rotation
        self._robot=robot
        self._diametre=rayon*20
        self._dps=(vitesse*10/self._robot.WHEEL_CIRCUMFERENCE)*360
        self._target=(self._diametre+self._robot.WHEEL_BASE_WIDTH)/self._robot.WHEEL_DIAMETER*angle
        self._coeff=(self._diametre+self._robot.WHEEL_BASE_WIDTH)/(self._diametre-self._robot.WHEEL_BASE_WIDTH)

    def start(self):                                #On attribue aux roues du robot l'angle de rotation
        self._robot.offset_motor_encoder(self._robot.MOTOR_LEFT, self._robot.get_motor_position()[0])

    def update(self):                                   #On fait évoluer la roue gauche plus vite que la roue droite
            self._robot.set_motor_dps(self._robot.MOTOR_LEFT,self._dps)
            self._robot.set_motor_dps(self._robot.MOTOR_RIGHT,self._dps/self._coeff)

    def stop(self):
        return self._robot.get_motor_position()[0]>=self._target
