def AND(x1,x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    t = 0 if (x1*w1 + x2*w2<=theta) else 1
    return t
    
if __name__=='__main__':    
    print("0 and 0  = ", AND(0,0))
    print("0 and 1  = ", AND(0,1))
    print("1 and 0  = ", AND(1,0))
    print("1 and 1  = ", AND(1,1))
