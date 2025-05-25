import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from tabulate import tabulate
from mpl_toolkits.axisartist.axislines import AxesZero


def set_axis_function():

    fig = plt.figure()      # creates a new figure
    fig.set_figwidth(6)     # sets width of figure in inches
    fig.set_figheight(6)    # sets height of figure in inches


    myAxis = fig.add_subplot(axes_class=AxesZero)    # creates coordinate axes
    
    myAxis.axis["xzero"].set_axisline_style("-|>")   # adds arrows at each end of the x axis
    myAxis.axis["yzero"].set_axisline_style("-|>")   # adds arrows at each end of the y axis


        
    myAxis.axis["xzero"].set_visible(True)  # adds X-axis from the origin
    myAxis.axis["yzero"].set_visible(True)  # adds Y-axis from the origin

    myAxis.set_xlim(-5, 10)  # sets range of values for the X-axis
    myAxis.set_ylim(-10, 10)  # sets range of values for the Y-axis

    myAxis.set_title("2D-Plane")    # sets a title for the coordinate axes


    myAxis.minorticks_on()      # displays a minor grid
    myAxis.grid(True, which='major', color='grey', linestyle='-')       # sets the color and style of the major grid
    myAxis.grid(True, which='minor', color='grey', linestyle='--')      # sets the color and style of the minor grid 


    myAxis.xaxis.set_major_locator(MultipleLocator(1))      # sets the horizontal spacing of the major grid
    myAxis.yaxis.set_major_locator(MultipleLocator(1))      # sets the vertical spacing of the major grid

    myAxis.xaxis.set_minor_locator(MultipleLocator(0.5))    # sets the horizontal spacing of the minor grid
    myAxis.yaxis.set_minor_locator(MultipleLocator(0.5))    # sets the vertical spacing of the minor grid

    return myAxis




def main_function():
    print("This is a program to generate a table of values")
    
    my_axis = set_axis_function() 

    t_values = np.linspace(-5,5,11)

    x_values = 5 + t_values
    y_values = 1 + 4*t_values
    z_values = 3 - 2*t_values
    
    print(x_values)
    print(y_values)
    print(z_values)
    print(t_values)

    my_axis.plot(x_values, y_values, z_values)


    plt.show()





if __name__ == "__main__":
    main_function()






    
print("End")

# encuentre la ecuacion vectorial y las ecuaciones parametricas para la linea que pasa a través del punto 5,1,3 y que es paralela al vector i+4j-2k