import TestData

from MasterRouter import MasterRouter
from GUI import InitialSetupGUI
import Packages as _Packages
from tkinter import Tk


"""GUI Manager for inital setup of values"""
root = Tk()
InitalSetupView = InitialSetupGUI("title",root)
root.mainloop()

Inital_vals = InitalSetupView.getData()
print( InitalSetupView.getData() )
#example output
#{'num_locations': 16, 'num_vehicles': 1, 'useGoogleData': 1}

#Create Master Router, initialised with search method
Master = MasterRouter(Inital_vals['method'],500,500)#method,wdith,height

if(Inital_vals['useGoogleData']) : 
    Locations = TestData.TestLocations()
    #Testing vehicles
    Vehicles = TestData.TestVehicles()
    #Assign vehicles to master router.
    #master will update internal 'capacity_sum'
    Master.setVehicles(Vehicles)
    #Generate Package List
    Packages = _Packages.TestPackages(Locations)
else:
    Locations = TestData.RandomLocations(Inital_vals['num_locations'])
    #Create vehicles
    Vehicles = TestData.RandomVehicles( Inital_vals['num_vehicles'] )
    #Assign vehicles to master router.
    #master will update internal 'capacity_sum'
    Master.setVehicles(Vehicles)
    #Generate Package List
    Packages = _Packages.GeneratePackages(Master.getField('capacity_sum'),Locations )









#Assign package list to master
Master.setPackages(Packages)

#Assign Masters World View
Master.setWorld(Locations)

#These methods will be changed to allow us to step through the program as it executes live

#Performs selected optimisation algoritm.
Master.Execute()
#
Master.Stats()

#start visualisation
Master.Visualise()#can take width & height