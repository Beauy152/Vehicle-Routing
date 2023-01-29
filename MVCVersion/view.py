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

        # DEFAULT VALUES  
        BaseComponent._debug    :bool = False
        BaseComponent._width    :float= self._canvas_width
        BaseComponent._height   :float= self._canvas_height
        
        # CONTROLS
        self.GlobalSettings = GlobalSettings(self.frame_controls)
        self.PsoSettings    = PsoSettings(self.frame_controls)
        self.MapSettings    = MapSettings(self.frame_controls)
        self.MethodSettings = MethodSettings(self.frame_controls)

        self.ButtonSettings = ButtonComponents(self.frame_controls,
        on_refresh=self.onRefreshClicked,
        on_submit=self.onSubmitClicked
            )

        # CANVAS
        self._canvas = tk.CTkCanvas(
            self,bg="grey",height=self._canvas_height,width=self._canvas_width
            )
        # self.artist = artistClass(self._canvas)
        self._canvas.pack(side=RIGHT)

        self.artist = Artist(self._canvas)

    def onRefreshClicked(self) -> None:
        self.controller.applySettings(
            self.GlobalSettings.getAllValues()
        )

    def onSubmitClicked(self) -> None:
        self.onRefreshClicked()
        self.controller.runApproach()

    def set_controller(self, controller) -> None:
        self.controller = controller
