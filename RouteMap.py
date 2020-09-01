#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#RouteMap.py
#from Location import Location
from math import sqrt
class Point():
    def __init__(self,_X,_Y):
        self.X = _X
        self.Y = _Y
        self.coords = (_X,_Y)
    def __repr__(self):
        return "X:{0},Y:{1}".format(self.X,self.Y)

class Neighbour(Point):
    def __init__(self,_X,_Y,_D):
        super().__init__(_X,_Y)
        self.dist = _D
    
    def __repr__(self):
        return "coords:({0},{1}), distance:{2}".format(self.X,self.Y,self.dist)

class Location(Point):
    def __init__(self,_X,_Y,_T='l'):
        super().__init__(_X,_Y)
        self.Type = _T
        self.neighbours = []

    def __repr__(self):
        results = "Location: %s\n  Neighbours:\n" % self.coords
        for n in self.neighbours:
            results = results + "    %s : %s,\n" % (n[0],n[1])
        return results

# class Location():
#     def __init__(self, _X, _Y,_T='l'):
#         self.Type = _T#default is l for location
#         self.X = _X
#         self.Y = _Y
#         self.coords = "({0},{1})".format(_X,_Y)
#         self.neighbours = []#[ ("x,y",dist), ... ]

#     def __repr__(self):
#         results = "Location: %s\n  Neighbours:\n" % self.coords
#         for n in self.neighbours:
#             results = results + "    %s : %s,\n" % (n[0],n[1])
#         return results

class RouteMap():

    def __init__(self, _warehouse, _locations):
        
        #2d array of locations
        #Example: [[X1,Y1],[X2, Y2]] 
        self.locations = _locations

        #Single array of warehouse coordinates
        self.warehouse = []
        self.warehouse.append(Location(_warehouse[0],_warehouse[1],'d'))#_warehouse

        #Array of Location objects
        self.locations = self.InitLocations()

    def InitLocations(self):
        world = []
        for l in self.locations:
            newlocation = Location(l[0],l[1])
            for n in self.locations:
                if n != l: 
                    dist = round(sqrt( ((n[0] - l[0])**2) + ((n[1] - l[1])**2) ),2 )
                    newlocation.neighbours.append( Neighbour(n[0],n[1],dist) )
            world.append(newlocation)
        return world

    def __repr__(self):
        result = "["
        for l in self.locations:
            result = result + (l.coords + ',')
        return result + "]"


  