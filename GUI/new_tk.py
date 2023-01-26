#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#GUI.py

from tkinter import BOTH,LEFT,RIGHT
import customtkinter as tk

from new_mapping import Location

from .components.basecomponent import BaseComponent
from .components.globalsettings import GlobalSettings
from .components.psosettings import PsoSettings
from .components.mapsettings import MapSettings
from .components.methodssettings import MethodSettings
from .components.buttons import ButtonComponents
from TestData import TestLocations, RandomLocations

class ConfigurationGUI(tk.CTk):
    def __init__(self,artistClass,width=400,height=400):
        super().__init__()
        #Configure Window
        

        self._canvas_width = width
        self._canvas_height= height
        self._canvas_padding = 15
        Location.sclX = self._canvas_width - self._canvas_padding
        Location.sclY = self._canvas_height - self._canvas_padding

        self.title("Capacitive Vehicle Routing Problem.")

        _width  :float = (self._canvas_width*2)-(self._canvas_width/2)
        _height :float = self._canvas_height

        self.geometry(f"{_width}x{_height}")

        self.settings   :dict[str,any] = {}
        self.locations  :list[tuple[int,int]] = None

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

        self.ButtonSettings = ButtonComponents(self.frame_controls,on_submit=self.getConfigurationValues,on_refresh=self.refreshMap)

        # CANVAS
        self._canvas = tk.CTkCanvas(
            self,bg="grey",height=self._canvas_height,width=self._canvas_width
            )
        self.artist = artistClass(self._canvas)
        self._canvas.pack(side=RIGHT)

    def getConfigurationValues(self):
        self.settings = self.GlobalSettings.getAllValues()
        print(self.settings)
        # return BaseComponent.getValues()

    def refreshMap(self):
        if len(self.settings) == 0: 
            self.getConfigurationValues()

        # If `useGoogleData` is selected, populate map using said data.
        if self.settings.get('useGoogleData') is True:
            self.locations = TestLocations()
        else:
            # Generate Random Map
            self.locations = RandomLocations(self.settings.get('numLocations',16))

        #
        for location in self.locations:
            location.scale()
            location.draw(self.artist)
        # Render Locations

    def drawNode():
        pass

    def drawRoute():
        pass

