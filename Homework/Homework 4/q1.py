import numpy as np
import matplotlib.pyplot as plt
import scipy
   
def driver():
  # given:
  Ti = 20   # Celsius
  Ts = -15  # Celsius
  alpha = 0.138e-6  # m^2/s
  t = 60 * 24 * 3600    # seconds

  # part (a) find f and f'
  f = lambda x: ((Ti - Ts) * scipy.special.erf(x / (2 * np.sqrt(alpha * t)))) + Ts
  f_deriv = lambda x: ((Ti - Ts) / np.sqrt(np.pi * alpha * t)) * np.exp(-(x**2)/(4*alpha*t))

  # part (a) plot f
  x = np.linspace(0, 5, 500)
  y = f(x)

  plt.figure(figsize=(8, 6))
  plt.plot(x, y)
  plt.axhline(0, color='red', linestyle='--', label='$f(x) = 0$')
  plt.xlabel('Depth (x) in meters')
  plt.ylabel('f(x)')
  plt.title('Plot of $f(x)$ vs Depth $x$')
  plt.show()

  # part (b) 
  a = 0
  b = 1
  tol = 1e-13

  [r,ier, count] = bisection(f,a,b,tol)
  print('the number of iterations was ', count)
  print('the approximate root is',r)
  print('the error message reads:',ier)
  print('f(astar) =', f(r))

  # part (c)
  fp = lambda x: ((Ti - Ts) / np.sqrt(np.pi * alpha * t)) * np.exp(-(x**2)/(4*alpha*t))
  p0 = 1

  Nmax = 100

  (p,pstar,info,it) = newton(f,fp,p0,tol,Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)

def bisection(f,a,b,tol):
    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
       ier = 1
       r = a
       return [r, ier, 0]
    if (fa == 0):
      r = a
      ier =0
      return [r, ier, 0]
    if (fb ==0):
      r = b
      ier = 0
      return [r, ier, 0]
    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        r = d
        ier = 0
        return [r, ier, count]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
    r = d
    ier = 0
    return [r, ier, count]

def newton(f,fp,p0,tol,Nmax):
  p = np.zeros(Nmax+1)
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      #p1 = p0 - (3 * (f(p0) / fp(p0)))
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [np.trim_zeros(p),pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]

def compute_order(x, xstar):
    # p_{n+1}-p (from the second index to the end)
    diff1 = np.abs(x[1::][0]-xstar)
    # p_n-p (from the first index to the second to last)
    diff2 = np.abs(x[0:-1][0]-xstar)

    # linear fit to log of difference
    fit = np.polyfit(np.log(diff2),np.log(diff1),1)
    print("the order equation is")
    print('log(|p_{n+1}-p|) = log(lamba) + alpha*log(|p_n-p|) where')
    print('lamba = ' +str(np.exp(fit[1])))
    print('alpha = ' +str(fit[0]))
    return [fit, diff1, diff2]
     
driver()