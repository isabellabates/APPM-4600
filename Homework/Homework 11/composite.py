import numpy as np
from scipy.integrate import quad

def driver():
    
    f = lambda s: 1/(1+s**2)
    a = -5
    b = 5
    
    n_trap = 1291
    n_simp = 92

    I_trap = CompTrap(a,b,n_trap,f)
    I_simp = CompSimp(a,b,n_simp,f)

    [scipyQuad4, msg4, info4] = quad(f, -5, 5, epsabs=1e-4, full_output=1)
    [scipyQuad6, msg6, info6] = quad(f, -5, 5, epsabs=1e-6, full_output=1)

    print('I_trap= ', I_trap)
    print('number of function evaluations = ', n_trap)   
    print('I_simp= ', I_simp)
    print('number of function evaluations = ', n_simp)   
    print('Scipys quad routine (10^-4) = ', scipyQuad4)  
    print('number of function evaluations = ', info4['neval'])    
    print('Scipys quad routine (10^-6) = ', scipyQuad6)  
    print('number of function evaluations = ', info6['neval']) 

def CompTrap(a,b,n,f):
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h
    
    I_trap = h*f(xnode[0])*1/2
    
    for j in range(1,n):
         I_trap = I_trap+h*f(xnode[j])
    I_trap= I_trap + 1/2*h*f(xnode[n])
    
    return I_trap     

def CompSimp(a,b,n,f):
    h = (b-a)/n
    xnode = a+np.arange(0,n+1)*h
    I_simp = f(xnode[0])

    nhalf = n/2
    for j in range(1,int(nhalf)+1):
         # even part 
         I_simp = I_simp+2*f(xnode[2*j])
         # odd part
         I_simp = I_simp +4*f(xnode[2*j-1])
    I_simp= I_simp + f(xnode[n])
    
    I_simp = h/3*I_simp
    
    return I_simp     

driver()    
