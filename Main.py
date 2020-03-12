
from Model import Model


import numpy as np

def mainFunc():
    """
    probRight = np.arange(5)
    probLeft = np.arange(5)
    carSpawn = np.arange(1, .1)
    NSgreenLightDur = np.array([5, 10, 15])
    EWgreenLightDur = np.array([3, 6, 9, 12, 15])
    leftTurnDif = np.array([0, 2, 4, 6])
    for pR in probRight:
        m = Model(probRight = probRight)
    
    
    """   
    
    listOfCarLists = []
    
    m = Model()
    borderCars = m.runModel()

    carCount = len(borderCars)
    avg = 0
    for car in boarderCars:
        avg = avg + car.timeToBorder
    
    
    avg = avg / carCount
    print("carCount: ", carCount)
    
    print()
    print("Avg time alive: ", avg)
        
        
