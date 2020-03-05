# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:40:13 2020

@author: esher
"""

class Lane(object):
   
    def __init__(self,x=7, y=4,lLane,rLane,ftLane):
        self.x=x
        self.y=y
        self.carList=[]
        #leftLane
        self.lLane=lLane
        #rightLane
        self.rLane=rLane
        #lane to the front
        self.sLane=fLane
    
    
        
        
    def addCar(self,car):
        self.carList.append(car)
    
    def removeCar(self, car):
        
        self.carList.remove(car)
    
    def turnRight(self, car):
        car.x=car.x+1
        car.y=car.y+2
        rLane.addCar(car)
        self.removeCar(car)
    
    def turnLeft(self,car):
        car.x=car.x-2
        car.y=car.y-2
        lLane.addCar(car)
        self.removeCar(car)
    
    def goStraight(self,car):
        car.x=car.x+2
        
        
        
        
        
    def moveCar(self, car):
        if (light="red"):
            pass
        if(car.car_move=="right"):
            self.turnRight(car)
        elif( car.move=="left"):
            self.turnLeft(car)
        else:
            self.goStraight(car)
            
        #returns false if 
        bool False
        
        
    #cars that reach boundary 
        
        
        
