import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm

def driver():
    
    f = lambda x: np.sin(10*x)
    a = 0
    b = 2*np.pi
    
    # number of intervals
    Nint = 25
    xint = np.linspace(a,b,Nint+1)

    yint = f(xint)

    # create points you want to evaluate at
    Neval = 100
    xeval =  np.linspace(xint[0],xint[Nint],Neval+1)
   
    (M,C,D) = create_periodic_spline(yint,xint,Nint)
    
    print('M =', M)

    yeval = eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D)
    
    # evaluate f at the evaluation points
    fex = f(xeval)
        
    nerr = norm(fex-yeval)
    print('nerr = ', nerr)
    
    plt.figure()    
    plt.plot(xeval,fex,'r-',label='exact function')
    plt.plot(xeval,yeval,'b--',label='periodic spline') 
    # plt.plot(xeval,yeval,'b--',label='clamped spline') 
    plt.title(f'periodic cubic spline method for N={Nint}')
    # plt.title(f'natural cubic spline for N={Nint}')
    plt.legend()
    plt.show()
     
    err = abs(yeval-fex)
    plt.figure() 
    plt.semilogy(xeval,err,'r--',label='absolute error')
    plt.legend()
    plt.show()

def create_periodic_spline(yint,xint,N):
#    create the right  hand side for the linear system
    b = np.zeros(N+1)
#  vector values
    h = np.zeros(N+1)  
    for i in range(1,N):
       hi = xint[i]-xint[i-1]
       hip = xint[i+1] - xint[i]
       b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
       h[i-1] = hi
       h[i] = hip

#  create matrix so you can solve for the M values
# This is made by filling one row at a time 
    A = np.zeros((N+1,N+1))

    # set up A for periodic conditions
    for j in range(1, N):
        A[j][j - 1] = h[j - 1] / 6
        A[j][j] = (h[j] + h[j - 1]) / 3
        A[j][j + 1] = h[j] / 6

    # periodic boundary conditions
    A[0][0] = (h[0] + h[N - 1]) / 3
    A[0][1] = h[0] / 6
    A[0][N] = h[N - 1] / 6
    A[N][N - 1] = h[N - 1] / 6
    A[N][0] = h[N - 1] / 6
    A[N][N] = (h[0] + h[N - 1]) / 3

    Ainv = inv(A)
    
    M  = Ainv.dot(b)

#  Create the linear coefficients
    C = np.zeros(N)
    D = np.zeros(N)
    for j in range(N):
       C[j] = yint[j]/h[j]-h[j]*M[j]/6
       D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
    return(M,C,D)
 
def create_natural_spline(yint,xint,N):
#    create the right  hand side for the linear system
    b = np.zeros(N+1)
#  vector values
    h = np.zeros(N+1)  
    for i in range(1,N):
       hi = xint[i]-xint[i-1]
       hip = xint[i+1] - xint[i]
       b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
       h[i-1] = hi
       h[i] = hip

#  create matrix so you can solve for the M values
# This is made by filling one row at a time 
    A = np.zeros((N+1,N+1))
    A[0][0] = 1.0
    for j in range(1,N):
       A[j][j-1] = h[j-1]/6
       A[j][j] = (h[j]+h[j-1])/3 
       A[j][j+1] = h[j]/6
    A[N][N] = 1

    Ainv = inv(A)
    
    M  = Ainv.dot(b)

#  Create the linear coefficients
    C = np.zeros(N)
    D = np.zeros(N)
    for j in range(N):
       C[j] = yint[j]/h[j]-h[j]*M[j]/6
       D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
    return(M,C,D)
       
def eval_local_spline(xeval,xi,xip,Mi,Mip,C,D):
# Evaluates the local spline as defined in class
# xip = x_{i+1}; xi = x_i
# Mip = M_{i+1}; Mi = M_i

    hi = xip-xi
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
            + C*(xip-xeval) + D*(xeval-xi)
    return yeval 
    
    
def  eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D):
    
    yeval = np.zeros(Neval+1)
    
    for j in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        atmp = xint[j]
        btmp= xint[j+1]
        
#   find indices of values of xeval in the interval
        ind= np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]

# evaluate the spline
        yloc = eval_local_spline(xloc,atmp,btmp,M[j],M[j+1],C[j],D[j])
#        print('yloc = ', yloc)
#   copy into yeval
        yeval[ind] = yloc

    return(yeval)
           
driver()               

