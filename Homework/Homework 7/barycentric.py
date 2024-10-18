import numpy as np
import numpy.linalg as la
from numpy.linalg import inv
from numpy.linalg import norm
import matplotlib.pyplot as plt

def driver():

    f = lambda x: 1/(1+(10*x)**2)
    N = 10000
    a = -1
    b = 1

    # create interpolation nodes
    i = np.arange(1,N+1,1)
    # h = 2/(N-1)
    # xint = -1 + ((i-1)*h)
    xint = np.cos((((2*i) - 1) * np.pi) / (2*N))

    yint = f(xint)

    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_b = np.zeros(Neval+1)

    weights = compute_weights(xint,N)

    for kk in range(Neval):
       yeval_b[kk] = eval_barycentric(xeval[kk], xint, yint, weights, N)

    fex = f(xeval)
    
    plt.figure()    
    plt.plot(xeval,fex,'r-', label='f(x)')
    plt.plot(xeval,yeval_b, 'b--', label='barycentric lagrange approx')
    plt.title(f'Barycentric with Chebyshev points, N={N}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def compute_phi(xint, xk):
    # initalize product for phi function (Φ_n(x))
    product = 1
    # loop through interpolation points
    for xi in xint:
        product = (xk - xi) * product # multiply by (x - x_i) for each i
    return product

def compute_weights(xint, N):
    # initial array to store barycentric weights
    w = np.zeros(N)
    # loop through each interpolation point
    for i in range(N):
        product = 1 # initialize product
        for j in range(N):
            if(i != j): # can't compute for i == j, no division by zero
                product = (xint[i] - xint[j]) * product
        w[i] = 1/product
    return w

def eval_barycentric(xeval, xint, yint, w, N): 
    sum = 0
    phi = compute_phi(xint, xeval) # compute Φ_n(x)
    for i in range(N):
        # add the weight for each interpolation point to the total sum
        sum = sum + (yint[i]*(w[i] / (xeval - xint[i])))
    return phi * sum

driver()