import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from matplotlib import pyplot as plt
from roboticstoolbox.tools.trajectory import *


def check_smooth_traj(q_list, i, jump_threshold=0.15):
    dists = []
    for current_q, next_q in zip(q_list[:-1], q_list[1:]):
        for j1, j2 in zip(current_q, next_q):
            dist = np.fabs(j1-j2)
            dists.append(dist)
    print(max(dists), "  i:", i)
    return max(dists) < jump_threshold


def zadanie_3():
    points_number = 50
    eef_height = 0.15
    r = 0.1
    x0 = 0.65
    y0 = 0.2
    angles = np.linspace(0,2*np.pi,points_number)

    Pt_list = []
    T_list = []
    for angle in angles:
        x = x0 + r * np.cos(angle)
        y = y0 + r * np.sin(angle)
        z = eef_height
        Pt_list.append([x, y, z])
        
        # Compute tangent direction for orientation
        tx = -np.sin(angle)  # Derivative of cos(angle)
        ty = np.cos(angle)   # Derivative of sin(angle)
        tangent = [tx, ty, 0]
        tangent /= np.linalg.norm(tangent)  # Normalize
        
        # Create transformation with correct orientation and position
        T = SE3(x, y, z) * SE3.OA(tangent, [0, 0, -1])
        T_list.append(T)

    Pt_list = np.asarray(Pt_list)
    x_toplot = Pt_list[:, 0]
    y_toplot = Pt_list[:, 1]

    # TODO: wykreśl wykres punktów o współrzędnych x_toplot, y_toplot
    plt.figure()
    plt.plot(x_toplot,y_toplot)
    plt.show()

    robot = rtb.models.DH.Panda()
    
    #T_list = [SE3(Pt_list[0])*SE3.OA(tangent, [0, 0, -1])]# TODO: do listy dodaj pierwszą macierz 4x4 - pozycję końcówki dla konfiguracji robot.qz
    #for i in range(len(Pt_list)-1):
        #T_list.append(SE3(Pt_list[i+1]*SE3.OA(tangent, [0, 0, -1]))) # TODO: rozszerz listę o listę macierzy 4x4 leżących na okręgu (do utworzenia listy macierzy użyj listy punktów Pt_list, pamiętaj o zadaniu orientacji - chwytak w dół)

    i = 0
    smooth_traj = False
    while not smooth_traj:
        q_list = []
        for T in T_list:
            sol = robot.ikine_LM(T)
            if not sol.success:
                print("IK failed!:" , T , "\n")
                return
            q_list.append(sol.q)
            
        q_list = np.array(q_list)
        smooth_traj = check_smooth_traj(q_list,i)
        i+=1

        if i==50:
            smooth_traj=True
    
    # TODO: wyświetl wizualizację ruchu w Swift / PyPlot
    traj = mstraj(q_list, dt=0.05, tacc=0.1,tsegment= 2.0 , q0=robot.qz)
    rtb.xplot(traj.q, block=True)
    robot.plot(traj.q, backend = 'pyplot', limits=[-0.25, 1.25, -0.5, 0.5, 0, 1], movie='laby3/zadanie3_panda_pyplot.gif')
    

if __name__ == '__main__':
    zadanie_3()
