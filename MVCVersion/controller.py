
# from Statics import COL_LIST,BLUE,YELLOW,GREEN,RED

from model import Model
from view import ConfigurationGUI as View
from sampledata import *

class Controller:
    def __init__(self, model, view):
        self.model:'Model' = model
        self.view :'View' = view

    def applySettings(self,settings:dict[str,any]):
        self.model.settings.update(settings)
        if not self.model.isset: self.applyDefaults()
        print(self.model.settings)
        self.view.artist.drawLocations(self.model.depot,self.model.locations)

    def applyDefaults(self):
        """Set the values for Vehicle, Locations etc
           Based on the configured settings"""
        settings = self.model.settings
        self.model.approach  = settings.get('method')
        self.model.vehicles  = testVehicles() if settings.get('useGoogleData') \
                            else RandomVehicles(settings.get('numVehicles',4))

        self.model.depot,    \
        self.model.locations = testLocations() if settings.get('useGoogleData') \
                            else RandomLocations(settings.get('numLocations',16))
        
        self.model.packages  = TestPackages(self.model.locations) if settings.get('useGoogleData') \
                            else GeneratePackages(
                                sum(v.capacity for v in self.model.vehicles),
                                self.model.locations)
        self.model.isset = True

    def runApproach(self):
        self.model.approach.runApproach(
            self.model.settings,
            self.model.vehicles,
            self.model.locations,
            self.model.depot,
            self.model.packages
        )
        self.view.artist.drawPaths(
            self.model.vehicles
        )
