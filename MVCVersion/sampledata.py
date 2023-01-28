from entities.new_package import Package
from entities.new_vehicle import DeliveryAgent
from entities.new_mapping import Location,LocationTypes
from random import randint,sample,choice

from GUI.consts import COL_LIST

def testLocations() -> tuple[Location,list[Location]]:
    """Returns a depot & list of locations based on Google's
        OR-Tools standard for C-VRP."""
    depot  = Location(456, 320,LocationTypes.depot)
    coords =[(228, 0  ),(912, 0  ),(0  , 80 ),(114, 80 ),
            (570, 160),(798, 160),(342, 240),(684, 240),
            (570, 400),(912, 400),(114, 480),(228, 480),
            (342, 560),(684, 560),(0  , 640),(798, 640)]
    
    return depot,[Location(*l) for l in coords]

def testVehicles() -> list[DeliveryAgent]:
    return [
    # TODO: Make these colours customisable
    DeliveryAgent(0,15,'blue'),
    DeliveryAgent(1,15,'yellow'),
    DeliveryAgent(2,15,'green'),
    DeliveryAgent(3,15,'red')
] 

def RandomLocations(n:int=16) -> tuple[Location,list[Location]]:
    """generate n random locations"""
    locations: list[Location] = []
    depot    : Location = None

    depot_index = randint(0,n-1)

    for i in range(n):
        if (i == depot_index):
            depot = Location(randint(0,1000) ,randint(0,1000),LocationTypes.depot)
        else:
            locations.append(Location(randint(0,1000) ,randint(0,1000)))

    return depot, locations

def RandomVehicles(n:int=5) -> list[DeliveryAgent]:
    """if n is unspecifed, default is 5,
    n being the number of delivery agents"""
    vehicles: list[DeliveryAgent] = []

    COLS = sample(COL_LIST,n)
    for _id in range(n):
        capacity = randint(50,100)
        agent = DeliveryAgent(_id,capacity,COLS[_id])
        vehicles.append( agent )#pos=(0,0) : all vehicles start at depot

    return vehicles

def GeneratePackages(total_capacity:int,locations) -> list[Package]:
    """Create a list of packages, with a max weight
    of no more than the combined carry capacity of
    all delivery agents"""
    Packages: list[Package] = []
    remaining_capacities = total_capacity
    while remaining_capacities > 0:
        rand_weight = randint(1,25)
        if (remaining_capacities - rand_weight) < 0:
            rand_weight = remaining_capacities
            break
        else:
            remaining_capacities = remaining_capacities - rand_weight
            
        Packages.append( 
            Package( choice(locations),rand_weight) )

    return Packages

def TestPackages(Locations:list[Location]) -> list[Package]:
    """Google or tools example package data"""
    Packages :list[Package] = []
    data = [1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]

    # for i,value in enumerate(data):
    #     Packages.append( Package(Locations[i], value) )
    for i in range(len(data)):
        Packages.append(Package(
            Locations[i],
            data[i] ) )

    return Packages

def packageListParser(filename:str,locations) -> list[Package]:
    """Opens and parses given file as input package list"""
    with open(filename,'r') as file:
        weights = [int(line) for line in file]

        packages = []
        for i,location in enumerate(locations): 
            packages.append(
                Package(location,weights[i])
            )

    return packages

