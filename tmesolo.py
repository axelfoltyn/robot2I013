import time
from projet import RobotVirtuel as RobotV
from projet import Adapter
from projet import Strategie_triagle_equi_10, Strategie_poly_n, Strategie_tour_arene
from projet import View
from threading import Thread



def q2_1():
    """
    on initialise ce qu'il faut pour lancer
    la simu graphique et on fait le triangle equilateral
    """
    robotv = RobotV()

    view = View(robotv._arene)
    robotv._arene.add_obs(view)
    robot = Adapter(robotv)

    thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
    thread_affichage.start()
    view.start()

    strat = Strategie_triagle_equi_10(robot)

    strat.start()
    while not strat.stop():
        strat.update()
        time.sleep(0.01)
    robot.finish()

def q2_2():
    """
    le 8 marche bien mais j'ai une erreur sur le 20
    """
    robotv = RobotV()

    view = View(robotv._arene)
    robotv._arene.add_obs(view)
    robot = Adapter(robotv)

    thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
    thread_affichage.start()
    view.start()

    strat = Strategie_poly_n(robot, 8)

    strat.start()
    while not strat.stop():
        strat.update()
        time.sleep(0.01)

    strat = Strategie_poly_n(robot, 20)

    strat.start()
    while not strat.stop():
        strat.update()
        time.sleep(0.01)
    robot.finish()

def q2_3():
    """
    il y a un decalage du a notre stratege qui ne fait pas exactement 90 degree en virage
    """
    robotv = RobotV()

    view = View(robotv._arene)
    robotv._arene.add_obs(view)
    robot = Adapter(robotv)

    thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
    thread_affichage.start()
    view.start()

    strat = Strategie_tour_arene(robot)

    strat.start()
    while not strat.stop():
        strat.update()
        time.sleep(0.01)
    robot.finish()

#decomenter une seul fn pour tester (question 1.1 et 1.2 sont toujour visible)

#q2_1()
#q2_2()
#q2_3()
