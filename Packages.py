from random import randint

def GeneratePackages():
    """Create a list of packages, with a max weight
    of no more than the combined carry capacity of
    all delivery agents"""

    #Get total capacity of agents



class Package():
    def __init__(self,_location,_weight,_earliest,_desired,_latest):
        self.location = _location
        self.weight   = _weight
        self.earliest = _earliest
        self.desired  = _desired
        self.latest   = _latest