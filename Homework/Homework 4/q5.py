import numpy as np
import matplotlib.pyplot as plt
        
def driver():
  # problem 5
  f = lambda x: (x**6) - x - 1

  # newtons method
  fp = lambda x: (6 * (x**5)) - 1
  p0 = 2

  Nmax = 100
  tol = 1e-13

  (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
  alpha = compute_order(pstar,p)
  print('the approximate root is', pstar)
  print('the error message reads:', info)
  print('number of iterations:', it)

  # 5(a) print the error for each step in the iteration 
  errors = abs(p - pstar)
  print('Errors:')
  for error in errors:
    print('{0:.16f}'.format(error))

  # secant method
  x0 = 2
  x1 = 1

  (p, r, ier, count) = secant(f,x0,x1,tol, Nmax)
  print('the approximate root is', r)
  print('the error message reads:',ier)
  print('number of iterations:', count)

  errors = abs(p - r)
  print('Errors:')
  for error in errors:
    print('{0:.16f}'.format(error))

  # 5(b) plot errors on log-log axes where α is the exact root for both methods
  x1 = np.array([0.5459041338497894,0.2960148498375430,0.1202468177079170,0.0268142943717937,0.0016291357689859,0.0000063899421097,0.0000000000987017])
  y1 = np.array([0.8652758615984806, 0.5459041338497894,0.2960148498375430,0.1202468177079170,0.0268142943717937,0.0016291357689859,0.0000063899421097])

  x2 = np.array([0.1185951061434549,0.0558536302751180,0.0170683074599678,0.0021925881853864,0.0000926696033334,0.0000004924528145,0.0000000001103035, 0.0000000000000002])
  y2 = np.array([0.1347241384015194,0.1185951061434549,0.0558536302751180,0.0170683074599678,0.0021925881853864,0.0000926696033334,0.0000004924528145,0.0000000001103035])  

  plt.loglog(x1,y1)
  plt.loglog(x2,y2)
  plt.legend(['Newton\'s Method', 'Secant Method'])
  plt.xlabel("|x(n) - r|")
  plt.ylabel("|x(n+1) - r|")
  plt.title("Error of Newton and Secant Methods")
  plt.show()

  # find slopes
  x1_nonzero = x1[x1 > 0]
  y1_nonzero = y1[y1 > 0]
  x2_nonzero = x2[x2 > 0]
  y2_nonzero = y2[y2 > 0]

  slope_newton, intercept_newton = np.polyfit(np.log(x1_nonzero), np.log(y1_nonzero), 1)
  slope_secant, intercept_secant = np.polyfit(np.log(x2_nonzero), np.log(y2_nonzero), 1)
  print("slope of newton's method: " +str(slope_newton))
  print("slope of secant method: " +str(slope_secant))

def secant(f,x0,x1,tol,Nmax):
   fx0 = f(x0)
   fx1 = f(x1)
   if(fx0 == 0):
      r = fx0
      ier = 0
      return [r, ier, 0]
   if(fx1 == 0):
      r = fx1
      ier = 0
      return [r, ier, 0]
   p = np.zeros(Nmax+1)
   p[0] = x1
   for it in range(Nmax):
      if(fx0 - fx1 == 0):
         ier = 1
         r = x1
         return [np.trim_zeros(p), r, ier, it]
      x2 = x1 - ((fx1 * (x1 - x0)) / (fx1 - fx0))
      p[it + 1] = x2
      if(abs(x2 - x1) < tol):
         r = x2
         ier = 0
         return [np.trim_zeros(p), r, ier, it]
      x0 = x1
      x1 = x2
      fx0 = f(x0)
      fx1 = f(x1)
   r = x1
   ier = 1
   return [p, r, 1, Nmax]

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
   index = 2
   error1 = abs(xstar[xstar.size - index] - x)
   while(error1 < 1e-4):
      index += 1
      # p_{n+1}-p (from the second index to the end)
      error1 = abs(xstar[xstar.size - index] - x)
   # p_n-p (from the first index to the second to last)
   error2 = abs(xstar[xstar.size - (index + 1)] - x)
   alpha = np.log(error1) / np.log(error2)
   print('alpha = ' +str(alpha))
   return alpha
    
driver()