# Consider the polynomial 
# p(x) = (x-2)^9 = x^9 - 18x^8 + 144x^7 - 672x^6 + 2016x^5 - 4032x^4 + 5376x^3 - 4608x^2 + 2304x - 512

import matplotlib.pyplot as plt
import math
import numpy as np

def driver():

    x_vals = np.arange(1.920,2.081,0.001)

    p_coeff = lambda x: x**9 - 18*(x**8) + 144*(x**7) - 672*(x**6) + 2016*(x**5) - 4032*(x**4) + 5376*(x**3) - 4608*(x**2) + 2304*x - 512
    p_exp = lambda x: (x-2)**9

    p1 = p_coeff(x_vals)
    p2 = p_exp(x_vals)

    # i. plot p(x) via its coefficients
    plt.plot(x_vals, p1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Evaluating p using expanded form')
    plt.show()

    # ii. plot p(x) via its binomial form
    plt.plot(x_vals, p2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Evaluating p using binomial form')
    plt.show()

    '''
    iii. What is the difference? What is causing the discrepancy? Which plot is correct?
    
    The obvious difference between the two plots is p(x) evaluated via its binomial form
    is a much smoother curve compared to p(x) evaluated via its coefficients.
    The plot of p(x) using its binomial form looks more correct because the curve should be smooth.
    When we are plotting via its coefficients, there are a lot of calculations that have to be made.
    The computer has to plug in the x value 9 times, while it only has to plug x in once for the binomial form.
    This could cause the outputs to be off. The more coefficients, the greater the error of the output could be 
    because the computer is rounding the decimal of the output each time.
    '''

driver()