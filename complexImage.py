from PIL import Image
import numpy as np
import random

def complexImage(A, solutions, tol, fname=None, show=False):
    """
    Function to create a image from the generated A with the corresponding solutions. 
    It assigns colors pseudo randomly (so my favorite colors is the favorite colors of the universe :) )
    It is rather slow, but it gets the job done. 
    
    A: matrix from eval_newton()
    solutions: array of solutions for f
    tol: tolerance for similarity between Aij and solution.
    
    """
    
    #creating a n*n*3 array. Here the 3 corresponds to the RGB of the (i, j)-th element in the data array
    data = np.zeros((len(A), len(A), 3), dtype = np.uint8)
    
    """
    Creating somewhat visually distinct colors. I do it this way
    so that i can re-use this function with the z^5 problem. Here i will
    need more than three colors. Sometimes the colors are not 100% distinct. But in my opinion it works great.
    """
    
    colors = {} #dictionary that holds the solutions with its corresponding random RGB values
    
    r = int(random.random() * 256)
    g = int(random.random() * 256)
    b = int(random.random() * 256)
    
    step = 256 / len(solutions)
    
    for i in range(len(solutions)): #generates a color for each solution.
        r += step
        g += step
        b += step
        
        colors[solutions[i]] = [r, g, b]
    
    
    #looping through A_ij and checking if it is similar to one of the solutions and assigning the corresponding color
    for i in range(len(A)): #O(n^3) not very good.. 
        for j in range(len(A)):
            
            Aij = A[i, j] #complex value
            
            for sol in solutions:
                if(np.absolute(Aij - sol) < tol): #taking the length of the complex diference
                    data[i, j] = colors[sol] #assigning the ij-th pixel the RGB value corresponding to the solution it converges towards.
                    

    img = Image.fromarray(data) #creating the image
    #if(show):  display(img) #displaying the image
    if(fname): img.save(fname)