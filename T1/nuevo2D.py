import matplotlib.pyplot as plt     #imports a module to work with figures and axes
import numpy as np                  #imports the numeric python module that allows us to perform many mathematical operations efficiently
from matplotlib.ticker import MultipleLocator       # imports a utility to be able to set grids on the axis


from mpl_toolkits.axisartist.axislines import AxesZero      # imports a utility to create a classical axes-zero coordinate system


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
    myAxis.set_ylim(-2, 10)  # sets range of values for the Y-axis

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

    print("This is an example of Taylor Series")

    axis = set_axis_function()

    axis.scatter(3, 5)  # draws a point at location (3, 5)
    axis.scatter(1, 5) # draws a point at location (1, 5)
    axis.scatter(5, 7) # draws a point at location (5, 7)

    plt.show() # shows all the operations performed on the axis


if __name__== "__main__":
    main_function()