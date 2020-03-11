from Car import Car 
import numpy as np

class LeftLane(object):

    def __init__(self, direction, probRight, probLeft, carLimit = 10):
        
        self.carLimit = carLimit
        self.carCount = 0
        self.direction = direction
        self.carList = []
        self.probRight = probRight
        self.probLeft = probLeft
        self.nextLaneFwd = None
        self.nextLaneLeft = None  
    """
    Helper method for moveCars. After a car has left this lane,
    each car moves forward in traffic.
    """
    def updatePosition(self):
        for inCar in self.carList:
            inCar.timeToBorder = inCar.timeToBorder + 1
            if self.direction == 'NORTH':
                inCar.loc_in_environ[0] = inCar.loc_in_environ[0] - 1
            elif self.direction == 'EAST':
                inCar.loc_in_environ[1] = inCar.loc_in_environ[1] + 1
            elif self.direction == 'WEST':
                inCar.loc_in_environ[1] = inCar.loc_in_environ[1] - 1
            elif self.direction == 'SOUTH':
                inCar.loc_in_environ[0] = inCar.loc_in_environ[0] + 1    
    
    """
    Moves the car at front of lane. This method would be called at each time
    step in the model class. Once the car has turned left, all cars that were
    behind it move forward in traffic.
    """
    def moveCars(self):
        carLeft = False
        if self.carList.len() != 0:
            self.carList[0].timeToBorder = self.carList[0].timeToBorder + 1
            self.carList[0].chooseTurn(self.probRight, self.probLeft)
            if self.carList[0].car_turn == "LEFT":
                if self.nextLaneLeft.carList.len() != \
                            self.nextLaneLeft.carLimit:
                    #- update car's coordinates based on direction lane is facing
                    if self.direction == 'NORTH':
                        self.carList[0].loc_in_environ[0] = self.carList[0].loc_in_environ[0] - 1
                        self.carList[0].loc_in_environ[1] = self.carList[0].loc_in_environ[1] - 1
                    elif self.direction == 'EAST':
                        self.carList[0].loc_in_environ[0] = self.carList[0].loc_in_environ[0] - 1
                        self.carList[0].loc_in_environ[1] = self.carList[0].loc_in_environ[1] + 1
                    elif self.direction == 'WEST':
                        self.carList[0].loc_in_environ[0] = self.carList[0].loc_in_environ[0] + 1
                        self.carList[0].loc_in_environ[1] = self.carList[0].loc_in_environ[1] - 1
                    elif self.direction == 'SOUTH':
                        self.carList[0].loc_in_environ[0] = self.carList[0].loc_in_environ[0] + 1
                        self.carList[0].loc_in_environ[1] = self.carList[0].loc_in_environ[1] + 1

                    #- add car to left lane list
                    self.carList[0].environ = self.nextLaneLeft
                    self.nextLaneLeft.addCar(self.carList[0])
                    self.removeCar(self.carList[0])
                    self.carCount = self.carCount - 1
                    carLeft = True
                
        # car is going straight or right the next turn.
            else:
                if self.nextLaneFwd.carList.len() != \
                            self.nextLaneFwd.carLimit:
                #- update car's coordinates based on direction lane is facing
                    if self.direction == 'NORTH':
                        self.carList[0].loc_in_environ[0] = self.carList[0].loc_in_environ[0] - 1
                        self.carList[0].loc_in_environ[1] = self.carList[0].loc_in_environ[1] - 1
                    elif self.direction == 'EAST':
                        self.carList[0].loc_in_environ[0] = self.carList[0].loc_in_environ[0] - 1
                        self.carList[0].loc_in_environ[1] = self.carList[0].loc_in_environ[1] + 1
                    elif self.direction == 'WEST':
                        self.carList[0].loc_in_environ[0] = self.carList[0].loc_in_environ[0] + 1
                        self.carList[0].loc_in_environ[1] = self.carList[0].loc_in_environ[1] - 1
                    elif self.direction == 'SOUTH':
                        self.carList[0].loc_in_environ[0] = self.carList[0].loc_in_environ[0] + 1
                        self.carList[0].loc_in_environ[1] = self.carList[0].loc_in_environ[1] + 1

                    #- add car to left lane list
                    self.carList[0].environ = self.nextLaneFwd
                    self.nextLaneFwd.addCar(self.carList[0])
                    self.removeCar(self.carList[0])
                    self.carCount = self.carCount - 1
                    carLeft = True
                
        #- call helper method to move rest of traffic forward
        if carLeft:
            self.updatePosition(self)
        

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
                   
              






                
