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
    myAxis_rectangular = fig.add_subplot(121, axes_class=AxesZero)
    myAxis_polar = fig.add_subplot(122, projection='polar')
    
    
    myAxis_rectangular.set_title(r'Rectangular form') 
    myAxis_polar.set_title("Polar Form") 

   
    
    myAxis_rectangular.axis["xzero"].set_axisline_style("-|>")   # adds arrows at each end of the x axis
    myAxis_rectangular.axis["yzero"].set_axisline_style("-|>")   # adds arrows at each end of the y axis


        
    myAxis_rectangular.axis["xzero"].set_visible(True)  # adds X-axis from the origin
    myAxis_rectangular.axis["yzero"].set_visible(True)  # adds Y-axis from the origin

    myAxis_rectangular.set_xlim(-3, 10)  # sets range of values for the X-axis
    myAxis_rectangular.set_ylim(-10, 10)  # sets range of values for the Y-axis

    myAxis_polar.set_ylim(0, 5)  # sets range of values for the Y-axis

       # sets a title for the coordinate axes


    myAxis_rectangular.minorticks_on()      # displays a minor grid
    myAxis_rectangular.grid(True, which='major', color='grey', linestyle='-')       # sets the color and style of the major grid
    myAxis_rectangular.grid(True, which='minor', color='grey', linestyle='--')      # sets the color and style of the minor grid 


    myAxis_rectangular.xaxis.set_major_locator(MultipleLocator(np.pi/2))      # sets the horizontal spacing of the major grid
    myAxis_rectangular.yaxis.set_major_locator(MultipleLocator(1))      # sets the vertical spacing of the major grid

    myAxis_rectangular.xaxis.set_minor_locator(MultipleLocator(np.pi/12))    # sets the horizontal spacing of the minor grid
    myAxis_rectangular.yaxis.set_minor_locator(MultipleLocator(0.5))    # sets the vertical spacing of the minor grid
   
    return myAxis_rectangular, myAxis_polar, fig

def update(frame, theta, r, theta_polar, r_polar, scat, line, scat_polar, line_polar,frame_count, point_coordinate, annotations):

   

    a = theta[:frame+1]
    b = r[:frame+1]

    a_polar = theta_polar[:frame+1]
    b_polar = r_polar[:frame+1]

    data = np.stack([a, b]).T
    scat.set_offsets(data)
    line.set_data(a,b)
    #scat_polar.set_o(data)
    line_polar.set_data(a_polar,b_polar)

    #t = y[frame] - 1 # from parametric equation
    frame_count.set_text('frame: {0}'.format(frame))
    point_coordinate.set_text('({:.3}, {:.3}) -> theta = {:.3}'.format(theta[frame], r[frame], theta[frame]))

    annotations.set_position((theta[frame], r[frame])) 
    annotations.xy = (theta[frame] + 2, r[frame] + 2) #this is for position of the text only
    annotations.set_text('({:.3}, {:.3}) \n theta = {:.3}'.format(theta[frame], r[frame], theta[frame])) 
   
    return (scat, line, scat_polar, line_polar, frame_count, point_coordinate, annotations)

def main_function():

    print("This is an example of an animation")
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
  
    axis_rect, axis_polar, fig = set_axis_function()

    theta = np.linspace(0, 2*np.pi, num=101) #linspace  no tiene el problema de redondeo que presenta arange
   
    r = 4 * np.cos(2*theta)
    r_to_plot = abs(r.copy())
    theta_to_plot = theta.copy()

    index = 0
    for r_val in r:
        
        if r_val < 0:
            theta_to_plot[index] = theta[index] + np.pi
        index += 1
    



    # axis_rect.scatter(theta, r, color="red", s=5, label='point')
    # axis_rect.plot(theta, r, color='blue', label='rectangular')
    #axis_polar.plot(theta + (r < 0)*np.pi, abs(r), color='red')# this modification is due to matplot's inability to to invert r direction when its sign is negative (is not actually an inability is just that we set the "y" axis of the plot to only show positive values, so that the polar axis looks more like the one we draw manually on paper), thats why i found this trick online to always use positive values of r but sumulate the negative ones changing the angle adding pi. This is possible because in polar we can represen one point in more than one way 
    #axis_polar.scatter(theta + (r < 0)*np.pi, abs(r), color='blue')                 # to be fair is not that matplot cannot represent negative values, it is just that we want to represent the polar curves gracefully using only positive values for r in the polar coordinate system an represent the negatives in the opposite direction just as we do manually, since wen we plot points manually in paper we dont tend to use negative values for the radius, we invert the direction of r instead.
                                                                    # by the way we can set the polar axis to show negative values using myAxis_polar.set_ylim(0, 5)and giving negative values to the first argument, the thing is that in such case the graphs of some curves won't look as those tha we see manually reresented in polar axis that go with circles fom radious = 0 to circles with only positive radious.
                                                                    #using the trick mentioned above the graphs plotted llok like those plotted by geogebra and the ones in the books.
     
    x= r* np.cos(theta) 
    y= r* np.sin(theta) 
    
    line_polar = axis_polar.plot(theta[0] + (r[0] < 0)*np.pi, abs(r[0]), color='red')[0]  # the (r[0] < 0) part is just to plot the point using only positive r and modifiying the angle to compensate for the use of only positive r's. That is not neccesary in this exercise since I use a different approach to animate, it is necessary though whe you plot a polart plot without animating
    scat_polar = axis_polar.scatter(theta[0] + (r[0] < 0)*np.pi, abs(r[0]), color='blue')
    
    scat = axis_rect.scatter(theta[0], r[0], c="b", s=5, label='point')
    line = axis_rect.plot(theta[0], r[0],label='curve')[0]
    frame_count = axis_rect.text(3,6, '', bbox=dict(facecolor='yellow', alpha=0.5))
    point_coordinate = axis_rect.text(3, 8, '', bbox=dict(facecolor='green', alpha=0.5))
    annotations = axis_rect.annotate('', xy=(theta[0]+2, r[0]+2), xytext=(theta[0], r[0]), bbox=dict(boxstyle="round", facecolor='pink', alpha=0.5),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.8', lw=1, color='red'),
             fontsize=14, color='blue', fontweight='normal')
    
    my_animation = animation.FuncAnimation(fig=fig, func=update, frames=len(theta), interval=100, fargs=[theta, r, theta_to_plot, r_to_plot, scat, line, scat_polar, line_polar,frame_count, point_coordinate, annotations], blit=True)
    my_animation.save('animation_drawing.gif', writer='imagemagick', fps=60)
    
    
    
                                                                
    headers = ["theta", "r", "x", "y"]
    table = zip(theta, r, x, y)


    print(tabulate(table, headers, floatfmt=".3f", tablefmt="fancy_grid"))

    plt.legend()
    plt.show() # shows all the operations performed on the axis


    

if __name__== "__main__":
    main_function()

print("End of this file....")