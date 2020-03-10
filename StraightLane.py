# -*- coding: utf-8 -*-
"""
@author: James Pfleger

This class represents a lane on the right side of the road. 
Cars are able to either drive straight throught the intersection,
make a right turn, or merge into the left lane.
"""

from .car import Car 
import numpy as np
class StraightLane(object):
   
    def __init__(self, direction, carLimit = 10):
         """
         Creates an instance of the StraightLane class
         
         Attributes
         ----------
         carLimit:
            The amount of cars that are able to fit on the lane. If the lane is full
            then no more cars are able to enter the lane.
            
         carCount:
            The amount of cars that are currently in the lane. Used to check if the
            lane is full or not.
          
         direction:
            The direction the lane is facing, North, East, South, or West. Used for the
            visualization and knowing which way lanes the car will travel to when
            traveling through the intersection.
         
         carList:
            The list of cars that are in the lane currently. Used to iterate throught the
            cars in the lane each time step and have them either move thought the
            intersection to a new lane, move up in their lane position,

         """
        self.carLimit = carLimit
        self.carCount = 0
        self.direction = direction
        self.carList = []
        self.carArray = np.empty(carLimit, dtype = Car)
        self.nextLaneFwd = None
        self.nextLaneLeft = None
        
        self.adjacentLeft = None
       
    def moveCars(self, greenLight = True):
        if greenLight:
            for inCar in self.carList:
               if inCar.lanePosition == 0:
                   if inCar.choice == "STRAIGHT":
                       if nextLaneFwd.carCount < nextLaneFwd.carLimit
                           inCar.environ = self.nextLaneFwd
                           inCar.lanePosition = self.carLimit
                           inCar.chooseTurn()
                           self.removeCar(self, inCar)
                    else:
                        if nextLaneRight.carCount < nextLaneRight.carLimit
                           inCar.environ = self.nextLaneRight
                           inCar.lanePosition = self.carLimit
                           self.removeCar(self, inCar)
                       
                  else:
                     if inCar.choice == "LEFT":
                        spaceAvailable = True
                        for otherCars in self.adjacentLeft.carList:
                           if otherCars.lanePosition == inCar.lanePosition
                              spaceAvailable = False
                        if spaceAvaiable:      
                           inCar.environ = self.adjacentLeft
                           self.removeCar(self, inCar)
                     else:
                        spaceAvailable = True
                        for otherCars in self.carList:
                           if otherCars.lanePosition == inCar.lanePosition - 1:
                              spaceAvailable = False
                        if spaceAvailable:
                           inCar.lanePosition = inCar.lanePosition - 1
                
     #adding car to the list of cars in the lane   
    def addCar(self,car):
        self.carList.append(car)
    #method to remove car after it leaves the lane
    def removeCar(self, car):  
        self.carList.remove(car)
