import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from tabulate import tabulate

fig = plt.figure()

# Configuración del eje
myAxis = fig.add_subplot(1,1,1)
myAxis.set_xlim(-10, 10)
myAxis.set_ylim(-10, 10)

myAxis.set_title("2D-Plane")
myAxis.set_xlabel("x-axis") 
myAxis.set_ylabel("y-axis")

myAxis.minorticks_on()
myAxis.grid(True, which='major', color='grey', linestyle='-')
myAxis.grid(True, which='minor', color='grey', linestyle='--')

myAxis.xaxis.set_major_locator(MultipleLocator(1))
myAxis.yaxis.set_major_locator(MultipleLocator(1))

myAxis.xaxis.set_minor_locator(MultipleLocator(0.5))
myAxis.yaxis.set_minor_locator(MultipleLocator(0.5))

np.set_printoptions(formatter={'float': '{: 0.10f}'.format})

# Curva paramétrica
t = np.linspace(-10.0, 10.0, num=101)
xc = t - 2  # x(t)
yc = np.power(t, 2) + 1  # y(t)

# Graficar la curva
myAxis.scatter(xc, yc, c='hotpink', s=10)
param_curve, = myAxis.plot(xc, yc, color='red', linestyle='-', label='Curva paramétrica')

# Punto y tangente en t = 1
t0 = 1
x0 = t0 - 2  # x(1)
y0 = t0**2 + 1  # y(1)
myAxis.scatter(x0, y0, c='blue', s=15)

# Extender la línea tangente en ambas direcciones
dx_dt = 1  # Derivada de x respecto a t
dy_dt = 2 * t0  # Derivada de y respecto a t en t = 1
tangent_length = 5  # Factor para extender la tangente en ambas direcciones

# Cálculo de los puntos para la tangente extendida
tangent_x_values = [x0 - tangent_length * dx_dt, x0 + tangent_length * dx_dt]
tangent_y_values = [y0 - tangent_length * dy_dt, y0 + tangent_length * dy_dt]

# Graficar la línea tangente extendida
tangent_line, = myAxis.plot(tangent_x_values, tangent_y_values, color='green', linestyle='-', label="Línea tangente extendida")
# Tabulación
headers = ["t", "x", "y"]
table = zip(t, xc, yc)
print(tabulate(table, headers, floatfmt=".3f", tablefmt="fancy_grid"))

# Leyendas y etiquetas
myAxis.legend(handles=[param_curve, tangent_line], loc='upper right', shadow=True)
p0_label = f"({x0},{y0})"
myAxis.text(x0, y0, p0_label)

plt.show()
