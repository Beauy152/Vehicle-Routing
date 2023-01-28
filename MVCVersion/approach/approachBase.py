from abc import ABC, abstractmethod
from entities.new_vehicle import DeliveryAgent
from entities.new_mapping import Location
from entities.new_package import Package

class Approach(ABC):
    @abstractmethod
    def run(self,settings:dict[str,any],vehicles:list[DeliveryAgent],
                locations:list[Location],depot:Location,packages:list[Package]):
        pass