from random import randint
from TestData import sys_globals

def GeneratePackages():
    """Create a list of packages, with a max weight
    of no more than the combined carry capacity of
    all delivery agents"""

    #Get total capacity of agents
    print(sys_globals["total_capacity"])


class Package():
    def __init__(self,_location,_weight,_earliest,_desired,_latest):
        self.location = _location
        self.weight   = _weight
        self.earliest = _earliest
        self.desired  = _desired
        self.latest   = _latest