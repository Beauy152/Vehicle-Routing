from enum import Enum
from entities.new_package import Package
from genericFunctions import calcDistance, calcSaving

from entities.new_artist import Artist


class LocationTypes(Enum):
    depot = "depot"
    target= "target"

class Point():
    def __init__(self,_X,_Y):
        self.x = _X
        self.y = _Y
        self.coords = (_X,_Y)
    def __repr__(self):
        return "X:{0},Y:{1}".format(self.x,self.y)

class Neighbour():
    def __init__(self,location:'Location',neighboured:'Location') -> None:
        self.location   :Location = location
        self.saving     :float    = calcDistance(neighboured,location)
        self.distance   :float    = calcSaving(neighboured,location)
        self.x          :float    = location.x
        self.y          :float    = location.y

class Location(Point):
    colourLookup = {
        LocationTypes.depot:"blue",
        LocationTypes.target:"black"
    }

    maxX:int    = 1
    maxY:int    = 1
    sclX:float  = None
    sclY:float  = None
    depot:'Location' = None

    @classmethod
    def updateMax(cls,_x,_y):
        """Updates class method. used to enable scaling location coordinates."""
        if _x > cls.maxX: cls.maxX = _x
        if _y > cls.maxY: cls.maxY = _y

    def __init__(self,X,Y,type:LocationTypes=LocationTypes.target) -> None:
        super().__init__(X,Y)
        self.type = type    
        self.neighbours = []
        self.packages:list[Package]   = []
        self.package_sum = self.sumPackages()
        # Determine the global Max coordinates for scaling
        self.updateMax(X,Y)

        # Utilities for drawing
        self.color = self.colourLookup.get(self.type)
        self.canvasObJId = None
        self.isScaled = False

    def sumPackages(self) -> float:
        self.package_sum = \
            sum(p.weight for p in self.packages) if len(self.packages) > 0 else 0
        return self.package_sum

    def scale(self) -> None:
        """Calculates coordinate scaling factor for the location"""
        self.x = (self.x / self.maxX) * self.sclX
        self.y = (self.y / self.maxY) * self.sclY
        self.isScaled = True

    def draw(self,artist:Artist):
        if not self.isScaled: self.scale()
        artist.drawLocation(self)