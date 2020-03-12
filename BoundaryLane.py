from Car import Car

"""
BoundaryLane class represents the edges of our simulation
boundary. Every Intersection object that is at the edge of the 
simulation would have a pointer to this class coming from some
direction. A car reaching this class will represent that car
having left the simulation. At this point, we would want to 
store the amount of time the car spent in the simulation, so we
can average these values for analysis in the Model class.
"""
class BoundaryLane(object):
   
    def __init__(self):
        #- list of floats, holds time taken for each car to reach boundary
        self.carTime = []
        self.carList = []
        self.carCount = 0
        self.carLimit = 1000000000000
        
    """
    When a car reaches the boundary of the simulation,
    we record its time spent within the boundary in our list.
    """
    def timeToReachBoundary(self, vehicle):
        self.carTime.append(vehicle.getTimeToBoundary(vehicle))
        
    def addCar(self,car):
        self.carList.append(car)
        self.carCount = self.carCount + 1
    #method to remove car after it leaves the lane
    def removeCar(self, car):  
        self.carList.remove(car)
        self.carCount = self.carCount - 1 
