import pygame
import pygame.gfxdraw
from Statics import *
#from Mapping import *

class Artist():
    def __init__(self,vehicles,world,width,height):
        self.vehicles = vehicles
        self.world = world

        self.width = width
        self.height= height

        """Layer is pygame display"""
        self.layer = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Test")
        #largest x,y values to determine the minimum size of the map
        self.XMAX =max(world.locations,key=lambda i : i.X).X + (R*2)#R is added to ensure entire nodes are visible
        self.YMAX =max(world.locations,key=lambda i : i.Y).Y + (R*2)
        #Scale values to fit data to screen
        self.XSCL = width/self.XMAX
        self.YSCL = height/self.YMAX   

    def Path(self,A,B,colour,thickness=2):
        """given two nodes, draws a line connecting them"""
        a = ( int(A.X*self.XSCL) , int(A.Y*self.YSCL) )#Scale X,Y values for screen
        b = ( int(B.X*self.XSCL) , int(B.Y*self.YSCL) )
        pygame.gfxdraw.line(self.layer,a[0],a[1],b[0],b[1],colour)
        #pygame.draw.line(self.layer,colour,a,b,thickness)

    def SplitPoint(self,A,B):
        X = (A.X + B.X) / 2
        Y = (A.Y + B.Y) / 2
        return self.world.location_type(X,Y,'s')#Location(X,Y,'s')

    def doNodes(self,d):
        """d is a node object"""
        for node in d:
            X = int(node.X*self.XSCL)
            Y = int(node.Y*self.YSCL)
            pygame.gfxdraw.filled_circle(self.layer,X,Y,R,COLOURS[node.Type])
            #pygame.draw.circle(self.layer,COLOURS[node.Type],(X,Y),R)
            #COLOURS[node.value] : looks up colour based on value of node
    
    def doNeighbourConnections(self):
        for node in self.world.locations:
            for n in node.neighbours:
                self.Path(node,n.actual_location,BLACK)
    
    def drawRoute(self,route,colour=(0,0,0),thickness=2):
        """Route should be a list of objects with X,Y attributes"""
        
        for i in range(len(route)-1) :
            self.Path(route[i],route[i+1],colour,thickness+2)

    def Draw(self):
        self.layer.fill(GREY)
        #self.doNeighbourConnections()
        for vehicle in self.vehicles:
            if vehicle.route is not None:
                self.drawRoute(vehicle.route,vehicle.colour,int(vehicle.id[2:]))

        self.doNodes(self.world.depot)#draw depot only
        self.doNodes(self.world.locations)#draw remaining locations

        pygame.display.update()