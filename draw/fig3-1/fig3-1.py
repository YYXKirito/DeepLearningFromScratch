import numpy as np
import matplotlib.pyplot as plt

def stepFunction(x):
    y = x>0
    return y.astype(np.int)

if __name__=='__main__':
    plt.xlim((-1.3,1.3))
    plt.ylim((-1.3,1.3))

    plt.xlabel('x')
    plt.ylabel('h_perceptron')

    x = np.arange(-2,2,0.0001)
    y = stepFunction(x)
    
    plt.plot(x,y)
    plt.show()
