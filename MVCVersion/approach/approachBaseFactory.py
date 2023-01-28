from abc import ABC, abstractmethod
from entities.new_vehicle import DeliveryAgent
from entities.new_mapping import Location
from entities.new_package import Package

class ApproachFactory(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def runApproach(self,settings:dict[str,any],vehicles:list[DeliveryAgent],
                locations:list[Location],depot:Location,packages:list[Package]) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        apporach = self.factory_method()
        # Now, use the product.
        result = apporach.run(settings,vehicles,locations,depot,packages)
        return result

