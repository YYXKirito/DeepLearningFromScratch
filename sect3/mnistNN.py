import sys,os,pickle
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from sigmoid import sigmoid
from softmax import softmax

def loadData():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize = True, flatten = True, one_hot_label = False)
    return x_test, t_test

def loadNN():
    with open("sample_weight.pkl", 'rb') as f:
        NN = pickle.load(f)
    return NN
    
def predict(NN, x):
    W1, W2, W3 = NN['W1'], NN['W2'], NN['W3']
    b1, b2, b3 = NN['b1'], NN['b2'], NN['b3']
    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    y = softmax(a3)
    
    return y
    
if __name__=='__main__':
    x, t = loadData()
    NN = loadNN()
    acc = 0
    for i in range(len(x)):
        y = predict(NN, x[i])
        p = np.argmax(y)
        if p==t[i]:
            acc += 1
    
    print("Accuracy:"+str(float(acc)/len(x)))
