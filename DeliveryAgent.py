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
        self.colour = _col

        #vehicle memory
        #self.mem = {}

    def Perform(self):
        """execute Route"""
        pass

    def printRoute(self):
        if self.route == None or len(self.route) < 1:return None
        result = ""

        for location in self.route:
            result += str(location)

        return result

    def sumRoute(self):
        if self.route == None or len(self.route) < 1:return None
        else:
            dsum = 0
            for i in range(len(self.route)):
                if i == len(self.route)-1:return dsum
                aStartLoc = self.route[i]
                aEndLoc = self.route[i+1]
                dsum += sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )
        
            #return sum(l.Distance for l in self.route)

    def __repr__(self):
            #Python magic function, defines how obj is represented in when print is called
        return "X:{1}, Y:{2}, C:{3}\n".format(self.x,self.y,self.capacity)

    def __str__(self):
        return "{0}:\ncapacity:{1}\nroute length:{2}\nroute:{3}".format(self.id,self.capacity,self.sumRoute(),self.printRoute())