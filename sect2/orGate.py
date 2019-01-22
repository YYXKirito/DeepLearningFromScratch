def OR(x1,x2):
    w1, w2, theta = 0.5, 0.5, 0.3
    t = 0 if (w1*x1+w2*x2<=theta) else 1
    return t
    
print("0 or 0  = ", OR(0,0))
print("0 or 1  = ", OR(0,1))
print("1 or 0  = ", OR(1,0))
print("1 or 1  = ", OR(1,1))
