import numpy as np
import matplotlib.pyplot as plt

def finite_diff(f, x, delX):
    return (f(x+delX) - f(x-delX)) / (2*delX)
    
# Exclude the end points, so use [2:] and [:-2]
# Without excluding the endpoints, can do:
# [1:]  = x+delX
# [:-1] = x-delX
def finite_diff2(y, x, delX):
    return (y[2:] - y[:-2]) / (2*delX)
    
if __name__ == '__main__':
    start = 0
    stop = 2 * np.pi
    delX = 0.01
    
    x = np.arange(start, stop, delX)
    
    # Calculates f twice
    y = finite_diff(np.sin, x, delX)
    
    # Calculates f once
    y = finite_diff2(np.sin(x), x, delX)
    
    cosX = np.cos(x[1:-1])
    
    # Results
    plt.plot(x[1:-1], y, x[1:-1], cosX)
    plt.show()
    
    # Abs error
    plt.plot(x[1:-1], y-cosX)
    plt.show()