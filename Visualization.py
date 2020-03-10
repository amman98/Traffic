import numpy as N
import matplotlib.pyplot as plt


"""
Pre: Initialized the model class, meaning all intersections,
lanes, and cars have been created.

Post: Create a visualization of the cars movement across traffic.
Each call to this method will show one time step in the simulation.
"""
def visualize(model):
    #- Preliminaries:
    
    length = 42
    width = 42
    data = N.ones((length, width, 3), dtype='f')*0.8 #- array of shape 42, 42, 3, all values are 0.8
    
    
    #- Create figure and axes:
    
    fig = plt.figure(figsize=(15,15)) #- sets window size to 5 x 5, returns a figure
    #ax = fig.add_axes( (0.0, 0.0, 1.0, 1.0), frameon=False )
    ax = fig.add_axes( (0.4, 0.3, 0.2, 0.4), frameon=False ) #- size of rectangle (left-right, up-down, width, height), returns axes?
    
    #- Set first display data values:
    data[:, 22, :] = N.array([1, 0, 0])
    data[:, 26, :] = N.array([1, 0, 0])
    
    """
    data[0,41,:] = N.array([1, 0, 0]) #- sets row 20, column 18's three slices to 1,0,0, which represents red on RGB
    
    colorit = matplotlib.colors.colorConverter.to_rgb('b') #- method for getting the color blue
    data[10,8,:] = colorit[:] #- sets row 10, column 8's three slices to the color blue, or 0,0,1 on RGB
    """
    
    #- Draw first image:
    img = ax.imshow(data, interpolation='none',
                    extent=[0, width, 0, length],
                    aspect="auto",
                    zorder=0) #- 5 parameters
    ax.axis('off') #- Turns off axis labels
    plt.draw() #- draws the figure, visualization is shown here
    
    coord = [(2,4),(6,8),(15,9),(20,2), (10,3)]
    for i in range(0, 5):
           
        
        plt.pause(1) #- pauses visualization for 2 seconds
        
        data = N.ones((length, width, 3), dtype='f')*0.8 #- array of shape 42, 42, 3, all values are 0.8
        data[:, 22, :] = N.array([1, 0, 0])
        data[:, 26, :] = N.array([1, 0, 0])
        data[coord[i][0], coord[i][1], :] = N.array([0, 0, 1])
    
        
        #- Change data some for second image to display:
        
        #data[0,41 - (i*2),:] = matplotlib.colors.colorConverter.to_rgb('r') #- sets row 20, column 18's three slices to yellow
        #data[3,2,:] = N.array([1,1,1]) #- sets row 3, column 2's three slices to white
        
        #- Draw second image:
        
        img.set_data(data) #- changes drawing to add new colors
        plt.draw() #- draws the figure, visualization is shown here
    
    
    
    
    #===== end file =====
