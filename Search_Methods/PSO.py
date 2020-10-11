
from random import randint

class Particle():
    def __init__(self,X,Y,capacity):
        self.X = X
        self.Y = Y
        self.Velocity = 0.0
        #self.inertia = 0.47
        self.pbest = None  # best pos visited by current particle
        self.gbest = None # best pos visited by any particle

    def __repr__(self):
        return "X:{0},Y:{1}".format(self.X,self.Y)
# class Swarm():
#     def __init__(self):
#         self.P = [] # set of best positions from each particle / local best
#         self.gbest = None # best pos visited by all particles

class PSO:
    def __init__(self,Master,width,height,population=20):
        self.width = width
        self.height= height
        self.population = population
        #c1 = 1.5
        #c2 = 2.5 both sum to 4
        #Randomly initialise particle position
        self.Master = Master
        #self.swarm = [Particle( randint(0,width),randint(0,height) ) for i in range(population)]

    def randomSwarm(self,capacity):
        return  [Particle( randint(0,self.width),
                           randint(0,self.height),
                           capacity)
                for i in range(self.population)]

    def greedyInitialRoutes(self):
        for Vehicle in self.Master.getField('vehicles'):
            swarm = randomSwarm(Vehicle.capacity)



    def run(self):
        """return """
        pass
        #loop this
        #eval each particles position according to objective function

        #if particles current pos is better than it's previous best, update it





#generate inital solutions
#encoding vectors for each particle
#get pertsonal & global best
#execute the survival sub-swarms adaptive pso-vb algorithm  <-
#generate new solution (Decoding)                            |
#executew local improvement heuristics                      |
#update personal & global best                             |
#                                                         |
#stopping condition met? ---- no ------------------------|
#     |
#   YES
#    |
#   END