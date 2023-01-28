import tkinter as tk
import customtkinter as ctk
from .basecomponent import BaseComponent
from .spinbox import Spinbox

class GlobalSettings(BaseComponent):
    def __init__(self,master,colour="transparent") -> None:
        super().__init__(master,"pink")
        self._valueGetters.append(self.getValues)

        self.label = ctk.CTkLabel(master=self.frame,text="Global Settings")
        self.label.grid(row=0,column=0)
        
        # Location & Vehicle settings
        self.numLocationsLabel = ctk.CTkLabel(master=self.frame,text="# Locations")
        self.numLocationsLabel.grid(row=1,column=0)

        self.numLocations = Spinbox(master=self.frame,step_size=1,min=1,max=50,default=self._defaults['num_locations'])
        self.numLocations.grid(row=2,column=0)

        self.numVehiclesLabel = ctk.CTkLabel(master=self.frame,text="# Vehicles")
        self.numVehiclesLabel.grid(row=1,column=1)

        self.numVehicles = Spinbox(master=self.frame,step_size=1,min=1,max=20,default=self._defaults['num_vehicles'])
        self.numVehicles.grid(row=2,column=1)


        #Return Frame
        # return self.frame

    def getValues(self):
        return {
            "numLocations":int( self.numLocations.get() ),
            "numVehicles":int( self.numVehicles.get() )
        }

