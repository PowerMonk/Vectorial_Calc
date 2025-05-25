import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from tabulate import tabulate
from mpl_toolkits.axisartist.axislines import AxesZero 

def set_axis_function():
    fig = plt.figure()  # Crea una nueva figura
    fig.set_figwidth(10)
    fig.set_figheight(10)

    # Crea ejes coordenados personalizados
    myAxis = fig.add_subplot(axes_class=AxesZero)
    myAxis.axis["xzero"].set_axisline_style("-|>")  # Flechas en el eje X
    myAxis.axis["yzero"].set_axisline_style("-|>")  # Flechas en el eje Y

    myAxis.axis["xzero"].set_visible(True)
    myAxis.axis["yzero"].set_visible(True)

    myAxis.set_xlim(-1.5, 1.5)  # Rango del eje X
    myAxis.set_ylim(-0.5, 2)    # Rango del eje Y
    myAxis.set_title("Parametric Curve")  # Título

    # Configuración de la cuadrícula
    myAxis.minorticks_on()
    myAxis.grid(True, which='major', color='grey', linestyle='-')
    myAxis.grid(True, which='minor', color='grey', linestyle='--')

    # Espaciado de la cuadrícula
    myAxis.xaxis.set_major_locator(MultipleLocator(0.5))
    myAxis.yaxis.set_major_locator(MultipleLocator(0.5))
    myAxis.xaxis.set_minor_locator(MultipleLocator(0.1))
    myAxis.yaxis.set_minor_locator(MultipleLocator(0.1))

    return myAxis

def main_function():
    print("Plotting the parametric curve...")
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
  
    axis = set_axis_function()

    # Rango de t
    t = np.linspace(0, np.pi / 2, num=101)

    # Ecuaciones paramétricas corregidas
    xc = np.cos(t) ** 2  # x = cos^2(t)
    yc = 1 - np.sin(t)   # y = 1 - sin(t)

    # Graficar puntos y curva
    axis.scatter(xc, yc, color="red", s=5, label='point')
    axis.plot(xc, yc, color='blue', label='curve')

    # Mostrar los valores en tabla
    headers = ["x", "y", "t"]
    table = zip(xc, yc, t)
    print(tabulate(table, headers, floatfmt=".3f", tablefmt="fancy_grid"))

    plt.legend()
    plt.show()  # Muestra la gráfica

if __name__ == "__main__":
    main_function()

print("End of this file....")
