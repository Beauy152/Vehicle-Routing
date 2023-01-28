import tkinter as tk
import customtkinter as ctk
from .basecomponent import BaseComponent

class MapSettings(BaseComponent):
    def __init__(self,master) -> None:
        super().__init__(master,"orange")
        self._valueGetters.append(self.getValues)

        self.title =ctk.CTkLabel(self.frame,text="Map Settings")
        self.title.grid(row=0,column=0)

        # Use default Google Data
        self.useGoogleData = ctk.CTkCheckBox(self.frame,text="Use OR-Tools Data.")
        self.useGoogleData.grid(row=1,column=0,sticky=tk.W)

        # Enable stepping through of routes
        # self.useSteppingLabel = ctk.CTkLabel(self.frame,text="Step Through Routes")
        # self.useSteppingLabel.grid(row=2,column=0)

        # self.useStepping = ctk.CTkCheckBox(self.frame)
        # self.useStepping.grid(row=2,column=1)
    
        # Package input file as list
        self.usePackages = ctk.CTkCheckBox(self.frame,text="Use Package Input File")
        self.usePackages.grid(row=2,column=0,sticky=tk.W)

        # Set Defaults
        if( bool( self._defaults['use_package_list'] ) is True):
            self.usePackages.select()

        if( bool( self._defaults['use_google_test_data'] ) is True):
            self.useGoogleData.select()

        # if( bool( self._defaults['use_route_stepping'] ) is True):
        #     self.useStepping.select()

    def getValues(self) -> dict[str, any]:
        return {
            'useGoogleData':bool(self.useGoogleData.get()),
            'usePackageList':bool(self.usePackages.get())
        }