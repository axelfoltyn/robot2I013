
def carre(taille, robot):
    i=0
    n = 80
    while (i<4):
        j=0
        while(j<taille):
            #if (robot.get_proximite() < taille-j and robot.get_proximite() < 8):
            #    #freine jusqua sarrete
            #    print("NON !")
            #    break
            #else:
            if j + n > taille:
                robot.Avancer(taille - j)
                j=taille
            else:
                robot.Avancer(n)
                j=j + n

        robot.tourner_droite(90)
        i=i+1

