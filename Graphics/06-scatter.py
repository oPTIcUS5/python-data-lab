"""
scattert graphic
"""

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([x for x in range(1, 12 + 1)])
ypoints = np.array([y for y in range(2, 26, 2)])


plt.scatter(xpoints, ypoints, color="#FF5900")
plt.title("Dots")
plt.show()

colors = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])

plt.scatter(xpoints, ypoints, c=colors, cmap='viridis')
plt.title("Dots")
plt.show()


plt.scatter(xpoints, ypoints, alpha=0.5)
plt.title("Dots")
plt.show()
