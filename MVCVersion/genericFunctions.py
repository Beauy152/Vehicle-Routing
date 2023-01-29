from math import sqrt
from entities.new_mapping import *


def calcDistance(start:'Location',end:'Location'):
    return sqrt( (end.x - start.x)**2 + (end.y - start.y)**2 )

def CalcDistance2(aStartLoc, aEndLoc):
    """takes two objects, with attributes x&y"""
    return sqrt( (aEndLoc.x - aStartLoc.x)**2 + (aEndLoc.y - aStartLoc.y)**2 )

def CalcDistance3(x,y,aEndLoc):
    """takes two raw x&y values, and one object with x&y attributess"""
    return sqrt( (aEndLoc.x - x)**2 + (aEndLoc.y - y)**2 )

def CalcDistance4(x1,y1,x2,y2):
    """takes four raw x&y values"""
    return sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def CalcDimensionalDistance(D1,D2):
    """Euclidian distance for d Dimensions"""
    result = 0
    for d1,d2 in zip(D1,D2):
        result += (d2 - d1)**2
    return sqrt(result)


def calcSaving(aStartLoc:'Location', aEndLoc:'Location'):
    #Apply savings formula
    depot = aStartLoc.depot
    return (calcDistance(depot, aStartLoc) + calcDistance(depot, aEndLoc) - calcDistance(aStartLoc, aEndLoc))
    

def SumRouteDistance(route):
    """sums the distance between all locations in route"""
    total_dist = 0
    if len(route) < 1 : return total_dist
    for i in range(len(route)-1):
        aStartLoc = route[i]
        aEndLoc = route[i+1]
        total_dist += sqrt( (aEndLoc.x - aStartLoc.x)**2 + (aEndLoc.y - aStartLoc.y)**2 )
    return total_dist

def SumRouteWeight(route):
    """sums the weight of all packages of locations in route"""
    if route == None or len(route) < 1: return 0
    return sum(l.sumPackages() for l in route)


def defaultsParser(filename):
    """Opens given file and parses as gui defaults format"""
    defaults = {}
    with open(filename,'r') as file:
        lines = [line.split(':') for line in file]
        #print(lines)
        for line in lines:
            defaults.update({line[0]:line[1].rstrip() })
    return defaults

def two_opt(p,route):
    """Local optimision of route, by swapping 
    pairs of locations to find more efficient permuations"""
    def swap(r,i,j):
        """Returns new route by reversing sections of existing route"""
        new_route = r[0:i-1]
        temp = r[i:k];temp.reverse()
        new_route.extend(temp)
        new_route.extend(r[k+1:])

        return new_route

    #route
    n = len(route)
    baseline = SumRouteDistance(route)

    for i in range(1,n-2):
        for k in range(i+2,n):
            new_route = swap(route,i,k)
            new_baseline = SumRouteDistance(new_route)
            if new_baseline < baseline:
                route = new_route
                baseline = new_baseline
                break

    return route