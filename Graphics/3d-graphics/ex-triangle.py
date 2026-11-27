"""
triangle
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(0, 0, 0, c='r')
ax.scatter(5, 0, 0, c='r')
ax.scatter(2, 4, 5, c='r')

x_points = np.array([0, 5, 2, 0])
y_points = np.array([0, 0, 4, 0])
z_points = np.array([0, 0, 5, 0])

ax.plot(x_points, y_points, z_points, c='blue')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D triangle')
plt.show()
