# -*- coding: utf-8 -*-
"""
@author: James Pfleger
"""
probLeft = 0.4
probRight = 0.3

from StraightLane import StraightLane
from LeftLane import LeftLane
#from .rightlane import RightLane


class Intersection(object):
   
    def __init__(self, leftFirst = True, carLimit = 10, rightLane = False, NSleftLightDur = 15, EWleftLightDur = 15, NSgreenLightDur = 15, EWgreenLightDur = 15, leftTurnDiff = 5):
        #lists which will hold the left and right lane of  of the 4 directions
        self.northLanes = []
        self.eastLanes = []
        self.southLanes = []
        self.westLanes = []
        """
        initalize each lane and set its adjcents 
        """
        
        if leftFirst:
           #add right and left lanes for every direction
           self.northLanes.append(LeftLane('NORTH', probRight, probLeft, carLimit))
           self.northLanes.append(StraightLane("NORTH", carLimit))

           self.eastLanes.append(LeftLane("EAST", probRight, probLeft, carLimit))
           self.eastLanes.append(StraightLane("EAST", carLimit))

           self.southLanes.append(LeftLane("SOUTH", probRight, probLeft, carLimit))
           self.southLanes.append(StraightLane("SOUTH", carLimit))

           self.westLanes.append(LeftLane("WEST", probRight, probLeft, carLimit))
           self.westLanes.append(StraightLane("WEST", carLimit))

           #set values for light duration
           self.NSgreenLightDur = NSgreenLightDur
           self.NSleftLightDur = NSgreenLightDur - leftTurnDiff

           self.EWgreenLightDur = EWgreenLightDur
           self.EWleftLightDur = EWgreenLightDur - leftTurnDiff

           self.lightOrder = [NSleftLightDur, NSgreenLightDur, EWgreenLightDur, EWleftLightDur]
        else:
      #add right and left lanes for every direction
           self.northLanes.append(StraightLane("NORTH", carLimit))
           self.northLanes.append(LeftLane("NORTH", carLimit))
           
           self.eastLanes.append(StraightLane("EAST", carLimit))
           self.eastLanes.append(LeftLane("EAST", carLimit))
          
           self.southLanes.append(StraightLane("SOUTH", carLimit))
           self.southLanes.append(LeftLane("SOUTH", carLimit))
           
           self.westLanes.append(StraightLane("WEST", carLimit))
           self.westLanes.append(LeftLane("WEST", carLimit))

           #set values for light duration
           self.NSgreenLightDur = NSgreenLightDur
           self.NSleftLightDur = NSgreenLightDur - leftTurnDiff

           self.EWgreenLightDur = EWgreenLightDur
           self.EWleftLightDur = EWgreenLightDur - leftTurnDiff

           self.lightOrder = [NSgreenLightDur, NSleftLightDur, EWleftLightDur, EWgreenLightDur]
      
      
      
        """
        light is an integer for the number of timesteps 
        that onc cycle takes 
        its NSgreenLight, EWLightDur, and 2 times the left because there are 
        2 different types of left turns (NS left turns and EW left turns)
        """
        self.light=NSgreenLightDur+(NSleftLightDur*2)+EWgreenLightDur
        self.currentLightTime=0
        self.currentLightIndex = 0
             
      
        """
        This methods calls the moveCars method on all the lanes in the intersection
        
        The method detrmines which lanes have green lights and which have redlights
        this is detrmined by the light and currentLightTime
        greenLight by defualt is true
        """
        
        def moveCars(self):
            #when light time is greater than maximum light time - green light duration of north and south lanes 
            if self.currentLightTime <= self.lightOrder[self.currentLightIndex]:
               # NS Left Turn
               if self.currentLightIndex == 0:
                  self.northLanes[self.currentLightIndex % 2].moveCars()
                  self.southLanes[self.currentLightIndex % 2].moveCars()
               elif self.currentLightIndex == 1:
                  self.northLanes[self.currentLightIndex % 2].moveCars()
                  self.southLanes[self.currentLightIndex % 2].moveCars()
               elif self.currentLightIndex == 2:
                  self.eastLanes[self.currentLightIndex % 2].moveCars()
                  self.westLanes[self.currentLightIndex % 2].moveCars()
               else:
                  self.eastLanes[self.currentLightIndex % 2].moveCars()
                  self.westLanes[self.currentLightIndex % 2].moveCars()
               
               self.currentLightTime = self.currentLightTime + 1
               
               if self.currentLightTime > self.lightOrder[self.currentLightIndex]:
                  self.currentLightTime = 0
                  self.currentLightIndex = self.currentLightIndex + 1
               if self.currentLightIndex == 4:
                  self.currentLightIndex = 0
              
        def addCarsRandom(self):
            self.northLanes[0].addCarRandom()
            self.northLanes[1].addCarRandom()
            self.eastLanes[0].addCarRandom()
            self.eastLanes[1].addCarRandom()
            self.southLanes[0].addCarRandom()
            self.southLanes[1].addCarRandom()
            self.westLanes[0].addCarRandom()
            self.westLanes[1].addCarRandom()
            
        """
        Method returns a list of tuples representing the coordinates
        of each car that is in this intersection. Each lane calls its
        getCoord() method to return a list and then each list is concatenated
        to create a bigger list that is returned here.
        """
        def getAllCoord(self):
            location = []
            location = self.northLanes[0].getCoord() + self.northLanes[1].getCoord() + \
            self.eastLanes[0].getCoord() + self.eastLanes[1].getCoord() + \
            self.southLanes[0].getCoord() + self.southLanes[1].getCoord() + \
            self.westLanes[0].getCoord() + self.westLanes[1].getCoord()
            return location
            
            
