import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from tabulate import tabulate
from mpl_toolkits.axisartist.axislines import AxesZero
import matplotlib.animation as animation

def set_axis_function():
    """Configura los ejes de coordenadas con flechas en los extremos."""
    fig = plt.figure()
    fig.set_figwidth(6)
    fig.set_figheight(6)

    myAxis = fig.add_subplot(axes_class=AxesZero)
    myAxis.axis["xzero"].set_axisline_style("-|>")
    myAxis.axis["yzero"].set_axisline_style("-|>")

    myAxis.axis["xzero"].set_visible(True)
    myAxis.axis["yzero"].set_visible(True)

    # Ajuste de los límites de los ejes
    myAxis.set_xlim(-1.5, 1.5)
    myAxis.set_ylim(-0.5, 2)

    myAxis.set_title("Parametric Curve Animation")

    # Configuración de la cuadrícula
    myAxis.minorticks_on()
    myAxis.grid(True, which='major', color='grey', linestyle='-')
    myAxis.grid(True, which='minor', color='grey', linestyle='--')

    myAxis.xaxis.set_major_locator(MultipleLocator(0.5))
    myAxis.yaxis.set_major_locator(MultipleLocator(0.5))
    myAxis.xaxis.set_minor_locator(MultipleLocator(0.1))
    myAxis.yaxis.set_minor_locator(MultipleLocator(0.1))

    return myAxis, fig

def update(frame, x, y, scat, line, frame_count, point_coordinate, annotations):
    """Actualiza la animación en cada frame."""
    a = x[:frame + 1]
    b = y[:frame + 1]
    data = np.stack([a, b]).T

    scat.set_offsets(data)  # Actualiza la posición del punto
    line.set_data(a, b)     # Dibuja la línea

    t_value = frame / 100 * (np.pi / 2)  # Calcula el valor de t correspondiente al frame
    frame_count.set_text(f'Frame: {frame}')
    point_coordinate.set_text(f'({x[frame]:.3f}, {y[frame]:.3f}) -> t = {t_value:.3f}')

    annotations.set_position((x[frame] + 0.1, y[frame] + 0.1))
    annotations.xy = (x[frame], y[frame])
    annotations.set_text(f'({x[frame]:.3f}, {y[frame]:.3f}) -> t = {t_value:.3f}')

    return scat, line, frame_count, point_coordinate, annotations

def main_function():
    """Función principal para configurar y ejecutar la animación."""
    print("Starting the parametric curve animation...")

    axis, fig = set_axis_function()
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

    # Generación del rango de t y de las funciones paramétricas
    t = np.linspace(0, np.pi / 2, num=101)
    xc = np.cos(t) ** 2  # x = cos^2(t)
    yc = 1 - np.sin(t)   # y = 1 - sin(t)

    # Configuración inicial del gráfico
    scat = axis.scatter(xc[0], yc[0], c="b", s=5, label='point')
    line = axis.plot(xc[0], yc[0], label='curve')[0]
    frame_count = axis.text(0.5, 1.8, '', bbox=dict(facecolor='yellow', alpha=0.5))
    point_coordinate = axis.text(0.5, 1.5, '', bbox=dict(facecolor='green', alpha=0.5))
    annotations = axis.annotate('', xy=(xc[0], yc[0]), xytext=(xc[0], yc[0]), 
                                bbox=dict(boxstyle="round", facecolor='pink', alpha=0.5),
                                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5', lw=1, color='red'),
                                fontsize=10, color='blue')

    plt.legend()

    # Tabla de valores x, y y t
    headers = ["x", "y", "t"]
    table = zip(xc, yc, t)
    print(tabulate(table, headers, floatfmt=".3f", tablefmt="fancy_grid"))

    # Configuración de la animación
    my_animation = animation.FuncAnimation(
        fig=fig, func=update, frames=len(xc), interval=100,
        fargs=[xc, yc, scat, line, frame_count, point_coordinate, annotations], 
        blit=True
    )

    # Guardar la animación como GIF
    my_animation.save('parametric_curve.gif', writer='imagemagick', fps=60)
    plt.show()

if __name__ == "__main__":
    main_function()

print("End of this file...")
