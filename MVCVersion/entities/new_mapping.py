from enum import Enum

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


class Location(Point):
    colourLookup = {
        LocationTypes.depot:"blue",
        LocationTypes.target:"black"
    }

    maxX:int    = 1
    maxY:int    = 1
    sclX:float  = None
    sclY:float  = None

    @classmethod
    def updateMax(cls,_x,_y):
        if _x > cls.maxX: cls.maxX = _x
        if _y > cls.maxY: cls.maxY = _y


    def __init__(self,X,Y,type:LocationTypes=LocationTypes.target) -> None:
        super().__init__(X,Y)
        self.type = type    

        # Determine the global Max coordinates for scaling
        self.updateMax(X,Y)

        # Utilities for drawing
        self.color = self.colourLookup.get(self.type)
        self.canvasObJId = None

    def scale(self) -> None:
        """   """
        self.x = (self.x / self.maxX) * self.sclX
        self.y = (self.y / self.maxY) * self.sclY

    def draw(self,artist:Artist):
        self.scale()
        artist.drawLocation(self)