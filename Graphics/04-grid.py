"""
labels
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

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Graphic", fontdict=font1, loc='left')
plt.xlabel("X axis", fontdict=font2)
plt.ylabel("Y axis", fontdict=font2)
plt.plot(x_points, y_points, marker='o')
plt.grid(axis='x')
plt.show()

plt.title("Graphic", fontdict=font1, loc='left')
plt.xlabel("X axis", fontdict=font2)
plt.ylabel("Y axis", fontdict=font2)
plt.plot(x_points, y_points, marker='o')
plt.grid(axis='both', color='r', ls='dotted', lw=1)
plt.show()