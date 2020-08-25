from math import sqrt

class DeliveryAgent():
    """Delivery Agent / Vehicle class"""
    def __init__(self,_x,_y,_capacity ):
        self.x = _x
        self.y = _y
        self.capacity = _capacity

    def getDistanceTo(self,location):
        """Given coordinate (x,y) of location, returns
        distance to it from agents current position
        (Straigh line distance)"""
        return sqrt( ( (self.x - location[0])**2 + (self.y - location[1])**2 ) )

    
    def __repr__(self):
            #Python magic function, defines how obj is represented in when print is called
        return "X:{0},Y:{1},C:{2}".format(self.x,self.y,self.capacity)