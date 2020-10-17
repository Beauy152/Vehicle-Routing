#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#ACO.py
#from RouteMap import RouteMap
#from RouteMap import Neighbour
from Mapping import Map,ACO_Neighbour as Neighbour
from Search_Methods.Ant import Ant
from DeliveryAgent import DeliveryAgent

class ACO():

    def __init__(self, aMap:Map, aAgents):

        #Delivery Agents
        self.fAgents = aAgents
        #World object
        self.fMap = aMap
        #Ant colony
        self.fColony = self.InitColony(aAgents)
        #Temporary termination condition
        self.RouteFound = False
        #Current Best Ant
        self.BestAnt = None
        #Best route cost
        self.BestCost = None

        self.BestRouteGroup = []
        self.BestGroupScore = 99999


    def run(self):
        return self.Optimize()

    def Optimize(self):
        #Temporary termination condition (main loop)
        lCount = 0

        while self.RouteFound == False:
            lTempBest = self.BestGroupScore
            #Initialize colony at depot
            self.ResetColony()
            #Establish a memory so other ants do not visit locations by previous ant routes in current loop
            lVisited = [Neighbour(self.fMap.depot[0], 0, 0)]
            # for lAnt in self.fColony:
            #     #Calculate individual ant route
            #     lAnt.FindRoute(lVisited, self.fMap)
            lIndex = 0
            while len(lVisited) < len(self.fMap.locations)  and lIndex < len(self.fColony):
                self.fColony[lIndex].FindRoute(lVisited, self.fMap)
                lIndex+= 1

            if len(lVisited) == len(self.fMap.locations)+1 :
                self.UpdateBest()
            #Apply global pheremone update
            self.UpdateGlobal()

            #Check if best route cost hasnt changed in x iterations (10 for now)
            if lTempBest == self.BestGroupScore:
                lCount += 1
                if (lCount > 500):
                    #Terminate if it hasn't changed in x iterations
                    self.RouteFound = True
            else:
                self.lCount = 0

        #Allocate agents with routes
        return self.AllocateRoutes()
        #NOTE Best route is the most optimal, so they would chose the route where they don't visit everything. Need to ensure everything is visited.

        

    def InitColony(self, aAgents):
        lAnts = []
        for lAgent in aAgents:
            #Append new ant based on available agents
            lAnts.append( Ant(self.fMap.depot[0], 50, lAgent.capacity ))

        return lAnts
 
    def ResetColony(self):
        #Set each ant back at depot
        for lAnt in self.fColony:
            lAnt.Location = self.fMap.depot[0]
            lAnt.ResetAnt()


    def AllocateRoutes(self):
        
        lRoutedAgents = []
        for lIndex, lRoute in enumerate(self.BestRouteGroup):
            #Allocate each agent with best route of corresponding ant
            self.fAgents[lIndex].route = lRoute
            #Append to updated agent array
            lRoutedAgents.append(self.fAgents[lIndex])

        return lRoutedAgents
        
    def UpdateGlobal(self):
        #Sort for the most efficient route
        self.GetBestColRoute()

        for lNeighbor in self.BestAnt.GetRoute():
            #Calculate global pheremone deposition
            if self.BestAnt.GetRouteCost() > 0:
                lNeighbor.SetPheremone((1 - lNeighbor.GetDecay()) * lNeighbor.GetPherLvl() + lNeighbor.GetDecay() * (self.BestAnt.GetRouteCost() ** -1))


    def UpdateBest(self):
        lGroupScore = 0
        for lAnt in self.fColony:
            lGroupScore += lAnt.GetRouteCost()

        if lGroupScore < self.BestGroupScore:
            
            self.BestGroupScore = lGroupScore
            self.BestRouteGroup = []
            for lAnt in self.fColony:
                self.BestRouteGroup.append(lAnt.GetRoute())
            


    def GetBestColRoute(self):
        #NOTE TO SELF: THE MOST EFFICIENT ROUTE WILL NOT ALWAYS BE THE MOST EFFICIENT (DOES NOT TAKE INTO ACCOUNT PACKAGES COLLECTED)
        lBestCost = 1000
        for lAnt in self.fColony:
            #Check if each ant is more efficient
            if (lAnt.GetDelta() <= lBestCost):
                #Update Best ant
                self.BestAnt = lAnt
                #Update local current cost
                lBestCost = lAnt.GetDelta()
                #Update best cost for colony
                self.BestCost = lBestCost



