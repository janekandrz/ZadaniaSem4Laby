# wczytanie potrzebnych podczas zajęć bibliotek:
import roboticstoolbox as rtb
import numpy as np
import math
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
import time
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
# ...

# definicje funkcji:
def przyklad_1():
    robot = rtb.models.DH.Puma560()

    # Sprawdzenie nazwy i producenta robota
    print("Name: ", robot.name)
    print("Manufacturer: ", robot.manufacturer)
    # Sprawdzenie konfiguracji (rodzajów) przegubów (R - obrotowy, P - przesuwny)
    print("Joint configuration: ", robot.structure)
    # Sprawdzenie, które przeguby są obrotowe
    print("Revolute joints: ", robot.revolutejoints)
    # Sprawdzenie, które przeguby są przesuwne
    print("Prismatic joints: ", robot.prismaticjoints)
    # Sprawdzenie liczby węzłów
    print("Number of joints: ", robot.n)
    # Sprawdzenie czy manipulator jest opisany zmodyfikowaną notacją DH (1) lub standardową notacją DH (0)
    print("MDH: ", robot.mdh)
    # Sprawdzenie czy robot posiada nadgarstek sferyczny
    print("Spherical wrist: ", robot.isspherical())
    # Sprawdzenie maksymalnego zasięgu robota
    print("Reach: ", robot.reach)

    # Dodawanie własnej konfiguracji
    robot.base = SE3(0,0,3)*SE3.Rx(np.pi)
    robot.addconfiguration_attr("mycfg", [0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    print(robot.mycfg)
    print(robot.q) #obecna pozycja 

    #robot.plot(robot.mycfg,block=True,limits=None)

    T = robot.fkine(robot.qn)

    ik_solution = robot.ikine_LM(Tep=T,q0=robot.qz)
    print(ik_solution.q)
    robot.plot(ik_solution.q, block=True)

def zadanie_1():
    l1 , l2 = symbol("l1,l2")

    robot = rtb.DHRobot([
        rtb.RevoluteDH(alpha=np.pi/2, d=l1),
        rtb.RevoluteDH(alpha=np.pi/2, offset=np.pi/2),
        rtb.PrismaticDH(alpha=0,theta=0,offset=l2)
    ])

    for i in range(len(robot.links)):
        print(robot.links[i])
    return robot
    
def zadanie_2(robot):
    pass # zastąp tę linię swoim kodem

def zadanie_3(robot):
    pass # zastąp tę linię swoim kodem

def zadanie_4():
    pass # zastąp tę linię swoim kodem

def zadanie_5():
    pass # zastąp tę linię swoim kodem

# ...

# wykonywanie wybranej funkcji
if __name__ == '__main__':
    #przyklad_1()
    robot = zadanie_1()
    #zadanie_2(robot)
    #zadanie_3(robot)
    #zadanie_4()
    #zadanie_5()