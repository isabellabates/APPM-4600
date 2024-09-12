import math
import matplotlib.pyplot as plt
import numpy as np

def driver():

# question 1
    # f = lambda x: x**2*(x-1)

# part (a)
    # a1 = 0.5
    # b1 = 2

# part (b)
    # a2 = -1
    # b2 = 0.5

# part (c)
    # a3 = -1
    # b3 = 2

# question 2
# part (a)
    f1 = lambda x: (x-1)*(x-3)*(x-5)
    a1 = 0
    b1 = 2.4

# part (b)
    f2 = lambda x: (x-3)*(x-1)**2
    a2 = 0
    b2 = 2

# part (c)
    f3 = lambda x: math.sin(x)
    a3 = 0
    b3 = 0.1
    a4 = 0
    b4 = (3*math.pi)/4

    tol = 1e-5

    [astar,ier] = bisection(f1,a1,b1,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f1(astar))

    [astar,ier] = bisection(f2,a2,b2,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f2(astar))

    [astar,ier] = bisection(f3,a3,b3,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f3(astar))

    [astar,ier] = bisection(f3,a4,b4,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f3(astar))

# question 3
# part (a)
    f1 = lambda x: x*(1+(7-x**5)/x**2)**3
    # fixed point is alpha1 = 1.47577316159

# part (b)
    f2 = lambda x: x-(x**5 -7)/x**2
    #fixed point is alpha2 = 1.47577316159

# part (c)
    f3 = lambda x: x-(x**5 -7)/(5*x**4)
    #fixed point is alpha2 = 1.47577316159

# part (d)
    f4 = lambda x: x-(x**5 -7)/12
    #fixed point is alpha2 = 1.47577316159

    Nmax = 100
    tol = 1e-10

# test f1 '''
    x0 = 1.0
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f1(xstar):',f1(xstar))
    print('Error message reads:',ier)
    
#test f2 '''
    x0 = 0.0
    [xstar,ier] = fixedpt(f2,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f2(xstar):',f2(xstar))
    print('Error message reads:',ier)

#test f3 '''
    x0 = 0.0
    [xstar,ier] = fixedpt(f3,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f2(xstar):',f2(xstar))
    print('Error message reads:',ier)

#test f4 '''
    x0 = 0.0
    [xstar,ier] = fixedpt(f4,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f2(xstar):',f2(xstar))
    print('Error message reads:',ier)

# define routines
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

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
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier]

def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
      
driver()               

