
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from tabulate import tabulate

fig = plt.figure()

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



#Curva paramétrica
t = np.linspace(-4.0, 6.0, num=111) #linspace  no tiene el problema de redondeo que presenta arange
xc = 1 + (4 * t) - t ** 2
yc = 2 - t ** 3

myAxis.scatter(xc, yc, c = 'hotpink', s = 10)
param_curve, = myAxis.plot(xc, yc, color='red', linestyle='-', label='Curva paramétrica')


#Punto conocido
t0 = 1  # El valor correcto de t
x0 = 1 + 4 * t0 - t0**2  # x(1)
y0 = 2 - t0**3            # y(1)
myAxis.scatter(x0, y0, c = 'blue', s = 15)


#Línea tangente
x_line_values = np.linspace(-10.0, 10.0, num=111)

m = -3 / 2
y_line_values = m * (x_line_values - x0) + y0
tangent_line, = myAxis.plot(x_line_values, y_line_values, color='green', linestyle='-', label='Línea tangente')


#Tabulación
headers = ["t","x","y"]
table = zip(t, xc, yc)

print(tabulate(table , headers, floatfmt=".3f", tablefmt="fancy_grid"))

#Leyendas y etiquetas
myAxis.legend(handles=[param_curve, tangent_line], loc='upper right', shadow=True)

p0_label = f"({x0},{y0})"
myAxis.text(x0, y0, p0_label)

plt.show()

