#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#MasterAgent.py

from Mapping import Map
from Artist import Artist
import pygame
import pygame.gfxdraw
from Search_Methods.PSO import PSO
from Search_Methods.ACO import ACO

class MasterRouter():
    def __init__(self,search_method,width,height):
        self.width = width
        self.height = height
        self.KB = {#Knowledge base. vehicle information
            'vehicles':[],
            'packages':[],
            'world'   :None,
            'package_sum':0,
            'capacity_sum':0,
            'search_method':search_method.lower(),
            'num_locations':0
        }

    def setVehicles(self,vehicles):
        """Assigns vehicles & their cumulative capacity to KB"""
        temp_capacity_sum = \
            sum(v.capacity for v in vehicles)

        self.KB['vehicles'] = vehicles
        self.KB['capacity_sum'] = temp_capacity_sum

    def setPackages(self,packages):
        """Assigns packages & their cumulative weight to KB"""
        temp_package_sum = \
            sum(p.weight for p in packages)

        self.KB['packages'] = packages
        self.KB['package_sum'] = temp_package_sum

    def setWorld(self,locations):
        """Assigns world representation to KB & num locations"""
        self.KB['world'] = \
            Map(self.getField('search_method'), locations, self.getField('packages') )
        self.setField('num_locations',len(locations)-1)

    def getField(self,field):
        """Generic Getter for KB"""
        if field in self.KB:
            return self.KB[field]
        else: return None

    def setField(self,field,value):
        """Generic Setter for KB"""
        if field in self.KB:
            self.KB[field] = value
            return True
        else: return False

    def Execute(self):
        """Execute algorithm from defined list"""
        method = self.getField('search_method')

        if method == 'aco':
            alg = ACO(self.getField('world'),self.getField('vehicles'))
        elif method == 'pso_s1':
            alg = PSO(self,self.width, self.height,True)
        elif method == 'pso_s2':
            alg = PSO(self,self.width, self.height,False)
   
        return alg.run()

    def Visualise(self,stepthrough=False):
        """Route visualisation"""
        pygame.init()
        #Initialise Artist, responsible for route drawing
        artist = Artist(self.getField('vehicles'),
                        self.getField('world'),
                        self.width, self.height)

        #Drawing Loop
        clock = pygame.time.Clock()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                #Draw
                artist.Draw(stepthrough)

            clock.tick(10)#Limit FPS
        pygame.quit()
    
    def RouteSum(self):
        return sum(v.sumRoute() for v in self.getField('vehicles'))

    def Stats(self):
        print("Num Vehicles:{0}\nNum Locations:{1}"\
            .format(len(self.getField('vehicles')),
                    len(self.getField('world').locations) ))

        pathsum = 0
        for v in self.getField('vehicles'):
            if v.route == None: break
            print(v)

            pathsum += v.sumRoute()
        pathavg = pathsum / len(self.getField('vehicles'))
        print("Path Avg:{0}\nPath Sum:{1}".format(pathavg,self.RouteSum()))

