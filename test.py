import time
from Projet import Strategie_fonce
from Projet import Adapter as Robot



text="resources/fichier_test.txt"
        # Test lecture de fichier et initialisation de l'arene
arene = lecture(text,self)
robot = Robot(arene = arene)
print("sjdfghsjdgf")
strat = Strategie_fonce(robot, 10, 15)

while not strat.stop():
    dt = strat.update()
    time.sleep(dt)
robot.finish()
