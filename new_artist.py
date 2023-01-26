from customtkinter import CTkCanvas
from new_mapping import *

class Artist:
    def __init__(self,canvas:CTkCanvas) -> None:
        self.canvas = canvas
        self.width = 400
        self.height = 400
        self.locationRadius = 7

        self.canvas.xview_scroll(15,'units')
        self.canvas.yview_scroll(15,'units')

    def drawLocation(self,l:'Location') -> None:
        r = self.locationRadius
        self.canvas.create_oval(
            l.x - r, l.y-r, l.x+r, l.y+r,
            fill=l.color )

    def drawRoutes(self,routes):
        pass