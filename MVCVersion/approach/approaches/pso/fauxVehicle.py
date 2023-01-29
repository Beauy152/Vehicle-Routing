class Faux_Vehicle():
    """Temporary Vehicle Class to avoid overwriting vehicle data 
    and allow for more flexible processing"""
    def __init__(self,xref,yref,radius,max_capacity):
        self.xref = xref
        self.yref = yref
        self.radius = radius
        self.capacity = 0
        self.max_capacity = max_capacity
        self.route = []