
from random import randint
from entities.new_mapping import Location
from entities.new_vehicle import DeliveryAgent
from approach.approaches.pso.pso import *
from approach.approaches.pso.particle import Particle
from genericFunctions import CalcDimensionalDistance


class Swarm():
    """Acts as a container for each particle to easily delegate processing
    and hold certain values required externally to the particle """
    def __init__(self,pso:'PSOApproach'):
        self.pso      = pso
        self.vehicles   :list['DeliveryAgent'] = pso.vehicles
        self.locations  :list['Location']      = pso.locations

        self.particles: list[Particle] = [ Particle(self.vehicles,pso.width, pso.height,self.locations) 
                                            for p in range(self.pso.settings.get('psoPopulation')) ]

    def evaluateNbest(self):
        """Delegates computation to each particle"""
        for p in self.particles:
            p.calculateNbest()

    def evaluateLbest(self,K=5):
        """determine local best location from other nearby particles"""
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

    def evaluateGbest(self):
        """get the overall best position from all particles"""
        best_particle = min(self.particles, key=lambda x: x.pbest_fitness)

        self.gbest = best_particle.pbest
        self.gbest_fitness = best_particle.pbest_fitness

    def evaluatePbest(self,world,useLocalImprovement):
        """Delegates computation to each particle"""
        for p in self.particles:
            pb_result = p.decode(p.pbest,self.vehicles,world,useLocalImprovement)
            pb_route = pb_result[0]
            pb_penalty = pb_result[1]

            p.pbest_fitness = p.calculate_fitness(pb_route,pb_penalty)

            if p.fitness < p.pbest_fitness:
                p.pbest = p.dimensions
                p.pbest_fitness = p.fitness

    def evaluateRoute(self):
        """Calculates Routes Fitnesses. Delegates computation to each particle"""
        for p in self.particles:
            p.fitness = p.calculate_fitness(p.routes,p.penalty)

    def updateParticles(self,t,T,xmax,xmin):
        """Update each particles position and velocity"""
        cp = 0.5#pb position acceleration constant
        cg = 0.5#global best position acceleration constant
        cl = 1.5#local best position acceleration constant
        cn = 1.5#neighbourhood best position acceleration constant
        w1 = 0.9#First Intertia Weight
        wT = 0.4#Last Interia Weight
        u  = randint(0,1)#uniform random number
        wt = wT + (t-T)/(1-T) * (w1 - wT)#interial weight of t'th iteration

        for p in self.particles:
            for d in range(len(p.dimensions)):
                p.velocity[d] = wt*p.velocity[d]+ \
                                    cp*u*(p.pbest[d]    - p.dimensions[d] ) + \
                                    cg*u*(self.gbest[d] - p.dimensions[d] ) + \
                                    cl*u*(p.lbest[d]    - p.dimensions[d] ) + \
                                    cn*u*(p.nbest[d]    - p.dimensions[d] )

                p.dimensions[d] = p.dimensions[d] + p.velocity[d]
                #Boundary Constraining
                if p.dimensions[d] > xmax:
                    p.dimensions[d] = xmax
                    p.velocity[d] = 0
                #Boundary Constrainings
                if p.dimensions[d] < xmin:
                    p.dimensions[d] = xmin
                    p.velocity[d] = 0

    def decode(self,world,useLocalImprovement):
        """Delegates processing to individual particles"""
        for p in self.particles:
            result = p.decode(p.dimensions,self.vehicles,world,useLocalImprovement)
            p.routes = result[0]
            p.penalty = result[1]

