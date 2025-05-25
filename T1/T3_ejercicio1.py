import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 1. Valores del parámetro t
t = np.linspace(-10.0*np.pi, 10.0*np.pi, num=200)

# 2. Definir la función paramétrica <sin(t), cos(t), t>
x = np.sin(t)
y = np.cos(t)
z = t

# 3. Graficar la línea (solo puntos)
for i in range(0, x.size):
    ax.scatter(x[i], y[i], z[i], color='blue')  # Puntos individuales
    if i > 0:
        # Conectar los puntos para formar la línea
        ax.plot([x[i-1], x[i]], [y[i-1], y[i]], [z[i-1], z[i]], color='blue')

# 4. (Opcional) Graficar vectores desde el origen hacia cada punto
# PARA PUNTOS ESPECIFICOS EN LA GRAFICA
# indices = [0, 10, 20, 30, 40]  # Solo algunos puntos
# for i in indices:
#     ax.quiver(0, 0, 0, x[i], y[i], z[i], color='red', arrow_length_ratio=0.1)

# Comenta esta sección si no quieres los vectores
for i in range(0, x.size, 1):  # Menos puntos para que no se sature la gráfica
    ax.quiver(0, 0, 0, x[i], y[i], z[i], color='red', arrow_length_ratio=0.01)

# 5. Configuración de los ejes y título
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-30, 30])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Gráfica de <sin(t), cos(t), t>')

# 6. Crear la tabla con los valores paramétricos
headers = ["t", "x", "y", "z"]
table = zip(t, x, y, z)
print("\nTable\n")
my_table = tabulate(table, headers, floatfmt=".3f", tablefmt="fancy_grid")
print(my_table)

# 7. Mostrar la gráfica
plt.show()
