#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#Ant.py
import random
from RouteMap import Location, Neighbour

class Ant():
    def __init__(self, aLocation : Location, aPherDelta, aAntCapacity):
        #Ants current location
        self.Location = aLocation
        #Pheremone delta increase
        self.PherDelta = aPherDelta
        #Vehicle capacity constraint
        self.AntCapacity = aAntCapacity
        #Current weight taken on route
        self.CurrentWeight = 0
        #Best Route Cost
        self.BestCost = None
        #Array of locations in best route
        self.BestRoute = []
        #Array of locations in current route
        self.CurrentRoute = []
        #Current route cost
        self.RouteCost = 0
        #Best Neighbor at current location
        self.BestNeighbor = None#min(aLocation.neighbours,key=lambda x:x.Distance) #None
        #Boolean indicating more locations to visit
        self.MoreLocations = True

    def CalculateMove(self):
        #Calculate individual scores
        self.Location.CalculateScores()
        #Calculate individual probabilities
        self.Location.CalculateProbabilities()

        lNeighbors = self.Location.GetNeighbors()
        for lNeighbor in lNeighbors:
            if (lNeighbor.GetPackageWeight() + self.CurrentWeight) > self.AntCapacity:
                lNeighbors.remove(lNeighbor)
                
        #Check if any valid neighbors
        if len(lNeighbors) > 0:
            #Choose random neighbor based on probability weights
            #TODO BUG!!! randomly, the number of probabilies increases. im guessing somewhere theyre being re-appende
            self.BestNeighbor = random.choices(self.Location.GetNeighbors(), weights=self.Location.GetProbabilities(), k=1)
            #Change location
            #NOTE random.choices returns a list, so we need to use the 0th index
            self.BestNeighbor = self.BestNeighbor[0]

            self.Location = self.BestNeighbor.GetLocation()
        else:
            #Mark no more locations
            self.MoreLocations = False
            #Send back to warehouse

            #NOTE instead of passing in a refernce to the depot for each ant
            #we can just add it the the start&end of the route once finished.
            self.CurrentRoute.append(self.CurrentRoute[0])
            

    def UpdateLocal(self): 
        #Update local pheremone 
        self.BestNeighbor.SetPheremone( ( (1 - self.BestNeighbor.GetDecay() ) * self.BestNeighbor.GetPherLvl() + self.PherDelta))


    def UpdateBest(self):
        #Update best ant route if current is better
        if self.RouteCost < self.BestCost:
            #Update best cost
            self.BestCost = self.RouteCost
            #Update best route of location objects
            self.BestRoute = self.CurrentRoute

    def FindRoute(self, aVisited):

        while self.MoreLocations:
            #Calculate move on current iteration
            self.CalculateMove()
            #Update local pheremone
            self.UpdateLocal()
        #Update best current route if better
        self.UpdateBest()

    def GetDelta(self):
        return self.PherDelta

    def GetRoute(self):
        return self.CurrentRoute

    def GetBestRoute(self):
        return self.BestRoute

    def GetRouteCost(self):
        return self.RouteCost

        
