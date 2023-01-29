
from random import randint
from entities.new_mapping import Location
from approach.approaches.pso.fauxVehicle import Faux_Vehicle
from genericFunctions import CalcDistance2, CalcDistance3, SumRouteWeight, two_opt, SumRouteDistance


class Particle():
    """Individual particle of swarm"""
    def __init__(self,vehicles,width,height,locations,capacity=15):
        self.fitness       = None
        self.pbest_fitness = None
        self.lbest_fitness = None
        self.nbest_fitness = None
        self.max_capacity  = capacity

        self.neighbours = []
        self.routes     = []
        self.capacity   = 0
        self.dimensions = []

        for v in vehicles: #3m dimensional representation, where m is number of vehicles
            self.dimensions.append(randint(1,width))#xref
            self.dimensions.append(randint(1,height))#yref
            self.dimensions.append(randint(int(width/3),int(width/2)))#radius
                    
        self.velocity = [0] * (3 * len(vehicles))

        self.pbest = self.dimensions.copy()#personal best, initially starting position
        self.lbest = None  #local best location
        self.nbest = None  #neighbourhood best location

        self.penalty = 0#multiplier for each missed location

    def updatePbest(self):
        """updates personal best to current position if it's fitness is better """
        if self.fitness < self.pb.fitness:
            self.pb = self.pos

    def calculateNbest(self):
        """determines personal best position of neighbours"""
        top_term = self.fitness - self.pbest_fitness # top term of division in equation
        nbest = []

        for d in range(len(self.dimensions)):
            #get neighobur with best value
            try:
                neighbour_fdr = [( (self.fitness - n.pbest_fitness)/(abs( self.dimensions[d] - n.pbest[d])) ,n) \
                                for n in self.neighbours]
            except ZeroDivisionError:
                #potenital BUG divide by zero bug when both same value. maybe set to 1, or set to one of their inital values
                neighbour_fdr =  [( (self.fitness - n.pbest_fitness)/ self.dimensions[d] ,n) \
                                for n in self.neighbours]
            best_fdr = min(neighbour_fdr,key=lambda x:x[0])
            nbest.append(best_fdr[1].pbest[d])
        
        self.nbest = nbest


    def calculate_fitness(self,routes,penalty):
        """Calculates fitness as sum of route distances
        + a penalty multiplier"""
        total_sum = 0
        for route in routes:
            total_sum += SumRouteDistance(route)

        return total_sum + (penalty * 10000)#adding penalty for missing locations

    def decode(self,dimensions,vehicle,locations,useLocalImprovement:bool):
        """Decoding takes a particles dimension (which relate to each vehicle),
        to predictably build a set of route of each vehicle, that adhere to
        capacity constraints"""
        visited = []
        routes = []

        d = 0
        vehicles = []
        for v in vehicle:
            xref = dimensions[d]
            yref = dimensions[(d+1)]
            radius = dimensions[(d+2)]
            V = Faux_Vehicle(
                            xref, yref, radius, v.capacity )
            vehicles.append(V)
            d += 3
            #2.a construct routes
            route = []

            #list of tuples (distance from v ref points to location,actual location object)
            location_distances = [ (CalcDistance3(xref,yref,l),l) for l in locations if l not in visited]
            #List of locations within vehicles radius
            in_radius = [l for l in location_distances if l[0] <= radius]

            #sort to give closest locations priority
            in_radius.sort(key=lambda l:l[0])

            for l in in_radius:
                if l[1].package_sum + SumRouteWeight(route) <= v.capacity:
                    route.append(l[1])
                    visited.append(l[1])

            route.insert(0,Location.depot);route.append(Location.depot)#add depots to route
            V.route = route
            routes.append(route)

        #2.b optimise partical routes
        #conditional route improvement
        if useLocalImprovement: self.useLocalImprovements(routes)
            
        #2.c insert remaining customers
        remaining = [l for l in locations if l not in visited]
        remaining.sort( key=lambda x: CalcDistance2( x,Location.depot ), reverse=True )

        for l in remaining:
            vehicles.sort(key=lambda x:CalcDistance3(x.xref,x.yref,l))
            for v in vehicles:#now ordered by closest to location
                if (l.package_sum + SumRouteWeight(v.route) <= v.max_capacity) and l not in visited:
                    if len(v.route) == 2:v.route.insert(-1,l)
                    else: v.route.insert(-2,l)
                    visited.append(l)
                    break


        #2.d re-optimise
        # #add a pentalty for this particle
        #this essentially ensures that any particle that does not visit all locations, will never be the best
        remaining = [l for l in locations if l not in visited]
        penalty = len(remaining)

        #conditional route improvement
        if useLocalImprovement: self.useLocalImprovements(routes)

        return (routes,penalty)

    def useLocalImprovements(self,routes):
        """apply two-opt algorithm to each route,
        to locally improve each"""
        for route in routes:
            route = two_opt(self,route)

    def __repr__(self):
        """Python representation function"""
        return "X:{0},Y:{1}".format(self.X,self.Y)
