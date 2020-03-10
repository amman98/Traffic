# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:40:13 2020

@author: James Pfleger
"""

from .car import Car 
import numpy as np
class StraightLane(object):
   
    def __init__(self, carLimit = 10):
        self.carList=[]
        self.carArray = np.empty(carLimit, dtype = Car)
        self.nextLaneFwd = None
        self.nextLaneRight = None
        
        self.adjacentLeft = None
        self.adjacentRight = None
       
    def moveCars(self):
        for inCar in self.carList:
            if inCar.location == 0:
                if inCar.chooseTurn() == "STRAIGHT":
                    inCar.environ = self.nextLaneFwd
                    self.removeCar(self, inCar)
                else:
                    inCar.environ = self.nextLaneRight
                    self.removeCar(self, inCar)
            else:
                inCar.location = inCar.location - 1   
                
                
     #adding car to the list of cars in the lane   
    def addCar(self,car):
        self.carList.append(car)
    #method to remove car after it leaves the lane
    def removeCar(self, car):  
        self.carList.remove(car)
