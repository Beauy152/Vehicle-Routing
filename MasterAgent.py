from HelperFunctions import ParseKIF

class MasterRouter():
    KB = {} #Knowledge base. vehicle information

    def __init__(self):
        pass

    def RouteAlgorithm(self):
        """Route finding algorithm goes here.
        a modular approach allows us to easily 
        implement multiple Routing methods"""
        pass

    # def publishRoutes(self):
    #     """Maybe Redundant? send route data to vehicles """
    #     pass

    # def draw(self):
    #     pass

    def AskIf(self):
        """Send inquiry to agent"""
        pass
    
    def Tell(self,sender,content):
        """Send knowledge/data to agent"""
        # self.KB.update({:})
        print("from:{0} to:{1} - {2}".format(sender,"master",content))
        command = ParseKIF(content)#format: [operator,[atrribute,object],value]
        print(command)
        for i in command:
            print(i)

        # print(command[1][1])
        # print(command[1][0])

        if(command[0] == '='):  
            self.KB.update({
                (command[1][1]) :{
                    (command[1][0]) : command[2]
                    }
                })
        print(self.KB)


    def Reply(self):
        """Reply to agent"""
        pass

    def Perform(self):
        """maybe not useful"""
        pass

    # def Broadcast(self):
    #     """send communication to all known agents"""
    #     pass
