import numpy as np

def driver():

    a = 4.82
    b = 5.2
    tol = 1e-4

    # part a
    print("Case (a): f(x) = (x - 5)^9")
    f = lambda x: (x-5)**9

    # call bisection routine
    [astar,ier,count] = bisection(f,a,b,tol)
    print('The approximate root is:', astar)
    print('The error message reads:', ier)
    print('f(astar) =', f(astar))
    print('Total number of iterations:', count) # print the # of iterations

    # part b
    print("Case (b): Expanded form of f(x)")
    f2 = lambda x: x**9-45*x**8+900*x**7-10500*x**6+78750*x**5-393750*x**4 +1312500*x**3 -2812500*x**2 +3515625*x -1953125

    [astar2,ier2,count2] = bisection(f2,a,b,tol)
    print('The approximate root is:', astar2)
    print('The error message reads:', ier2)
    print('f(astar) =', f2(astar2))
    print('Total number of iterations:', count2)

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
           return [astar, ier,count]
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