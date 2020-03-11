class Model(object):
    
    #- Global Variables
    
    """
    probCar: float that determines probability of how many cars will be on road, 
    used to simulate how congested traffic can be at different times of
    day.
    """
    probCar = 0.60 
    
    """
    redLightLength: int representing seconds light stays red.
    """
    redLightLength = 15
    
    """
    greenLightLength: int representing seconds light stays
    green.
    """
    greenLightLength = 17
    
    """
    YELLOW_LIGHT_LENGTH: constant int representing length of time
    light stays yellow. Determined by research on average length
    of time light stays yellow and observation of Lake City Way traffic.
    """
    YELLOW_LIGHT_LENGTH = 4
    
    sim_length = 30 #- simulation length in minutes
    
    dt = 1/15 #- time step is 4 seconds, or 1/15 of a minute
    
    """
    Pre: Have a lane and car class created.
    
    Post: Creates lanes and places cars on each lane.
    Also decides which lanes are to the front, left, right
    and adjacent to each lane.
    """
    def __init__(self, ):
        
        border = boundaryLane()
        intersectionArray = np.array(2, 2, dtype = Intersection)
        intersectionArray[0][0] = Intersection()
        intersectionArray[0][1] = Intersection()
        intersectionArray[1][0] = Intersection()
        intersectionArray[1][1] = Intersection()
        
        # North Bound Lanes                     
        # left turn lane                   
        intersectionArray[0][0].northLanes[0].nextLaneFwd = border 
        intersectionArray[0][0].northLanes[0].nextLaneLeft = border 
        
        # straight lane                     
        intersectionArray[0][0].northLanes[1].nextLaneFwd = border 
        intersectionArray[0][0].northLanes[1].nextLaneFwdLeft = border 
        intersectionArray[0][0].northLanes[1].nextLaneRightFwd = border 
        intersectionArray[0][0].northLanes[1].nextLaneRightLeft = border 
        
        # East Bound Lanes                       
        # left turn lane
        intersectionArray[0][0].eastLanes[0].nextLaneFwd = border 
        intersectionArray[0][0].eastLanes[0].nextLaneLeft = border 
        
        # straight lane
        intersectionArray[0][0].eastLanes[1].nextLaneFwd = intersectionArray[0][1].eastLanes[1]
        intersectionArray[0][0].eastLanes[1].nextLaneFwdLeft = intersectionArray[0][1].eastLanes[0]
        intersectionArray[0][0].eastLanes[1].nextLaneRightFwd = intersectionArray[0][1].eastLanes[1]
        intersectionArray[0][0].eastLanes[1].nextLaneRightLeft = intersectionArray[0][1].eastLanes[0]
        
        # South Bound Lanes                       
        # left turn lane
        intersectionArray[0][0].southLanes[0].nextLaneFwd = intersectionArray[0][1].eastLanes[1] 
        intersectionArray[0][0].southLanes[0].nextLaneLeft = intersectionArray[0][1].eastLanes[0]
        
        # straight lane
        intersectionArray[0][0].southLanes[1].nextLaneFwd = intersectionArray[1][0].southLanes[1]
        intersectionArray[0][0].southLanes[1].nextLaneFwdLeft = intersectionArray[1][0].southLanes[0]
        intersectionArray[0][0].southLanes[1].nextLaneRightFwd = intersectionArray[1][0].southLanes[1]
        intersectionArray[0][0].southLanes[1].nextLaneRightLeft = intersectionArray[1][0].southLanes[0]

                             """
        create four intersection objects and make
        clear which ones are adjacent to which.
        
        have each intersection adjacent to the 
        boundary.
        """
        self.timeWithinBoundary = []
    
    
    """
    Pre: Have initialized each lane and car object.
    
    Post: Runs the model and plots visualization of the
    cars moving through traffic.
    """
    def runModel(self):
        
        for i in range (sim_length*15):
            
            for lane in laneArray:
                lane.nextMove()
                
        
      return None
    
    """
    Calculates average time a spent within the traffic boundary
    for a single simulation run.
    """
    def getAverageTime(self):
        average = 0
        #- sums up all car times
        for i in range(0, len(self.timeWithinBoundary)):
            average = average + self.timeWithinBoundary[i]
        #- divides sum by number of cars that left boundary
        average = average /len(self.timeWithinBoundary    
        return average
    
    """
    This method will run the traffic simulation nunerous times,
    each time changing the length of time the simulation runs.
    It will record the average time a car was within the simulation
    boundary for each simulation run, and plot these values on a line
    graph.
    """
    def plotAverage(self):
        
