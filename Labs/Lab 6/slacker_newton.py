import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm

def driver():

    x0 = np.array([1,0])
    Nmax = 100
    tol = 1e-10

    t = time.time()
    for j in range(20):
        [xstar,ier,its,count] = SlackerNewton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Slacker Newton: the error message reads:',ier)
    print('Slacker Newton: took this many seconds:',elapsed/20)
    print('Slacker Newton: number of iterations is:',its)

def evalF(x): 
#    F = np.zeros(2)
#    F[0] = (4 * (x[0]**2)) + (x[1]**2) - 4
#    F[1] = x[0] + x[1] - np.sin(x[0] - x[1])
     F = np.zeros(3)
     F[0] = 3*x[0]-math.cos(x[1]*x[2])-1/2
     F[1] = x[0]-81*(x[1]+0.1)**2+math.sin(x[2])+1.06
     F[2] = np.exp(-x[0]*x[1])+20*x[2]+(10*math.pi-3)/3
     return F

def evalJ(x):
    J = np.array([[3.0, x[2]*math.sin(x[1]*x[2]), x[1]*math.sin(x[1]*x[2])],
    [2.*x[0], -162.*(x[1]+0.1), math.cos(x[2])],
    [-x[1]*np.exp(-x[0]*x[1]), -x[0]*np.exp(-x[0]*x[1]), 20]])
    return J
    
def evalJ(x): 
    J = np.array([[8*x[0],2*x[1]],[1-np.cos(x[0]-x[1]), 1+np.cos(x[0]-x[1])]])
    return J

def SlackerNewton(x0,tol,Nmax):

    J = evalJ(x0)
    Jinv = inv(J)
    count = 1
    for its in range(Nmax):

        F = evalF(x0)
        x1 = x0 - Jinv.dot(F)
       
        if (norm(x1-x0) < tol):
           xstar = x1
           ier = 0
           return[xstar,ier,its,count]
        
        if (norm(x1-x0) > 1e-2):
            J = evalJ(x1)
            Jinv = inv(J)
            count += 1
   
        x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its,count]  

driver()