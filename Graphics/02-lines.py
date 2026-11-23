"""
lines and styles
"""

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 5, 8, 10, 11, 13]

z = [3, 6, 9, 12, 15, 18]
w = [1, 3, 5, 7, 9, 11]

x_points = np.array(x)
y_points = np.array(y)

z_points = np.array(z) # x'
w_points = np.array(w) # y'

# two lines in one plot
plt.xlabel("Two plots")
plt.plot(x_points, c='b')
plt.plot(y_points, c='r')
plt.show()

plt.title("Two lines in one plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x_points, y_points, z_points, w_points)
plt.show()

