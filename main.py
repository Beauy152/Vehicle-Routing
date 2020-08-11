import pygame
from data import GoogleTestData


Data = GoogleTestData()

###Constants###
#Colours
BLACK= (   0,   0,   0)
WHITE= ( 255, 255, 255)
BLUE = (  84, 131, 179)
#node radius
R = 5
#Screen Dimensions
WIDTH  = 600
HEIGHT = 600
#largest x,y values to determine the minimum size of the map
#R is added to ensure entire nodes are visible
XMAX =max(Data,key=lambda i : i[0])[0] + R
YMAX =max(Data,key=lambda i : i[1])[1] + R 
#Scale values to fit data to screen
XSCL = WIDTH/XMAX#-0.01
YSCL = HEIGHT/YMAX



"""
Ultimately, the gui output should be reflecting the 
processing being completed by the master routing agent.
"""

#Drawing Functions
def doNodes(d):
    """d is a list of tuples [(x,y),...]"""
    for node in d:
        X = int(node[0]*XSCL)
        Y = int(node[1]*YSCL)
        pygame.draw.circle(screen,BLUE,(X,Y),R)


def draw():
    """Main drawing func, spreads work between functions """
    screen.fill(WHITE)

    doNodes(Data)

    pygame.display.update()

#PyGame Drawing
#Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

#Drawing Loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #Draw
        draw()
        #Logic before or after drawing.

    clock.tick(10)#Limit FPS
pygame.quit()