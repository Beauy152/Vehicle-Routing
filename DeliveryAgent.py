from math import sqrt

class DeliveryAgent():
    """Delivery Agent / Vehicle class"""
    def __init__(self,_id,_x=0,_y=0,_capacity=100 ):
        self.id = "v_%s" % _id
        self.x  = _x
        self.y  = _y
        self.capacity = _capacity

    #Currently Redundant
    # def getDistanceTo(self,location):
    #     """Given coordinate (x,y) of location, returns
    #     distance to it from agents current position
    #     (Straigh line distance)"""
    #     return sqrt( ( (self.x - location[0])**2 + (self.y - location[1])**2 ) )

    def AskIf(self):
        """Send inquiry to agent"""
        pass
    
    def Tell(self):
        """Send knowledge/data to agent"""
        pass

    def Reply(self):
        """Reply to agent"""
        pass

    def Perform(self):
        """maybe not useful"""
        pass


    def __repr__(self):
            #Python magic function, defines how obj is represented in when print is called
        return "ID:{0}, X:{1}, Y:{2}, C:{3}\n".format(self.id,self.x,self.y,self.capacity)