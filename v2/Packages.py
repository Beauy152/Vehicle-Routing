#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#Packages.py

from random import choice,randint

def GeneratePackages(total_capacity,_locations):
    """Create a list of packages, with a max weight
    of no more than the combined carry capacity of
    all delivery agents"""
    Packages = []
    locations = _locations
    remaining_capacities = total_capacity

    while remaining_capacities > 0:
        rand_weight = randint(1,25)

        if (remaining_capacities - rand_weight) < 0:
            rand_weight = remaining_capacities
            break
        else:
            remaining_capacities = remaining_capacities - rand_weight

        Packages.append( 
            Package(
                choice(locations),rand_weight) 
            )
    return Packages



class Package():
    def __init__(self,_location,_weight):
        self.location = _location
        self.weight   = _weight

    def __repr__(self):
        return "for:{0},{1}kg.".format(self.location,self.weight)