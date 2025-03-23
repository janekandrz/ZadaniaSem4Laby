import roboticstoolbox as rtb
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
import time


# nie modyfikuj tej funkcji:
def print_results(results):
    for res in results.items():
      print(f"time {res[0]} = {res[1][0]:.2f} ms")
      print(f"error {res[0]} = {res[1][1]:.1e}")
      
    sort_time = sorted(results.items(), key=lambda x: x[1][0], reverse=False)
    sort_error = sorted(results.items(), key=lambda x: x[1][1], reverse=False)

    print(sort_time[1][1][0]/sort_time[0][1][0] > 12)
    print(sort_error[0][0])


def zadanie_5():
    np.set_printoptions(precision=3, suppress=True)
    results = {
      'ikine_a': list(),
      'ikine_LM': list(),
      'ikine_GN': list(),
      'ikine_NR': list()
    }

    # Stworz robota i oblicz kin. prosta
    # twoj kod:
    robot = rtb.models.DH.Puma560()
    T= robot.fkine(robot.qn)
    

    # ikine_a
    # twoj kod
    start_time = time.time()
    sol = robot.ikine_a(T)
    end_time = time.time()
    tim = (end_time - start_time) * 1000  # Convert to milliseconds
    error = np.linalg.norm(T.A - robot.fkine(sol.q).A)
    results['ikine_a'] = [tim, error]

    # ikine_LM
    # twoj kod
    start_time = time.time()
    sol = robot.ikine_LM(T)
    end_time = time.time()
    tim = (end_time - start_time) * 1000  # Convert to milliseconds
    error = np.linalg.norm(T.A - robot.fkine(sol.q).A)
    results['ikine_LM'] = [tim, error]

    # ikine_GN
    # twoj kod
    start_time = time.time()
    sol = robot.ikine_GN(T)
    end_time = time.time()
    tim = (end_time - start_time) * 1000  # Convert to milliseconds
    error = np.linalg.norm(T.A - robot.fkine(sol.q).A)
    results['ikine_GN'] = [tim, error]

    # ikine_NR
    # twoj kod
    start_time = time.time()
    sol = robot.ikine_NR(T)
    end_time = time.time()
    tim = (end_time - start_time) * 1000  # Convert to milliseconds
    error = np.linalg.norm(T.A - robot.fkine(sol.q).A)
    results['ikine_NR'] = [tim, error]

    print_results(results)

if __name__ == '__main__':
    zadanie_6()
