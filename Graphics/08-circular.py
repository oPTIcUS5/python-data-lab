"""
circular
"""

import numpy as np
import matplotlib.pyplot as plt

y = np.array([30, 20, 15, 20, 15])
y_labels = ["Appples", "Bananas", "Cherries", "Strawberries", "Blackberries"]

plt.pie(y, labels=y_labels, startangle=180)
plt.legend()
plt.show()
