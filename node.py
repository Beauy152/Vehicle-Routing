class Node():
    def __init__(self,_x,_y,value):
        self.X = _x
        self.Y = _y
        self.value = value #location:l, depot:d, selected:s
        self.coords= (self.X,self.Y)



    #Setter - Update Nodes value
    def setValue(self,value):
        self.value = value

    #Python magic function, defines how obj is represented in when print is called
    def __repr__(self):
        return "X:{0},Y:{1},V:{2}".format(self.X,self.Y,self.value)