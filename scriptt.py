from Projet import AdaptateurVirtuel as Robot
robot=Robot(True)
while(True):
    robot.tourner_gauche(90)
    robot.Avancer(50)
    robot.tourner_droite(90)

