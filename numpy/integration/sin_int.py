import numpy as np
import matplotlib.pyplot as plt

def riemann(f, x, a, b, delX):
    # excluding the endpoints
    # x(i) = x[1:]
    # x(i-1) = x[:-1]
    
    xPrime = (x[1:] + x[:-1] ) / 2
    
    return np.sum(f(xPrime)*delX)
    
if __name__ == '__main__':
    start = 0
    stop = np.pi / 2
    delX = 0.00001
    
    x = np.arange(start, stop, delX)
    s = riemann(np.sin, x, start, stop, delX)
    
    print(s)
    print(1-s)
    
    
    
'''

0 1 2 3 4 5 6

x[1:]
1 2 3 4 5 6

x[:-1]
0 1 2 3 4 5

i=0; skip because end point
i=1; x1 - x0
i=2; x2 - x1
...
i=6; skip because end point

'''