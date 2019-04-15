import time
from projet import RobotVirtuel as RobotV
from projet import Adapter
from projet import Strategie_triagle_equi_10, Strategie_poly_n, Strategie_tour_arene
from projet import View
from threading import Thread



def q2_1():
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
    robotv = RobotV()

    view = View(robotv._arene)
    robotv._arene.add_obs(view)
    robot = Adapter(robotv)

    thread_affichage = Thread(target=robotv._arene.boucle_actualiser, args=(25.,))
    thread_affichage.start()
    view.start()

    strat = Strategie_poly_n(robot, 20)

    strat.start()
    while not strat.stop():
        strat.update()
        time.sleep(0.01)
    robot.finish()

def q2_3():
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

#q2_1()
#q2_2()
q2_3()
