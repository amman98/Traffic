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
   
    def __init__(self, leftFirst = True, probCarNS = .9, probCarEW = .2, probLeft = .2, probRight = .4,\
        carLimit = 15, NSleftLightDur = 5, EWleftLightDur = 2, NSgreenLightDur = 8, \
        EWgreenLightDur = 4, startingCarCount = 5, int_number=0,x=0,y=0):
    
    
        """
        probRightNS = .2, probRightEW = .4,\
        probLeftNS = .2, probLeftEW = .4, 
        """
        """probRight = .2, probLeft = .4, carLimit = 10, \
        NSleftLightDur = 15, EWleftLightDur = 15, NSgreenLightDur = 15, EWgreenLightDur = 15):"""
    
    
    
        #lists which will hold the left and right lane of  of the 4 directions
        self.northLanes = []
        self.eastLanes = []
        self.southLanes = []
        self.westLanes = []
        self.int_number=0
        self.x=x
        self.y=y
        self.probCarNS=probCarNS
        self.probCarEW=probCarEW
        """
        initalize each lane and set its adjcents 
        """
        self.northLanes.append(LeftLane('NORTH',startingX=self.x+2,startingY=self.y+3,probCarNS=self.probCarNS,probCarEW=self.probCarEW,probRight=self.probRight,probLeft=self.probLeft))
        self.northLanes.append(StraightLane("NORTH",startingX=self.x+1,startingY=self.y+3,probCarNS=self.probCarNS,probCarEW=self.probCarEW,probRight=self.probRight,probLeft=self.probLeft))

        self.eastLanes.append(LeftLane("EAST",startingX=self.x-3,startingY=self.y+1,probCarNS=self.probCarNS,probCarEW=self.probCarEW,probRight=self.probRight,probLeft=self.probLeft))
        self.eastLanes.append(StraightLane("EAST",startingX=self.x-3,startingY=self.y+2,probCarNS=self.probCarNS,probCarEW=self.probCarEW,probRight=self.probRight,probLeft=self.probLeft))

        self.southLanes.append(LeftLane("SOUTH",startingX=self.x+2,startingY=self.y-2,probCarNS=self.probCarNS,probCarEW=self.probCarEW,probRight=self.probRight,probLeft=self.probLeft))
        self.southLanes.append(StraightLane("SOUTH",startingX=self.x+1,startingY=self.y-2,probCarNS=self.probCarNS,probCarEW=self.probCarEW,probRight=self.probRight,probLeft=self.probLeft))
            
        self.westLanes.append(LeftLane("WEST",startingX=self.x+3,startingY=self.y-1,probCarNS=self.probCarNS,probCarEW=self.probCarEW,probRight=self.probRight,probLeft=self.probLeft))
        self.westLanes.append(StraightLane("WEST",startingX=self.x+3,startingY=self.y-2,probCarNS=self.probCarNS,probCarEW=self.probCarEW,probRight=self.probRight,probLeft=self.probLeft))
        
      
      
      
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
    """
    this method determines which lanes
    are boundary lanes            
    """
    def addCarsRandom(self):
        if(self.int_number==0):
          
            self.eastLanes[0].addCarRandom()
            self.eastLanes[1].addCarRandom()
            self.southLanes[0].addCarRandom()
            self.southLanes[1].addCarRandom()          
        
        elif(self.int_number==1):
            
            self.southLanes[0].addCarRandom()
            self.southLanes[1].addCarRandom()
            self.westLanes[0].addCarRandom()
            self.westLanes[1].addCarRandom()
        elif(self.int_number==2):
            self.northLanes[0].addCarRandom()
            self.northLanes[1].addCarRandom()
            self.eastLanes[0].addCarRandom()
            self.eastLanes[1].addCarRandom()
            
        else:
            self.northLanes[0].addCarRandom()
            self.northLanes[1].addCarRandom()
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
        
    """
    this method is called by the model to set the
    adjacent lanes of lanes.
    outBoundsLanes are lanes tha belong to other intersections
    they are also the lanes that the cars will go to after they leave 
    the current intersection
    """
    def setAdjacents(self, outBoundLanes):
        
        """
        NORTH
        """
        #facing North turning left
        self.northLanes[0].nextLaneFwd=outBoundLanes[6]
        self.northLanes[0].nextLaneLeft=outBoundLanes[7]
        #facing North going straight
        self.northLanes[1].nextLaneFwd=outBoundLanes[0]
        self.northLanes[1].nextLaneFwdLeft=outBoundLanes[1]
        #facing North turning right
        self.northLanes[1].nextLaneRightFwd=outBoundLanes[4]
        self.northLanes[1].nextLaneRightLeft=outBoundLanes[5]
        
        """
        SOUTH
        """
        #facing south turning left
        self.southLanes[0].nextLaneFwd=outBoundLanes[4]
        self.southLanes[0].nextLaneLeft=outBoundLanes[5]
        #facing south going straight
        self.southLanes[1].nextLaneFwd=outBoundLanes[2]
        self.southLanes[1].nextLaneLeft=outBoundLanes[3]
        #facing south turning right
        self.southLanes[1].nextLaneRightFwd=outBoundLanes[6]
        self.southLanes[1].nextLaneRightLeft=outBoundLanes[7]
        """
        EAST
        """
        #facing east turning left
        self.eastLanes[0].nextLaneFwd=outBoundLanes[0]
        self.eastLanes[0].nextLaneLeft=outBoundLanes[1]
        #facing east going straight
        self.eastLanes[1].nextLaneFwd=outBoundLanes[4]
        self.eastLanes[1].nextLaneLeft=outBoundLanes[5]
        #facing east turning right
        self.eastLanes[1].nextLaneRightFwd=outBoundLanes[2]
        self.eastLanes[1].nextLaneRightLeft=outBoundLanes[3]
        
        """
        WEST
        """
        
        #facing west turning left
        self.westLanes[0].nextLaneFwd=outBoundLanes[2]
        self.westLanes[0].nextLaneLeft=outBoundLanes[3]
        #facing west going straight
        self.westLanes[1].nextLaneFwd=outBoundLanes[6]
        self.westLanes[1].nextLaneLeft=outBoundLanes[7]
        #facing west turning right
        self.westLanes[1].nextLaneRightFwd=outBoundLanes[0]
        self.westLanes[1].nextLaneRightLeft=outBoundLanes[1]
        
           
            
            
