# -*- coding: utf-8 -*-
"""
@author: James Pfleger

This class represents a lane on the right side of the road. 
Cars are able to either drive straight throught the intersection,
or make a right turn.
"""
import numpy as N
from Car import Car 
class StraightLane(object):
   
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
            intersection to a new lane or move up in their lane position.

         nextLaneFwd:
            A pointer the the next lane if the car travels forward to the next
                intersection
        
         nextLaneFwdLeft:
             A pointer to the next lane if the car travels forward and then
                wants to take a left turn next.
        
         nextLaneRight:
             A pointer to the next lane if the car travels right and then
                wants to travel forward.
        
         nextLaneRightLeft:
             A pointer to the next lane if the car travels right and then
                wants to take a left turn next.
         """
    nextLaneFwd = None
    nextLaneFwdLeft = None 
    nextLaneRightFwd = None           
    nextLaneRightLeft = None
    def __init__(self, direction, startingX, startingY, fromBound = True, probCarNS = .9, probCarEW = .2, probRight = .2, probLeft = .4, carLimit = 10, startingCarCount = startingCarCount):
        self.carLimit = carLimit
        self.carCount = 0
        self.direction = direction
        self.startingX = startingX
        self.startingY = startingY
        self.carList = []
        self.probRight = probRight
        self.probLeft = probLeft
        self.carProbNS = probCarNS
        self.carProbEW = probCarEW
        self.fromBound = fromBound
        
        for i in range(startingCarCount):
            self.carList.append(Car(self, 2, 4))
        
            
        self.carCount = startingCarCount
        self.nextLaneFwd = None
        self.nextLaneFwdLeft = None 
        self.nextLaneRightFwd = None           
        self.nextLaneRightLeft = None
       
    def moveCars(self):
        carLeft = False
        # check that the lane is not empty
        if len(self.carList) != 0:
             #- update car's coordinates based on direction lane is facing

             # car wants to go straight throught the intersection
             if self.carList[0].car_turn == "STRAIGHT":

                 # car wants to go straight or right in the next intersection
                 self.carList[0].chooseTurn(self.probRight, self.probLeft)
                 if self.carList[0].car_turn == "STRAIGHT" or \
                     self.carList[0].car_turn == "RIGHT":
                     if len(self.nextLaneFwd.carList) != \
                         self.nextLaneFwd.carLimit:
                         # car is traveling North
                         if self.direction == 'NORTH':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] - 1

                         # car is traveling East
                         elif self.direction == 'EAST':
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] + 1

                         # car is traveling West
                         elif self.direction == 'WEST':
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] - 1

                         # car is traveling South
                         elif self.direction == 'SOUTH':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] + 1

                         # adding the car to the new lane
                         self.carList[0].environ = self.nextLaneFwd
                         self.carList[0].timeToBoundary = self.carList[0].timeToBoundary  + 1

                         self.nextLaneFwd.addCar(self.carList[0])
                         self.removeCar(self.carList[0])
                         self.carCount = self.carCount - 1
                         carLeft = True

                 # car wants to turn left at next intersection
                 # car will enter the left lane immediatly   
                 else:
                     # checking for room in the left lane
                     if len(self.nextLaneFwdLeft.carList) != \
                         self.nextLandFwdLeft.carLimit:
                         # car is traveling North
                         if self.direction == 'NORTH':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] - 1

                         # car is traveling East
                         elif self.direction == 'EAST':
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] + 1

                         # car is traveling West
                         elif self.direction == 'WEST':
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] - 1

                         # car is traveling South
                         elif self.direction == 'SOUTH':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] + 1

                         # adding the car to the new lane
                         self.carList[0].environ = self.nextLaneFwdLeft
                         self.carList[0].timeToBoundary = self.carList[0].timeToBoundary + 1
                         self.nextLaneFwdLeft.addCar(self.carList[0])
                         self.removeCar(self.carList[0])
                         self.carCount = self.carCount - 1
                         carLeft = True

             # car is turning right
             else:

                 # need to decide next movement to know which lane to enter
                 self.carList[0].chooseTurn(self.probRight, self.probLeft )
                 if self.carList[0].car_turn == "STRAIGHT" or \
                     self.carList[0].car_turn == "RIGHT":
                     if len(self.nextLaneRightFwd.carList) != \
                         self.nextLaneRightFwd.carLimit:
                         # car is traveling North
                         if self.direction == 'NORTH':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] - 1
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] + 1

                         # car is traveling East
                         elif self.direction == 'EAST':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] + 1
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] + 1

                         # car is traveling West
                         elif self.direction == 'WEST':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] - 1
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] - 1

                         # car is traveling South
                         elif self.direction == 'SOUTH':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] + 1
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] + 1

                         # adding the car to the new lane
                         self.carList[0].environ = self.nextLaneRightFwd
                         self.carList[0].timeToBoundary = self.carList[0].timeToBoundary  + 1
                         self.nextLaneRightFwd.addCar(self.carList[0])
                         self.removeCar(self.carList[0])
                         self.carCount = self.carCount - 1
                         carLeft = True

                 # car wants to turn left at next intersection
                 # car will enter the left lane immediatly   
                 else:
                     # checking for room in the left lane
                     if len(self.nextLaneRightLeft.carList) != \
                         self.nextLandRightLeft.carLimit:
                         # car is traveling North
                         if self.direction == 'NORTH':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] - 1
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] + 1

                         # car is traveling East
                         elif self.direction == 'EAST':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] + 1
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] + 1

                         # car is traveling West
                         elif self.direction == 'WEST':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] - 1
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] - 1

                         # car is traveling South
                         elif self.direction == 'SOUTH':
                             self.carList[0].loc_in_environ[0] = \
                                 self.carList[0].loc_in_environ[0] + 1
                             self.carList[0].loc_in_environ[1] = \
                                 self.carList[0].loc_in_environ[1] + 1

                         # adding the car to the new lane
                         self.carList[0].environ = self.nextLaneRightLeft
                         self.carList[0].timeToBoundary = self.carList[0].timeToBoundary + 1
                         self.nextLaneRightLeft.addCar(self.carList[0])
                         self.removeCar(self.carList[0])
                         self.carCount = self.carCount - 1
                         carLeft = True


        #- call helper method to move rest of traffic forward if a car left
        # the lane
        if carLeft:
            self.updatePosition()
             
    def updatePosition(self):
        """
        Helper method that moves all the cars in the lane up one position
            forward depending on the facing of the lane.
        """
        for inCar in self.carList:
            inCar.timeToBoundary = inCar.timeToBoundary + 1
            if self.direction == 'NORTH':
                inCar.loc_in_environ[0] = inCar.loc_in_environ[0] - 1
            elif self.direction == 'EAST':
                inCar.loc_in_environ[1] = inCar.loc_in_environ[1] + 1
            elif self.direction == 'WEST':
                inCar.loc_in_environ[1] = inCar.loc_in_environ[1] - 1
            elif self.direction == 'SOUTH':
                inCar.loc_in_environ[0] = inCar.loc_in_environ[0] + 1              
                
    def addCarRandom(self):
      if fromBound:
          addMoreCars = True
          while self.carCount < self.carLimit and addMoreCars:
             a= N.random.uniform()      
             if self.direction == "NORTH" or self.direction == "SOUTH":
                addMoreCars = a <= self.carProbNS
             else:
                addMoreCars = a <= self.carProbEW
             if addMoreCars:
                if self.direction == "NORTH":
                   theNewCar = Car(self, ( self.carList[-1].loc_in_environ[1] + 1 ), (self.carList[-1].loc_in_environ[0]))
                   theNewCar.chooseTurn(self.probRight, self.probLeft)
                   self.addCar(theNewCar)           
                elif self.direction == "EAST":
                   theNewCar = Car(self, ( self.carList[-1].loc_in_environ[1] ), (self.carList[-1].loc_in_environ[0] - 1 ))
                   theNewCar.chooseTurn(self.probRight, self.probLeft)
                   self.addCar(theNewCar)
                elif self.direction == "SOUTH":
                   theNewCar = Car(self, ( self.carList[-1].loc_in_environ[1] - 1 ), (self.carList[-1].loc_in_environ[0] ) )
                   theNewCar.chooseTurn(self.probRight, self.probLeft)
                   self.addCar(theNewCar)
                else:
                   theNewCar = Car(self, ( self.carList[-1].loc_in_environ[1] ), (self.carList[-1].loc_in_environ[0] + 1 ) )
                   theNewCar.chooseTurn(self.probRight, self.probLeft)
                   self.addCar(theNewCar)
      
      
     #adding car to the list of cars in the lane   
    def addCar(self,car):
        self.carList.append(car)
        self.carCount = self.carCount + 1
    #method to remove car after it leaves the lane
    def removeCar(self, car):  
        self.carList.remove(car)
        self.carCount = self.carCount - 1 
    
    """
    This method returns a list of tuples that
    represent the coordinates of each car on this lane.
    This list will be used in the Model class to aid in
    visualizing each car's location.
    """    
    def getCoord(self):
        location = []
        for inCar in self.carList:
            carLocation = (inCar.loc_in_environ[0], inCar.loc_in_environ[1])
            location.append(carLocation)
        return location
         
