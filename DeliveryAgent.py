#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#DeliveryAgent.py

from math import sqrt

class DeliveryAgent():
    """Delivery Agent / Vehicle class"""
    def __init__(self,_id,_x=0,_y=0,_capacity=100,_col=(0,0,0) ):
        self.id = "v_%s" % _id
        self.x  = _x
        self.y  = _y
        self.capacity = _capacity
        self.route = None
        self.fLocation = None
        self.colour = _col

    def Perform(self):
        """execute Route"""
        pass


    def __repr__(self):
            #Python magic function, defines how obj is represented in when print is called
        return "ID:{0}, X:{1}, Y:{2}, C:{3}\n".format(self.id,self.x,self.y,self.capacity)