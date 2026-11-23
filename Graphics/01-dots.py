"""
Graph a plot
"""

import random
import matplotlib.pyplot as plt
import numpy as np

random_matrix = []
random_point = []

x_points = []
y_points = []

print("random numbers:")
for i in range(100):
    random_point = []

    random_point.append(random.randint(1, 100))
    random_point.append(random.randint(1, 100))

    random_matrix.append(random_point)

# sublists to tuples
# dots = list(map(lambda x: tuple(x), random_matrix))
# print(dots)

print(random_matrix)

print("x")
for i in range(len(random_matrix)):
    x_points.append(random_matrix[i][0])

x_points = np.array(x_points)
print(type(x_points))

print()

print("y")
for j in range(len(random_matrix)):
    y_points.append(random_matrix[j][1])

y_points = np.array(y_points)
print(type(y_points))

# line and dots
plt.plot(x_points, y_points, marker='o', linestyle='dotted', color='r')
plt.show()
# 'o' point
# '*' star
# '.' point
# 'X' x filled
# '1' tri up

# linestyle dashed
plt.plot(x_points, y_points, marker='o', linestyle='dashed', color='r')
plt.show()

# default x points 0, 1, 2, 3...
plt.plot(y_points, marker='o', linestyle='dashed', color='r')
plt.show()

# dots
# marker='' type of dot
plt.scatter(x_points, y_points, marker='o')
plt.show()

# marker o, linestyle dashed, color green
plt.plot(x_points, y_points, 'o--g')
plt.show()

plt.plot(x_points, y_points, '*--c', ms=15, mec='k')
plt.show()

plt.xlabel("marker=o, linestyle=dashed, markersize=15, markeredgecolor=blue, markerfacecolor=red")
plt.plot(x_points, y_points, 'o--c', ms=15, mec='b', mfc='r')
plt.show()


plt.plot(x_points, y_points, 'o--c', ms=15, mec='b', mfc='r', lw='20.5')
plt.show()
