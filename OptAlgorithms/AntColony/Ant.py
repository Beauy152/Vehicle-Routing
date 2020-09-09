#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#Ant.py


from RouteMap import Location
class Ant():
    def __init__(self, aLocation : Location, aPherDelta, aAntCapacity):
        #Ants current location
        self.Location = aLocation
        #Pheremone delta increase
        self.PherDelta = aPherDelta
        #Vehicle capacity constraint
        self.AntCapacity = aAntCapacity
        #Array of locations in best route
        self.BestRoute = []
        #Array of locations in current route
        self.CurrentRoute = []

    def CalculateMove(self):
        #Method of movement calculation
        lBestMove = None
        for lNeighbor in self.Location.neighbours:
            #IMPLEMENT FORMULA FOR FITNESS FUNCTION
            #UPDATE BEST MOVE IF FUNCTION EVALUATES HIGHER

        #Update route
    def UpdateLocal(self): 
        #Update local pheremone

        #IMPLEMENT PHEREMONE UPDATE FORMULA

    def UpdateBest(self):
        #Update best route 
        
        
