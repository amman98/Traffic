# -*- coding: utf-8 -*-
"""

@author: James Pfleger
"""


from .straightlane import StraightLane
from .leftlane import LeftLane
from .rightlane import RightLane


class Intersection(object):
   
    def __init__(self, rightLane = False, greenLightDur = 15, leftLightDur = 10, redLightDur = 15):
        self.northBoundLanes = []
        self.eastBoundLanes = []
        self.southBoundLanes = []
        self.westBoundLanes = []
        
        self.northBoundLanes.append(LeftLane())
        self.northBoundLanes.append(StraightLane())
        
        self.eastBoundLanes.append(LeftLane())
        self.easthBoundLanes.append(StraightLane())
        
        self.southBoundLanes.append(LeftLane())
        self.southBoundLanes.append(StraightLane())
        
        self.westBoundLanes.append(LeftLane())
        self.westBoundLanes.append(StraightLane())
        
        self.greenLightDur = greenLightDur
        self.redLightDur = redLightDur
        self.leftLightDur - leftLightDur
        if rightLane:
            self.northBoundLanes.append(RightLane())    
            self.eastBoundLanes.append(RightLane())
            self.southBoundLanes.append(RightLane())    
            self.westBoundLanes.append(RightLane())



        def moveCars(direction):
            carsMoved = 0
            if direction == "NS":
                for lane in self.northBoundLanes:
                    carsMoved += lane.moveCars()
                for lane in self.southBoundLanes:
                    carsMoved += lane.moveCars()
            elif direction == "EW":
                for lane in self.eastBoundLanes:
                    carsMoved += lane.moveCars()
                for lane in self.westBoundLanes:
                    carsMoved += lane.moveCars()
            
            
            return carsMoved
