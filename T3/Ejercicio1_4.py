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
t = np.linspace(-1.0, 1.0, num=101)  # Límite de t para visualizar mejor la curva en el gráfico
xc = np.exp(2 * t)  # x(t) = e^(2t)
yc = np.exp(t)      # y(t) = e^(t)

# Graficar la curva
myAxis.scatter(xc, yc, c='hotpink', s=10)
param_curve, = myAxis.plot(xc, yc, color='red', linestyle='-', label='Curva paramétrica')

# Punto y tangente en t = 0
t0 = 0
x0 = np.exp(2 * t0)  # x(0) = e^(2*0)
y0 = np.exp(t0)      # y(0) = e^(0)
myAxis.scatter(x0, y0, c='blue', s=15)

# Extender la línea tangente en ambas direcciones
dx_dt = 2 * np.exp(2 * t0)  # Derivada de x respecto a t
dy_dt = np.exp(t0)          # Derivada de y respecto a t
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
myAxis.legend(handles=[param_curve, tangent_line], loc='upper left', shadow=True)
p0_label = f"({x0:.2f},{y0:.2f})"
myAxis.text(x0, y0, p0_label)

plt.show()
