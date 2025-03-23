import numpy as np
from spatialmath import *
import roboticstoolbox as rtb
from roboticstoolbox.tools.trajectory import *
from roboticstoolbox.backends.swift import Swift
import time

# definicje funkcji:
def przyklad_1():
    # PyPlot  
    robot = rtb.models.DH.Panda()
    T = SE3(0.7, 0.2, 0.1) * SE3.OA([0, 1, 0], [0, 0, -1])
    solution = robot.ikine_LM(T)
    traj = jtraj(robot.qz, solution.q, 50)
    robot.plot(traj.q, backend = 'pyplot', limits=[-0.25, 1.25, -0.5, 0.5, 0, 1], movie='panda_pyplot.gif')

def zadanie_1():
    robot = rtb.models.Puma560()
    t_start = robot.fkine(robot.qz)
    t_end1 = t_start * SE3(0.2,0,0)
    t_end2 = t_start * SE3(0,-0.2,0)
    t_end3 = t_start * SE3(0,0,0.2)
    t_end4 = t_start * SE3(0.25,0,0) * SE3.Ry(90,'deg')
    t_end5 = t_start * SE3(0,0,-0.2) * SE3.Rx(90,'deg')

    solution = robot.ikine_LM(t_end5)
    traj = jtraj(robot.qz,solution.q,50)
    robot.plot(traj.q, backend = 'pyplot', limits=[-0.25, 1.25, -0.5, 0.5, 0, 1], movie='panda_pyplot.gif')


def zadanie_2():
    robot = rtb.models.Puma560()
    t_start = robot.fkine(robot.qz)

    t_end = t_start * SE3(0.3,0,0) * SE3(0,0,-0.3) * SE3.Rx(90,'deg')

    solution = robot.ikine_LM(t_end)
    traj = jtraj(robot.qz,solution.q,50)
    robot.plot(traj.q, backend = 'pyplot', limits=[-0.25, 1.25, -0.5, 0.5, 0, 1], movie='panda_pyplot.gif')


def zadanie_3():
    pass # zastąp tę linię swoim kodem

# wykonywanie wybranej funkcji
if __name__ == '__main__':
    #przyklad_1()
    zadanie_1()
    #zadanie_2()
    #zadanie_3()