from math import sqrt

def CalcDistance2(aStartLoc, aEndLoc):
    return sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )

def CalcDistance3(X,Y,aEndLoc):
    return sqrt( (aEndLoc.X - X)**2 + (aEndLoc.Y - Y)**2 )

def CalcDistance4(X1,Y1,X2,Y2):
    return sqrt( (X2 - X1)**2 + (Y2 - Y1)**2 )

def CalcDimensionalDistance(D1,D2):
    """Euclidian distance for d Dimensions"""
    result = 0
    for d1,d2 in zip(D1,D2):
        result += (d2 - d1)**2
    return sqrt(result)

def SumRouteDistance(route):
    total_dist = 0
    if len(route) < 1 : return total_dist
    for i in range(len(route)-1):
        aStartLoc = route[i]
        aEndLoc = route[i+1]
        total_dist += sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )
    return total_dist

def SumRouteWeight(route):
    if route == None or len(route) < 1: return 0
    #s = sum(route,key=lambda x:x.GetPackageWeight())
    return sum(l.GetPackageWeight() for l in route)