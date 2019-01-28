import numpy as np
import matplotlib.pyplot as plt

def ReLU(x):
    return np.maximum(0,x)
    
if __name__=='__main__':
    plt.xlim((-6,6))
    plt.ylim((-1,5))
    
    plt.xlabel('x')
    plt.ylabel('h_ReLU')
    
    x = np.arange(-5,4.5,0.01)
    y = ReLU(x)
    
    plt.plot(x,y)
    plt.show()
