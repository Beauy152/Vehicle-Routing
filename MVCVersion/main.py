
import tkinter as tk
from controller import *
from model import *
from view import *


class App:
    def __init__(self):
        # create a model
        self.model = Model()

        # create a view and place it on the root window
        self.view = ConfigurationGUI(600,600)

        # create a controller
        self.controller = Controller(self.model, self.view)

        # set the controller to view
        self.view.set_controller(self.controller)

    def start(self):
        self.view.mainloop()

if __name__ == '__main__':
    app = App()
    app.start()