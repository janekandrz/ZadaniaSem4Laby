import roboticstoolbox as rtb
import roboticstoolbox.models as models
import numpy as np
from spatialmath import *
from spatialmath.base import *
from matplotlib import pyplot as plt
from roboticstoolbox.tools.trajectory import mstraj,jtraj

def check_smooth_traj(q1, q2 , jump_threshold=0.5):
    dists = []
    for i in range(len(q1)):
        dists.append(np.fabs(q1[i]-q2[i]))
    print(max(dists))
    return max(dists) < jump_threshold

def zadanie_3():
    points_number = 50
    eef_height = 0.15
    r = 0.1
    x0 = 0.65
    y0 = 0.2
    # TODO: utwórz listę kątów od 0 do 2pi o długości points_number
    angles = np.linspace(0,2*np.pi,points_number)

    Pt_list = np.array([[x0 +r*np.cos(angle),y0 + r*np.sin(angle),eef_height] for angle in angles])

    Pt_list = np.asarray(Pt_list)
    x_toplot = Pt_list[:, 0]
    y_toplot = Pt_list[:, 1]
    
    # TODO: wykreśl wykres punktów o współrzędnych x_toplot, y_toplot
    plt.figure()
    plt.plot(x_toplot,y_toplot)
    plt.show()

    # TODO: załaduj robota PandaP
    robot = models.DH.Panda()
    
    # TODO: do listy dodaj pierwszą macierz 4x4 - pozycję końcówki dla konfiguracji robot.qz
    # TODO: rozszerz listę o listę macierzy 4x4 leżących na okręgu (do utworzenia listy macierzy użyj listy punktów Pt_list, pamiętaj o zadaniu orientacji - chwytak w dół)
    T_list = [robot.fkine(robot.qz)] + [SE3(x,y,z)*SE3.OA([0,1,0],[0,0,-1]) for x,y,z in Pt_list]
   
    sol_init = robot.ikine_LM(T_list[0]).q
    sol_list = [sol_init] + [] 
    #i=0
    for pos in T_list:  
        smooth_traj = False
        sol = robot.ikine_LM(pos,q0=sol_list[i])
        """
        while not smooth_traj:
        # w tym while z checkiem 
            sol = robot.ikine_LM(pos, q0=sol_lsit[i]) # ro bez while zrobic 
            smooth_traj = check_smooth_traj(np.asarray(sol.q),np.asarray(sol_list[i]))
            print(i)
        i+=1 
        smooth_traj = False
        """
        #print(sol.q)
        sol_list.append(sol.q)

    #sol_list = [initial] + [sol_list]

    # TODO: utwórz trajektorię o wielu odcinkach - lista waypointów to lista konfiguracji z rozwiązania kin. odwr.
    traj = mstraj(np.asarray(sol_list),dt=0.02,tacc=0.02,qdmax=5.0) 
    rtb.xplot(traj.q, block=True)
    
    # TODO: wyświetl wizualizację ruchu w Swift / PyPlot
    robot.plot(traj.q, backend = 'pyplot', limits=[-0.25, 1.25, -0.5, 0.5, 0, 1], movie='zadanie3_panda_pyplot.gif') 


if __name__ == '__main__':
    zadanie_3()
