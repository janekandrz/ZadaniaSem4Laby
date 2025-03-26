from os.path import join
import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from matplotlib import pyplot as plt
from roboticstoolbox.tools.trajectory import *


def check_smooth_traj(sol, jump_threshold=0.15):
    dists = []
    for current_q, next_q in zip(sol.q[1:], sol.q[2:]):
        for j1, j2 in zip(current_q, next_q):
            dist = np.fabs(j1-j2)
            dists.append(dist)
    print(max(dists))
    return max(dists) < jump_threshold


def zadanie_3():
    points_number = 50
    eef_height = 0.15
    r = 0.1
    x0 = 0.65
    y0 = 0.2
    angles = np.linspace(0,2*np.pi,points_number)# TODO: utwórz listę kątów od 0 do 2pi o długości points_number

    Pt_list = []
    for angle in angles:
        x = x0 + r * np.sin(angle)
        y = y0 + r * np.cos(angle)
        z = eef_height
        Pt_list.append([x,y,z]) # TODO: do listy Pt_list dla każdego kąta dodaj punkt [x,y,z] leżący na okręgu (wykorzystaj równanie parametryczne okręgu)

    Pt_list = np.asarray(Pt_list)
    x_toplot = Pt_list[:, 0]
    y_toplot = Pt_list[:, 1]
    
    # TODO: wykreśl wykres punktów o współrzędnych x_toplot, y_toplot
    #plt.figure()
    #plt.plot(x_toplot,y_toplot)
    #plt.show()

    robot = rtb.models.DH.Panda()# TODO: załaduj robota Panda
    
    T_init = robot.fkine(robot.qz) # TODO: do listy dodaj pierwszą macierz 4x4 - pozycję końcówki dla konfiguracji robot.qz
    
    T_list = [SE3(x,y,z)*SE3.OA([0,1,0],[0,0,-1]) for x,y,z in Pt_list]
    T_list[:] = [T_init] + T_list

    smooth_traj = False
    joint_c = []
    i = 0 
    while not smooth_traj:
        for T in T_list:
            sol = robot.ikine_LM(T)# TODO: oblicz kinematykę odwrotną dla listy macierzy transformacji
            if not sol.success:
                print("IK failed for", T, "\n")
                return
            joint_c.append(sol.q)
            i+=1
            #print(i, "   ", sol.q)
            if i==48:
                smooth_traj=True

    #smooth_traj = check_smooth_traj(sol)

    print(joint_c)
    joint_c = np.array(joint_c)
    traj = rtb.mstraj(joint_c,dt=0.02,tacc=0.2,qdmax=2.0) # TODO: utwórz trajektorię o wielu odcinkach - lista waypointów to lista konfiguracji z rozwiązania kin. odwr.
    rtb.xplot(traj.q, block=True)
    
    # TODO: wyświetl wizualizację ruchu w Swift / PyPlot
    robot.plot(traj.q, backend = 'pyplot', limits=[-0.25, 1.25, -0.5, 0.5, 0, 1], movie='laby3/zadanie3_panda_pyplot.gif') 

if __name__ == '__main__':
    zadanie_3()
