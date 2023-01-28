from approach.approachBaseFactory import ApproachFactory
from approach.approaches.aco import ACOFactory
from approach.approaches.pso import PSOFactory
from entities.new_package import Package
from entities.new_vehicle import DeliveryAgent
from entities.new_mapping import Location,LocationTypes

class Model:
    def __init__(self):
        self._approach  : ApproachFactory      = None
        self._settings  : dict[str,any]        = {}
        self._vehicles  : list[DeliveryAgent]  = None
        self._locations : list[Location]       = None
        self._packages  : list[Package]        = None 
        self._depot     : Location             = None

    @property
    def settings(self) -> dict[str,any]:
        return self._settings

    @settings.setter
    def settings(self, value:dict[str,any]) -> None:
        self._settings.update(value)

    @property
    def vehicles(self) -> dict[str,any]:
        return self._vehicles

    @vehicles.setter
    def vehicles(self, value:list[DeliveryAgent]) -> None:
        self._vehicles = value
    
    @property
    def locations(self) -> list[Location]:
        return self._locations

    @locations.setter
    def locations(self, value:list[Location]) -> None:
        self._locations = value

    @property
    def packages(self) -> list[Package]:
        return self._packages

    @packages.setter
    def packages(self, value:list[Package]) -> None:
        self._packages = value

    @property
    def depot(self) -> Location:
        return self._depot

    @depot.setter
    def depot(self, value:Location) -> None:
        self._depot = value

    @property
    def approach(self) -> ApproachFactory:
        return self._approach

    @approach.setter
    def approach(self, value:str) -> None:
        match self.settings.get('method'):
            case 'aco':
                self._approach = ACOFactory()
            case 'pso_s1':
                self._approach = PSOFactory()
            case 'pso_s2':
                self._approach = PSOFactory()
            case _:
                self._approach = ACOFactory()
            # case 'test':
            #     self.approach = PSOFactory()
    # def save(self):

    #     with open('emails.txt', 'a') as f:
    #         f.write(self.email + '\n')

