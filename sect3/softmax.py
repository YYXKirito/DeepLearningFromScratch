import numpy as np

def softmax(a):
    c = np.max(a)
    expA = np.exp(a-c)
    return expA / np.sum(expA)
    
if __name__=='__main__':
    a = np.array([1010,1000,990])
    print(softmax(a))
