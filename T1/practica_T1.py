import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


P0 = [2, 1, 0]  # Punto inicial 
v1 = [1, 1, 0]  # Vector  1
v2 = [0, 1, 1]  # Vector 2

t = np.linspace(-2.0, 2.0, num=41)

# VECTOR 1
x1 = P0[0] + v1[0] * t
y1 = P0[1] + v1[1] * t
z1 = P0[2] + v1[2] * t

# VECTOR 2
x2 = P0[0] + v2[0] * t
y2 = P0[1] + v2[1] * t
z2 = P0[2] + v2[2] * t

print("Ecuaciones paramétricas y simétricas para las líneas:\n")

print("Línea 1 (v1 = <1, 1, 0>):")
print("x1 = 2 + t")
print("y1 = 1 + t")
print("z1 = 0\n")

print("Ecuaciones simétricas para la línea 1:")
print("(x - 2)/1 = (y - 1)/1\n")

print("Línea 2 (v2 = <0, 1, 1>):")
print("x2 = 2")
print("y2 = 1 + t")
print("z2 = t\n")

print("Ecuaciones simétricas para la línea 2:")
print("y - 1 = z\n")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# GRAFICAR LOS PUNTOS DE LAS LINEAS CON SCATTER
ax.scatter(x1, y1, z1, color='blue', label='Línea 1: v1 = <1, 1, 0>')
ax.plot(x1, y1, z1, color='blue')
# USAMOS QUIVER PARA GRAFICAR LOS VECTORES DESDE EL ORIGEN
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='red', arrow_length_ratio=0.1)

ax.scatter(x2, y2, z2, color='green', label='Línea 2: v2 = <0, 1, 1>')
ax.plot(x2, y2, z2, color='green')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='red', arrow_length_ratio=0.1)

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Gráfica de las líneas paramétricas')
# PARA MOSTRAR LA LEYENDA DE LA GRAFICA
plt.legend()

# TABLA DE VALORES
headers = ["t", "x1", "y1", "z1", "x2", "y2", "z2"]
table = zip(t, x1, y1, z1, x2, y2, z2)
my_table = tabulate(table, headers, floatfmt=".3f", tablefmt="fancy_grid")

print("\nTabla de valores:\n")
print(my_table)

plt.show()
