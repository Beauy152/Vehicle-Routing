import pygame
import pygame.gfxdraw
from math import sqrt
from RouteMap import Location
#from DeliveryAgent import DeliveryAgent
#Colours
GREY = (  54,  54,  54)
BLACK= (   0,   0,   0)
WHITE= ( 255, 255, 255)
BLUE = (  84, 131, 179)
MINT = ( 130, 255, 193)
GREEN= (  57, 143,  57)
YELLOW=( 255, 241, 120)
ORANGE=( 255, 200, 138)
PINK  =( 252, 157, 157)
RED   =( 235,  63,  63)
NIGHT =( 140, 136, 181)
#Colour Lookup
COLOURS = {
    'l':BLUE, #location
    'd':BLACK,#Depot
    's':MINT  #Selected
}

#An iterable list of colours. useful when assigning colours
#to clusters of nodes
COL_LIST = [MINT,GREEN,YELLOW,ORANGE,PINK,RED,NIGHT]
#node radius
R = 8
#Screen Dimensions
WIDTH  = 600
HEIGHT = 600

class GuiController():#Set flags on init to enable/disable certain rendering
    """Gui Controller should encapsulate all drawing
    and gui functionality"""
    def __init__(self,Locations):
        """Layer is pygame display"""
        self.layer = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Test")
        #largest x,y values to determine the minimum size of the map
        self.XMAX =max(Locations,key=lambda i : i[0])[0] + (R*2)#R is added to ensure entire nodes are visible
        self.YMAX =max(Locations,key=lambda i : i[1])[1] + (R*2)
        #Scale values to fit data to screen
        self.XSCL = WIDTH/self.XMAX
        self.YSCL = HEIGHT/self.YMAX    
    

    #Drawing Functions
    def update(self):
        """Refresh drawings on screen. always call after drawing to canvas/layer"""
        pygame.display.update()

    def Path(self,A,B,colour,thickness=2):
        """given two nodes, draws a line connecting them"""
        a = ( int(A.X*self.XSCL) , int(A.Y*self.YSCL) )#Scale X,Y values for screen
        b = ( int(B.X*self.XSCL) , int(B.Y*self.YSCL) )
        pygame.gfxdraw.line(self.layer,a[0],a[1],b[0],b[1],colour)
        #pygame.draw.line(self.layer,colour,a,b,thickness)

    def SplitPoint(self,A,B):
        X = (A.X + B.X) / 2
        Y = (A.Y + B.Y) / 2
        return Location(X,Y,'s')

    def doNodes(self,d):
        """d is a node object"""
        for node in d:
            X = int(node.X*self.XSCL)
            Y = int(node.Y*self.YSCL)
            pygame.gfxdraw.filled_circle(self.layer,X,Y,R,COLOURS[node.Type])
            #pygame.draw.circle(self.layer,COLOURS[node.Type],(X,Y),R)
            #COLOURS[node.value] : looks up colour based on value of node
    
    def doNeighbourConnections(self,Data):
        for node in Data:
            for n in node.neighbours:
                self.Path(node,n,BLACK)
    
    def drawRoute(self,route,colour=(0,0,0),thickness=2):
        """Route should be a list of objects with X,Y attributes"""
        
        for i in range(len(route)-1) :
            self.Path(route[i],route[i+1],colour,thickness+2)

    def Draw(self,Depot,Data,Vehicles):
        Locations = Data
        self.layer.fill(GREY)#WHITE)

        #self.doNeighbourConnections(Locations)
        for vehicle in Vehicles:
            if vehicle.route is not None:
                self.drawRoute(vehicle.route,vehicle.colour,int(vehicle.id[2:]))

        #Locations.append(self.SplitPoint(Depot[0],Locations[2]))

        

        self.doNodes(Depot)
        self.doNodes(Locations)
    