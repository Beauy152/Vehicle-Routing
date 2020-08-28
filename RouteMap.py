#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#RouteMap.py
from Location import Location
from math import sqrt


class RouteMap():

    def __init__(self, aWarehosue, aCoordinates):
        
        #2d array of locations
        #Example: [[X1,Y1],[X2, Y2]] 
        self.fCoordinates = aCoordinates

        #Single array of warehouse coordinates
        self.fWarehouse = aWarehosue

        #Array of Location objects
        self.fLocations = self.InitLocations()

    def InitLocations(self):

        lLocations = []
        #Loop over each location coordinate array
        for lCoordinate in self.fCoordinates:
            #Declare new location
            lLocation = Location(lCoordinate[0], lCoordinate[1])
            #Loop over coordinates to calculate neighbor distances for each location
            for lNeighbor in self.fCoordinates:
                lLocation.fNeighborMatrix.append(sqrt( ( (lLocation.fX - lNeighbor[0])**2 + (lLocation.fY- lNeighbor[1])**2 ) ))


        return lLocations
            



  