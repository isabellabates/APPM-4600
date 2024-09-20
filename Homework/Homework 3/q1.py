import numpy as np

def driver():
    # function 2x-1-sin(x)
    f = lambda x: 2*x-1-np.sin(x)
    # closed interval [a,b]
    a = 0
    b = 1

    tol = 1e-8

    # call bisection routine
    [astar,ier,count] = bisection(f,a,b,tol)
    print('The approximate root is:', astar)
    print('The error message reads:', ier)
    print('f(astar) =', f(astar))
    print('Total number of iterations:', count) # print the # of iterations

# define routines
def bisection(f,a,b,tol):
    # Inputs:
    # f,a,b - function and endpoints of initial interval
    # tol - bisection stops when interval length < tol
    # Returns:
    # astar - approximation of root
    # ier - error message
    # ier = 1 => Failed
    # ier = 0 == success

    # check there is a root in the interval
    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier, 0]

    # verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier, 0]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier, 0]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
        fd = f(d)
        if (fd ==0):   
           astar = d
           ier = 0
           return [astar, ier]
        if (fa*fd<0):
           b = d
        else: 
           a = d
           fa = fd
        d = 0.5*(a+b)
        count = count +1
    
    astar = d
    ier = 0
    return [astar, ier, count]
      
driver()   