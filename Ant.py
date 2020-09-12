#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#Ant.py

from RouteMap import Location, Neighbour

class Ant():
    def __init__(self, aLocation : Location, aPherDelta, aAntCapacity):
        #Ants current location
        self.Location = aLocation
        #Pheremone delta increase
        self.PherDelta = aPherDelta
        #Vehicle capacity constraint
        self.AntCapacity = aAntCapacity
        #Best Route Cost
        self.BestCost = None
        #Array of locations in best route
        self.BestRoute = []
        #Array of locations in current route
        self.CurrentRoute = []
        #Current route cost
        self.RouteCost = 0
        #Best Neighbor at current location
        self.BestNeighbor = None

    def CalculateMove(self):
        #Method of movement calculation
        lBestMove = None
        for lNeighbor in self.Location.neighbours:
            pass
            #IMPLEMENT FORMULA FOR FITNESS FUNCTION
            #UPDATE BEST MOVE BASED ON PROBABILITY OUTPUT

        #Update route

        
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

    def GetDelta(self):
        return self.PherDelta

    def GetRoute(self):
        return self.CurrentRoute

    def GetBestRoute(self):
        return self.BestRoute

    def GetRouteCost(self):
        return self.RouteCost
        
        
