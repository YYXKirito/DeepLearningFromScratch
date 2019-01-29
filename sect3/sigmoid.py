import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

if __name__=='__main__':
    plt.xlim((-6,6))
    plt.ylim((-0.1,1.1))
    
    plt.xlabel('x')
    plt.ylabel('h_sigmoid')
    
    x = np.arange(-6,6,0.01)
    y = sigmoid(x)
    
    plt.plot(x,y)
    plt.show()
