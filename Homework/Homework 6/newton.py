import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    #initial_guesses = [np.array([1, 1]), np.array([1, -1]), np.array([0, 0])]
    #x0 = np.array([0,1,1])
    x0 = np.array([-0.01576827, 0.14095965, 1.00981878])
    Nmax = 100
    #tol = 1e-10
    tol = 1e-6

    t = time.time()
    for j in range(50):
        [xstar,ier,its] =  Newton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Newton: the error message reads:',ier) 
    print('Newton: took this many seconds:',elapsed/50)
    print('Netwon: number of iterations is:',its)
    
    #for x0 in initial_guesses:
     #   print(f"Testing with initial guess: {x0}")
     #   t = time.time()
     #   for j in range(50):
     #       [xstar,ier,its] =  Newton(x0,tol,Nmax)
     #   elapsed = time.time()-t
     #   print(xstar)
     #   print('Newton: the error message reads:',ier) 
     #   print('Newton: took this many seconds:',elapsed/50)
     #   print('Netwon: number of iterations is:',its)
        
def evalF(x): 
    #F = np.zeros(2)
    #F[0] = (x[0]**2) + (x[1]**2) - 4
    #F[1] = np.exp(x[0]) + x[1] - 1

    F = np.zeros(3)
    F[0] = x[0] + np.cos(x[0]*x[1]*x[2]) - 1
    F[1] = ((1-x[0])**(1/4)) + x[1] + (0.05 * (x[2]**2)) - (0.15 * x[2]) - 1
    F[2] = -(x[0]**2) - (0.1 * (x[1]**2)) + (0.01 * x[1]) + x[2] - 1
    return F
    
def evalJ(x): 
    #J = np.array([[2*x[0], 2*x[1]],
    #              [np.exp(x[0]), 1]])
    J = np.array([[1-(x[1]*x[2]*np.sin(x[0]*x[1]*x[2])), -x[0]*x[2]*np.sin(x[0]*x[1]*x[2]), -x[0]*x[1]*np.sin(x[0]*x[1]*x[2])],
                   [(-1/4)*((1-x[0])**(-3/4)), 1, (0.1*x[2]) - 0.15],
                   [-2*x[0], (-0.2*x[1]) + 0.01, 1]])
    return J

def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       J = evalJ(x0)
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]

driver()