# wczytanie potrzebnych podczas zajęć bibliotek:
import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
import matplotlib
from matplotlib import pyplot as plt
# ...

#komentarz test windowsa srindowsa czy działa git extensions 

# definicje funkcji:
def przyklad_1():
    pass # zastąp tę linię swoim kodem

def zadanie_1():
    list = np.linspace(0,2*np.pi,num=30)
    rots = SO3.Rx(list)
    print(rots)

def zadanie_1_s():
    Rz = SO3.Rz(-(np.pi/3))
    Ry = SO3.Ry(np.pi/6)
    Rx = SO3.Rx(np.pi/4)

    #roll = pi/4 pitch = pi/6 yaw = -pi/3

    R03 = Rz*Ry*Rx 
    R03.animate(frame="A", color="red", width=2,dims=[0,3],nframes=100)

    #

    print("wyznacznik = 1")
    print(np.linalg.det(R03.R))
    print("transpose = invers")

    print(np.transpose(R03.R))
    print(np.linalg.inv(R03.R))

    print("jednostkowa długosc kolumn")

    print(np.transpose(R03.n)*R03.o == np.transpose(R03.o)*R03.a == np.transpose(R03.a)*R03.n == 0)

    print("jednostkowe długosci")

    lenn = np.linalg.norm(R03.n)
    leno = np.linalg.norm(R03.o)
    lena = np.linalg.norm(R03.a)

    print(lenn == leno == lena == 1)

    print("cross product")
    print(np.cross(R03.n,R03.o)==R03.a and np.cross(R03.o,R03.a)==R03.n and np.cross(R03.a,R03.n)==o)

def zadanie_2():
    pass



# wykonywanie wybranej funkcji
if __name__ == '__main__':
    zadanie_1_s()