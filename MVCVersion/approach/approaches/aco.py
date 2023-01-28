from approach.approachBase import Approach
from approach.approachBaseFactory import ApproachFactory

class ACOApproach(Approach):
    def run(self,settings,vehicles,locations,depot,packages):
        print("This si the ACO Approach")
    

class ACOFactory(ApproachFactory):
    def factory_method(self) -> Approach:
        return ACOApproach()