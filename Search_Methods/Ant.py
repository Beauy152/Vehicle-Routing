#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#Ant.py
import random
import numpy as np
from Mapping import ACO_Location as Location,ACO_Neighbour as Neighbour
#RouteMap import Location, Neighbour

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
        self.BestCost = 999999
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

        self.LocalVisited = []

    def CalculateMove(self, aVisited, aMap):
        
        #Calculate individual scores
        self.Location.CalculateScores()
        #Calculate individual probabilities
        self.Location.CalculateProbabilities()

        lTest = self.Location.GetNeighbors()

        lNeighbors = []
        lProbs = []
        
        for lNeighbor in lTest:
            if((lNeighbor.GetPackageWeight() + self.CurrentWeight) <= self.AntCapacity) and (self.SameLoc(lNeighbor, aVisited) == False):
                lNeighbors.append(lNeighbor)
                lProbs.append(lNeighbor.GetProbability())
                
        #Check if any valid neighbors
        if len(lNeighbors) > 0:

            self.BestNeighbor = random.choices(lNeighbors, weights=lProbs, k=1)
            #Change location
            self.BestNeighbor = self.BestNeighbor[0]

            self.Location = self.BestNeighbor.GetLocation()
            self.CurrentWeight += self.BestNeighbor.GetPackageWeight()

            aVisited.append(self.BestNeighbor)
            self.CurrentRoute.append(self.BestNeighbor)
            self.RouteCost += self.BestNeighbor.GetDist()

        else:
            #Mark no more locations
            self.MoreLocations = False
            #Send back to warehouse
            if len(self.CurrentRoute) > 0:
                self.CurrentRoute.append(self.CurrentRoute[0])
            

    def UpdateLocal(self): 
        #Update local pheremone 
        if self.BestNeighbor != None:
            self.BestNeighbor.SetPheremone( ( (1 - self.BestNeighbor.GetDecay() ) * self.BestNeighbor.GetPherLvl() + self.PherDelta))


    def UpdateBest(self):
        #Update best ant route if current is better
        if self.RouteCost < self.BestCost:
            #Update best cost
            self.BestCost = self.RouteCost
            #Update best route of location objects
            self.BestRoute = self.CurrentRoute

    def FindRoute(self, aVisited, aMap):
        self.CurrentRoute.append(aVisited[0])
        while self.MoreLocations:
            #Calculate move on current iteration
            self.CalculateMove(aVisited, aMap)
            #Update local pheremone
            self.UpdateLocal()
        #Update best current route if better
        self.UpdateBest()

    def SameLoc(self, aNeighbor, aList):
        for location in aList:
            if aNeighbor.X == location.X and aNeighbor.Y == location.Y:
                return True
        return False

    def ResetAnt(self):
        self.CurrentRoute = []
        self.CurrentWeight = 0
        self.MoreLocations = True

        self.RouteCost = 0


    def GetDelta(self):
        return self.PherDelta

    def GetRoute(self):
        return self.CurrentRoute

    def GetBestRoute(self):
        return self.BestRoute

    def GetRouteCost(self):
        return self.RouteCost

        
