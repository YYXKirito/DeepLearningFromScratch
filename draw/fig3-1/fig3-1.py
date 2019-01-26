import numpy as np
import matplotlib.pyplot as plt

def stepFunction(x):
    y = x>0
    return y.astype(np.int)

if __name__=='__main__':
    plt.xlim((-2,2))
    plt.ylim((-2,2))

    plt.xlabel('x')
    plt.ylabel('y')

    x = np.arange(-2,2,0.001)
    y = stepFunction(x)
    
    plt.plot(x,y)
    plt.show()
