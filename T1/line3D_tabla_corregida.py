import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

a_x_p = np.array([1, 0, 0])
a_x_m = np.array([-1, 0, 0])
a_y_p = np.array([0, 1, 0])
a_y_m = np.array([0, -1, 0])
a_z_p = np.array([0, 0, 1])
a_z_m = np.array([0, 0, -1])

ax.quiver(0, 0, 0, a_x_p[0], a_x_p[1], a_x_p[2], color='r', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, a_x_m[0], a_x_m[1], a_x_m[2], color='r', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, a_y_p[0], a_y_p[1], a_y_p[2], color='g', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, a_y_m[0], a_y_m[1], a_y_m[2], color='g', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, a_z_p[0], a_z_p[1], a_z_p[2], color='b', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, a_z_m[0], a_z_m[1], a_z_m[2], color='b', arrow_length_ratio=0.1)

ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

ax.set_xlabel('X') # para colocar etiqueta a los ejes
ax.set_ylabel('Y')
ax.set_zlabel('Z') # para colocar etiqueta a los ejes

plt.title('3D Line Plot') # para colocar título a la gráfica

print("\nDrawing a line\n")

P0 = [5, 1, 3]
r0 = np.array(P0)

v = [1, 0, 0]
v_direction = np.array(v)

t = np.linspace(-2.0, 2.0, num=41)

print("\nLos valores de t son:\n", t)

print("\nEl punto conocido P0 es:\n", P0)

print("\nEl vector de direccion es:\n", v_direction)

# Parametric equations of the line (corrected)
x = P0[0] + v_direction[0] * t
y = P0[1] + v_direction[1] * t
z = P0[2] + v_direction[2] * t

# Plotting the line
for i in range(0, x.size):
    ax.scatter(x[i], y[i], z[i], color='blue')
    if i > 0:
        ax.plot([x[i-1], x[i]], [y[i-1], y[i]], [z[i-1], z[i]], color='blue')
        ax.quiver(0, 0, 0, x[i], y[i], z[i], color='red', arrow_length_ratio=0.1)



headers = ["t", "x", "y", "z"]
table = zip(t, x, y, z)
print("Table \n")

my_table = tabulate(table, headers, floatfmt=".3f", tablefmt="fancy_grid")

print(my_table)

plt.show()