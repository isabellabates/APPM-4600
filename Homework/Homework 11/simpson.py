import numpy as np

def driver():

    f = lambda t: -np.cos(1/t) * t
    a = 0
    b = 1
    n = 4

    I_simp = CompSimp(a,b,n,f)

    print('I_simp= ', I_simp)
    print('number of function evaluations = ', n)   


def CompSimp(a,b,n,f):
    h = (b-a)/n
    xnode = np.linspace(a,b,n+1)

    # needs to be 0 otherwise limit does not exist
    I_simp = 0

    for j in range(1,n,2):
        # even part
        I_simp += 2 * f(xnode[j])
        # odd part
        I_simp += 4 * f(xnode[j+1])
    I_simp -= f(xnode[n])
    return (h/3)*I_simp

driver()