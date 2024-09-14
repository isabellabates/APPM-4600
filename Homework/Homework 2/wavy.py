import numpy as np
import matplotlib.pyplot as plt

def x_theta(R, delta_r, f, p, theta):
    vals = R*(1 + (delta_r * np.sin((f*theta) + p))) * np.cos(theta)
    return vals

def y_theta(R, delta_r, f, p, theta):
    vals = R*(1 + (delta_r * np.sin((f*theta) + p))) * np.sin(theta)
    return vals

def driver():
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    # part a
    # p = 0
    # R = 1.2
    # delta_r = 0.1
    # f = 15
    # x = x_theta(R, delta_r, f, p, theta)
    # y = y_theta(R, delta_r, f, p, theta)
    # plt.plot(x,y)

    # part b
    for i in range(10):
       p = np.random.uniform(low=0,high=2)
       x = x_theta(i, 0.05, 2 + i, p, theta)
       y = y_theta(i, 0.05, 2 + i, p, theta)
       plt.plot(x,y)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot 2')
    plt.show()

driver()