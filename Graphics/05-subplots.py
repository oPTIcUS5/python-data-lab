"""
subplots
"""

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 5, 8, 10, 11, 13]

z = [3, 6, 9, 12, 15, 18]
w = [1, 3, 5, 7, 9, 11]

x_points = np.array(x)
y_points = np.array(y)
z_points = np.array(z)
w_points = np.array(w)

# first plot
# subplot 1
plt.title("Graphic 1")
plt.subplot(1, 2, 1) # 1 row, 2 columns, graphic 1
plt.plot(x_points, y_points, c='b')

# subplot 2
plt.subplot(1, 2, 2) # 1 row, 2 columns, graphic 2
plt.plot(z_points, w_points, c='r')

plt.show()

# second plot
# sub plot 1
plt.subplot(2, 1, 1) # 1 row, 2 columns, graphic 1
plt.plot(x_points, y_points, c='b')
plt.title("First", loc='right') # sub title, graphic 1

# subplot 2
plt.subplot(2, 1, 2) # 1 row, 2 columns, graphic 2
plt.plot(z_points, w_points, c='r')
plt.title("Second", loc='center') # subtitle, graphic 2

plt.suptitle("Graphic 2")
plt.show()
