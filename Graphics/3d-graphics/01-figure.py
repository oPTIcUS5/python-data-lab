"""
3d space
"""

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

ax.set_xlabel("X")
ax.set_ylabel('Y')
ax.set_zlabel("Z")

ax.set_title("3D graphic")
plt.show()
