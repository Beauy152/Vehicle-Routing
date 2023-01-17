#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#GUI.py

from tkinter import BOTH,LEFT,RIGHT
import customtkinter as tk
from components.basecomponent import BaseComponent
from components.globalsettings import GlobalSettings
from components.psosettings import PsoSettings
from components.mapsettings import MapSettings
from components.methodssettings import MethodSettings
from components.buttons import ButtonComponents

class ConfigurationGUI(tk.CTk):
    def __init__(self,width=400,height=400):
        super().__init__()
        #Configure Window
        self._canvas_width = width
        self._canvas_height= height

        self.title("Capacitive Vehicle Routing Problem.")
        _width = (self._canvas_width*2)-(self._canvas_width/2)
        _height = self._canvas_height
        self.geometry(f"{_width}x{_height}")

        # CONTROLS FRAME
        self.frame_controls = tk.CTkFrame(self,
            width=self._canvas_width,height=self._canvas_height )
        self.frame_controls.pack(fill=BOTH,side=LEFT)

        #   CONTROLS
        BaseComponent._debug = not True

        self.GlobalSettings = GlobalSettings(self.frame_controls)
        self.PsoSettings    = PsoSettings(self.frame_controls)
        self.MapSettings    = MapSettings(self.frame_controls)
        self.MethodSettings = MethodSettings(self.frame_controls)

        self.ButtonSettings = ButtonComponents(self.frame_controls,on_submit=self.getConfigurationValues,on_refresh=self.refreshMap)

        # CANVAS
        self._canvas = tk.CTkCanvas(
            self,bg="grey",height=self._canvas_height,width=self._canvas_width
            )
        self._canvas.pack(side=RIGHT)

    def getConfigurationValues(self):
        results = self.GlobalSettings.getAllValues()
        print(results)
        # return BaseComponent.getValues()

    def refreshMap(self):
        pass

    def drawNode():
        pass

    def drawRoute():
        pass




app = ConfigurationGUI()
app.mainloop()
