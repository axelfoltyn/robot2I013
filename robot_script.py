import time
from PIL import Image
from robot2I013 import Robot2I013 as Robot
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore, StrategieCarreAmeliore, StrategieArcGauche, StrategieArcDroit

calibrage=0.99 # defaut=1 , augmenter legerement pour devier vers la droite
#VITESSE MAX = 20

robot=Adapter(Robot(), calibrage)

# sauvegarde d'image
#time.sleep(1)
#arry=robot.get_image()
#img=Image.fromarray(arry).convert('RGB')
#img=img.rotate(180)
#img.save('image.jpg')


#strat=StrategieCarreAmeliore(robot, 20, 20)
#strat=StrategieFonce(robot, 5, 20)
#strat=StrategieFonceAmeliore(robot, 2, 20)
strat=StrategieArcDroit(robot,10,20,360)


strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.stop()
