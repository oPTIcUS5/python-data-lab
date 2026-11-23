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
# 'o' point
# '*' star
# '.' point
# 'X' x filled
# '1' tri up
plt.show()

# dots
plt.scatter(x_points, y_points, marker='o')
plt.show()
