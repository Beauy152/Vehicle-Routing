from abc import ABC, abstractmethod
from entities.new_vehicle import DeliveryAgent
from entities.new_mapping import Location
from entities.new_package import Package

class Approach(ABC):
    def __init__(self,settings:dict[str,any],vehicles:list[DeliveryAgent],
                locations:list[Location],depot:Location,packages:list[Package]) -> None:
        self.settings = settings
        self.vehicles = vehicles
        self.locations= locations
        self.depot    = depot
        self.packages = packages

    @abstractmethod
    def run():
        pass