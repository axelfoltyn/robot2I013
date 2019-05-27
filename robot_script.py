import time
from PIL import Image
from robot2I013 import Robot2I013 as Robot
from projet import Adapter
from projet import StrategieCarreAmeliore, StrategieArcGauche, StrategieArcDroit, StrategieFonceAmeliore

calibrage=1.003 # defaut=1 , augmenter legerement pour devier vers la droite
#VITESSE MAX = 20

robot=Adapter(Robot(), calibrage)

# sauvegarde d'image
#time.sleep(1)
#arry=robot.get_image()
#img=Image.fromarray(arry).convert('RGB')
#img=img.rotate(180)
#img.save('image.jpg')


strat1=StrategieCarreAmeliore(robot, 20, 20)
strat2=StrategieArcGauche(robot,10,20,360)
strat3=StrategieArcDroit(robot,10,20,360)
strat4=StrategieFonceAmeliore(robot, 3, 20)
strats=[strat1,strat2,strat3,strat4]

for strat in strats:
    strat.start()
    while not strat.stop():
        strat.update()
        time.sleep(0.01)
robot.stop()
