# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:40:13 2020

@author: esher
"""

class Lane(object):
   
    def __init__(self,x=7, y=4,lLane,rLane,ftLane,direction):
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
        
     #adding car to the list of cars in the lane   
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
            car.y=car.y+1
            car.x=car.x+1
        elif(self.direction=="South"):
            car.y=car.y-1
            car.x=car.x-1
            
        elif(self.direction=="East"):
            car.x=car.x+1
            car.y=car.y-1
        else :
            car.x=car.x-1
            car.y=car.y+1
            
            
        self.rLane.addCar(car)
        self.removeCar(car)
        
    """
    this method moves the car left, the way it does it will depend on the 
    direction of the lane
    
    """   
    
    def turnLeft(self,car):
        
        if(self.direction=="North"):
            car.y=car.y+2
            car.x=car.x-1
        elif(self.direction=="South"):
            car.y=car.y-2
            car.x=car.x+1
            
        elif(self.direction=="East"):
            car.x=car.x+2
            car.y=car.y+1
        else :
            car.x=car.x-2
            car.y=car.y-1
        
        self.lLane.addCar(car)
        self.removeCar(car)
    
        
    # continues to go straight on its lane
    def goStraight(self,car):
        if(self.direction=="North"):
            car.y=car.y+1
        elif(self.direction=="South"):
            car.y=car.y-1
        elif(self.direction=="East"):
            car.x=car.x+1
        else :
            car.x=car.x-1
    """
    at each time step a car in the front will leave the lane
    and cars behind it will move one cell closer to the intersection
    
    """        
    def nextMove(self):
        if(self.c_downG>=0):
            c_downR=c_downR-1
        else:
            self.moveCar(self.carList[0])
            for i in self.carList:
                self.goStraight(i)
    """
    this method call a turn based on the direction the car 
    wants to go, its assumed that the car is first in the lane 

    """    
        
    def moveCar(self, car):
        if(car.car_move=="RIGHT"):
            self.turnRight(car)
        elif( car.move=="LEFT"):
            self.turnLeft(car)
        else:
            self.goStraight(car)
            
        
        
        
    #cars that reach boundary 
        
