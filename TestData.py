#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#TestData.py

from random import choice,randint
from DeliveryAgent import DeliveryAgent
from Packages import Package 
from gui_functions import COL_LIST

def TestLocations():
    """Returns location data from google or-tools example"""
    return [(456, 320), # location 0 - the depot
            (228, 0  ), # location 1
            (912, 0  ), # location 2
            (0  , 80 ), # location 3
            (114, 80 ), # location 4
            (570, 160), # location 5
            (798, 160), # location 6
            (342, 240), # location 7
            (684, 240), # location 8
            (570, 400), # location 9
            (912, 400), # location 10
            (114, 480), # location 11
            (228, 480), # location 12
            (342, 560), # location 13
            (684, 560), # location 14
            (0  , 640), # location 15
            (798, 640)] # location 16

def TestVehicles(n=5):
    """if n is unspecifed, default is 5,
    n being the number of delivery agents"""
    vehicles = []

    for _id in range(n):
        capacity = randint(50,100)
        agent = DeliveryAgent(_id,0,0,capacity,COL_LIST[_id])
        vehicles.append( agent )#pos=(0,0) : all vehicles start at depot

    return vehicles
