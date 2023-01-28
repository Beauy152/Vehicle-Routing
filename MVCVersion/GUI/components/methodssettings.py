import tkinter as tk
import customtkinter as ctk
from .basecomponent import BaseComponent

class MethodSettings(BaseComponent):
    def __init__(self,master) -> None:
        super().__init__(master,"orange")
        self._valueGetters.append(self.getValues)

        self.title =ctk.CTkLabel(self.frame,text="Map Settings")
        self.title.grid(row=0,column=0)

        self.SearchMethods = [
            ("ACO","aco","normal"),
            ("PSO W/Local improvement","pso_s1","normal"),
            ("PSO No Local Improvement","pso_s2","normal"),
            ("Testing (10-50 Locations)", "test", "normal")]

        self.searchMethodVar = ctk.StringVar()
        self.searchMethodVar.set("aco")

        _row = 1
        for text,val,state in self.SearchMethods:
            ctk.CTkRadioButton(self.frame,variable=self.searchMethodVar,
                                text=text,value=val,state=state).grid(row=_row,column=0,sticky=tk.W)
            _row += 1

    def getValues(self) -> dict[str, any]:
        return {
            'method':self.searchMethodVar.get()
        }

