import tkinter as tk
import customtkinter as ctk
from .basecomponent import BaseComponent
from .spinbox import Spinbox

class PsoSettings(BaseComponent):
    def __init__(self,master) -> None:
        super().__init__(master,"purple")
        self._valueGetters.append(self.getValues)

        ctk.CTkLabel(self.frame,text="PSO Settings").grid(row=0,column=0)

        # Population
        self.psoPopulationLabel = ctk.CTkLabel(self.frame,text="Swarm Population")
        self.psoPopulationLabel.grid(row=1,column=0)

        self.psoPopulation = Spinbox(self.frame,step_size=100,min=50,max=500,default=self._defaults['pso_population'])
        self.psoPopulation.grid(row=2,column=0)

        # Iterations
        self.psoIterationsLabel = ctk.CTkLabel(self.frame,text="# Iterations")
        self.psoIterationsLabel.grid(row=1,column=1)

        self.psoIterations = Spinbox(self.frame,step_size=50,min=1,max=2000,default=self._defaults['pso_iterations'])
        self.psoIterations.grid(row=2,column=1)

    def getValues(self) -> dict[str, any]:
        return {
            'psoPopulation':self.psoPopulation.get(),
            'psoIterations':self.psoIterations.get()
        }