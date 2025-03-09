# wczytanie potrzebnych podczas zajęć bibliotek:
import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
from matplotlib import pyplot as plt

# UWAGA! DOSTOSUJ NAZWY ZMIENNYCH DO PODANYCH PONIZEJ.
# Nalezy pozostawic nazwy ponizszych zmiennych bez zmian!
def zadanie_3_1():
    pD = np.array([1,-2,2],dtype=np.float64)

    rPs = SO3(np.array([[-1,0,0],
                        [0,1,0],
                        [0,0,-1]]))
    rBs = SO3(np.array([[0,-1,0],
                        [1,0,0],
                        [0,0,1]]))
    tPs = np.array([3,-6,4],dtype=np.float64)
    tBs = np.array([2,5,0],dtype=np.float64)
    mtBs = np.array([-2,-5,0],dtype=np.float64)


    pTs = SE3.Rt(rPs,tPs) # Transformacja ukladu S wzgledem ukladu P
    bTs = SE3.Rt(rBs, tBs) # Transformacja ukladu S wzgledem ukladu B
    sD = pTs * pD# punkt D w ukladzie S
    bD = bTs * pD # punkt D w ukladzie B
    
    # nie umieszczaj w kodzie innych funkcji print
    print(f'pTs:\n{pTs}\nbTs:\n{bTs}\nsD.t:\n{np.transpose(sD)}\nbD.t:\n{np.transpose(bD)}') # pozostaw ta linie bez zmian

# wykonywanie wybranej funkcji
if __name__ == '__main__':
    zadanie_3_1()


    #odpowiedz
    #[-2 7 2 ]