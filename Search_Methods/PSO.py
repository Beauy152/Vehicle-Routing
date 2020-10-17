from math import sqrt
from random import randint,choice
#from queue import PriorityQueue
from genericFunctions import CalcDistance2,CalcDistance3

class Temp_Vehicle:
    def __init__(self,_xr,_yr,_r,_w):
        self.xref = _xr
        self.yref = _yr
        self.r    = _r
        self.route = []

        self.capacity = 0
        self.max_capacity = _w

    def sumRoute(self):
        if self.route == None or len(self.route) < 1:return None
        else:
            dsum = 0
            for i in range(len(self.route)):
                if i == len(self.route)-1:return dsum
                aStartLoc = self.route[i]
                aEndLoc = self.route[i+1]
                dsum += sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )
        

class Position():#essentially a vector
    def __init__(self,x,y):
        self.X = x; self.Y = y
    
    def __add__(self,aOther):
        """Magic method for adding two vectors"""
        if type(self)==Position and type(aOther) == Position:
            return Position(self.X+aOther.X,self.Y+aOther.Y)
        else:
            raise TypeError("Mistmach {0} and {1}".format(type(self),type(aOther)))

class Particle():
    def __init__(self,X,Y,R,capacity=15):
        self.pos = Position(X,Y)
        self.R = R

        self.Velocity = Position(0,0)#0.0
        #self.inertia = 0.47
        self.pbest = self.pos  # best pos visited by current particle
        self.pbest_fitness = None
        self.lbest = None # best pos visited by any particle
        self.lbest_fitness = None


        self.maxCapacity = capacity
        self.capacity = 0

        self.vehicles = []

        self.dimensions = [] #3m dimensions max

        self.fitness = 0
    def __repr__(self):
        return "X:{0},Y:{1}".format(self.X,self.Y)
# class Swarm():
#     def __init__(self):
#         self.P = [] # set of best positions from each particle / local best
#         self.gbest = None # best pos visited by all particles
# def CalcDistance(aStartLoc, aEndLoc):
#     return sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )


class PSO:
    def __init__(self,Master,width,height):
        self.width = width
        self.height= height
        #c1 = 1.5
        #c2 = 2.5 both sum to 4
        #Randomly initialise particle position
        self.Master = Master
        self.world = Master.getField('world')

    def initSwarm(self,population):
        """Generate array of particles w/random x,y coordinates"""#maybe this radiuss value is tweakable
        return [ Particle(randint(0,self.width), randint(0,self.height),randint(50,self.width))
                for p in range(population) ]


    def performance(self,particle,t):
        #Fitness : total cost of routes

        fitness = 0
        for v in particle.vehicles:
            fitness += v.sumRoute()
        
        particle.fitness = fitness

        if t == 0:
            particle.pbest_fitness = fitness
    def decode(self,particle,vehicles):
        #xref,yref,r = None # temporary?
        #the above three vals are the particles dimensions for each vehicle


        #This will need to be refactored, its not 100% correct (I think)
        #Extract Vehicle Properties
        for v in vehicles:
            particle.vehicles.append(
                Temp_Vehicle( particle.pos.X,
                              particle.pos.Y,
                              particle.R,
                              v.capacity
                )
            )


        #Route Construction
        locations = list(self.world.locations)
        for v in particle.vehicles:
            #a. Construct Route
            
            in_radius = []
            out_radius = []
            temp_route = []
            for l in locations:
                dist = CalcDistance3(v.xref,v.yref,l)
                if dist > v.r:
                    #appended as (l,d); d = distance from ref to l
                    out_radius.append((l,dist))
                else:
                    in_radius.append((l,dist))

            in_radius.sort(key=lambda x:x[1])#i:0 smallest, i:n largest
            out_radius.sort(key=lambda x:x[1],reverse=True)


            for l in in_radius:#list is pre sorted, therefore shorest distance is prioritised
                #append location if locations package weight + vehicles current weight 
                #do not exceed vehicle max weight
                if v.capacity + l[0].GetPackageWeight() <=  v.max_capacity:
                    v.route.append(l[0])
                    v.capacity += l[0].GetPackageWeight()
                    locations.remove(l[0])
                else:
                    break#pass
        
            #b. Optimise partial route
            #x = 1
            #2-opt
            #1-1 exchange
            #1-0 exchange

            #c. insert remaining customers
            #prioritise furthest location / 
            for l in out_radius:#list is pre sorted, therefore shorest distance is prioritised
                #append location if locations package weight + vehicles current weight 
                #do not exceed vehicle max weight
                if v.capacity + l[0].GetPackageWeight() <=  v.max_capacity:
                    v.route.append(l[0])
                    v.capacity += l[0].GetPackageWeight()
                    locations.remove(l[0])
                else:
                    break#pass

            #consider best insert position?
            #d. optimise routes with local improvemetn procedures
            #2-opt
            #1-1 exchange
            #1-0 exchange


            
        #y = 1
            
                   


    def run(self):
        #1. Initialise
        iterations = 10     #T=1000
        swarm = self.initSwarm( 20 )#I=50 #self.Master.getField('num_locations') )
        gbest_fitness = 100000#arbitrary
        gbest = None
        #t = 1
        #Iterate
        for t in range(iterations):

            #2.Decode
            for p in swarm:
                self.decode(p,self.Master.getField('vehicles'))
                #self.decode(p,p.pbest,self.Master.getField('vehicles'))

            #3. compute performance func of R_i for particles i=1..n
            for p in swarm:
                self.performance(p,t)
                #self.performance(p.pbest)

            #4. update pbest:
            for p in swarm:
                if p.fitness < p.pbest_fitness:
                    p.pbest_fitness = p.fitness
                    p.pbest = p.pos

                #5. update gbest
                if p.pbest_fitness < gbest_fitness:
                    gbest_fitness = p.pbest_fitness
                    gbest = p.pbest

            #6. Update lbest
            #neighbours = 5

            for p in swarm:
                K = 5 # neighbours
                sortedl = list(swarm) 
                sortedl.sort(key=lambda x: CalcDistance2(p.pos,x.pos) )
                
                neighbours = sortedl[:5]
                neighbours.sort(key=lambda x: x.pbest_fitness)

                for n in neighbours:
                    n.lbest = neighbours[0].pbest
                    n.lbest_fitness = neighbours[0].pbest_fitness


            #7. Generate nbest
            
        




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