
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

    myAxis.set_xlim(-5, 25)  # sets range of values for the X-axis
    myAxis.set_ylim(-10, 10)  # sets range of values for the Y-axis

    myAxis.set_title("Parametric Curve")    # sets a title for the coordinate axes


    myAxis.minorticks_on()      # displays a minor grid
    myAxis.grid(True, which='major', color='grey', linestyle='-')       # sets the color and style of the major grid
    myAxis.grid(True, which='minor', color='grey', linestyle='--')      # sets the color and style of the minor grid 


    myAxis.xaxis.set_major_locator(MultipleLocator(1))      # sets the horizontal spacing of the major grid
    myAxis.yaxis.set_major_locator(MultipleLocator(1))      # sets the vertical spacing of the major grid

    myAxis.xaxis.set_minor_locator(MultipleLocator(0.5))    # sets the horizontal spacing of the minor grid
    myAxis.yaxis.set_minor_locator(MultipleLocator(0.5))    # sets the vertical spacing of the minor grid

    return myAxis



def main_function():

    print("This is an example of an animation")
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
  
    axis = set_axis_function()

    t = np.linspace(-2, 5, num=101) #linspace  no tiene el problema de redondeo que presenta arange
   
    xc = np.power(t, 2) - 2 * t
    yc = t + 1


    axis.scatter(xc, yc, color="red", s=5, label='point')
    axis.plot(xc, yc, color='blue', label='curve')
    


    headers = ["x", "y", "t"]
    table = zip(xc, yc, t)


    print(tabulate(table , headers, floatfmt=".3f", tablefmt="fancy_grid"))

    plt.legend()
    plt.show() # shows all the operations performed on the axis


    

if __name__== "__main__":
    main_function()

print("End of this file....")