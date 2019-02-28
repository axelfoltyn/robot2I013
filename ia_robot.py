def ia_robot(arene,robot):
    while (True):
        if(robot.proximite_bruit(arene)<20):
            robot.avancer(20)
        else :
            tourner(90)

#De ce que j'ai essayé ça fonctionne
