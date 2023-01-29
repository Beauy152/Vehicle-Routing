from customtkinter import CTkCanvas
from entities.new_vehicle import *
from entities.new_mapping import *

class Artist:
    def __init__(self,canvas:CTkCanvas) -> None:
        self.canvas = canvas

        self.locationRadius = 8

        self.canvas.xview_scroll(30,'units')
        self.canvas.yview_scroll(30,'units')

    def clear(self):
        self.canvas.delete('all')
        # self.locations.clear()
        # Location.maxX = 0
        # Location.maxY = 0

    def drawLocations(self,depot:'Location',locations:list['Location']):
        self.clear()

        self.drawLocation(depot)
        for location in locations:
            self.drawLocation(location)


    def drawLocation(self,l:'Location'):
        r = self.locationRadius
        l.scale()
        self.canvas.create_oval(
            l.x - r, l.y-r, l.x+r, l.y+r,
            fill=l.color )

    def drawPaths(self,vehicles:list['DeliveryAgent']):
        for vehicle in vehicles:
            for i,location in enumerate(locations:= vehicle.route):
                if i >= len(locations)-1:
                    break
                else:
                    self.drawPath(location,locations[i+1],vehicle.colour)

    def drawPath(self,l1:'Location',l2:'Location',colour='orange'):
        self.canvas.create_line(
            l1.x,l1.y,l2.x,l2.y,fill=colour,width=2
        )
        
