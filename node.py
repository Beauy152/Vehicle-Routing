class Node():
    def __init__(self,_x,_y,value):
        self.X = _x
        self.Y = _y
        self.value = value #delivery location 'l', or depot 'd'
        self.coords= (self.X,self.Y)



    def __repr__(self):
        return "X:{0},Y:{1},V:{2}".format(self.X,self.Y,self.value)