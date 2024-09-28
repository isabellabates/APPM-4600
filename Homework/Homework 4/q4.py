import numpy as np
import scipy
     
def driver():
  # problem 4
  f = lambda x: np.exp(3 * x) - (27 * (x**6)) + (27 * (x**4) * np.exp(x)) - (9 * (x**2) * np.exp(2 * x))
  fp = lambda x: 3 * (np.exp(x) - (6 * x)) * ((np.exp(x) - (3 * (x**2))) ** 2)
  fpp = lambda x: 3 * (np.exp(x) - (3 * (x**2))) * ((90 * (x**2)) - (3 * np.exp(x) * ((x**2) + (8 * x) + 2)) + (3 * np.exp(2 * x)))
  
  # interval (3,5)
  p0 = 3
  Nmax = 100
  tol = 1e-13
 
  g = lambda x: f(x) / fp(x)
  gp = lambda x: 1 - ((f(x) * fpp(x)) / (fp(x) ** 2))

  (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
  alpha = compute_order(pstar,p)
  print('the approximate root is', pstar)
  print('the error message reads:', info)
  print('Number of iterations:', it)
  print('alpha = ' +str(alpha))

  (p, pstar, info, it) = newton(g, gp, p0, tol, Nmax)
  alpha = compute_order(pstar, p)
  print('the approximate root is', pstar)
  print('the error message reads:', info)
  print('Number of iterations:', it)
  print('alpha = ' +str(alpha))

def newton(f,fp,p0,tol,Nmax):
  p = np.zeros(Nmax+1)
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      # p1 = p0 - (3 * (f(p0) / fp(p0)))
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
   return alpha
        
driver()