import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt('points_circle.dat')
vector = np.array([2.1, 1.1])
shifted_points = points + vector

x = points[:,0]
y = points[:,1]

xn = shifted_points[:,0]
yn = shifted_points[:,1]

plt.plot(x, y, 'o')
plt.plot(xn, yn, 'o')
# plt.annotate("", xy=points[0,:] + vector, xytext=points[0,:], arrowprops={"arrowstyle": "-|>"})
plt.show()