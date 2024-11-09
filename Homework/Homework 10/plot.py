import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm

def driver():
    f = lambda x: np.sin(x)
    t = lambda x: 1-x+x**2/2-x**3/6+x**4/24-x**5/120
    p3_3 = lambda x: (x - (7/60)*x**3) / (1 + (1/20)*x**2)
    p2_4 = lambda x: (x) / (1 + (1/6)*x**2 + (7/360)*x**4)
    p4_2 = lambda x: (x - (7/60)*x**3) / (1 + (1/20)*x**2)

    x = np.linspace(0, 5, 500)

    error_maclaurin = np.abs(f(x) - t(x))
    error_p3_3 = np.abs(f(x) - p3_3(x))
    error_p2_4 = np.abs(f(x) - p2_4(x))
    error_p4_2 = np.abs(f(x) - p4_2(x))

    plt.figure(figsize=(10, 6))
    plt.plot(x, error_maclaurin, label="Maclaurin")
    plt.plot(x, error_p3_3, label="Pade (3,3)")
    plt.plot(x, error_p2_4, label="Pade (2,4)")
    plt.plot(x, error_p4_2, label="Pade (4,2)")
    plt.yscale("log")
    plt.xlabel("x")
    plt.ylabel("error")
    plt.title("Error Comparison")
    plt.legend()
    plt.show()

driver() 