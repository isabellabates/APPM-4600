import math
import matplotlib.pyplot as plt
import numpy as np


def driver():
    # chosen values for x
    x1 = math.pi
    x2 = 10**6

    delta = np.logspace(-16, 0, num=100)

    orig1 = lambda x: np.cos(x1 + x) - np.cos(x)
    orig2 = lambda x: np.cos(x2 + x) - np.cos(x)

    new1 = lambda x: -2 * np.sin((x / 2) + x1) * np.sin(x)
    new2 = lambda x: -2 * np.sin((x / 2) + x2) * np.sin(x)

    expr1 = new1(delta) - orig1(delta)
    expr2 = new2(delta) - orig2(delta)

    diff_x1 = np.abs(new1(delta) - orig1(delta))
    diff_x2 = np.abs(new2(delta) - orig2(delta))

    plt.figure(figsize=(10, 6))

    # Plot for x = pi
    plt.subplot(2, 1, 1)
    plt.plot(delta, diff_x1, label=r"$x = \pi$", color="blue")
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(r'$\delta$')
    plt.ylabel(r'Difference')
    plt.title('Difference between expressions at x = 10^6')
    plt.grid(True)

    # Plot for x = 10^6
    plt.subplot(2, 1, 2)
    plt.plot(delta, diff_x2, label=r"$x = 10^6$", color="green")
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(r'$\delta$')
    plt.ylabel(r'Difference')
    plt.grid(True)

    plt.show()

    # part b
    taylor1 = lambda x: -x * np.sin(x1) + ((x**2)/2)
    taylor2 = lambda x: -x * np.sin(x2) + ((x**2)/2)

    new3 = lambda x: -2 * np.sin((x / 2) + x1) * np.sin(x)
    new4 = lambda x: -2 * np.sin((x / 2) + x2) * np.sin(x)

    expr1 = new3(delta) - taylor1(delta)
    expr2 = new4(delta) - taylor2(delta)

    plt.plot(delta, expr2)
    plt.xscale('log')
    plt.xlabel(r'$\delta$')
    plt.ylabel('y')
    plt.title('Difference between expressions at x = 10^6')
    plt.show()

driver()