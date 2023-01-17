import tkinter as tk
import customtkinter as ctk
from .basecomponent import BaseComponent

class ButtonComponents(BaseComponent):
    def __init__(self,master,on_submit:callable, on_refresh:callable) -> None:
        super().__init__(master,"red")

        self.submitButton = ctk.CTkButton(self.frame,text="Done",width=80,
                                        command=on_submit)
        self.submitButton.grid(row=0,column=0)

        self.refreshMap = ctk.CTkButton(self.frame,text="New Map",width=80,
                                        command=on_refresh)
        self.refreshMap.grid(row=0,column=1)