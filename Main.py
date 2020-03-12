
from Model import Model


import numpy as np
import matPlotlib.pyplot as plt
#def mainFunc():

probTurn = [(.2, .4), (.4, .6), (.6, .8), (.8, 1), (.2, .6), (.2, .8), (.2, 1), (.1, .2)]
carSpawn = [(.1, .9), (.2, .8), (.3, .7), (.4, .6), (.5, .5)]
greenLightDur = [(15, 10), (12, 8), (9, 6), (6, 4), (3, 2)]
leftLightDur = [(10, 8), (8, 6), (6, 4), (4, 2), (2, 1)]
startingCarCount = [10, 8, 6, 4, 2, 0] 

default = []
changeTurnProb = []
changeCarSpawn = []
changeGreenLight = []
changeLeftLight = []
changeStartingCars = []

defaultAvg = []
changeTurnProbAvg = []
changeCarSpawnAvg = []
changeGreenLightAvg = []
changeLeftLightAvg = []
changeStartingCarsAvg = []
avgD = 0
carD = 0
avgC = 0
carC = 0
avgT = 0
carT = 0
avgG = 0
carG = 0
avgL = 0
carL = 0
avgS = 0
carS = 0



avg2 = 0
carCount2 = 0
for i in range(1000)
    m = Model()
    borderCars = m.runModel())
    carCount = len(borderCars)
    avg = 0
    for car in borderCars:
        avg = avg + car.timeToBoundary
        avg = avg / carCount
    default.append((carCount, avg))
    avgT = avgT + default[i][0]
    carT = carT + default[i][1]
defaultAvg.append((avgT / 1000, carT / 1000)) 

for turn in probTurn:
    for i int range(1000)
        m = Model(probLeft = probTurn[1], probRight = probTurn[0])
        borderCars = m.runModel())
        carCount = len(borderCars)
        avg = 0
        for car in borderCars:
            avg = avg + car.timeToBoundary
            avg = avg / carCount
        changeTurnProb.append((carCount, avg))
        avgT = avgT + changeTurnProb[i][0]
        carT = carT + changeTurnProb[i][1]
    changeTurnProbAvg.append((avgT / 1000, carT / 1000))   

    
avgT = 0
carT = 0
for spawn in carSpawns:
    m = Model(probCarNS = spawn[1], probCarEW = spawn[0])
    borderCars = m.runModel())
        carCount = len(borderCars)
        avg = 0
        for car in borderCars:
            avg = avg + car.timeToBoundary
            avg = avg / carCount
        changeCarSpawn.append((carCount, avg))
        avgT = avgT + changeCarSpawn[i][0]
        carT = carT + changeCarSpawn[i][1]
    changeCarSpawnAvg.append((avgT / 1000, carT / 1000))  
     
avgT = 0
carT = 0
for green in greenLightDur:
    m = Model(NSgreenLightDur = green[0], EWgreenLightDur = green[1])
    borderCars = m.runModel())
        carCount = len(borderCars)
        avg = 0
        for car in borderCars:
            avg = avg + car.timeToBoundary
            avg = avg / carCount
        changeGreenLight.append((carCount, avg))
        avgT = avgT + changeGreenLight[i][0]
        carT = carT + changeGreenLight[i][1]
    changeGreenLightAvg.append((avgT / 1000, carT / 1000)) 
    
avgT = 0
carT = 0 
for left in leftLightDur:
    m = Model(NSleftLightDur = left[0], EWleftLightDur = left[1])
    borderCars = m.runModel())
        carCount = len(borderCars)
        avg = 0
        for car in borderCars:
            avg = avg + car.timeToBoundary
            avg = avg / carCount
        changeLeftLight.append((carCount, avg))
        avgT = avgT + changeLeftLight[i][0]
        carT = carT + changeLeftLight[i][1]
    changeLeftLightAvg.append((avgT / 1000, carT / 1000)) 
    
avgT = 0
carT = 0        
for start in startingCarCount:
    m = Model(startingCarCount = start)
    borderCars = m.runModel())
        carCount = len(borderCars)
        avg = 0
        for car in borderCars:
            avg = avg + car.timeToBoundary
            avg = avg / carCount
        changeStartingCars.append((carCount, avg))
        avgT = avgT + changeStartingCars[i][0]
        carT = carT + changeStartingCars[i][1]
    changeStartingCarsAvg.append((avgT / 1000, carT / 1000)) 

    
    defaultAvg = []
changeTurnProbAvg = []
changeCarSpawnAvg = []
changeGreenLightAvg = []
changeLeftLightAvg = []
changeStartingCarsAvg = []
print("defaultAvg: ", defaultAvg)
print("changeTurn: ", changeTurnProbAvg)
print("spawn: ", changeCarSpawnAvg)
print("green: ", changeGreenLightAvg)
print("left: ", changeLeftLightAvg)
print("start: ", changeStartingCarsAvg)



    
