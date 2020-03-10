import numpy as np
import random

class Car(object):
    
    """
    Pre: Have attributes loc_in_environ
    and environ for the Car class.
    
    Post: Initializes car's location on the
    road and which lane(environ) it's on.
    
    lane: environ object to represent
    which lane the car is on.
    
    location: 1D array of size 2 to 
    represent the coordinates of the car.
    timeToBoundary: number of time steps
    it takes for a car to reach a boundary
    """
    def __init__(self, lane, location):
       self.environ = lane
       self.loc_in_environ = location
       self.timeToBoundary=0
    
    """
    Pre: Car's loc_in_environ and environ attributes
    have been initialized.
    
    Post: Car makes decision on which direction it will turn.
    
    probRight: float representing the percent
    chance the car wants to turn right.
    
    probLeft: float representing the percent
    chance the car wants to turn left.
    """
    def chooseTurn(self, probRight, probLeft):
        probTurn = random.uniform()
        if probTurn <= probLeft:
            self.car_turn = 'LEFT'
        elif probTurn <= probRight:
            self.car_turn = 'RIGHT'
            
        self.car_turn = 'STRAIGHT'
        
    """
    accessor method for the instance variable
    timeToBoundary. When car leaves boundary,
    Model class will add this value to list
    of car times within boundary.
    """
    def getTimeToBoundary(self):
        return self.timeToBoundary
