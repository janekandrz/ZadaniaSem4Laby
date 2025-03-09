import roboticstoolbox as rtb
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
import numpy as np
import matplotlib.pyplot as plt

def zadanie_3_2():
    # Definicje transformacji i punktów z zadania 3.1
    pD = np.array([1, -2, 2], dtype=np.float64)
    
    rPs = SO3(np.array([[-1, 0, 0],
                        [0, 1, 0],
                        [0, 0, -1]]))
    rBs = SO3(np.array([[0, -1, 0],
                        [1, 0, 0],
                        [0, 0, 1]]))
    tPs = np.array([3, -6, 4], dtype=np.float64)
    tBs = np.array([2, 5, 0], dtype=np.float64)
    
    pTs = SE3.Rt(rPs, tPs)  # Transformacja S względem P
    bTs = SE3.Rt(rBs, tBs)  # Transformacja S względem B
    
    # Obliczenie współrzędnych punktu D w układach S i B
    sD = pTs.inv() * pD     # Punkt D w układzie S
    bD = bTs * sD           # Punkt D w układzie B
    
    # Tworzenie wykresu
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Rysowanie układu B (globalnego)
    trplot(np.eye(4), frame='B', color='blue', ax=ax, length=1)
    
    # Rysowanie układu S (transformacja B -> S)
    trplot(bTs.inv().A, frame='S', color='green', ax=ax, length=1)
    
    # Rysowanie układu P (transformacja B -> P)
    trplot((pTs * bTs.inv()).A, frame='P', color='red', ax=ax, length=1)
    
    # Rysowanie wektora d^B (od początku układu B do punktu bD)
    ax.quiver(0, 0, 0, bD[0], bD[1], bD[2], color='magenta', label='d^B', arrow_length_ratio=0.1)
    
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    ax.legend()
    plt.show()
    plt.savefig("laby1/plot.png")

# Wykonanie funkcji
if __name__ == '__main__':
    zadanie_3_2()
