import numpy as np
import numpy.linalg as la
from numpy.linalg import inv
from numpy.linalg import norm
import matplotlib.pyplot as plt

def driver():
    f = lambda x: 1/(1+(10*x)**2)
    N = 19
    a = -1
    b = 1

    # create interpolation nodes
    i = np.arange(1,N+1,1)
    h = 2/(N-1)
    xint = -1 + ((i-1)*h)
    # print('xint =',xint)

    # create interpolation data
    yint = f(xint)
    # print('yint =',yint)

    # create the Vandermonde matrix
    V = Vandermonde(xint,N)
    # print('V = ',V)

    # invert the Vandermonde matrix
    Vinv = inv(V)
    # print('Vinv = ' , Vinv)

    # apply inverse to rhs to create the coefficients
    coef = Vinv @ yint
    # print('coef = ', coef)

    Neval = 1001
    xeval = np.linspace(a,b,Neval+1)
    yeval = eval_monomial(xeval,coef,N,Neval)

    # exact function
    yex = f(xeval)
    err = norm(yex-yeval)
    print('err = ', err)
    
    plt.figure()    
    plt.plot(xeval,yex,'r-', label='f(x)')
    plt.plot(xeval,yeval, 'b-', label='monomial approximation')
    plt.plot(xint, yint, 'bo', label='data points')
    plt.title(f'Monomial with N={N}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def eval_monomial(xeval,coef,N,Neval):
    yeval = coef[0]*np.ones(Neval+1)
    for j in range(1,N):
        for i in range(Neval+1):
            yeval[i] = yeval[i] + coef[j]*xeval[i]**j
    return yeval

def Vandermonde(xint,N):
    V = np.zeros((N,N))
    for j in range(N):
        V[j][0] = 1.0
    for i in range(1,N):
        for j in range(N):
            V[j][i] = xint[j]**i
    return V

driver()