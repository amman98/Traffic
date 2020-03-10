# -*- coding: utf-8 -*-
"""
@author: James Pfleger
"""


from .straightlane import StraightLane
from .leftlane import LeftLane
from .rightlane import RightLane


class Intersection(object):
   
    def __init__(self, rightLane = False, NSgreenLightDur = 15, leftLightDur = 10, EWLightDur = 15):
        #lists which will hold the left and right lane of  of the 4 directions
        self.northLanes = []
        self.eastLanes = []
        self.southLanes = []
        self.westLanes = []
        
        #add right and left lanes for every direction
        self.northLanes.append(LeftLane())
        self.northLanes.append(StraightLane())
        
        self.eastLanes.append(LeftLane())
        self.eastLanes.append(StraightLane())
        
        self.southLanes.append(LeftLane())
        self.southLanes.append(StraightLane())
        
        self.westLanes.append(LeftLane())
        self.westLanes.append(StraightLane())
        
        #set values for light duration
        self.NSgreenLightDur = NSgreenLightDur
        self.EWLightDur = EWLightDur
        self.leftLightDur=leftLightDur
        """
        light is an integer for the number of timesteps 
        that onc cycle takes 
        its NSgreenLight, EWLightDur, and 2 times the left because there are 
        2 different types of left turns (NS left turns and EW left turns)
        """
        self.light=NSgreenLightDur+(leftLightDur*2)+EWLightDur
        self.currentLightTime=0
        
        """
        This methods calls the moveCars method on all the lanes in the intersection
        
        The method detrmines which lanes have green lights and which have redlights
        this is detrmined by the light and currentLightTime
        greenLight by defualt is true
        """
        
        def moveCars(self):
            #when light time is greater than maximum light time - green light duration of north and south lanes 
            if(self.currentLightTime>self.light-self.NSgreenLightDur):
                #these lanes are going straight, North and South, have green light
                self.northLanes[1].moveCars()
                self.southLanes[1].moveCars()
                #these lanes turning left, from Norht and Suth, have a red light
                self.northLanes[0].moveCars(greenLight=False)
                self.southLanes[0].moveCars(greenLight=False)
                
                #all lanes from east and west have red light
                self.eastLanes.moveCars(greenLight=False)
                self.westLanes.moveCars(greenLight=False)
                
                #decrement the light time
                self.currentLightTime=self.currentLightTime-1
            #when current light time is between end of north south green light and east west light duration
            elif(self.currentLightTime>self.light-self.NSgreenLightDur-EWLightDur):
                #norht and south Lanes have red lights
                self.northLanes.moveCars(greenLight=False)
                self.southLanes.moveCars(greenLight=False)
                
                #lanes on east and west turning left have red lights
                self.eastLanes[0].moveCars(greenLight=False)
                self.westLanes[0].moveCars(greenLight=False)
                #lanes on east and west going straight have green lights
                self.eastLanes[1].moveCars(greenLight=True)
                self.westLanes[1].moveCars(greenLight=True) 
                
                #decrement current light by 1
                self.currentLightTime=self.currentLightTime-1
            #current light time between end of east west green light and duration of left lightDuration
            #for east and west Left turns 
            elif(self.currentLightTime>self.light-self.NSgreenLightDur-EWLightDur-leftLightDur):
                #all north and south lanes have red lights
                self.northLanes.moveCars(greenLight=False)
                self.southLanes.moveCars(greenLight=False)
                
                #lanes on east and west turning left has green light
                self.eastLanes[0].moveCars(greenLight=True)
                self.westLanes[0].moveCars(greenLight=True)
                
                #lanes on east and west going straight have red lights
                self.eastLanes[1].moveCars(greenLight=False)
                self.westLanes[1].moveCars(greenLight=False)
                
                #decrement current time by 1
                self.currentLightTime=self.currentLightTime-1
            #last light to turn green( left turns for norht and south lane)    
            else:
                #North and south lanes have red lights (going straight)
                self.northLanes[1].moveCars(greenLight=False)
                self.southLanes[1].moveCars(greenLight=False)
                
                #North and south Lanes turning left have green light
                self.northLanes[0].moveCars(greenLight=True)
                self.southLanes[0].moveCars(greenLight=True)
                #east and west lanes have red light
                self.eastLanes.moveCars(greenLight=False)
                self.westLanes.moveCars(greenLight=False)
                #decrement time by 1
                self.currentLightTime=self.currentLightTime-1
            #when current time hits 0 the current time resets to time so it can 
            #complete the cycle again
            if(self.currentLightTime<=0):
                self.currentLightTime=self.light
                
  
