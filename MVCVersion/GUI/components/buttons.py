import tkinter as tk
import customtkinter as ctk
from .basecomponent import BaseComponent
from typing import Union

class ButtonComponents(BaseComponent):
    def __init__(self,master,on_submit:Union[callable,list[callable]], on_refresh:Union[callable,list[callable]]) -> None:
        super().__init__(master,"red")

        self.submitButton = ctk.CTkButton(self.frame,text="Done",width=80,
                                        command=lambda:self.execute(on_submit))
        self.submitButton.grid(row=0,column=0)

        self.refreshMap = ctk.CTkButton(self.frame,text="New Map",width=80,
                                        command=lambda:self.execute(on_refresh))
        self.refreshMap.grid(row=0,column=1)

    def execute(self,executable:Union[callable,list[callable]]):
        if type(executable) is list:
            for func in executable:
                func()
        else:
            executable()