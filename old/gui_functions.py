import pygame
from math import sqrt
#Colours
BLACK= (   0,   0,   0)
WHITE= ( 255, 255, 255)
BLUE = (  84, 131, 179)
MINT = ( 130, 255, 193)
GREEN= (  57, 143,  57)
YELLOW=( 255, 241, 120)
#Colour Lookup
COLOURS = {
    'l':BLUE, #location
    'd':BLACK,#Depot
    's':MINT  #Selected
}

#An iterable list of colours. useful when assigning colours
#to clusters of nodes
COL_LIST = [BLUE,MINT,GREEN,YELLOW]
#node radius
R = 8
#Screen Dimensions
WIDTH  = 600
HEIGHT = 600

#Assist Functions
def StraightDistance(L1,L2):
    """Take two coordinate tuples (x1,y1),(x2,y2),
    returns float of straigt line distance between"""
    return sqrt( ( (L2[0] - L1[0])**2 + (L2[1] - L1[1])**2 ) )



class GuiController():#Set flags on init to enable/disable certain rendering
    """Gui Controller should encapsulate all drawing
    and gui functionality"""
    def __init__(self,Data):
        """Layer is pygame display"""
        self.layer = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Test")
        #largest x,y values to determine the minimum size of the map
        self.XMAX =max(Data,key=lambda i : i[0])[0] + (R*2)#R is added to ensure entire nodes are visible
        self.YMAX =max(Data,key=lambda i : i[1])[1] + (R*2)
        #Scale values to fit data to screen
        self.XSCL = WIDTH/self.XMAX
        self.YSCL = HEIGHT/self.YMAX    
    

    #Drawing Functions
    def update(self):
        """Refresh drawings on screen. always call after drawing to canvas/layer"""
        pygame.display.update()

    def Path(self,A,B):
        """given two nodes, draws a line connecting them"""
        a = (A[0]*self.XSCL , A[1]*self.YSCL )#Scale X,Y values for screen
        b = (B[0]*self.XSCL , B[1]*self.YSCL )
        pygame.draw.line(self.layer,BLACK,a,b,5)

    def doNodes(self,d):
        """d is a node object"""
        for node in d:
            X = int(node.X*self.XSCL)
            Y = int(node.Y*self.YSCL)
            pygame.draw.circle(self.layer,COLOURS[node.value],(X,Y),R)
            #COLOURS[node.value] : looks up colour based on value of node
    
    def Draw(self,Data):
        self.layer.fill(WHITE)

        self.doNodes(Data)
    