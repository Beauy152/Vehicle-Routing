#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#ACO.py
from RouteMap import RouteMap
from RouteMap import Neighbour
from Ant import Ant
from DeliveryAgent import DeliveryAgent

class ACO():

    def __init__(self, aMap : RouteMap, aAgents):

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



    def Optimize(self):
        #Temporary termination condition (main loop)
        while self.RouteFound == False:
            #Initialize colony at depot
            self.ResetColony()

            for lAnt in self.fColony:
                #Calculate individual ant movements
                lAnt.CalculateMove()
                #Apply local pheremone update
                lAnt.UpdateLocal()
            #Apply global pheremone update
            self.UpdateGlobal()

        #Allocate agents with routes
        return self.AllocateRoutes()

        

    def InitColony(self, aAgents):
        lAnts = []
        for lAgent in aAgents:
            #Append new ant based on available agents
            lAnts.append( Ant(self.fMap.depot[0], 10, lAgent.capacity ))

        return lAnts

    def ResetColony(self):
        for lAnt in self.fColony:
            lAnt.Location = self.fMap.depot[0]


    def AllocateRoutes(self):

        lRoutedAgents = []
        for lIndex, lAnt in enumerate(self.fColony):
            #Allocate each agent with best route of corresponding ant
            self.fAgents[lIndex].route = lAnt.GetBestRoute()
            #Append to updated agent array
            lRoutedAgents.append(self.fAgents[lIndex])

        return lRoutedAgents
        
    def UpdateGlobal(self):
        #Sort for the most efficient route
        self.GetBestColRoute()

        for lNeighbor in self.BestAnt.GetRoute():
            #Calculate global pheremone deposition
            lNeighbor.SetPheremone((1 - lNeighbor.GetDecay()) * lNeighbor.GetPheremoneLvl() + lNeighbor.GetDecay() * (self.BestAnt.GetRouteCost() ** -1))

        

        
    def GetBestColRoute(self):
        #NOTE TO SELF: THE MOST EFFICIENT ROUTE WILL NOT ALWAYS BE THE MOST EFFICIENT (DOES NOT TAKE INTO ACCOUNT PACKAGES COLLECTED)
        lBestCost = 1000
        for lAnt in self.fColony:
            #Check if each ant is more efficient
            if (lAnt.GetDelta() <= lBestCost):
                #Update Best ant
                self.BestAnt = lAnt
                #Update best cost
                lBestCost = lAnt.GetDelta()



