"""
3d space
"""

import matplotlib.pyplot as plt
import numpy as np

x_points = [x for x in range(-9, 10)]
y_points = [y for y in range(-9, 10)]
z_points = [z for z in range(-9, 10)]

x_points = np.array(x_points)
y_points = np.array(y_points)
z_points = np.array(z_points)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

# point (1, 2, 3)
ax.scatter(1, 2, 3, c='orange')
ax.scatter(3, 1, 4, c='pink')

# many points
ax.scatter(x_points, y_points, z_points, c='green')

# a line between those points
ax.plot(x_points, y_points, z_points, c='r', lw=1)

# a vector
ax.quiver(0, 0, 0, 3, 1, 6)

ax.set_xlabel("X")
ax.set_ylabel('Y')
ax.set_zlabel("Z")

ax.set_title("3D graphic")
plt.show()
