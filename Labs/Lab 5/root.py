import numpy as np

def driver():  
    f = lambda x: x**3+x-4
    a = 1
    b = 4

    tol = 1e-7
    Nmax=100

    [astar,ier] = bisection(f,a,b,tol,Nmax)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))

def bisection(f,fp,a,b,tol,Nmax):
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
    fb = f(b)

    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb == 0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)

    p0 = d

    p = np.zeros(Nmax+1)
    p[0] = p0
    for it in range(Nmax):
        p1 = p0-f(p0)/fp(p0)
        p[it+1] = p1
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [p,pstar,info,it]
        p0 = p1
    pstar = p1
    info = 1
    return [p,pstar,info,it]

    #while (abs(d-a)>tol or abs(a-(f(d)/fp(d)))<1): # when |g'(x)| < 1
    #  fd = f(d)
    #  if (fd ==0):
    #    astar = d
    #    ier = 0
    #    return [astar, ier]
    #  if (fa*fd<0):
    #     b = d
    #  else: 
    #    a = d
     #   fa = fd
     # d = 0.5*(a+b)
     # count = count +1
      
    #astar = d
    #ier = 0
    #return [astar, ier]
      
driver()               

