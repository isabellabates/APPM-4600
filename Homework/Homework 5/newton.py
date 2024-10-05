import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm

def driver():
    x0 = np.array([1.0, 1.0]) 
    Nmax = 100
    tol = 1e-10
    
    t = time.time()
    [xstar, ier, its, iterations] = Newton(x0, tol, Nmax)
    elapsed = time.time()-t
    print('The approximate root is: ',xstar)
    print('Newton: the error message reads:',ier)
    print('Newton: took this many seconds:',elapsed/50)
    print('Newton: number of iterations is:',its)
    if ier == 0:
        print("Convergence was successful.")
    else:
        print("Failed to converge within the maximum number of iterations.")
    for it in range(its + 1):
        print('x value: ', iterations[it][0], 'y value: ', iterations[it][1])
    
def evalF(x): 
    F = np.zeros(2)
    F[0] = (3*(x[0]**2)) - (x[1]**2) 
    F[1] = (3 * x[0] * (x[1]**2)) - (x[0]**3) - 1 
    return F

def evalJ(x):
    J = np.array([[6*x[0], -(2*x[1])],
                  [(3 * (x[1]**2)) - (3*(x[0]**2)), 6*x[0]*x[1]]])
    return J

def Newton(x0,tol,Nmax):
    iterations = np.zeros([Nmax, 2])
    iterations[0] = x0

    for its in range(Nmax):
        J = evalJ(x0)
        Jinv = inv(J)
        F = evalF(x0)

        x1 = x0 - Jinv.dot(F)
        iterations[its + 1] = x1
        
        if (norm(x1-x0) < tol):
            xstar = x1
            ier =0
            return[xstar, ier, its, iterations]
        x0 = x1
    xstar = x1
    ier = 1
    return[xstar,ier,its,iterations]

driver()

