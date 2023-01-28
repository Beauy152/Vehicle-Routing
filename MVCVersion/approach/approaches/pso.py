from approach.approachBase import Approach
from approach.approachBaseFactory import ApproachFactory

class PSOApproach(Approach):
    def run(self,settings,vehicles,locations,depot,packages):
        v= vehicles[0]
        for location in locations:
            v.route.append(location)
        print("This si the PSO Approach")
        
    

class PSOFactory(ApproachFactory):
    def factory_method(self) -> Approach:
        return PSOApproach()