import numpy as np

def driver():

    t = np.linspace(0, np.pi, 31)
    y = np.cos(t)
    S = 0
    for i in range(31):
        S += t[i] * y[i]

    print(f"The sum is: {S}")

driver()

