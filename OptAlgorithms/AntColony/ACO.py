#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#ACO.py
from RouteMap import RouteMap
from Ant import Ant
from DeliveryAgent import DeliveryAgent

class ACO():

    def __init__(self, aMap : RouteMap, aAgents):

        #Delivery Agents
        self.fAgents = aAgents
        #Ant colony
        self.fAnts = self.InitColony(aAgents)
        #World object
        self.fMap = aMap
        #Temporary termination condition
        self.RouteFound = False



    def Optimize(self):
        #Temporary termination condition (main loop)
        while self.RouteFound == False:
            #Initialize colony at depot
            self.ResetColony()

            for lAnt in self.fAnts:
                #Calculate individual ant movements
                lAnt.CalculateMove()
                #Apply local pheremone update
                lAnt.LocalUpdate()
            #Apply global pheremone update
            self.UpdateGlobal()

        #Allocate agents with routes
        return self.AllocateRoutes()

        

    def InitColony(self, aAgents):
        lAnts = []
        for lAgent in aAgents:
            #Append new ant based on available agents
            lAnts.append(Ant(self.fMap.Depot[0]), 10, lAgent.GetCapacity())

        return lAnts

    def ResetColony(self):
        for lAnt in self.fAnts:
            lAnt.Location = self.fMap.Depot[0]


    def AllocateRoutes(self):

        lRoutedAgents = []
        for lIndex, lAnt in enumerate(self.fAnts):
            #Allocate each agent with best route of corresponding ant
            self.fAgents[lIndex].SetRoute(lAnt.BestRoute())
            #Append to updated agent array
            lRoutedAgents.append(self.fAgents[lIndex])

        return lRoutedAgents
        
    def UpdateGlobal(self):
        #Method of global pheremone update
        
        #IMPLEMENT GLOBAL UPDATE FORMULA
