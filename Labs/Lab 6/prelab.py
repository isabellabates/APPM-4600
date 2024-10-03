import numpy as np

def driver():

    s = np.pi/2
    f = lambda x: np.cos(x)

    h = 0.01 * 2.**(-np.arange(0,10))

    forward = lambda h: ((f(s+h)-f(s))/h)
    center = lambda h: ((f(s+h)-f(s-h))/(2*h))

    forwardDifference = forward(h)
    centeredDifference = center(h)

    print('Forward Difference:')
    for i in range(forwardDifference.size):
         print(forwardDifference[i])

    print('Centered Difference:')
    for i in range(centeredDifference.size):
         print(centeredDifference[i])

driver()



