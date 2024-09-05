import numpy as np
import matplotlib.pyplot as plt

# some basics
x=[1,2,3]
x*3

y=np.array([1,2,3])
3*y

# print('this is 3y', 3*y)

#X = np.linspace(0, 2 * np.pi, 100)
#Ya = np.sin(X)
#Yb = np.cos(X)
#plt.plot(X, Ya)
#plt.plot(X, Yb)
#plt.xlabel('x')
#plt.ylabel('y')
# plt.show()

# exercises: the basics
# 1
x=np.linspace(0,20,21)
y=np.arange(0,21,1)
print(x)
print(y)

# 2
x[0:3]

# 3
print('the first three entries of x are', x[0:3])

# 4
w = 10**(-np.linspace(1,10,10))
print(w)

x = [i for i in range(len(w))]
print(x)

plt.plot(x, w)
plt.semilogy()
plt.xlabel('x')
plt.ylabel('w')
plt.show()

# 5
s = 3*w

plt.plot(x, s)
plt.semilogy()
plt.xlabel('x')
plt.ylabel('s')
plt.show()

# 6 
# I saved them as pngs.






