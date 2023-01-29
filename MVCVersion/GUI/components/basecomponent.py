
import tkinter as tk
import customtkinter as ctk
from typing import List, Dict
from .defaults import defaultsParser

class BaseComponent:
    _debug = False
    _defaults = defaultsParser("GUI_Defaults.txt")
    _valueGetters:List[callable] = []
    _width:float = None
    _height:float = None
    def __init__(self,master,debugColour:str,colour="transparent") -> None:
        self.colour = debugColour if self._debug else colour

        self.frame = ctk.CTkFrame(master=master,fg_color=self.colour,bg_color=self.colour)
        self.frame.pack(side=tk.TOP)

    def getAllValues(self) -> Dict[str,any]:
        results = {'width':self._width,'height':self._height}
        for _getter in self._valueGetters:
            results.update(_getter())
        
        return results
