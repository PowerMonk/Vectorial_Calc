import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from tabulate import tabulate
from mpl_toolkits.axisartist.axislines import AxesZero 
import matplotlib.animation as animation


#plt.rcParams['text.usetex'] = True


def set_axis_function():

    fig = plt.figure()      # creates a new figure
    fig.set_figwidth(6)     # sets width of figure in inches
    fig.set_figheight(6)    # sets height of figure in inches
    myAxis_rectangular = fig.add_subplot(221, axes_class=AxesZero)
    myAxis_rectangular_polar = fig.add_subplot(222, axes_class=AxesZero)
    myAxis_polar = fig.add_subplot(212, projection='polar')
    
    
    myAxis_rectangular.set_title('Rectangular form') 
    myAxis_rectangular_polar.set_title('Rectangular-polar form')
    myAxis_polar.set_title("Polar Form") 

   
    
    myAxis_rectangular.axis["xzero"].set_axisline_style("-|>")   # adds arrows at each end of the x axis
    myAxis_rectangular.axis["yzero"].set_axisline_style("-|>")   # adds arrows at each end of the y axis

    myAxis_rectangular_polar.axis["xzero"].set_axisline_style("-|>")   # adds arrows at each end of the x axis
    myAxis_rectangular_polar.axis["yzero"].set_axisline_style("-|>")   # adds arrows at each end of the y axis


        
    myAxis_rectangular.axis["xzero"].set_visible(True)  # adds X-axis from the origin
    myAxis_rectangular.axis["yzero"].set_visible(True)  # adds Y-axis from the origin

    myAxis_rectangular_polar.axis["xzero"].set_visible(True)  # adds X-axis from the origin
    myAxis_rectangular_polar.axis["yzero"].set_visible(True)  # adds Y-axis from the origin

    myAxis_rectangular.set_xlim(-3, 10)  # sets range of values for the X-axis
    myAxis_rectangular.set_ylim(-10, 10)  # sets range of values for the Y-axis

    myAxis_rectangular_polar.set_xlim(-6, 6)  # sets range of values for the X-axis
    myAxis_rectangular_polar.set_ylim(-6, 6)  # sets range of values for the Y-axis

    myAxis_polar.set_ylim(0, 5)  # sets range of values for the Y-axis

       # sets a title for the coordinate axes


    myAxis_rectangular.minorticks_on()      # displays a minor grid
    myAxis_rectangular.grid(True, which='major', color='grey', linestyle='-')       # sets the color and style of the major grid
    myAxis_rectangular.grid(True, which='minor', color='grey', linestyle='--')      # sets the color and style of the minor grid 


    myAxis_rectangular.xaxis.set_major_locator(MultipleLocator(np.pi/2))      # sets the horizontal spacing of the major grid
    myAxis_rectangular.yaxis.set_major_locator(MultipleLocator(1))      # sets the vertical spacing of the major grid

    myAxis_rectangular.xaxis.set_minor_locator(MultipleLocator(np.pi/12))    # sets the horizontal spacing of the minor grid
    myAxis_rectangular.yaxis.set_minor_locator(MultipleLocator(0.5))    # sets the vertical spacing of the minor grid


    myAxis_rectangular_polar.minorticks_on()      # displays a minor grid
    myAxis_rectangular_polar.grid(True, which='major', color='grey', linestyle='-')       # sets the color and style of the major grid
    myAxis_rectangular_polar.grid(True, which='minor', color='grey', linestyle='--')      # sets the color and style of the minor grid 


    myAxis_rectangular_polar.xaxis.set_major_locator(MultipleLocator(1))      # sets the horizontal spacing of the major grid
    myAxis_rectangular_polar.yaxis.set_major_locator(MultipleLocator(1))      # sets the vertical spacing of the major grid

    myAxis_rectangular_polar.xaxis.set_minor_locator(MultipleLocator(0.5))    # sets the horizontal spacing of the minor grid
    myAxis_rectangular_polar.yaxis.set_minor_locator(MultipleLocator(0.5))    # sets the vertical spacing of the minor grid
   
    return myAxis_rectangular, myAxis_rectangular_polar, myAxis_polar


def main_function():

    print("This is an example of a polar graph")
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
  
    axis_rect,  axis_rect_polar, axis_polar = set_axis_function()

    theta = np.linspace(0, 2*np.pi, 101) #linspace  no tiene el problema de redondeo que presenta arange
   
    r = 4 * np.cos(2*theta)
   




    axis_rect.scatter(theta, r, color="red", s=5, label='point')
    axis_rect.plot(theta, r, color='blue', label='rectangular')
    axis_polar.plot(theta + (r < 0)*np.pi, abs(r), color='red')# this modification is due to matplot's inability to to invert r direction when its sign is negative (is not actually an inability is just that we set the "y" axis of the plot to only show positive values, so that the polar axis looks more like the one we draw manually on paper), thats why i found this trick online to always use positive values of r but sumulate the negative ones changing the angle adding pi. This is possible because in polar we can represen one point in more than one way 
    axis_polar.scatter(theta + (r < 0)*np.pi, abs(r), s=5, color='blue')                 # to be fair is not that matplot cannot represent negative values, it is just that we want to represent the polar curves gracefully using only positive values for r in the polar coordinate system an represent the negatives in the opposite direction just as we do manually, since when we plot points manually in paper we dont tend to use negative values for the radius, we invert the direction of r instead.
    # by the way we can set the polar axis to show negative values using myAxis_polar.set_ylim(0, 5)and giving negative values to the first argument, the thing is that in such case the graphs of some curves won't look as those tha we see manually reresented in polar axis that go with circles fom radious = 0 to circles with only positive radious.
    #using the trick mentioned above the graphs plotted llok like those plotted by geogebra and the ones in the books.
     
    x = r * np.cos(theta) 
    y = r * np.sin(theta) 
    
    axis_rect_polar.plot(x, y, color='blue', label='rectangular')  
    axis_rect_polar.scatter(x, y, color="red", s=5, label='point')
    
                                                                
    headers = ["theta", "r", "x", "y"]
    table = zip(theta, r, x, y)

    my_table = tabulate(table, headers, floatfmt=".3f", tablefmt="fancy_grid")
    print(my_table)

    plt.legend()
    plt.show() # shows all the operations performed on the axis


    

if __name__== "__main__":
    main_function()

print("End of this file....")