#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#MasterAgent.py

from HelperFunctions import ParseKIF
from RouteMap import RouteMap as Map

class MasterRouter():
    KB = {} #Knowledge base. vehicle information

    def __init__(self):
        self.id = "m_"
        self.packages = None

    def RouteAlgorithm(self):
        """Route finding algorithm goes here.
        a modular approach allows us to easily 
        implement multiple Routing methods"""
        pass

    def SetWorld(self,depot,locations):
        self.world = Map(depot,locations)

    def SumCapacities(self):
        """any KB entry with prefix v_ is a vehicle, sum each capacity attribute"""
        capacity_sum = 0
        for key in self.KB.keys():
            if key[0:2] == "v_":
                capacity_sum = capacity_sum + int(self.KB[key]['capacity'])
        self.KB.update({"m_":{
            "total_capacity":capacity_sum
        }})

        return capacity_sum
    # def publishRoutes(self):
    #     """Maybe Redundant? send route data to vehicles """
    #     pass

    # def draw(self):
    #     pass

    def Ask(self,content):
        """Send inquiry to agent"""
        command = ParseKIF(content)
        if(len(command) == 2 ): #if len=2 basic query for a value 
            try:
                return self.KB[command[1]][command[0]]
            except KeyError as e:
                return "{0} could not perform query:{1}".format(self.id,content)
            
        
    def Tell(self,sender,content):
        """Adds knowledge to KB"""
        command = ParseKIF(content)#format: [operator,[atrribute,object],value]

        if(command[0] == '='):  
            self.KB.update({
                (command[1][1]) :{
                    (command[1][0]) : command[2]
                    }
                })

    def SetPackages(self,_packages):
        self.packages = _packages

    def Perform(self,command):
        """maybe not useful"""
        """Can't find implementation examples?
        Currently just accepts a command and tries to exec() it"""
        try:
            return eval("self."+command+"()")
        except AttributeError as e:
            return "%s tried to 'Perform' and invalid action." % self.id
