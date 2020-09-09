#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#RouteMap.py
#from Location import Location
from math import sqrt

class Point():
    """base class for location-based object. implements
    standard X,Y,Coords attributes and representation"""
    def __init__(self,_X,_Y):
        self.X = _X
        self.Y = _Y
        self.coords = (_X,_Y)
    def __repr__(self):
        return "X:{0},Y:{1}".format(self.X,self.Y)

class Neighbour(Point):
    """inherits point class, extends with distance"""
    def __init__(self,_X,_Y,_D,_S):
        super().__init__(_X,_Y)
        #Distance between initial location and neighbor
        self.Distance = _D
        #Pheremone level of path between location and neighbor
        self.PheremoneLvl = 0
        #Savings calculation of adding neighbor to route instead of starting from depot
        self.Savings = _S
        #Pheremone evaporation coefficient of path between location and neighbor
        self.EvapCoefficient = None  #Need to figure out
        

    
    def __repr__(self):
        return "coords:({0},{1}), distance:{2}".format(self.X,self.Y,self.Distance)




class Location(Point):
    """inherits point class"""
    def __init__(self,_X,_Y,_T='l'):
        super().__init__(_X,_Y)
        self.Type = _T
        self.neighbours = []

    def __repr__(self):
        results = "Location: %s\n  Neighbours:\n" % str(self.coords)
        if len(self.neighbours) > 0:
            for n in self.neighbours:
                results = results + "    %s : %s,\n" % (n.coords,n.dist)
        else:
            results = results + "no neighbours."
        return results


class RouteMap():

    def __init__(self, _Depot, _locations):
        
        #2d array of locations
        #Example: [[X1,Y1],[X2, Y2]] 
        self.locations = _locations

        #Single array of warehouse coordinates
        self.Depot = []
        self.Depot.append(Location(_Depot[0],_Depot[1],'d'))#_warehouse

        #Array of Location objects
        self.locations = self.InitLocations()

    def InitLocations(self):
        world = []
        for l in self.locations:
            newlocation = Location(l[0],l[1])
            for n in self.locations:
                if n != l: 
                    
                    #Append new neighbor with distance and savings calculations
                    newlocation.neighbours.append( 
                        Neighbour(n[0],n[1],
                        self.CalcDistance(l,n), 
                        self.CalceSavings(l, n) )
                        )

            world.append(newlocation)
        return world

    def CalceSavings(self, aStartLoc, aEndLoc):
        return (self.CalcDistance(self.Depot[0], aStartLoc) + self.CalcDistance(self.Depot[0], aEndLoc) - self.CalcDistance(aStartLoc, aEndLoc))


    def CalcDistance(self, aStartLoc, aEndLoc):
        return sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )

    def __repr__(self):
        result = "["
        for l in self.locations:
            result = result + (l.coords + ',')
        return result + "]"


  