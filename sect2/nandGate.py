def NAND(x1,x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    t = 0 if (w1*x1 + w2*x2<= theta) else 1
    return t
    
print("0 nand 0  = ", NAND(0,0))
print("0 nand 1  = ", NAND(0,1))
print("1 nand 0  = ", NAND(1,0))
print("1 nand 1  = ", NAND(1,1))
