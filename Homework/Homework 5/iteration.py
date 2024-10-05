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
    [xstar, ier, its, iterations] = iteration_scheme(x0, tol, Nmax)
    elapsed = time.time()-t
    print('The approximate root is: ',xstar)
    print('The error message reads:',ier)
    print('This took this many seconds:',elapsed/50)
    print('The number of iterations is:',its)
    if ier == 0:
        print("Convergence was successful.")
    else:
        print("Failed to converge within the maximum number of iterations.")
    for it in range(its + 1):
        print('x value: ', iterations[it][0], 'y value: ', iterations[it][1])
    
def evalF(x): 
    F = np.zeros(2)
    F[0] = (3*(x[0]**2)) - (x[1]**2)  # f(x, y)
    F[1] = (3 * x[0] * (x[1]**2)) - (x[0]**3) - 1  # g(x, y)
    return F

def iteration_scheme(x0, tol, Nmax):
    M = np.array([[1/6, 1/18], [0, 1/6]])
    
    iterations = np.zeros([Nmax, 2])
    iterations[0] = x0

    for its in range(Nmax):
        F = evalF(x0) 
        
        x1 = x0 - M.dot(F)
        iterations[its + 1] = x1
        
        if norm(x1 - x0) < tol:
            ier=0
            return [x1, ier, its, iterations] 
        
        x0 = x1 
    ier=1
    return [x1, ier, Nmax, iterations] 

driver()

