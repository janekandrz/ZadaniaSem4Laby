import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from matplotlib import pyplot as plt
from roboticstoolbox.tools.trajectory import *
from roboticstoolbox.backends.swift import Swift


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
    angles = # TODO: utwórz listę kątów od 0 do 2pi o długości points_number

    Pt_list = []
    for angle in angles:
        Pt_list.append([...]) # TODO: do listy Pt_list dla każdego kąta dodaj punkt [x,y,z] leżący na okręgu (wykorzystaj równanie parametryczne okręgu)

    Pt_list = np.asarray(Pt_list)
    x_toplot = Pt_list[:, 0]
    y_toplot = Pt_list[:, 1]
    
    # TODO: wykreśl wykres punktów o współrzędnych x_toplot, y_toplot


    robot = # TODO: załaduj robota Panda
    
    T_list = # TODO: do listy dodaj pierwszą macierz 4x4 - pozycję końcówki dla konfiguracji robot.qz
    T_list.extend(...) # TODO: rozszerz listę o listę macierzy 4x4 leżących na okręgu (do utworzenia listy macierzy użyj listy punktów Pt_list, pamiętaj o zadaniu orientacji - chwytak w dół)

    smooth_traj = False
    while not smooth_traj:
        sol = # TODO: oblicz kinematykę odwrotną dla listy macierzy transformacji
        if not sol.success:
            print("IK failed!\n")
            return
        smooth_traj = check_smooth_traj(sol)

    traj = # TODO: utwórz trajektorię o wielu odcinkach - lista waypointów to lista konfiguracji z rozwiązania kin. odwr.
    rtb.xplot(traj.q, block=True)
    
    # TODO: wyświetl wizualizację ruchu w Swift / PyPlot
    

if __name__ == '__main__':
    zadanie_3()
