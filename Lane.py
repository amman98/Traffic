# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:40:13 2020
@author: esher
"""


import Car
class Lane(object):
   
    def __init__(self,lLane,rLane,fLane,direction,adjacentLane):
        self.x=x
        self.y=y
        self.carList=[]
        #leftLane
        self.lLane=lLane
        #rightLane
        self.rLane=rLane
        #lane to the front
        self.sLane=fLane
        # type of lane 
        self.direction=direction
        #to make a potential lane change
        self.adjLane=adjacentLane
    """
    this method sets the length of the green and red light
    
    
    
    """
    def setLight(self,gLight,rLight,yLight):
        self.gLight=gLight
        self.rLight=rLight
        self.yLight=yLight
        #light countdown
        self.c_downG=gLight
        self.c_downR=rLight
        
    """
     adding car to the list of cars in the lane  
    """
    def addCar(self,car):
        self.carList.append(car)
        
    #method to remove car after it leaves the lane
    def removeCar(self, car):  
        self.carList.remove(car)
        
        
    """
    this method moves the car right, the way it does it will depend on the 
    direction of the lane
    
    """
    def turnRight(self, car):
       
        if(self.direction=="North"):
            car.loc_in_environ[0] = car.loc_in_environ[0] - 1
            car.loc_in_environ[1] = car.loc_in_environ[1] + 1
        elif(self.direction=="South"):
            car.loc_in_environ[0] = car.loc_in_environ[0] + 1
            car.loc_in_environ[1] = car.loc_in_environ[1] - 1   
        elif(self.direction=="East"):
            car.loc_in_environ[0] = car.loc_in_environ[0] - 1
            car.loc_in_environ[1] = car.loc_in_environ[1] - 1     
        else :
            car.loc_in_environ[0] = car.loc_in_environ[0] + 1
            car.loc_in_environ[1] = car.loc_in_environ[1] + 1
            
            
        self.rLane.addCar(car)
        self.removeCar(car)
        
    """
    this method moves the car left, the way it does it will depend on the 
    direction of the lane
    
    """   
    
    
    """
    at each time step a car in the front will leave the lane
    and cars behind it will move one cell closer to the intersection
    
    """        
    def nextMove(self):
        if(self.c_downG>=0):
            self.c_downR=self.c_downR-1
        else:
            self.moveCar(self.carList[0])
            for i in self.carList:
                self.goStraight(i)
        
     
    """
    this makes new cars, for lanes 
    that go out to the boundary
    """
    def incomingCar(self,numCars):
        for i in range(numCars):
            j=Car(self,self.y,self.x)
            
            self.carList.append(j)
    '''
    method to change lane to an adjacent lane 
    from straight or right lane to a left turn lane
    '''
    def changeLane(self,car):
        #if checks the direction to determine weather to check the x or the y
        if (self.direction =="EAST" or self.direction=="WEST" ):
            car.y=car.y+1
        else:
            car.x=car.x+1
        self.adjLane.addCar(car)
        self.removeCar(car)
            
            
    
        
        
        
        
        
        
        
    #cars that reach boundary 
