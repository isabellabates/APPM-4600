import numpy as np

def driver():
    # given from problem
    A = (1/2) * np.array([[1, 1], [1 + (10**(-10)), 1- (10**(-10))]])
    norm_A = np.linalg.norm(A,2) # compute ||A||

    # the inverse of A
    A_inv = (1/2) * np.array([[1 - (10**10), 10**10], [1 + (10**10), -10**10]]) 
    norm_A_inv = np.linalg.norm(A_inv, 2) # compute ||A^-1||

    k = norm_A_inv * norm_A # k = ||A^-1|| ||A||

    print(f"The condition number of A is: {k}")

driver()