from complexImage import *
from newton import *

def main():
    #This may take some runtime im afraid.
    
    f = lambda z: z*z*z - 1
    df = lambda z: 3*z*z

    #complex solutions to the system. The converging solutions from the newton
    #iteration will be color coded in a distinct color representing the solution it 
    #converges to
    solutions = [(1), (-1/2 + (np.sqrt(3) / 2)*1j), ((-1/2 - (np.sqrt(3) / 2)*1j))]

    M_low = eval_newton(f, df, 100) #Low quality
    M_high = eval_newton(f, df, 1024) #Low quality

    complexImage(M_low, solutions, 1e-1, fname="figs/test_lowquality.pdf")
    complexImage(M_high, solutions, 1e-1, fname="figs/test_highquality.pdf")

    #Testing with more interesting functions:    
    f2 = lambda z: z**5 - 1
    df2 = lambda z: 5*z**4

    #Testing with a lower maxiter. This will make the image more black, as we will have
    #less convergence.
    complexImage(eval_newton(f2, df2, 1024, maxiter = 5), solutions, 1e-1, fname="figs/blobs.pdf")
    complexImage(eval_newton(f2, df2, 1024, maxiter = 15), solutions, 1e-1, fname="figs/space_art.pdf")
    complexImage(eval_newton(f2, df2, 1024), solutions, 1e-1, fname="figs/fractals.pdf")

if __name__ == "__main__":
    main()

