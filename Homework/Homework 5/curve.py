import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm

def driver():

    x0 = np.array([1,1,1])
    Nmax = 100
    tol = 1e-10

    f = lambda x: (x[0]**2) + (4*(x[1]**2)) + (4*(x[2]**2)) - 16

    [xstar,ier,its,iterations] =  iteration(f, x0,tol,Nmax)
    print('The approximate root is: ',xstar)
    print('The error message reads:',ier)
    print('The number of iterations is:',its)
    if ier == 0:
        print("Convergence was successful.")
    else:
        print("Failed to converge within the maximum number of iterations.")
    for it in range(its + 1):
        print('x value: ', iterations[it][0], 'y value: ', iterations[it][1])
    
    print(f(xstar))

def evalD(f, x):
    D = np.zeros(3)
    fx = 2 * x[0]
    fy = 8 * x[1]
    fz = 8 * x[2]

    d = f(x) / (fx**2 + fy**2 + fz**2)

    D[0] = d * fx
    D[1] = d * fy
    D[2] = d * fz
    return D

def iteration(f, x0, tol, Nmax):

    iterations = np.zeros([Nmax, 3])
    iterations[0] = x0

    for its in range(Nmax):
        D = evalD(f,x0)

        x1 = x0 - D
        iterations[its + 1] = x1

        if(f(x1) == 0):
            xstar = x1
            ier = 0
            return[xstar, ier, its+1, iterations]
        x0 = x1
    xstar = x1
    its = 1
    return[xstar,ier,Nmax,iterations]

driver()