import numpy as np

def driver():
    #for n in range(4, 21, 4):  # n = 4:4:20
    #    H = np.fromfunction(lambda i, j: 1 / (i + j + 1), (n, n), dtype=int)
    #   evalue, evector, iter = power_method(H)
    #    print(n, evalue, iter)
    n = 16
    H = np.fromfunction(lambda i, j: 1 / (i + j + 1), (n, n), dtype=int)
    smallest_evalue, evector, iter = power_method(H)

    exact_evalues = np.linalg.eigvalsh(H)
    exact_smallest_evalue = exact_evalues[0]

    print(smallest_evalue, exact_smallest_evalue, abs(smallest_evalue - exact_smallest_evalue))

def power_method(A, tol=1e-6, max_iter=1000):

    n = A.shape[0]
    v = np.random.rand(n)  # start with a random vector
    v = v / np.linalg.norm(v)  # normalize initial vector
    lambda_old = 0

    for k in range(max_iter):
        w = np.matmul(A,v)  
        v = w / np.linalg.norm(w)  # normalize the product
        lambda_new = np.matmul(v.T,A)
        lambda_new = np.matmul(lambda_new,v)

        if abs(lambda_new - lambda_old) < tol:
            #return lambda_new, v, k + 1
            return 1/lambda_new, v, k + 1

        lambda_old = lambda_new

    return lambda_new, v, max_iter

driver()

