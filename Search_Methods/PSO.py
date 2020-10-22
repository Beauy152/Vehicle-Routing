from math import sqrt
from random import randint,choice
#from queue import PriorityQueue
from genericFunctions import CalcDistance2,CalcDistance3,CalcDistance4,SumRouteWeight,CalcDimensionalDistance


# def CalcDistance(aStartLoc, aEndLoc):
#     return sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )



# class Temp_Vehicle:
#     def __init__(self,_xr,_yr,_r,_w):
#         self.xref = _xr
#         self.yref = _yr
#         self.r    = _r
#         self.route = []

#         self.capacity = 0
#         self.max_capacity = _w

#     def sumRoute(self):
#         if self.route == None or len(self.route) < 1:return None
#         else:
#             dsum = 0
#             for i in range(len(self.route)):
#                 if i == len(self.route)-1:return dsum
#                 aStartLoc = self.route[i]
#                 aEndLoc = self.route[i+1]
#                 dsum += sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )
        

# class Vector():#essentially a vector
#     def __init__(self,x,y,r,v,f):
#         self.X = x
#         self.Y = y
#         self.R = r
#         self.V = v
#         self.fitness = f
    
#     def __add__(self,aOther):
#         """Magic method for adding two vectors"""
#         if type(self)==Vector and type(aOther) == Vector:
#             return Vector(self.X+aOther.X,
#                           self.Y+aOther.Y,
#                           self.R+aOther.R,
#                           self.V+aOther.V,
#                           None)
#         else:
#             raise TypeError("Mistmach {0} and {1}".format(type(self),type(aOther)))

#     def __sub__(self,aOther):
#         """Magic method for adding two vectors"""
#         if type(self)==Vector and type(aOther) == Vector:
#             return Vector(self.X-aOther.X,
#                           self.Y-aOther.Y,
#                           self.R-aOther.R,
#                           self.V-aOther.V,
#                           None)
#         else:
#             raise TypeError("Mistmach {0} and {1}".format(type(self),type(aOther)))

class Particle():
    def __init__(self,vehicles,width,height,capacity=15):
        #self.velocity = 0
        self.fitness = None
        self.pbest_fitness = None
        self.lbest_fitness = None
        self.nbest_fitness = None

        self.neighbours = []
        self.routes = [] #should be array of arrays?

        self.capacity = 0
        self.max_capacity = capacity

        self.dimensions = [] # 3m; m = num vehicles
        for v in vehicles:
            self.dimensions.append(randint(1,width))#xref
            self.dimensions.append(randint(1,height))#yref
            self.dimensions.append(randint(int(width/6),int(width/2)))#radius
            
        self.velocity = [0] * (3 * len(vehicles))

        self.pbest = self.dimensions.copy()
        self.lbest = None
        self.nbest = None
        #self.pbest_pentaly = 0
        #self.pbest.routes = 0
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
                # if self.dimensions[d] == 0:
                #     se
                #BUG divide by zero bug when both same value. maybe set to 1, or set to one of their inital values
                neighbour_fdr =  [( (self.fitness - n.pbest_fitness)/ self.dimensions[d] ,n) \
                                for n in self.neighbours]
            best_fdr = min(neighbour_fdr,key=lambda x:x[0])
            nbest.append(best_fdr[1].pbest[d])
        
        self.nbest = nbest
            #bottom_term = abs( self.dimensions[d] - .dimensions[d]) #try without abs
        # results_d = []
        # for d in range(len(self.dimensions)): #For each dimension
        #     n = max(self.neighbours, key=lambda x: x.dimension[d])
        #     results_d.append(
        #         (self.pos.fitness - self.pb.pos.fitness) / \
        #         ( CalcDistance2(self.pos,n.pos) )
        #     )
        # results_d

    def calculate_fitness(self,routes,penalty):
        total_sum = 0
        for route in routes:
            for i in range(len(route)-1):
                if len(route) < 1 : break

                aStartLoc = route[i]
                aEndLoc = route[i+1]
                total_sum += sqrt( (aEndLoc.X - aStartLoc.X)**2 + (aEndLoc.Y - aStartLoc.Y)**2 )

        return total_sum + (penalty * 50)#adding penalty for missing locations

    def decode2(self,dimensions,vehicle,world):
        routes = []
        visited = []
        d = 0
        #1. Extract vehicle properties from dimensions
        for v in vehicle:#for d in range(len(self.dimensions)):
            self.capacity = 0
            xref = dimensions[d]
            yref = dimensions[(d+1)]
            radius = dimensions[(d+2)]
            d += 3
        
            #2.a Construct Routes
            route = []
            location_distances = [ (CalcDistance3(xref,yref,l),l) for l in world.locations]
            in_radius = [l for l in location_distances if l[0] <= radius]
            out_radius = [l for l in location_distances if l[0] > radius]

            in_radius.sort(key=lambda l:l[0])
            out_radius.sort(key=lambda l:l[0], reverse=True)
            #2.1
            #location_distances.sort(key=lambda x:x[0])#sort by distances,low to high
            for t in range(10):#run for 100 iterations or until capacity is reached
                for l in in_radius: #location is tuple (distance,location object)
                    if (l[1].GetPackageWeight() + self.capacity <= self.max_capacity):
                        if l[1] not in visited:
                            route.append(l[1])
                            visited.append(l[1])
                            self.capacity += l[1].GetPackageWeight()
                    #else:break

                for l in out_radius: #location is tuple (distance,location object)
                    if (l[1].GetPackageWeight() + self.capacity <= self.max_capacity):
                        if l[1] not in visited:
                            route.append(l[1])
                            visited.append(l[1])
                            self.capacity += l[1].GetPackageWeight()
                    #else:break
                #early exit condition
                if self.capacity == self.max_capacity: break

            #TODO last two points on step 2.c of algorithm 3
            #2.D - Optimise
            #TODO Optimise
            #visited.extend(route)   
            route.insert(0,world.depot[0])
            route.append(world.depot[0])
            routes.append(route)
            #v.route = route
        
        #add a pentalty for this particle
        remaining = [l for l in world.locations if l not in visited]
        penalty = len(remaining)

        return (routes,penalty)
        #ensure no particles aren't assigned a route
        # remaining = [l for l in world.locations if l not in visited]
        # for l in remaining:
        #     for r in self.routes:
        #         if l.GetPackageWeight() + SumRouteWeight(r) <= self.max_capacity:
        #             r.insert(-1,l)


    def decode(self,vehicles,world):
            #1. Extract vehicle properties.
            
            #while True:#len(visited) < len(world.locations)
            visited = []
            #    print("v:{0}   l:{1}".format(len(visited),len(world.locations)))
            i = 0
            for v in vehicles:
                
                self.capacity = 0
                v.xref = self.dimensions[i]# v.xref = self.pos.X#should this be swapped?
                v.yref = self.dimensions[i+1]#self.pos.Y
                v.r    = self.dimensions[i+2]#self.pos.R
                i += 3

                #2. Route Construction
                #2.A
                temp_route = []
                location_dist = []
                for l in world.locations:
                    dist = ( CalcDistance3(v.xref,v.yref,l),l ) #create tuple (distance,location)
                    location_dist.append(dist)
                ##2.1
                location_dist.sort(key=lambda x:x[0])
                ##2.2
                temp_location_dist = location_dist.copy()
                for l in temp_location_dist:
                    if (l[1].GetPackageWeight() + self.capacity > self.max_capacity):
                        location_dist.remove(l)#pass #what to do i this will make the vehicle too heavy
                    else:
                        if l[1] not in visited:
                            temp_route.append(l[1])
                            self.capacity += l[1].GetPackageWeight()
                            location_dist.remove(l)
                #2.B - Optimise
                #TODO

                #2.C
                location_dist.reverse()
                temp_location_dist = location_dist.copy()#this is to ensure proper looping when items are removed from the list
                for l in temp_location_dist:
                    if (l[1].GetPackageWeight() + self.capacity > self.max_capacity):
                        location_dist.remove(l)#pass #what to do i this will make the vehicle too heavy
                    else:
                        if l[1] not in visited:
                            temp_route.append(l[1])
                            self.capacity += l[1].GetPackageWeight()
                            location_dist.remove(l)


                #TODO last two points on step 2.c of algorithm 3
                #2.D - Optimise
                #TODO Optimise                
                #v.routes.append(temp_route) #particle maybe?
                #v.route.append(temp_route)

                visited.extend(temp_route)
                temp_route.insert(0,world.depot[0])
                temp_route.append(world.depot[0])
                v.route = temp_route

    def __repr__(self):
        return "X:{0},Y:{1}".format(self.X,self.Y)


class Swarm():
    def __init__(self,population,vehicles,width,height):
        self.vehicles = vehicles
        
        self.particles = [ Particle(vehicles,width, height)#,choice([i.capacity for i in vehicles]))
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

    def evaluatePbest(self,world):
        for p in self.particles:
            pb_result = p.decode2(p.pbest,self.vehicles,world)
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


        # for p in self.particles:
        #     pass
            #vel = inertia * p.V + 0.5 * randint(0,1) * ()

    def decode(self,world):
        for p in self.particles:#for i in range(len(self.particles)): #careful when indexing. we cannot start at 0. range(0->max)
            result = p.decode2(p.dimensions,self.vehicles,world)
            p.routes = result[0]
            p.penalty = result[1]


class PSO:
    def __init__(self,Master,width,height):
        self.width = width
        self.height= height
        #c1 = 1.5
        #c2 = 2.5 both sum to 4
        #Randomly initialise particle position
        self.Master = Master
        self.world = Master.getField('world')
        self.vehicles = self.Master.getField('vehicles')

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

    def run(self,iterations = 30):
        #9. Stopping criteria
        K = 5 #num of neighbours; arbirary value
        T = iterations
        for t in range(1,T):
            #inertia = 0.4 + ( ((t-1)-T) / (1-T) ) * (0.9 - 0.4)
            #1. Initialise
            vehicles = self.vehicles

            swarm = Swarm(50, vehicles,self.width,self.height)       

            #2. Deocode
            swarm.decode(self.world)

            #3. Compute Performance measure for each particle
            swarm.evaluateRoute()

            #4. Update pbest
            swarm.evaluatePbest(self.world)

            #5. Update gbest
            swarm.evaluateGbest()

            #6. Update lbest
            swarm.evaluateLbest(K)

            #7. Generate nbest
            swarm.evaluateNbest()

            #8. Update Velocity
            swarm.updateParticles(t,T,self.width,1)

        #10. Decode final solution
        p = Particle(vehicles,self.width,self.height)
        p.dimensions = swarm.gbest
        p.fitness = swarm.gbest_fitness

        final_routes = p.decode2(p.dimensions,vehicles,self.world) 
        self.AssignRoutes(final_routes[0])
        