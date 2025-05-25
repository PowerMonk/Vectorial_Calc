import matplotlib.pyplot as plt #imports a module to work with figures and axes
import numpy as np # imports the numeric python module that allows us to perform many mathematical operations efficiently
from matplotlib.ticker import MultipleLocator # imports a utility to be able to set grids on the axis


fig = plt.figure() #creates a new figure

myAxis = fig.add_subplot(111) #adds an Axes to the current figure 

myAxis.set_xlim(0,10) # sets limits for the x-axis
myAxis.set_ylim(0,10) # sets limits for the y-axis


myAxis.minorticks_on() # displays a minor grid

myAxis.grid(True,which='major', color='grey', linestyle='-') # sets the color and style of the major grid
myAxis.grid(True,which='minor',color='grey', linestyle='--') # sets the color and style of the minor grid 

myAxis.xaxis.set_major_locator(MultipleLocator(1)) #sets the horizontal spacing of the major grid
myAxis.yaxis.set_major_locator(MultipleLocator(1)) #sets the vertical spacing of the major grid

myAxis.xaxis.set_minor_locator(MultipleLocator(0.5)) #sets the horizontal spacing of the minor grid
myAxis.yaxis.set_minor_locator(MultipleLocator(0.5)) #sets the vertical spacing of the minor grid

myAxis.scatter(3, 5) # draws a point at location (3, 5)
myAxis.scatter(1, 5) # draws a point at location (1, 5)

myAxis.scatter(5, 7) # draws a point at location (5, 7)


plt.show() # shows all the operations performed on the axis



