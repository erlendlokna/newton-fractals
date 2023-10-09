# newton-fractals
Using newton iteration to find a solution to a complex equating f(z) with known soultions. In order to create the image i first setup a 2D grid corresponding the 1D exptension of the real line.
For each grid value i use this value as the starting point in a the newton scheme. Then i color a pixel in the image based on what solution it converged to.

For example, for the equation, $z^3 - 1 = 0$,, there are three solutions, which I assign three distinct colors. We see that different coordinate points converge to different solutions and we get the fractal shape.

![](https://github.com/erlendlokna/newton-fractals/blob/main/figs/test_highquality-1.png)
