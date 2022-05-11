import time
import numpy as np

def my_newton(f, Df, x0, **kwargs):
    """
    Function that does the newton iteration. If tolerance and maxiter not specified, it will provide
    a reasonable alternative.
    
    f: function
    Df: derivative of f
    x0: initial guess
    ***kwargs: contains the the tolerance and maxiter if specified.
    """

    t0 = time.time() #algorithm starting time
    
    e = 1 #error starting value, doesnt really matter what it is
    tol = 1e-12 #tolerance in case not specified
    maxiter = None #maxiter if not specified
    it = 0 #number of iterations
    x_n = x0 #assigning starting guess
    
    #assigning possible specified maxiter or tol.
    if 'maxiter' in kwargs:
        maxiter = kwargs['maxiter']
    
    if 'tol' in kwargs:
        tol = kwargs['tol']
    
    while(e > tol and (maxiter == None or it < maxiter)): #iterating using newtons method
        x_np1 = x_n - f(x_n) / Df(x_n)
        
        e = abs(x_np1 - x_n)
        x_n = x_np1
        it += 1

    t1 = time.time() #algo. ending time
    return (x_n, it, e,  t1 - t0) #returning sollution, number of iterations
                              # and the runtime of the algorithm
    
        
def printInfo(S): #a function for use in tests
    print("solution: ", S[0], '\n', "iterations: ", S[1], '\n', "runtime: ", S[3], '\n', "error: ", S[2] , '\n')


def eval_newton(f, Df, n, **kwargs):
    """
    Function that generates a n by n matrix containing complex solutions from the my_newton function.
    
    f: function
    Df: the derivative
    n: integer for size of square matrix.
    
    """
    #creating arrays containing the real x's and y's. z = x + iy
    Re = np.linspace(-1, 1, n)
    Im = np.linspace(1, -1, n)
    
    #n by n matrix. Will contain the complex solutions from my_newton iteration
    A = np.zeros((n, n), dtype = 'complex') #containing only zero elements at the moment.
    
    for i, y in enumerate(Im): #looping through each value in Im and Re
        for j, x in enumerate(Re):
            z = x + y*1j 
            A[i, j] = my_newton(f, Df, z, **kwargs)[0] #running newton iteration on z. [0] because my_newton returns
            # the solution as the 0-th element.
    
    return A #returning array.