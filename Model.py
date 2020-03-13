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
    length = 50
    width = 42
    data = N.ones((length, width, 3), dtype='f')*0.8 #- array of shape 42, 42, 3, all values are 0.8

    """
    probCar: float that determines probability of how many cars will be on road, 
    used to simulate how congested traffic can be at different times of
    day.
    """
    probCar2 = 0.60 
    
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
    def __init__(self, iter = 1000, probCarNS = .9, probCarEW = .4, probLeft = .4, probRight = .2,\
        carLimit = 10, NSleftLightDur = 4, EWleftLightDur = 2, NSgreenLightDur = 10, \
        EWgreenLightDur = 8, startingCarCount = 5):

        self.border = BoundaryLane()
        self.intersectionArray = N.array((\
        [Intersection(probCarNS = probCarNS, probCarEW = probCarEW, probLeft = probLeft, probRight = probRight,\
        carLimit = carLimit, NSleftLightDur = NSleftLightDur, EWleftLightDur = EWleftLightDur, NSgreenLightDur = NSgreenLightDur, \
        EWgreenLightDur = EWgreenLightDur, startingCarCount = startingCarCount,int_number=0,x=14,y=15),\
        
        Intersection(probCarNS = probCarNS, probCarEW = probCarEW, probLeft = probLeft, probRight = probRight,\
        carLimit = carLimit, NSleftLightDur = NSleftLightDur, EWleftLightDur = EWleftLightDur, NSgreenLightDur = NSgreenLightDur, \
        EWgreenLightDur = EWgreenLightDur, startingCarCount = startingCarCount,int_number=1,x=14,y=27)],\
        
        [Intersection(probCarNS = probCarNS, probCarEW = probCarEW, probLeft = probLeft, probRight = probRight,\
        carLimit = carLimit, NSleftLightDur = NSleftLightDur, EWleftLightDur = EWleftLightDur, NSgreenLightDur = NSgreenLightDur, \
        EWgreenLightDur = EWgreenLightDur, startingCarCount = startingCarCount,int_number=2,x=36,y=15),\
        
        Intersection(probCarNS = probCarNS, probCarEW = probCarEW, probLeft = probLeft, probRight = probRight,\
        carLimit = carLimit, NSleftLightDur = NSleftLightDur, EWleftLightDur = EWleftLightDur, NSgreenLightDur = NSgreenLightDur, \
        EWgreenLightDur = EWgreenLightDur, startingCarCount = startingCarCount,int_number=3,x=36,y=27)]))

        #self.intersectionArray[0][0] = Intersection()
        #self.intersectionArray[0][1] = Intersection()
        #self.intersectionArray[1][0] = Intersection()
        #self.intersectionArray[1][1] = Intersection()
        
        #intersection top left
        self.intersectionArray[0,0].setAdjacents([self.border,self.border,self.intersectionArray[1,0].southLanes[1]\
                                                 ,self.intersectionArray[1,0].southLanes[0],\
                                                 self.intersectionArray[0,1].eastLanes[1],\
                                                 self.intersectionArray[0,1].eastLanes[0],self.border,self.border])
        #intersection top right
        self.intersectionArray[0,1].setAdjacents([self.border,self.border,self.intersectionArray[1,1].southLanes[1],\
                                                 self.intersectionArray[1,1].southLanes[0],self.border,self.border,\
                                                 self.intersectionArray[0,0].westLanes[1],\
                                                 self.intersectionArray[0,0].westLanes[1]])
        #intersection bottom left
        self.intersectionArray[1,0].setAdjacents([self.intersectionArray[0,0].northLanes[1]\
                                                 ,self.intersectionArray[0,0].northLanes[1],self.border,\
                                                 self.border,self.intersectionArray[1,1].eastLanes[1],\
                                                 self.intersectionArray[1,1].eastLanes[0],self.border,self.border])
        #intersection bottom right 
        self.intersectionArray[1,1].setAdjacents([self.intersectionArray[0,1].northLanes[1],\
                                                 self.intersectionArray[0,1].northLanes[0],self.border,\
                                                 self.border,self.border,self.border,self.intersectionArray[1,0].westLanes[1],\
                                                 self.intersectionArray[1,0].westLanes[1]])
        
        """
        create four intersection objects and make
        clear which ones are adjacent to which.
        
        have each intersection adjacent to the 
        boundary.
        """
        self.timeWithinBoundary = []

    
    def visualizeIntersection(self, row, col):
        #- draw lanes and intersections here
        #- boundary of traffic
        self.data[:, 0, :] = N.array([0, 1, 0])
        self.data[0, :, :] = N.array([0, 1, 0])
        self.data[:, -1, :] = N.array([0, 1, 0])
        self.data[-1, :, :] = N.array([0, 1, 0])
        # backwards L (half of lane)
        self.data[2+row: 12+row, 7+col, :] = N.array([1, 0, 0]) # 1
        self.data[11+row, 2+col:7+col, :] = N.array([1, 0, 0]) # 2
        
        # forwards L (half of lane)
        self.data[2+row: 12+row, 12+col, :] = N.array([1, 0, 0]) # 3
        self.data[11+row, 12+col:17+col, :] = N.array([1, 0, 0]) # 4
        
        # reflected forwards L
        self.data[17+row: 27+row, 12+col, :] = N.array([1, 0, 0]) # 5
        self.data[17+row, 12+col:17+col, :] = N.array([1, 0, 0]) # 6
        
        #reflected backwards L
        self.data[17+row: 27+row, 7+col, :] = N.array([1, 0, 0]) # 7
        self.data[17+row, 2+col:7+col, :] = N.array([1, 0, 0]) # 8

    
    """
    Pre: Have initialized each lane and car object.
    
    Post: Runs the model and plots visualization of the
    cars moving through traffic.
    """
    def runModel(self, vis = False):
        if vis:

            #- Create figure and axes:

            fig = plt.figure(figsize=(15,15)) #- sets window size to 5 x 5, returns a figure
            #ax = fig.add_axes( (0.0, 0.0, 1.0, 1.0), frameon=False )
            ax = fig.add_axes( (0.2, 0.2, 0.6, 0.6), frameon=False ) #- size of rectangle (left-right, up-down, width, height), returns axes?

            self.visualizeIntersection(0, 5) #- top-left
            self.visualizeIntersection(0, 17) #- top-right
            self.visualizeIntersection(22, 5) #- bottom-left
            self.visualizeIntersection(22, 17) #- bottom-right


            img = ax.imshow(data, interpolation='none',
                    extent=[0, width, 0, length],
                    aspect="auto",
                    zorder=0) #- 5 parameters
            ax.axis('off') #- Turns off axis labels
            plt.draw() #- draws the figure, visualization is shown here
            allCoord = []
            for i in range (50):

                plt.pause(1) #- pauses visualization for 2 seconds
                #- boundary of traffic
                self.data[:, 0, :] = N.array([0, 1, 0])
                self.data[0, :, :] = N.array([0, 1, 0])
                self.data[:, -1, :] = N.array([0, 1, 0])
                self.data[-1, :, :] = N.array([0, 1, 0])
                self.visualizeIntersection(0, 5)
                self.visualizeIntersection(0, 17)
                self.visualizeIntersection(22, 5)
                self.visualizeIntersection(22, 17)
                self.intersectionArray[0][0].moveCars()
                self.intersectionArray[0][1].moveCars()
                self.intersectionArray[1][0].moveCars()
                self.intersectionArray[1][1].moveCars()

                self.intersectionArray[0][0].addCarsRandom()
                self.intersectionArray[0][1].addCarsRandom()
                self.intersectionArray[1][0].addCarsRandom()
                self.intersectionArray[0][1].addCarsRandom()

                allCoord = self.intersectionArray[0][0].getAllCoord() + \
                self.intersectionArray[0][1].getAllCoord() + \
                self.intersectionArray[1][0].getAllCoord() + \
                self.intersectionArray[1][1].getAllCoord()
                for i in range(0, len(allCoord)):
                    self.data[allCoord[i][0], allCoord[i][1], :] = N.array([0, 0, 1])
                img.set_data(self.data) #- changes drawing to add new colors
                plt.draw() #- draws the figure, visualization is shown here
                self.data = N.ones((self.length, self.width, 3), dtype='f')*0.8 #- array of shape 42, 42, 3, all values are 0.8

        else:
            
            for i in range(1800):
                self.intersectionArray[0][0].moveCars()
                self.intersectionArray[0][1].moveCars()
                self.intersectionArray[1][0].moveCars()
                self.intersectionArray[1][1].moveCars()
    
                self.intersectionArray[0][0].addCarsRandom()
                self.intersectionArray[0][1].addCarsRandom()
                self.intersectionArray[1][0].addCarsRandom()
                self.intersectionArray[0][1].addCarsRandom()
        return self.border.carList
            
                
                
            
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
        
