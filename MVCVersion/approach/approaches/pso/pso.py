from approach.approaches.pso.particle import Particle
from approach.approaches.pso.swarm import Swarm
from entities.new_package import Package
from entities.new_vehicle import DeliveryAgent
from entities.new_mapping import Location,Neighbour
from approach.approachBase import Approach
from approach.approachBaseFactory import ApproachFactory

class PSOFactory(ApproachFactory):
    def factory_method(self,settings:dict[str,any],vehicles:list[DeliveryAgent],
                locations:list[Location],depot:Location,packages:list[Package]) -> Approach:
        return PSOApproach(settings,vehicles,locations,depot,packages)

#This approach has local_improvements set to false.
class PSOApproach(Approach):
    def __init__(self,settings,vehicles,locations,depot,packages) -> None:
        super().__init__(settings,vehicles,locations,depot,packages)
        #needed for random particle position initialisation
        Location.depot = self.depot #TODO: Remove this if possible.
        self.width  :float  = self.settings.get('width')
        self.height :float  = self.settings.get('height')
        self.world = self.locations
        # self.world  = Master.getField('world')
        self.useLocalImprovement:bool = \
            True if self.settings.get('method') == 'pso_s1' else False

    def run(self):
        """Main entry point, this function encapsulates all necessary orchestration"""
        #9. Stopping criteria
        #TODO: Make these params configurable
        K = 5 #num of neighbours; arbirary
        T = self.settings.get('psoIterations')
        population = self.settings.get('psoPopulation')
        
        # GENERATE NEIGHBOURS
        for location in self.locations:
            location.neighbours = [Neighbour(neighbour,location) for neighbour in self.locations]
            location.neighbours.sort(key=lambda n:n.distance,reverse=True)  # Sort Low-High -> Closest-Furthest
            # location.neighbours = location.neighbours[:K]                   # Takes first K Neighbours

        print("--Particle Swarm Optimisation--\n--Local Improvements:%s--\nT(%s) P(%s)\n" % (self.useLocalImprovement,T,population)) 
        for t in range(1,T):
            #1. Initialise
            swarm = Swarm(self)       
            #2. Deocode
            swarm.decode(self.locations,self.settings.get('use'))
            #3. Compute Performance measure for each particle
            swarm.evaluateRoute()
            #4. Update pbest
            swarm.evaluatePbest(self.locations,self.useLocalImprovement)
            #5. Update gbest
            swarm.evaluateGbest()
            #6. Update lbest
            swarm.evaluateLbest(K)
            #7. Generate nbest
            swarm.evaluateNbest()
            #8. Update Velocity
            swarm.updateParticles(t,T,self.width,1)

        #10. Decode final solution
        p = Particle(self.vehicles,self.width,self.height,self.locations)
        p.dimensions = swarm.gbest
        p.fitness    = swarm.gbest_fitness

        final_routes = p.decode(p.dimensions,self.vehicles,self.locations,self.useLocalImprovement) 

        self.AssignRoutes(final_routes[0])
        
    def AssignRoutes(self,routes):
        """Assign final route set to each vehicle"""
        #print("Assigning Routes to Vehicles")
        for i in range(len(self.vehicles)):
            self.vehicles[i].route = routes[i]
            print(self.vehicles[i].id + ": Route Assigned.")
    


        