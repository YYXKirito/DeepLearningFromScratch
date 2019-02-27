from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.arange(-10,10,1)
y = np.arange(-10,10,1)
X, Y = np.meshgrid(x, y)
Z = 1/20*X*X+Y*Y


ax.plot_surface(X,Y,Z)
plt.show()
