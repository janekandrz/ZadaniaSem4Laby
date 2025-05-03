import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
import sympy as sp


def zadanie_3():
    # wykorzystaj zmienne symboliczne o nazwach:  l1, l2, t1, t2, d3

    l1, l2, t1, t2, d3 = symbol("l1, l2, t1, t2, d3")

    robot = rtb.DHRobot([
        rtb.RevoluteDH(d=l1, a=0, alpha=pi()/2),  # Przegub 1 (sterowany przez θ1)
        rtb.RevoluteDH(d=0, a=0, alpha=pi()/2,offset=pi()/2),   # Przegub 2 (sterowany przez θ2 + 90°)
        rtb.PrismaticDH(theta=0, a=0, alpha=0,offset=l2) 
    ])

    for i in range(len(robot.links)):
        print(robot.links[i])
    return robot

    J = robot.jacob0([t1, t2, d3])
    np.set_printoptions(precision=3,suppress=True)
    print(simplify(J))
    #nie umieszczaj w kodzie innych funkcji print

# wykonywanie wybranej funkcji
if __name__ == '__main__':
    zadanie_3()