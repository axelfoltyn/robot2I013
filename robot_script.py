import time
from PIL import Image
from robot2I013 import Robot2I013 as Robot
from projet import Adapter
from projet import StrategieCarre, StrategieFonce, StrategieFonceAmeliore, StrategieCarreAmeliore, StrategieArcGauche, StrategieArcDroit

calibrage=0.99 # defaut=1 , augmenter legerement pour devier vers la droite

robot=Adapter(Robot(), calibrage)
#time.sleep(1)
#VITESSE MAX = 20.9
#var=robot.get_image()
#print(var)
#var2=[]
#for i in var:
#    for j in i:
#        var2[i][j].append(var[-i][-j])
#img=Image.fromarray(var2).convert('RGB')
#img.save('image.jpg')


#strat=StrategieFonceAmeliore(robot, 2, 20)
#strat=StrategieFonce(robot, 5, 20)
#strat=StrategieFonceAmeliore(robot, 300, 40)
strat=StrategieArcDroit(robot,10,20,360)


strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.stop()
strat=StrategieArcGauche(robot,10,20,360)
strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.stop()
strat=StrategieCarreAmeliore(robot, 20, 20)
strat.start()
while not strat.stop():
    strat.update()
    time.sleep(0.01)
robot.stop()
