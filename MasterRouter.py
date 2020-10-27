#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#MasterAgent.py

#from gui_functions import *
from Mapping import Map
from Artist import Artist
import pygame
import pygame.gfxdraw
from Search_Methods.PSO import PSO
from Search_Methods.ACO import ACO
#from ACO import ACO

class MasterRouter():
    def __init__(self,search_method,width,height):
        self.width = width
        self.height = height
        #self.id = "m_"
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
        temp_capacity_sum = \
            sum(v.capacity for v in vehicles)

        self.KB['vehicles'] = vehicles
        self.KB['capacity_sum'] = temp_capacity_sum

    def setPackages(self,packages):
        temp_package_sum = \
            sum(p.weight for p in packages)

        self.KB['packages'] = packages
        self.KB['package_sum'] = temp_package_sum


    def setWorld(self,locations):
        self.KB['world'] = \
            Map(self.getField('search_method'), locations, self.getField('packages') )
        self.setField('num_locations',len(locations)-1)

    def getField(self,field):
        """Generic Getter for KB"""
        if field in self.KB:
            return self.KB[field]
        else:
            print("Key doesn't exist in KB")
            return None

    def setField(self,field,value):
        """Generic Setter for KB"""
        if field in self.KB:
            self.KB[field] = value
            return True
        else:
            print("Key doesn't exist in KB")
            return False

    def Execute(self):
         
        method = self.getField('search_method')

        if method == 'aco':
            alg = ACO(self.getField('world'),self.getField('vehicles'))
        elif method == 'pso_s1':
            alg = PSO(self,self.width, self.height,True)
        elif method == 'pso_s2':
            alg = PSO(self,self.width, self.height,False)
            #results = pso.run()    
        return alg.run()

    def Visualise(self):
        pygame.init()
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
                artist.Draw()

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
            if v.route == None: break#return None
            print(v)
            pathsum += v.sumRoute()
        pathavg = pathsum / len(self.getField('vehicles'))
        print("Path Avg:{0}\nPath Sum:{1}".format(pathavg,self.RouteSum()))
        #results = ""

        return None#results



    # def RouteAlgorithm(self,alg,agents):
    #     """Route finding algorithm goes here.
    #     a modular approach allows us to easily 
    #     implement multiple Routing methods"""
    #     if alg.lower() == "aco": 
    #         aco = ACO(self.world,agents)
    #         return aco.Optimize()