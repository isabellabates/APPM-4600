import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y=math.exp(x)
    print(y) # to see what y is originally
    return y -1

def p(x):
    y = x + x**(2)/2 + x**(3)/6 + x**(4)/24 + x**(5)/120
    return y

def driver():
    # for part b
    test_values = [-100, -50, 1, 20, 50, 100]  # test values of x 
    for x in test_values:
        result = f(x)
        print(f"f({x}) = e^{x} - 1 = {result:.10e}")

    # part c
    x = 9.999999995*10**(-10)
    result = f(x)
    print(f"f({x}) = e^{x} - 1 = {result:.16e}")

    # part e
    result1 = p(x)
    print(f"f({x}) = e^{x} - 1 = {result1:.16e}")

driver()

