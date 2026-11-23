"""
Bars
"""

import numpy as np
import matplotlib.pyplot as plt

y = np.array([x for x in range(1, 6+1)])
x = np.array(['A', 'B', 'C', 'D', 'E', 'F'])

plt.bar(x, y, color='r', width=0.5)
plt.show()


# horizontal
plt.barh(x, y, height=0.5)
plt.show()


