import roboticstoolbox as rtb
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
import numpy as np
import matplotlib.pyplot as plt

def zadanie_3_2():
    B = SE3()
    pD = np.array([1,-2,2],dtype=np.float64)

    rPs = SO3(np.array([[-1,0,0],
                        [0,1,0],
                        [0,0,-1]]))
    rBs = SO3(np.array([[0,-1,0],
                        [1,0,0],
                        [0,0,1]]))
    tPs = np.array([3,-6,4],dtype=np.float64)

    tBs = np.array([2,5,0],dtype=np.float64)

    pTs = SE3.Rt(rPs,tPs) 
    bTs = SE3.Rt(rBs, tBs) 
    bD = bTs * pD   

    S = B*tBs    
    P = S*tPs
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    trplot(B.A, frame='B', color='blue', ax=ax, length=1)
    trplot(SE3(S).A, frame='S', color='green', ax=ax, length=1)
    trplot(SE3(P).A, frame='P', color='red', ax=ax, length=1)
    
    ax.quiver(0, 0, 0, bD[0], bD[1], bD[2], color='magenta', label='d^B', arrow_length_ratio=0.1)
    
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    plt.show()
    plt.savefig("laby1/plot.png")

def zadanie_3_2_1(): # szokujaco rozwioazanie banaszaka 
    B=SE3()
    t_BS = np.transpose(np.array([2, 5, 0]))
    R_BS = SO3.Rz(np.pi / 2)
    T_BS= SE3.Rt(R_BS,t_BS)
    S=B*T_BS
    t_PS = np.transpose(np.array([3, -6, 4]))
    R_PS = SO3(np.array([[-1, 0, 0],
                         [0, 1, 0],
                         [0, 0, -1]]))
    T_SP= SE3.Rt(np.transpose(R_PS), -np.transpose(R_PS)@t_PS)
    P= S*T_SP

    B.plot(frame='B', color='red', width=2)
    S.plot(frame='S', color='green', width=2)
    P.plot(frame='P', color='blue', width=2)
    plt.quiver(0, 0, 0, -2, 7, 2)

    plt.show()
    plt.savefig('outputimage.png')

# Wykonanie funkcji
if __name__ == '__main__':
    zadanie_3_2()
