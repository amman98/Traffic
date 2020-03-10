from Car import Car 
import numpy as np

class LeftLane(Lane):
    
    def __init__(self, carLimit , direction, leftLane):
        self.carList=[]
        self.carArray = np.empty(carLimit, dtype = Car)
        self.nextLaneLeft = leftLane
        """
        self.nextLaneRight = None
        
        self.adjacentLeft = None #- doesn't have adjacent left
        self.adjacentRight = None
        """
        self.direction = self.direction
        
    """
    Helper method for moveCars. After a car has left this lane,
    each car moves forward in traffic.
    """
    def updatePosition(self):
        for inCar in self.carList:
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
        self.removeCar(self, self.carList[0])
        self.nextLaneLeft.addCar(nextLaneLeft, self.carList[0])
        #- call helper method to move rest of traffic forward
        self.updatePosition(self)
        

                
