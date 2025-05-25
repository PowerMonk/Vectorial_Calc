import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from tabulate import tabulate
from mpl_toolkits.axisartist.axislines import AxesZero 

# Función para configurar los ejes del gráfico
def set_axis_function():
    fig = plt.figure()      # Crea una nueva figura
    fig.set_figwidth(6)     # Define el ancho de la figura en pulgadas
    fig.set_figheight(6)    # Define la altura de la figura en pulgadas

    # Crea los ejes coordinados con un estilo especial (AxisZero añade los ejes X e Y en el centro)
    myAxis = fig.add_subplot(axes_class=AxesZero)    

    # Establece flechas en los extremos de los ejes X e Y
    myAxis.axis["xzero"].set_axisline_style("-|>")   
    myAxis.axis["yzero"].set_axisline_style("-|>")   

    # Hace visibles los ejes X e Y desde el origen (0,0)
    myAxis.axis["xzero"].set_visible(True)  
    myAxis.axis["yzero"].set_visible(True)  

    # Establece el rango de valores de los ejes
    myAxis.set_xlim(-5, 25)  # Rango del eje X
    myAxis.set_ylim(-10, 50)  # Rango del eje Y

    # Título del gráfico
    myAxis.set_title("Curva Paramétrica")    

    # Activa la visualización de la cuadrícula menor
    myAxis.minorticks_on()  
    # Establece la cuadrícula mayor (color gris, líneas continuas)
    myAxis.grid(True, which='major', color='grey', linestyle='-') 
    # Establece la cuadrícula menor (color gris, líneas discontinuas)
    myAxis.grid(True, which='minor', color='grey', linestyle='--')  

    # Establece la separación de la cuadrícula mayor y menor en los ejes X e Y
    myAxis.xaxis.set_major_locator(MultipleLocator(1))    
    myAxis.yaxis.set_major_locator(MultipleLocator(5))    
    myAxis.xaxis.set_minor_locator(MultipleLocator(0.5))  
    myAxis.yaxis.set_minor_locator(MultipleLocator(2.5))  

    return myAxis


# Función principal que grafica la curva paramétrica
def main_function():
    print("Graficando la curva paramétrica...")
    
    # Establece la configuración de los ejes
    axis = set_axis_function()

    # Crea un rango de valores para 't' (variable paramétrica)
    t = np.linspace(0, 8, num=100)  # Rango de t de 0 a 8 con 100 puntos

    # Define las ecuaciones paramétricas x(t) y y(t)
    xc = 8 * np.power(t, 1.5)  # x(t) = 8t^(3/2)
    yc = 3 + np.power(8 - t, 1.5)    # y(t) = 3 + (8 - t)^(3/2)

    # Grafica los puntos en la curva (en rojo) y la línea de la curva (en azul)
    axis.scatter(xc, yc, color="red", s=5, label='puntos')  # Puntos rojos en la curva
    axis.plot(xc, yc, color='blue', label='curva')  # Línea azul que conecta los puntos

    # Imprime una tabla con los valores de x, y y t
    headers = ["x(t)", "y(t)", "t"]  # Encabezados de la tabla
    table = zip(xc, yc, t)  # Combina los valores de x, y, t en una tabla
    print(tabulate(table , headers, floatfmt=".3f", tablefmt="fancy_grid"))  # Muestra la tabla formateada

    plt.legend()  # Añade una leyenda al gráfico
    plt.show()    # Muestra el gráfico con todos los elementos

    
# Llamada a la función principal cuando se ejecuta el archivo
if __name__ == "__main__":
    main_function()

print("Fin del programa...")
