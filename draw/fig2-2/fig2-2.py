import numpy as np
import matplotlib.pyplot as plt

plt.xlim((-2,2))
plt.ylim((-2,2))

plt.xlabel('x1')
plt.ylabel('x2')

plt.grid()

axis = np.arange(-2,3,1)
plt.plot(axis, [0]*axis.size, color='black')
plt.plot([0]*axis.size, axis, color='black')

x1 = np.array([0,1])
x2 = np.array([1,0])
plt.scatter(x1,x2, color='green')
plt.scatter([0,1],[0,1], color='red')

x = np.arange(-3,3,1)
y = -x+1.4
plt.plot(x,y)
plt.show()
