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




def main_function():


    myAxis = set_axis_function()

    x_data = np.linspace(-5.0, 5.0, num=11)
    y_data = np.linspace(-5.0, 5.0, num=11)

    X, Y = np.meshgrid(x_data, y_data)
    print("X values", X)
    
    print("Y values", Y)

    z = (12 - 2 * X - 3 * Y) / 4  
    # z = (50 - 6 * X - 10 * Y) / 7
    # z = X +Y

    print("z values", z)

    headers = ["x", "y", "z"]
    
    for i in range(0, X[0].size):
        table = zip(X[i],Y[i],z[i])
        print(tabulate(table , headers, floatfmt=".4f", tablefmt="fancy_grid"))

    # myAxis.plot_surface(X, Y, z, color = 'hotpink')
    myAxis.plot_surface(X, Y, z, color = 'lightgreen', alpha = 0.7, linewidth = 0.6, edgecolor = 'blue')
    plt.show()



if __name__ == "__main__":
    main_function()

print("\nEnd of this File\n")