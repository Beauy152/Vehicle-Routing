#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#GUI.py

from tkinter import BOTH,LEFT,RIGHT
import customtkinter as tk
from controller import *

from entities.new_mapping import Location
from entities.new_artist import Artist

from GUI.components.basecomponent import BaseComponent
from GUI.components.globalsettings import GlobalSettings
from GUI.components.psosettings import PsoSettings
from GUI.components.mapsettings import MapSettings
from GUI.components.methodssettings import MethodSettings
from GUI.components.buttons import ButtonComponents


class ConfigurationGUI(tk.CTk):
    def __init__(self,width=400,height=400):
        super().__init__()
        self.controller:'Controller' = None
        # Configure Window
        self._canvas_width = width - 10
        self._canvas_height= height - 10
        self._canvas_padding = 30

        Location.sclX = self._canvas_width - self._canvas_padding
        Location.sclY = self._canvas_height - self._canvas_padding

        self.title("Capacitive Vehicle Routing Problem.")

        _width  :float = (self._canvas_width*2)-(self._canvas_width/2)
        _height :float = self._canvas_height

        self.geometry(f"{_width}x{_height}")


        # CONTROLS FRAME
        self.frame_controls = tk.CTkFrame(self,
            width=self._canvas_width,height=self._canvas_height )
        self.frame_controls.pack(fill=BOTH,side=LEFT)

        #   CONTROLS
        BaseComponent._debug    :bool = False

        self.GlobalSettings = GlobalSettings(self.frame_controls)
        self.PsoSettings    = PsoSettings(self.frame_controls)
        self.MapSettings    = MapSettings(self.frame_controls)
        self.MethodSettings = MethodSettings(self.frame_controls)

        self.ButtonSettings = ButtonComponents(self.frame_controls,
        on_refresh=self.onRefreshClicked,
        on_submit=[self.onRefreshClicked,self.onSubmitClicked]
            )

        # CANVAS
        self._canvas = tk.CTkCanvas(
            self,bg="grey",height=self._canvas_height,width=self._canvas_width
            )
        # self.artist = artistClass(self._canvas)
        self._canvas.pack(side=RIGHT)

        self.artist = Artist(self._canvas)

    def onRefreshClicked(self):
        self.controller.applySettings(
            self.GlobalSettings.getAllValues()
        )

    def onSubmitClicked(self):
        self.onRefreshClicked()
        self.controller.runApproach()




    # def refreshMap(self):
    #     self.getConfigurationValues()
        
    #     self.locations.clear()
    #     Location.maxX = 0
    #     Location.maxY = 0

    #     locations = self.router.setLocations()

    #     self._canvas.delete('all')
    #     for location in locations:
    #         location.draw(self.artist)

    # def drawRoutes(self):
    #     for vehicle in self.router.vehicles:
    #         for i,location in enumerate(locations := vehicle.route):
    #             if i+1 >= len(locations): 
    #                 break
    #             else:
    #                 self.artist.drawPath(location,locations[i+1])



        # for i in range(len(route)-1) :
        # self.Path(route[i],route[i+1],colour,thickness)
        # if stepthrough:#if flag set, draw step by step
        #     self.doNodes(self.world.depot)#draw depot only
        #     self.doNodes(self.world.locations)#draw remaining locations
        #     pygame.display.update()
        #     pygame.time.delay(500)#sleep(0.5)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
