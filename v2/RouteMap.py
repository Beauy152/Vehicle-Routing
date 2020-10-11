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

class Neighbour():
    """inherits point class, extends with distance"""
    def __init__(self,_L,_D,_S):#, _P,):
        self.actual_location = _L
        #Distance between initial location and neighbor
        self.Distance = _D
        #perhaps these can be inherited by classes for specific algorithms
        #Pheremone level of path between location and neighbor
        self.PheremoneLvl = 1
        #Savings calculation of adding neighbor to route instead of starting from depot
        self.Savings = _S
        #Pheremone evaporation coefficient of path between location and neighbor
        self.Decay = 0.25#None  #Need to figure out
        #Score of attractiveness before probability
        self.Score = None
        #Probability of selection amongst other neighbors
        self.Probability = None
        #Weight of package being delivered to neighbor
        #self.PackageWeight = _P


    def SetPheremone(self, aNum):
        self.PheremoneLvl = aNum

    def GetDecay(self):
        return self.Decay

    def GetPherLvl(self):
        return self.PheremoneLvl
    
    def GetLocation(self):
        return self.actual_location

    def CalculateScore(self):
        #Calculates individual score based off distance heuristic, pheremone level and savings
        #self.Score = ((1 / self.Distance) * (self.PheremoneLvl) * (self.Savings))
        self.Score = ((1 / self.Distance) * (self.PheremoneLvl))


    def CalculateProbability(self, aSum):
        #Calculates probability of selection
        if self.Score==0 and aSum==0:return 0
        self.Probability = (self.Score / aSum)

    def GetScore(self):
        if self.Score is None: self.CalculateScore()
        return self.Score

    def GetProbability(self):

        return self.Probability

    def GetDist(self):
        return self.Distance

    def GetPackageWeight(self):
        #if len(self.actual_location.packages) < 1: return 0
        return sum(p.weight for p in self.actual_location.packages)#self.PackageWeight
    

    def GetX(self):
        return self.actual_location.X

    def GetY(self):
        return self.actual_location.Y


    def __repr__(self):
        return "coords:({0},{1}), distance:{2}".format(self.actual_location.X, \
                                                        self.actual_location.Y, \
                                                        self.Distance)


class Location(Point):
    """inherits point class"""
    def __init__(self,_X,_Y,_Packages,_T='l'):
        super().__init__(_X,_Y)
        self.Type = _T
        self.neighbours = []
        self.Probabilities = []
        self.packages = _Packages
        self.X = _X
        self.Y = _Y

    def __repr__(self):
        results = "Location: %s\n  Neighbours:\n" % str(self.coords)
        if len(self.neighbours) > 0:
            for n in self.neighbours:
                results = results + "    %s : %s,\n" % (n.coords,n.dist)
        else:
            results = results + "no neighbours."
        return results

    def CalculateScores(self):
        #Calculates individual scores for each neighbor
        for lNeighbor in self.neighbours:
            lNeighbor.CalculateScore()

    def ScoreSum(self):
        #Calculates sum of scores over each neighbor
        lSum = 0
        for lNeighbor in self.neighbours:
            lSum = lSum + lNeighbor.GetScore()
        return lSum
    
    def CalculateProbabilities(self):

        lCurrentProb = []
        for lNeighbor in self.neighbours:
            lNeighbor.CalculateProbability(self.ScoreSum())
            lCurrentProb.append(lNeighbor.GetProbability())

        self.Probabilities = lCurrentProb

    def GetNeighbors(self):
        return self.neighbours

    def RemoveNeighbour(self, aNeighbour):
        self.neighbours.remove(aNeighbour)
        
    def GetProbabilities(self):
        return self.Probabilities



class RouteMap():

    def __init__(self,_locations, _packages):
        #2d array of locations
        #Example: [[X1,Y1],[X2, Y2]] 
        self.locations = []
        #convert location tuple to location objects
        for l in _locations: 
            temp_packages = [p for p in _packages if p.location == l ]
            #print("temp packages: %s" % temp_packages)
            self.locations.append(Location(l[0],l[1],temp_packages) )
        
        #set first item in array as type depot
        self.locations[0].Type = 'd'

        #Single array of warehouse coordinates
        self.depot = []
        self.depot.append(self.locations[0])#_warehouse
        #depot_neighbours 
        #Array of Location objects
        self.InitLocations()

    def CalcDistance(self, aStartLoc, aEndLoc):
        return sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )

    def InitLocations(self):
        for l in self.locations:
            for n in self.locations:
                if n != l:
                    #Append new neighbor with distance and savings calculations
                    l.neighbours.append( 
                        Neighbour(n,
                            self.CalcDistance(l,n), 
                            self.CalcSavings(l, n) 
                        ))
            #l.CalculateProbabilities()




    def CalcSavings(self, aStartLoc, aEndLoc):
        return (self.CalcDistance(self.depot[0], aStartLoc) + self.CalcDistance(self.depot[0], aEndLoc) - self.CalcDistance(aStartLoc, aEndLoc))

    def __repr__(self):
        result = "["
        for l in self.locations:
            result = result + (l.coords + ',')
        return result + "]"


  