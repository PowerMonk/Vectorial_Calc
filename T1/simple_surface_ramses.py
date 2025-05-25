import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def set_axis_function():

    fig = plt.figure()      # creates a new figure
    fig.set_figwidth(6)     # sets width of figure in inches
    fig.set_figheight(6)    # sets height of figure in inches

    myAxis = fig.add_subplot(111, projection='3d')    # creates 3-D coordinate axes

    plt.title('3D-Space')

    myAxis.set_xlim([-15, 15])
    myAxis.set_ylim([-15, 15])
    myAxis.set_zlim([-15, 15])

    myAxis.set_xlabel('X')
    myAxis.set_ylabel('Y')
    myAxis.set_zlabel('Z')

    a_x_p = np.array([1, 0, 0])
    a_x_m = np.array([-1, 0, 0])
    a_y_p = np.array([0, 1, 0])
    a_y_m = np.array([0, -1, 0])
    a_z_p = np.array([0, 0, 1])
    a_z_m = np.array([0, 0, -1])

    #create arrows as a set of coordinate axes of reference
    myAxis.quiver(0, 0, 0, a_x_p[0], a_x_p[1], a_x_p[2], color='r', arrow_length_ratio=0.1)
    myAxis.quiver(0, 0, 0, a_x_m[0], a_x_m[1], a_x_m[2], color='r', arrow_length_ratio=0.1)
    myAxis.quiver(0, 0, 0, a_y_p[0], a_y_p[1], a_y_p[2], color='g', arrow_length_ratio=0.1)
    myAxis.quiver(0, 0, 0, a_y_m[0], a_y_m[1], a_y_m[2], color='g', arrow_length_ratio=0.1)
    myAxis.quiver(0, 0, 0, a_z_p[0], a_z_p[1], a_z_p[2], color='b', arrow_length_ratio=0.1)
    myAxis.quiver(0, 0, 0, a_z_m[0], a_z_m[1], a_z_m[2], color='b', arrow_length_ratio=0.1)

    return myAxis

def plot_plane_and_vectors(myAxis):
    # Generar un plano a partir de la ecuación 2x + 3y + 4z = 12
    x_data = np.linspace(-5.0, 5.0, num=11)
    y_data = np.linspace(-5.0, 5.0, num=11)

    X, Y = np.meshgrid(x_data, y_data)
    Z = (12 - 2 * X - 3 * Y) / 4  # Ecuación del plano
    

    myAxis.plot_surface(X, Y, Z, color='cyan', alpha=0.5)  # Dibujar el plano

    # Dibujar los puntos A, B, C, D
    points = np.array([[2, 4, -1], [6, 0, 0], [0, 4, 0], [0, 0, 3]])
    labels = ['A', 'B', 'C', 'D']
    for i, point in enumerate(points):
        myAxis.scatter(point[0], point[1], point[2], color='black')
        myAxis.text(point[0], point[1], point[2], f'{labels[i]}', color='black')

    # Dibujar el vector u = (4,7,3) desde A
    A = np.array([2, 4, -1])
    u = np.array([4, 7, 3])
    myAxis.quiver(A[0], A[1], A[2], u[0]-A[0], u[1]-A[1], u[2]-A[2], color='purple', arrow_length_ratio=0.1)

def main_function():
    myAxis = set_axis_function()
    
    # Plot the plane, points, and vector
    plot_plane_and_vectors(myAxis)

    plt.show()

if __name__ == "_main_":
    main_function()

print("\nEnd of this File\n")