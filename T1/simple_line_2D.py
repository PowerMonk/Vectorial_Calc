
import matplotlib.pyplot as plt #imports a module to work with figures and axes
import numpy as np # imports the numeric python module that allows us to perform many mathematical operations efficiently
from matplotlib.ticker import MultipleLocator # imports a utility to be able to set grids on the axis

from tabulate import tabulate

fig = plt.figure() #creates a new figure

myAxis = fig.add_subplot(111) #adds an Axes to the current figure 

myAxis.set_xlim(-5,10) # sets limits for the x-axis
myAxis.set_ylim(-5,15) # sets limits for the y-axis


myAxis.minorticks_on() # displays a minor grid

myAxis.grid(True,which='major', color='grey', linestyle='-') # sets the color and style of the major grid
myAxis.grid(True,which='minor',color='grey', linestyle='--') # sets the color and style of the minor grid 

myAxis.xaxis.set_major_locator(MultipleLocator(1)) #sets the horizontal spacing of the major grid
myAxis.yaxis.set_major_locator(MultipleLocator(1)) #sets the vertical spacing of the major grid

myAxis.xaxis.set_minor_locator(MultipleLocator(0.5)) #sets the horizontal spacing of the minor grid
myAxis.yaxis.set_minor_locator(MultipleLocator(0.5)) #sets the vertical spacing of the minor grid


print("\nProgram to draw a line\n")




"""
v = [1, 2]

v_direction = np.array(v)

t = np.linspace(-2, 5, num=71)

print("\nLos valores de t son:\n", t)

print("\nEl punto conocido P0 es:\n", P0)

print("\nEl vector de direccion es:\n", v_direction)


x = 3 + t
y = 4 + 2*t

print("\nTodas las coordenadas x de los puntos son:\n", x)
print("\nTodas las coordenadas y de los puntos son:\n", y)



for i in range(0, x.size):# ciclo for que itera desde la posicion cero del arreglo de las x asta la ultima posicion especificada por el tamaño del arreglo
    myAxis.arrow(0, 0, x[i], y[i], head_width=0.05, color='blue', head_length=0.09) # se muestra una flecha que apunta a cada par ordenado obtenido desde los arreglos x and y
    
    myAxis.scatter(x[i], y[i]) #se dibuja un punto por cada par ordenado obtenido desde los arreglos x and y


headers = ["t","x", "y"] # encabezado de la tabla
table = zip(t, x, y)     # orienta los arreglos en forma de tabla

my_table = tabulate(table , headers, floatfmt=".3f", tablefmt="fancy_grid") #crea la tabla

print(my_table) #muestra la tabla
"""

plt.show() # shows all the operations performed on the axis



