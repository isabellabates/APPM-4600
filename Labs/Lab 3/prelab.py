# import libraries
import numpy as np
import matplotlib.pyplot as plt
    
def driver():

    g = lambda x: (10/(x+4))**(1/2)
    # fixed point is p = 1.3652300134140976

    Nmax = 100
    tol = 1e-10

    # test f1 '''
    x0 = 1.5
    [xstar, ier, x, count] = fixedpt(g,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('g(xstar):', g(xstar))
    print('Error message reads:',ier)
    print('The approximations of the fixed point are ', x)

    print('It takes ' + str(count) + ' iterations to converge.')
    [fit, diff1, diff2] = compute_order(x, xstar)

    


# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    # initialize an empty array
    x = np.zeros((Nmax + 1, 1))
    x[0] = x0 # store initial guess

    count = 0
    while (count < Nmax):
       count = count + 1
       x1 = f(x0)
       x[count] = x1  # store current approximation

       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar, ier, x[:count + 1], count]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, x[:Nmax + 1], count]

def compute_order(x, xstar):
    # p_{n+1}-p (from the second index to the end)
    diff1 = np.abs(x[1::][0]-xstar)
    # p_n-p (from the first index to the second to last)
    diff2 = np.abs(x[0:-1][0]-xstar)

    # linear fit to log of difference
    fit = np.polyfit(np.log(diff2),np.log(diff1),1)
    print("the order equation is")
    print('log(|p_{n+1}-p|) = log(lamba) + alpha*log(|p_n-p|) where')
    print('lamba = ' +str(np.exp(fit[1])))
    print('alpha = ' +str(fit[0]))
    return [fit, diff1, diff2]
driver()