from math import sqrt

def CalcDistance2(aStartLoc, aEndLoc):
    return sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )

def CalcDistance3(X,Y,aEndLoc):
    return sqrt( (aEndLoc.X - X)**2 + (aEndLoc.Y - Y)**2 )