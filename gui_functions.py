import pygame
from math import sqrt
#Colours
BLACK= (   0,   0,   0)
WHITE= ( 255, 255, 255)
BLUE = (  84, 131, 179)
MINT = ( 130, 255, 193)
GREEN= (  57, 143,  57)
YELLOW=( 255, 241, 120)

#An iterable list of colours. useful when assigning colours
#to clusters of nodes
COLOURS = [BLUE,MINT,GREEN,YELLOW]
#node radius
R = 5
#Screen Dimensions
WIDTH  = 600
HEIGHT = 600
#largest x,y values to determine the minimum size of the map

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
        self.layer = pygame.display.set_mode((WIDTH,HEIGHT))#self.layer = layer
        pygame.display.set_caption("Test")
        #R is added to ensure entire nodes are visible
        self.XMAX =max(Data,key=lambda i : i[0])[0] + (R*2)
        self.YMAX =max(Data,key=lambda i : i[1])[1] + (R*2)
        #Scale values to fit data to screen
        self.XSCL = WIDTH/self.XMAX#-0.01
        self.YSCL = HEIGHT/self.YMAX    
    

    #Drawing Functions
    def update(self):
        pygame.display.update()

    def Path(self,A,B):
        a = (A[0]*self.XSCL , A[1]*self.YSCL )
        b = (B[0]*self.XSCL , B[1]*self.YSCL )
        pygame.draw.line(self.layer,BLACK,a,b,5)

    def doNodes(self,d):
        """d is a list of tuples [(x,y),...]"""
        for node in d:
            X = int(node[0]*self.XSCL)
            Y = int(node[1]*self.YSCL)
            pygame.draw.circle(self.layer,BLUE,(X,Y),R)
    
    def Draw(self,Data):
        self.layer.fill(WHITE)

        self.doNodes(Data)
    