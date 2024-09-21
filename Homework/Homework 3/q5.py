import numpy as np
import matplotlib.pyplot as plt

def driver():
    # 5(a) plot f(x)= x-4sin(2x)-3
    f = lambda x: x - 4*np.sin(2*x) - 3
    # x = np.linspace(-10,10,1000)
    x = np.linspace(-3,10,1000)
    y = f(x)

    plt.plot(x,y,color='orange')
    plt.hlines(0, -3, 10, colors='red', linestyles='dashed')
    plt.xlabel('x')
    plt.xticks(np.arange(-3, 10, 1))
    plt.ylabel('y')
    plt.title('f(x)=x-4sin(2x)-3')
    plt.show()
    
driver()