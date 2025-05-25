import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

fig = plt.figure()
myAxis = fig.add_subplot(111, projection='3d')

# Vectores unitarios para los ejes
a_x_p = np.array([1, 0, 0])
a_x_m = np.array([-1, 0, 0])
a_y_p = np.array([0, 1, 0])
a_y_m = np.array([0, -1, 0])
a_z_p = np.array([0, 0, 1])
a_z_m = np.array([0, 0, -1])

# Dibujar los vectores unitarios
myAxis.quiver(0, 0, 0, a_x_p[0], a_x_p[1], a_x_p[2], color='r', arrow_length_ratio=0.1)
myAxis.quiver(0, 0, 0, a_x_m[0], a_x_m[1], a_x_m[2], color='r', arrow_length_ratio=0.1)
myAxis.quiver(0, 0, 0, a_y_p[0], a_y_p[1], a_y_p[2], color='g', arrow_length_ratio=0.1)
myAxis.quiver(0, 0, 0, a_y_m[0], a_y_m[1], a_y_m[2], color='g', arrow_length_ratio=0.1)
myAxis.quiver(0, 0, 0, a_z_p[0], a_z_p[1], a_z_p[2], color='b', arrow_length_ratio=0.1)
myAxis.quiver(0, 0, 0, a_z_m[0], a_z_m[1], a_z_m[2], color='b', arrow_length_ratio=0.1)

myAxis.set_xlim([-20, 20])
myAxis.set_ylim([-20, 20])
myAxis.set_zlim([-20, 20])

np.set_printoptions(formatter={'float': '{: 0.10f}'.format})

# Curva paramétrica
t = np.linspace(-12.0, 12.0, num=101)  # Ajuste de intervalo
xc = np.sin(t)**2
yc = np.cos(t)**2
zc = np.tan(t)**2

myAxis.scatter(xc, yc, zc, c='hotpink', s=10)
param_curve, = myAxis.plot(xc, yc, zc, color='red', linestyle='-', label='Curva paramétrica')

# Punto conocido en t = pi/4
t0 = np.pi/4
x0 = np.sin(t0)**2  # 0.5
y0 = np.cos(t0)**2  # 0.5
z0 = np.tan(t0)**2  # 1

myAxis.scatter(x0, y0, z0, c='blue', s=15)

# Derivada r'(t) y vector tangente en t = pi/4
r_prime_t0 = np.array([1, -1, 4])  # Derivada en t = pi/4
magnitude_r_prime_t0 = np.sqrt(1**2 + (-1)**2 + 4**2)
unit_tangent = r_prime_t0 / magnitude_r_prime_t0

# Ecuación de la línea tangente: r(t) + t * T(t)
t_line_values = np.linspace(-20.0, 20.0, num=101)  # Ajustado para estar cerca de t = pi/4
x_line = x0 + t_line_values * unit_tangent[0]
y_line = y0 + t_line_values * unit_tangent[1]
z_line = z0 + t_line_values * unit_tangent[2]

# Dibujar línea tangente
tangent_line, = myAxis.plot(x_line, y_line, z_line, color='green', linestyle='-', label='Línea tangente')

# Tabulación
headers = ["t", "x", "y", "z"]
table = zip(t, xc, yc, zc)
print(tabulate(table, headers, floatfmt=".3f", tablefmt="fancy_grid"))

# Leyendas y etiquetas
myAxis.legend(handles=[param_curve, tangent_line], loc='upper right', shadow=True)

p0_label = f"({x0},{y0},{z0})"
myAxis.text(x0, y0, z0, p0_label)

plt.show()
