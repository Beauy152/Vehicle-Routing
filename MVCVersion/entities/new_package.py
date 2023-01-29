#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#Packages.py

from entities.new_mapping import *


class Package:
    """Package class, each pacakge is assigned a package,
    some locations may not be assigned any packages"""
    def __init__(self,_location,_weight):
        self.location: 'Location' = _location
        self.weight  : float    = _weight

    def __repr__(self):
        return "for:{0},{1}kg.".format(self.location,self.weight)