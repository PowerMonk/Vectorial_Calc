import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from tabulate import tabulate
from mpl_toolkits.axisartist.axislines import AxesZero 
import matplotlib.animation as animation

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

    return myAxis, fig


def update(frame, xc, yc, t, x_tan, tan_lines, tangent_line, p_0, frame_count, point_coordinate, annotations):

   
    tangent_line.set_data(x_tan, tan_lines[frame])
    slope = 3 * (t[frame] - (1/t[frame])) / 2
    # slope = 1 / (2 * t[frame] - 2)


    data = np.stack([xc[frame], yc[frame]]).T
    p_0.set_offsets(data)
    # a=x[:frame+1]
    # b= y[:frame+1]
    # data = np.stack([a, b]).T
    # scat.set_offsets(data)
    # curve.set_data(a,b)
    # t = y[frame] - 1 # from parametric equation
    frame_count.set_text('frame: {0}'.format(frame))
    point_coordinate.set_text('({:.3}, {:.3}) -> t = {:.3}'.format(xc[frame], yc[frame], t[frame]))

    annotations.set_position((xc[frame] + 2, yc[frame] + 2)) 
    annotations.xy = (xc[frame], yc[frame])
    annotations.set_text('({:.3}, {:.3}) -> t = {:.3}\n m = {:.3} '.format(xc[frame], yc[frame], t[frame], slope)) 
   
    return (tangent_line, frame_count, p_0, point_coordinate, annotations)


def parametric_function(t):

    # x = np.power(t, 2) - 2 * t
    # y =  t + 1

    x = np.power(t, 2)
    y = np.power(t, 3) - 3 * t

    # x = (1 + np.sin(b*t)) * np.cos(t)
    # y = (1 + np.sin(b*t)) * np.sin(t)
    # x = np.power(t, 2) - 2*t
    # y = t + 1
    

    return x, y


def main_function():

    print("This is an example of an animation")

  
    axis, fig = set_axis_function()

    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
    #x_data = np.arange(-2, 2.01, 0.1)
    t = np.linspace(-2, 2, num=41) #linspace  no tiene el problema de redondeo que presenta arange
   
 
    xc, yc = parametric_function(t)

    axis.plot(xc, yc, label='curve')

    axis.scatter(xc, yc, c="b", s=5, label='point')

    x_tangent = np.linspace(-2, 10, 13)

    slope = 3 * (t - (1/t)) / 2
    #slope = 1 / (2 * t - 2)

    tangent_line = axis.plot(xc[0], yc[0], color="red", label='tangent_line')[0]
    p_0 = axis.scatter(xc[0], yc[0], s=15, c="r")

    tangent_lines = []
    for t_element in t:
        x_0, y_0 = parametric_function(t_element)
        #slope = 1 / (2 * t_element - 2)
        slope = 3 * (t_element - (1/t_element)) / 2
        tangent_lines.append(slope * (x_tangent - x_0) + y_0)

 
    frame_count = axis.text(3,6, '', bbox=dict(facecolor='yellow', alpha=0.5))
    point_coordinate = axis.text(3, 8, '', bbox=dict(facecolor='green', alpha=0.5))
    annotations = axis.annotate('', xy=(xc[0], yc[0]), xytext=(xc[0], yc[0]), bbox=dict(boxstyle="round", facecolor='pink', alpha=0.5),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5', lw=1, color='green'),
            fontsize=14, color='blue', fontweight='normal')
      

    #plt.legend()

   # headers = ["x", "y", "t"]
    #table = zip(xc, yc, t)


    #print(tabulate(table , headers, floatfmt=".3f", tablefmt="fancy_grid"))

    my_animation = animation.FuncAnimation(fig=fig, func=update, frames=t.size, interval=500, fargs=[xc, yc, t, x_tangent, tangent_lines, tangent_line, p_0, frame_count, point_coordinate, annotations], blit=True)
                                
    #ani.save('animation_drawing.mp4', writer='ffmpeg', fps=60)
    my_animation.save('animation_drawing.gif', writer='imagemagick', fps=60)
    plt.show() # shows all the operations performed on the axis


    

if __name__== "__main__":
    main_function()

print("End of this file....")