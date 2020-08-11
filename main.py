import pygame
from data import GoogleTestData
from gui_functions import *
from node import Node

Data  = GoogleTestData()
Nodes =[]

#Convert Locations to Nodes
depot = True
for loc in Data:
    #janky as fuck, just sets the first location as the depot
    if depot: 
        val = 'd'
        depot = False
    else: val = 'l'

    Nodes.append( Node(loc[0],loc[1],val) )

print(Nodes)


"""
Ultimately, the gui output should be reflecting the 
processing being completed by the master routing agent.
"""

#PyGame Drawing
#Setup
pygame.init()
GC = GuiController( Data )

#Drawing Loop
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Draw
        GC.Draw(Data)
        GC.Path(Nodes[0].coords,Nodes[11].coords)
        GC.update()
    clock.tick(10)#Limit FPS
pygame.quit()