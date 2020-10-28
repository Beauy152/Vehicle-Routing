from math import sqrt
from random import randint,choice
#from queue import PriorityQueue
from genericFunctions import CalcDistance2,CalcDistance3,CalcDistance4,SumRouteWeight,\
CalcDimensionalDistance,SumRouteDistance




def two_opt(p,route):
    def swap(r,i,j):
        new_route = r[0:i-1]
        temp = r[i:k];temp.reverse()
        new_route.extend(temp)
        new_route.extend(r[k+1:])

        return new_route

    #route
    n = len(route)
    baseline = SumRouteDistance(route)

    for i in range(1,n-2):
        for k in range(i+2,n):
            new_route = swap(route,i,k)
            new_baseline = SumRouteDistance(new_route)
            if new_baseline < baseline:
                route = new_route
                baseline = new_baseline
                break
        #break

    return route

    # baseline = SumRouteDistance(route)
    # new_route = route.copy()

    # n = len(new_route)-1#-2#2 for depots

    # for i in range(1,n-2):
    #     for j in range(i+2,n):
    #         #2.a
    #         new_route[i],new_route[i+1] = new_route[j],new_route[j+1]
    #         #2.b
    #         new_baseline = SumRouteDistance(route)
    #         if new_baseline < baseline:
    #             baseline = new_baseline
    #             route[:] = new_route
    #         else:
    #             new_route = route.copy()
    # return route


# def one_zero_exchange(p,route1,route2):
#     n = len(route1) #- 2
#     m = len(route2) #- 2
#     delta = 10#ten meters added as delta value
#     #baseline1 = SumRouteDistance(route1)#+delta
#     baseline_weight1 = SumRouteWeight(route1)
#     #baseline2 = SumRouteDistance(route2)#+delta
#     baseline_weight2 = SumRouteWeight(route2)
#     baseline = SumRouteDistance(route1) + SumRouteDistance(route2)

#     new_r1 = route1.copy()
#     new_r2 = route2.copy()

#     for i in range(1,n-1):
#         for j in range(1,m-2):#starting from 1 and ending at m-1 allows us to skip the depot
#             temp_l = new_r1.pop(i)
#             new_r2.insert(j+1,temp_l)
#             new_baseline = SumRouteDistance(new_r1) + SumRouteDistance(new_r2)
#             if ( new_baseline < baseline )  \
#                 and ((SumRouteWeight(new_r1) <= baseline_weight1) and (SumRouteWeight(new_r2) <= baseline_weight2)):
#                 #distance is shorter, and weight distrubution is better or the same
#                 route1[:] = new_r1
#                 route2[:] = new_r2
#                 baseline = SumRouteDistance(route1) + SumRouteDistance(route2)
#                 baseline_weight1 = SumRouteWeight(route1)
#                 #baseline2 = SumRouteDistance(route2)
#                 baseline_weight2 = SumRouteWeight(route2)
#             else:
#                 new_r1 = route1.copy()
#                 new_r2 = route2.copy()


# def one_one_exchange(p,route1,route2):
#     n = len(route1)
#     # n = len(route1) #- 2
#     # m = len(route2) #- 2

#     # delta = 10#ten meters added as delta value
#     # #baseline1 = SumRouteDistance(route1)#+delta
#     # baseline_weight1 = SumRouteWeight(route1)
#     # #baseline2 = SumRouteDistance(route2)#+delta
#     # baseline_weight2 = SumRouteWeight(route2)
#     # baseline = SumRouteDistance(route1) + SumRouteDistance(route2)

#     # new_r1 = route1.copy()
#     # new_r2 = route2.copy()

#     # for i in range(1,n-1):
#     #     for j in range(1,m-2):
#     #         new_r1[i],new_r2[j] = new_r2[j],new_r1[i]
#     #         #3.a
#     #         new_baseline = SumRouteDistance(new_r1) + SumRouteDistance(new_r2)
#     #         if ( new_baseline < baseline ) \
#     #             and ((SumRouteWeight(new_r1) <= baseline_weight1) and (SumRouteWeight(new_r2) <= baseline_weight2)):
#     #             #distance is shorter, and weight distrubution is better or the same
#     #             route1[:] = new_r1
#     #             route2[:] = new_r2
#     #             baseline = SumRouteDistance(route1) + SumRouteDistance(route2)
#     #             baseline_weight1 = SumRouteWeight(route1)
#     #             #baseline2 = SumRouteDistance(route2)
#     #             baseline_weight2 = SumRouteWeight(route2)
#     #         else:
#     #             new_r1 = route1.copy()
#     #             new_r2 = route2.copy()

#     #one_one_exchange()
#     #one_zero_exchange()
    

class Faux_Vehicle():
    def __init__(self,xref,yref,radius,max_capacity):
        self.xref = xref
        self.yref = yref
        self.radius = radius
        self.capacity = 0
        self.max_capacity = max_capacity
        self.route = []

class Particle():
    def __init__(self,vehicles,width,height,locations,capacity=15):
        #self.velocity = 0
        self.fitness = None
        self.pbest_fitness = None
        self.lbest_fitness = None
        self.nbest_fitness = None

        self.neighbours = []
        self.routes = [] #should be array of arrays?

        self.capacity = 0
        self.max_capacity = capacity

        self.dimensions = []
        for v in vehicles:
            self.dimensions.append(randint(1,width))#xref
            self.dimensions.append(randint(1,height))#yref
            self.dimensions.append(randint(int(width/3),int(width/2)))#radius
                    
        self.velocity = [0] * (3 * len(vehicles))

        self.pbest = self.dimensions.copy()
        self.lbest = None
        self.nbest = None
        self.penalty = 0# a multiplier of some kind for not visiting all locations
        

    def updateGbest(self):
        pass

    def updatePbest(self):
        if self.fitness < self.pb.fitness:#current fitness < best fitness
            self.pb = self.pos#.copy()

    def calculateNbest(self):
        #TODO THis will need to be thoroughly looked over
        top_term = self.fitness - self.pbest_fitness # top term of division in equation
        nbest = []
        for d in range(len(self.dimensions)):


            #average the values of all neighoburs OR
            #get neighobur with best value
            #for n in self.neighbours
            try:
                neighbour_fdr = [( (self.fitness - n.pbest_fitness)/(abs( self.dimensions[d] - n.pbest[d])) ,n) \
                                for n in self.neighbours]
            except ZeroDivisionError:
                #BUG divide by zero bug when both same value. maybe set to 1, or set to one of their inital values
                neighbour_fdr =  [( (self.fitness - n.pbest_fitness)/ self.dimensions[d] ,n) \
                                for n in self.neighbours]
            best_fdr = min(neighbour_fdr,key=lambda x:x[0])
            nbest.append(best_fdr[1].pbest[d])
        
        self.nbest = nbest


    def calculate_fitness(self,routes,penalty):
        #return SumRouteDistance(route)
        total_sum = 0
        for route in routes:
            total_sum += SumRouteDistance(route)


        return total_sum + (penalty * 50)#adding penalty for missing locations

    def decode(self,dimensions,vehicle,world,local_improvement):
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

            
            location_distances = [ (CalcDistance3(xref,yref,l),l) for l in world.locations if l not in visited]
            in_radius = [l for l in location_distances if l[0] <= radius]

            in_radius.sort(key=lambda l:l[0])

            for l in in_radius:
                if l[1].package_sum + SumRouteWeight(route) <= v.capacity:
                    route.append(l[1])
                    visited.append(l[1])


            
            #visited.extend(route)                                      #add to visited
            route.insert(0,world.depot[0]);route.append(world.depot[0])#add depots to route
            V.route = route
            routes.append(route)
        #2.b optimise partical routes
        if local_improvement: self.local_improvements(routes)
            
        #2.c insert remaining customers
        remaining = [l for l in world.locations if l not in visited]
        remaining.sort( key=lambda x: CalcDistance2( x,world.depot[0] ), reverse=True )

        for l in remaining:
            vehicles.sort(key=lambda x:CalcDistance3(x.xref,x.yref,l))
            for v in vehicles:#now ordered by closest to location
                if (l.package_sum + SumRouteWeight(v.route) <= v.max_capacity) and l not in visited:
                    if len(v.route) == 2:v.route.insert(-1,l)
                    else: v.route.insert(-2,l)
                    visited.append(l)
                    break


        #2.d re-optimise
        #self.local_improvements(routes)
        # #add a pentalty for this particle
        #this essentially ensures that any particle that does not visit all locations, will never be the best
        remaining = [l for l in world.locations if l not in visited]
        penalty = len(remaining) * 1000#50

        # self.local_improvements(routes)
        if local_improvement: self.local_improvements(routes)
        #print(len([l for l in world.locations if l not in visited]))

        return (routes,penalty)


    def local_improvements(self,routes):
        for route in routes:
            route = two_opt(self,route)
        


        # routes.sort(key=lambda x:SumRouteDistance(x))

        # n = len(routes)
        # I = int(n/2)#to find mid poiunt
        # n -= 1
        # for i in range(0,I):
        #     if i == n-i: 
        #         one_one_exchange(self,routes[i],routes[i+1])
        #     else:
        #         one_one_exchange(self,routes[i],routes[n-i])

        # for i in range(0,I):
        #     if i == n-i: 
        #         one_zero_exchange(self,routes[i],routes[i+1])
        #     else:
        #         one_zero_exchange(self,routes[i],routes[n-i])

        # for i in range(len(routes)-1):
        #     one_one_exchange( self, routes[i],routes[i+1] )
        
        # for i in range(len(routes)-1):
        #     one_zero_exchange( self, routes[i],routes[i+1] )


    def __repr__(self):
        return "X:{0},Y:{1}".format(self.X,self.Y)


class Swarm():
    def __init__(self,population,vehicles,width,height,locations):
        self.vehicles = vehicles
        #self.local_improvement = local_improvement
        self.particles = [ Particle(vehicles,width, height,locations)#,choice([i.capacity for i in vehicles]))
                for p in range(population) ]

        #self.gbest = None

    def evaluateNbest(self):
        for p in self.particles:
            p.calculateNbest()


    def evaluateLbest(self,K=5):
        for p in self.particles:
            #Get Neighbours
            neighbours = [n for n in self.particles if n != p]
            neighbours.sort(key=lambda x: CalcDimensionalDistance(p.pbest,x.pbest))#sort closest to furthest
            p.neighbours = neighbours[:K]#take only the K-closest

            neighbours.append(p)#append so we can easily set lbest for all


        lbest_particle = min(neighbours,key=lambda x: x.pbest_fitness)
        for n in neighbours:
            n.lbest = lbest_particle.pbest
            n.lbest_fitness = lbest_particle.pbest_fitness

        # _neighbours = self.particles.copy()
        # for p in self.particles:
        #     neighbours = _neighbours.copy()
        #     neighbours.sort(key=lambda x: CalcDimensionalDistance(p.dimensions) )

        #     neighbours = neighbours[:K+1]#+1 for self
        #     if p not in neighbours:
        #         neighbours.pop()#remove last item
        #         p.neighbors = neighbours
        #         neighbours.append(p)

        #     lbest_particle = min(neighbours,key=lambda x: x.fitness)
        #     for n in neighbours:
        #         pass#p.setLbest(lbest_particle)

    def evaluateGbest(self):
        best_particle = min(self.particles, key=lambda x: x.pbest_fitness)

        self.gbest = best_particle.pbest
        self.gbest_fitness = best_particle.pbest_fitness

    def evaluatePbest(self,world,local_improvement):
        for p in self.particles:
            pb_result = p.decode(p.pbest,self.vehicles,world,local_improvement)
            pb_route = pb_result[0]
            pb_penalty = pb_result[1]

            p.pbest_fitness = p.calculate_fitness(pb_route,pb_penalty)

            if p.fitness < p.pbest_fitness:
                p.pbest = p.dimensions
                p.pbest_fitness = p.fitness


                


    def evaluateRoute(self):
        for p in self.particles:
            p.fitness = p.calculate_fitness(p.routes,p.penalty)

    def updateParticles(self,t,T,xmax,xmin):
        cp = 0.5
        cg = 0.5
        cl = 1.5
        cn = 1.5
        w1 = 0.9
        wT = 0.4
        u  = randint(0,1)
        wt = wT + (t-T)/(1-T) * (w1 - wT)

        for p in self.particles:
            for d in range(len(p.dimensions)):
                #not plid is referenced in the equations, but i don't know what that is
                p.velocity[d] = wt*p.velocity[d]+ \
                                    cp*u*(p.pbest[d]    - p.dimensions[d] ) + \
                                    cg*u*(self.gbest[d] - p.dimensions[d] ) + \
                                    cl*u*(p.lbest[d]    - p.dimensions[d] ) + \
                                    cn*u*(p.nbest[d]    - p.dimensions[d] )

                p.dimensions[d] = p.dimensions[d] + p.velocity[d]
                if p.dimensions[d] > xmax:
                    p.dimensions[d] = xmax
                    p.velocity[d] = 0
                
                if p.dimensions[d] < xmin:
                    p.dimensions[d] = xmin
                    p.velocity[d] = 0

    def decode(self,world,local_improvement):
        for p in self.particles:#for i in range(len(self.particles)): #careful when indexing. we cannot start at 0. range(0->max)
            result = p.decode(p.dimensions,self.vehicles,world,local_improvement)
            p.routes = result[0]
            p.penalty = result[1]


class PSO:
    def __init__(self,Master,width,height,local_improvements):
        self.width = width
        self.height= height
        #c1 = 1.5
        #c2 = 2.5 both sum to 4
        #Randomly initialise particle position
        self.Master = Master
        self.world = Master.getField('world')
        #self.world.locations = self.world.locations 
        self.vehicles = self.Master.getField('vehicles')
        self.local_improvement = local_improvements#boolean
        #self.initSwarm( 20 )#I=50 #self.Master.getField('num_locations') )




    def performance(self,particle,t):
        #Fitness : total cost of routes

        fitness = 0
        for v in particle.vehicles:
            fitness += v.sumRoute()
        
        particle.pos.fitness = fitness

        if t == 0:
            particle.pb.fitness = fitness



    def AssignRoutes(self,routes):
        for i in range(len(self.vehicles)):
            self.vehicles[i].route = routes[i]
            # self.vehicles[i].route.append(self.world.depot[0])
            # self.vehicles[i].route.insert(0,self.world.depot[0])

    def run(self,population=25,iterations = 250):
        #9. Stopping criteria
        K = 5 #num of neighbours; arbirary value
        T = iterations
        #
        print("--Particle Swarm Optimisation--\n--Local Improvements:%s--\nT(%s) P(%s)" % (self.local_improvement,iterations,population)) 
        for t in range(1,T):
            #inertia = 0.4 + ( ((t-1)-T) / (1-T) ) * (0.9 - 0.4)
            #1. Initialise
            vehicles = self.vehicles

            swarm = Swarm(population, vehicles,self.width,self.height,self.world.locations)       

            #2. Deocode
            swarm.decode(self.world,self.local_improvement)

            #3. Compute Performance measure for each particle
            swarm.evaluateRoute()

            #4. Update pbest
            swarm.evaluatePbest(self.world,self.local_improvement)

            #5. Update gbest
            swarm.evaluateGbest()

            #6. Update lbest
            swarm.evaluateLbest(K)

            #7. Generate nbest
            swarm.evaluateNbest()

            #8. Update Velocity
            swarm.updateParticles(t,T,self.width,1)


        #
        #print("Decoding final routes:")
        #10. Decode final solution
        p = Particle(vehicles,self.width,self.height,self.world.locations)
        p.dimensions = swarm.gbest
        p.fitness = swarm.gbest_fitness

        final_routes = p.decode(p.dimensions,vehicles,self.world,self.local_improvement) 

        self.AssignRoutes(final_routes[0])

        #return route sum
        #return 
        