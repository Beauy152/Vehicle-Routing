from HelperFunctions import ParseKIF

class MasterRouter():
    KB = {} #Knowledge base. vehicle information

    def __init__(self):
        self.id = "Master"

    def RouteAlgorithm(self):
        """Route finding algorithm goes here.
        a modular approach allows us to easily 
        implement multiple Routing methods"""
        pass

    def SumCapacities(self):
        """any KB entry with prefix v_ is a vehicle, sum each capacity attribute"""
        capacity_sum = 0
        for key in self.KB.keys():
            if key[0:2] == "v_":
                capacity_sum = capacity_sum + int(self.KB[key]['capacity'])
        self.KB.update({"g_":capacity_sum})

        return capacity_sum
    # def publishRoutes(self):
    #     """Maybe Redundant? send route data to vehicles """
    #     pass

    # def draw(self):
    #     pass

    def Ask(self):
        """Send inquiry to agent"""
        pass
    
    def Tell(self,sender,content):
        """Send knowledge/data to agent"""
        command = ParseKIF(content)#format: [operator,[atrribute,object],value]

        if(command[0] == '='):  
            self.KB.update({
                (command[1][1]) :{
                    (command[1][0]) : command[2]
                    }
                })


    def Reply(self):
        """Reply to agent"""
        pass

    def Perform(self,command):
        """maybe not useful"""
        """Can't find implementation examples?
        Currently just accepts a command and tries to exec() it"""
        try:
            return eval("self."+command+"()")
        except AttributeError as e:
            return "%s tried to 'Perform' and invalid action." % self.id
        

    # def Broadcast(self):
    #     """send communication to all known agents"""
    #     pass
