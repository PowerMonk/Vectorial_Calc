
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

fig = plt.figure()


myAxis = fig.add_subplot(111, projection='3d')

a_x_p = np.array([1, 0, 0])
a_x_m = np.array([-1, 0, 0])
a_y_p = np.array([0, 1, 0])
a_y_m = np.array([0, -1, 0])
a_z_p = np.array([0, 0, 1])
a_z_m = np.array([0, 0, -1])



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



#Curva paramétrica
t = np.linspace(-10.0, 10.0, num=61) #linspace  no tiene el problema de redondeo que presenta arange
# xc = np.power(t, 3) + 3 * t
xc = np.power(t, 2) + 3 * t
yc = np.power(t, 2) + 1
zc = 3 * t + 4

myAxis.scatter(xc, yc, zc, c = 'hotpink', s = 10)
#myAxis.quiver(0, 0, 0, xc, yc, zc, color='b', arrow_length_ratio=0.05)
param_curve, = myAxis.plot(xc, yc, zc, color='red', linestyle='-', label='Curva paramétrica')


#Punto conocido
t0 = 1
# x0 = np.power(t0, 3) + 3 * t0
x0 = np.power(t0, 2) + 3 * t0
y0 = np.power(t0, 2) + 1
z0 = 3*t0 + 4


myAxis.scatter(x0, y0, z0, c = 'blue', s = 15)


#Línea tangente
t_line_values = np.linspace(-10.0, 10.0, num=61)

x_line = 4 + 6 * t_line_values
y_line = 2 + 2 * t_line_values
z_line = 7 + 3 * t_line_values

myAxis.scatter(x_line, y_line, z_line, c = 'red', s = 10)
#myAxis.quiver(0, 0, 0, x_line, y_line, z_line, color='g', arrow_length_ratio=0.05)
tangent_line, = myAxis.plot(x_line, y_line, z_line, color='green', linestyle='-', label='Línea tangente')


#Tabulación
headers = ["t","x","y", "z"]
table = zip(t, xc, yc, zc)

print(tabulate(table, headers, floatfmt=".3f", tablefmt="fancy_grid"))

#Leyendas y etiquetas
myAxis.legend(handles=[param_curve, tangent_line], loc='upper right', shadow=True)

p0_label = f"({x0},{y0}, {z0})"
myAxis.text(x0, y0, z0, p0_label)

plt.show()
