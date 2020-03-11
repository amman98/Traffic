# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:49:28 2020

@author: Amman Nega
"""

from Intersection import Intersection
import numpy as N
from BoundaryLane import BoundaryLane
import matplotlib.pyplot as plt


class Model(object):
    
    #- Global Variables
    
    """
    probCar: float that determines probability of how many cars will be on road, 
    used to simulate how congested traffic can be at different times of
    day.
    """
    probCar = 0.60 
    
    """
    redLightLength: int representing seconds light stays red.
    """
    redLightLength = 15
    
    """
    greenLightLength: int representing seconds light stays
    green.
    """
    greenLightLength = 17
    
    """
    YELLOW_LIGHT_LENGTH: constant int representing length of time
    light stays yellow. Determined by research on average length
    of time light stays yellow and observation of Lake City Way traffic.
    """
    YELLOW_LIGHT_LENGTH = 4
    
    sim_length = 30 #- simulation length in minutes
    
    dt = 1/15 #- time step is 4 seconds, or 1/15 of a minute
    
    """
    Pre: Have a lane and car class created.
    
    Post: Creates lanes and places cars on each lane.
    Also decides which lanes are to the front, left, right
    and adjacent to each lane.
    """
    def __init__(self ):

        border = BoundaryLane()
        self.intersectionArray = N.array(([Intersection(), Intersection()], [Intersection(), Intersection()]))

        #self.intersectionArray[0][0] = Intersection()
        #self.intersectionArray[0][1] = Intersection()
        #self.intersectionArray[1][0] = Intersection()
        #self.intersectionArray[1][1] = Intersection()

        # First Intersection
        
        # North Bound Lanes                     
        # left turn lane                   
        self.intersectionArray[0][0].northLanes[0].nextLaneFwd = border 
        self.intersectionArray[0][0].northLanes[0].nextLaneLeft = border 

        # straight lane                     
        self.intersectionArray[0][0].northLanes[1].nextLaneFwd = border 
        self.intersectionArray[0][0].northLanes[1].nextLaneFwdLeft = border 
        self.intersectionArray[0][0].northLanes[1].nextLaneRightFwd = border 
        self.intersectionArray[0][0].northLanes[1].nextLaneRightLeft = border 
        
        # East Bound Lanes                       
        # left turn lane
        self.intersectionArray[0][0].eastLanes[0].nextLaneFwd = border 
        self.intersectionArray[0][0].eastLanes[0].nextLaneLeft = border 
        
        # straight lane
        self.intersectionArray[0][0].eastLanes[1].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[0][0].eastLanes[1].nextLaneFwdLeft = self.intersectionArray[0][1].eastLanes[0]
        self.intersectionArray[0][0].eastLanes[1].nextLaneRightFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[0][0].eastLanes[1].nextLaneRightLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # South Bound Lanes                       
        # left turn lane
        self.intersectionArray[0][0].southLanes[0].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1] 
        self.intersectionArray[0][0].southLanes[0].nextLaneLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # straight lane
        self.intersectionArray[0][0].southLanes[1].nextLaneFwd = self.intersectionArray[1][0].southLanes[1]
        self.intersectionArray[0][0].southLanes[1].nextLaneFwdLeft = self.intersectionArray[1][0].southLanes[0]
        self.intersectionArray[0][0].southLanes[1].nextLaneRightFwd = self.intersectionArray[1][0].southLanes[1]
        self.intersectionArray[0][0].southLanes[1].nextLaneRightLeft = self.intersectionArray[1][0].southLanes[0]

        # West Bound Lanes
        # left turn lane
        self.intersectionArray[0][0].westLanes[0].nextLaneFwd = border 
        self.intersectionArray[0][0].westLanes[0].nextLaneLeft = border 
        
        # straight lane
        self.intersectionArray[0][0].westLanes[1].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[0][0].westLanes[1].nextLaneFwdLeft = self.intersectionArray[0][1].eastLanes[0]
        self.intersectionArray[0][0].westLanes[1].nextLaneRightFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[0][0].westLanes[1].nextLaneRightLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # Second Intersection
        
        # North Bound Lanes                     
        # left turn lane                   
        self.intersectionArray[0][1].northLanes[0].nextLaneFwd = border 
        self.intersectionArray[0][1].northLanes[0].nextLaneLeft = border 

        # straight lane                     
        self.intersectionArray[0][1].northLanes[1].nextLaneFwd = border 
        self.intersectionArray[0][1].northLanes[1].nextLaneFwdLeft = border 
        self.intersectionArray[0][1].northLanes[1].nextLaneRightFwd = border 
        self.intersectionArray[0][1].northLanes[1].nextLaneRightLeft = border 
        
        # East Bound Lanes                       
        # left turn lane
        self.intersectionArray[0][1].eastLanes[0].nextLaneFwd = border 
        self.intersectionArray[0][1].eastLanes[0].nextLaneLeft = border 
        
        # straight lane
        self.intersectionArray[0][1].eastLanes[1].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[0][1].eastLanes[1].nextLaneFwdLeft = self.intersectionArray[0][1].eastLanes[0]
        self.intersectionArray[0][1].eastLanes[1].nextLaneRightFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[0][1].eastLanes[1].nextLaneRightLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # South Bound Lanes                       
        # left turn lane
        self.intersectionArray[0][1].southLanes[0].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1] 
        self.intersectionArray[0][1].southLanes[0].nextLaneLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # straight lane
        self.intersectionArray[0][1].southLanes[1].nextLaneFwd = self.intersectionArray[1][0].southLanes[1]
        self.intersectionArray[0][1].southLanes[1].nextLaneFwdLeft = self.intersectionArray[1][0].southLanes[0]
        self.intersectionArray[0][1].southLanes[1].nextLaneRightFwd = self.intersectionArray[1][0].southLanes[1]
        self.intersectionArray[0][1].southLanes[1].nextLaneRightLeft = self.intersectionArray[1][0].southLanes[0]

        # West Bound Lanes
        # left turn lane
        self.intersectionArray[0][1].westLanes[0].nextLaneFwd = border 
        self.intersectionArray[0][1].westLanes[0].nextLaneLeft = border 
        
        # straight lane
        self.intersectionArray[0][1].westLanes[1].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[0][1].westLanes[1].nextLaneFwdLeft = self.intersectionArray[0][1].eastLanes[0]
        self.intersectionArray[0][1].westLanes[1].nextLaneRightFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[0][1].westLanes[1].nextLaneRightLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # Third Intersection
        
        # North Bound Lanes                     
        # left turn lane                   
        self.intersectionArray[1][0].northLanes[0].nextLaneFwd = border 
        self.intersectionArray[1][0].northLanes[0].nextLaneLeft = border 

        # straight lane                     
        self.intersectionArray[1][0].northLanes[1].nextLaneFwd = border 
        self.intersectionArray[1][0].northLanes[1].nextLaneFwdLeft = border 
        self.intersectionArray[1][0].northLanes[1].nextLaneRightFwd = border 
        self.intersectionArray[1][0].northLanes[1].nextLaneRightLeft = border 
        
        # East Bound Lanes                       
        # left turn lane
        self.intersectionArray[1][0].eastLanes[0].nextLaneFwd = border 
        self.intersectionArray[1][0].eastLanes[0].nextLaneLeft = border 
        
        # straight lane
        self.intersectionArray[1][0].eastLanes[1].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[1][0].eastLanes[1].nextLaneFwdLeft = self.intersectionArray[0][1].eastLanes[0]
        self.intersectionArray[1][0].eastLanes[1].nextLaneRightFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[1][0].eastLanes[1].nextLaneRightLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # South Bound Lanes                       
        # left turn lane
        self.intersectionArray[1][0].southLanes[0].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1] 
        self.intersectionArray[1][0].southLanes[0].nextLaneLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # straight lane
        self.intersectionArray[1][0].southLanes[1].nextLaneFwd = self.intersectionArray[1][0].southLanes[1]
        self.intersectionArray[1][0].southLanes[1].nextLaneFwdLeft = self.intersectionArray[1][0].southLanes[0]
        self.intersectionArray[1][0].southLanes[1].nextLaneRightFwd = self.intersectionArray[1][0].southLanes[1]
        self.intersectionArray[1][0].southLanes[1].nextLaneRightLeft = self.intersectionArray[1][0].southLanes[0]

        # West Bound Lanes
        # left turn lane
        self.intersectionArray[1][0].westLanes[0].nextLaneFwd = border 
        self.intersectionArray[1][0].westLanes[0].nextLaneLeft = border 
        
        # straight lane
        self.intersectionArray[1][0].westLanes[1].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[1][0].westLanes[1].nextLaneFwdLeft = self.intersectionArray[0][1].eastLanes[0]
        self.intersectionArray[1][0].westLanes[1].nextLaneRightFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[1][0].westLanes[1].nextLaneRightLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # Fourth Intersection
        
        # North Bound Lanes                     
        # left turn lane                   
        self.intersectionArray[1][1].northLanes[0].nextLaneFwd = border 
        self.intersectionArray[1][1].northLanes[0].nextLaneLeft = border 

        # straight lane                     
        self.intersectionArray[1][1].northLanes[1].nextLaneFwd = border 
        self.intersectionArray[1][1].northLanes[1].nextLaneFwdLeft = border 
        self.intersectionArray[1][1].northLanes[1].nextLaneRightFwd = border 
        self.intersectionArray[1][1].northLanes[1].nextLaneRightLeft = border 
        
        # East Bound Lanes                       
        # left turn lane
        self.intersectionArray[1][1].eastLanes[0].nextLaneFwd = border 
        self.intersectionArray[1][1].eastLanes[0].nextLaneLeft = border 
        
        # straight lane
        self.intersectionArray[1][1].eastLanes[1].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[1][1].eastLanes[1].nextLaneFwdLeft = self.intersectionArray[0][1].eastLanes[0]
        self.intersectionArray[1][1].eastLanes[1].nextLaneRightFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[1][1].eastLanes[1].nextLaneRightLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # South Bound Lanes                       
        # left turn lane
        self.intersectionArray[1][1].southLanes[0].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1] 
        self.intersectionArray[1][1].southLanes[0].nextLaneLeft = self.intersectionArray[0][1].eastLanes[0]
        
        # straight lane
        self.intersectionArray[1][1].southLanes[1].nextLaneFwd = self.intersectionArray[1][0].southLanes[1]
        self.intersectionArray[1][1].southLanes[1].nextLaneFwdLeft = self.intersectionArray[1][0].southLanes[0]
        self.intersectionArray[1][1].southLanes[1].nextLaneRightFwd = self.intersectionArray[1][0].southLanes[1]
        self.intersectionArray[1][1].southLanes[1].nextLaneRightLeft = self.intersectionArray[1][0].southLanes[0]

        # West Bound Lanes
        # left turn lane
        self.intersectionArray[1][1].westLanes[0].nextLaneFwd = border 
        self.intersectionArray[1][1].westLanes[0].nextLaneLeft = border 
    
        # straight lane
        self.intersectionArray[1][1].westLanes[1].nextLaneFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[1][1].westLanes[1].nextLaneFwdLeft = self.intersectionArray[0][1].eastLanes[0]
        self.intersectionArray[1][1].westLanes[1].nextLaneRightFwd = self.intersectionArray[0][1].eastLanes[1]
        self.intersectionArray[1][1].westLanes[1].nextLaneRightLeft = self.intersectionArray[0][1].eastLanes[0]

        
        """
        create four intersection objects and make
        clear which ones are adjacent to which.
        
        have each intersection adjacent to the 
        boundary.
        """
        self.timeWithinBoundary = []

    
    """
    Pre: Have initialized each lane and car object.
    
    Post: Runs the model and plots visualization of the
    cars moving through traffic.
    """
    def runModel(self):

        length = 42
        width = 42
        data = N.ones((length, width, 3), dtype='f')*0.8 #- array of shape 42, 42, 3, all values are 0.8


        #- Create figure and axes:
    
        fig = plt.figure(figsize=(15,15)) #- sets window size to 5 x 5, returns a figure
        #ax = fig.add_axes( (0.0, 0.0, 1.0, 1.0), frameon=False )
        ax = fig.add_axes( (0.2, 0.2, 0.6, 0.6), frameon=False ) #- size of rectangle (left-right, up-down, width, height), returns axes?

        #- draw lanes and intersections here
        #- boundary of traffic
        data[:, 0, :] = N.array([0, 1, 0])
        data[0, :, :] = N.array([0, 1, 0])
        data[:, -1, :] = N.array([0, 1, 0])
        data[-1, :, :] = N.array([0, 1, 0])
        
        img = ax.imshow(data, interpolation='none',
                extent=[0, width, 0, length],
                aspect="auto",
                zorder=0) #- 5 parameters
        ax.axis('off') #- Turns off axis labels
        plt.draw() #- draws the figure, visualization is shown here
        allCoord = []
        for i in range (5):
            
            plt.pause(1) #- pauses visualization for 2 seconds
            #- boundary of traffic
            data[:, 0, :] = N.array([0, 1, 0])
            data[0, :, :] = N.array([0, 1, 0])
            data[:, -1, :] = N.array([0, 1, 0])
            data[-1, :, :] = N.array([0, 1, 0])
            self.intersectionArray[0][0].moveCars()
            self.intersectionArray[0][1].moveCars()
            self.intersectionArray[1][0].moveCars()
            self.intersectionArray[1][1].moveCars()
            allCoord = self.intersectionArray[0][0].getAllCoord() + \
            self.intersectionArray[0][1].getAllCoord() + \
            self.intersectionArray[1][0].getAllCoord() + \
            self.intersectionArray[1][1].getAllCoord()
            for i in range(0, len(allCoord)):
                data[allCoord[i][0], allCoord[i][1], :] = N.array([0, 0, 1])
            img.set_data(data) #- changes drawing to add new colors
            plt.draw() #- draws the figure, visualization is shown here
            data = N.ones((length, width, 3), dtype='f')*0.8 #- array of shape 42, 42, 3, all values are 0.8

                
                
                
            
    """
    Calculates average time a spent within the traffic boundary
    for a single simulation run.
    """
    def getAverageTime(self):
        average = 0
        #- sums up all car times
        for i in range(0, len(self.timeWithinBoundary)):
            average = average + self.timeWithinBoundary[i]
        #- divides sum by number of cars that left boundary
        average = average /len(self.timeWithinBoundary) 
        return average
    
    
    """
    This method will run the traffic simulation nunerous times,
    each time changing the length of time the simulation runs.
    It will record the average time a car was within the simulation
    boundary for each simulation run, and plot these values on a line
    graph.
    """
 #   def plotAverage(self):
        
