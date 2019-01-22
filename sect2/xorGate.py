import andGate
import nandGate
import orGate

def XOR(x1,x2):
    t1 = nandGate.NAND(x1,x2)
    t2 = orGate.OR(x1,x2)
    t3 = andGate.AND(t1,t2)
    return t3
    
if __name__=='__main__':  
    print("0 xor 0", XOR(0,0))
    print("0 xor 1", XOR(0,1))
    print("1 xor 0", XOR(1,0))
    print("1 xor 1", XOR(1,1))
