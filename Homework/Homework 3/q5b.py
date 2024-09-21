import numpy as np
    
def driver():
    f = lambda x:  -np.sin(2 * x) + ((5/4) * x) - (3/4)
    Nmax = 100
    tol = 0.5e-10
    
    x0 = 4.5
    [xstar,ier,count] = fixedpt(f,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f(xstar):',f(xstar))
    print('Error message reads:',ier)
    print('Total number of iterations:', count)


# define routines
def fixedpt(f,x0,tol,Nmax):
    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    
    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs((x1-x0) / x1) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier,count]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier,count]
driver()