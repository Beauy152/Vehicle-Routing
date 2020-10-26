import TestData

from MasterRouter import MasterRouter
from GUI import InitialSetupGUI
import Packages as _Packages
from tkinter import Tk
import time
import resource
from memory_profiler import memory_usage
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

elif (Inital_vals['method'].lower() == "test") :

    for x in range(2):
        if x == 0:
            lMethod = 'aco'
        else:
            lMethod = 'pso'
        Master = MasterRouter(lMethod,500,500)
        lAcoMem = [0] * 5
        lAcoTime = [0] * 5
        lIndex = 0
        lLocationSize = 10
        for i in range(1,50):

            Locations = TestData.RandomLocations(lLocationSize)
            Vehicles = TestData.RandomVehicles( Inital_vals['num_vehicles'] )
            Master.setVehicles(Vehicles)
            Packages = _Packages.GeneratePackages(Master.getField('capacity_sum'),Locations )
            Master.setPackages(Packages)
            Master.setWorld(Locations)

            lStart = time.time()
            lMemUse = memory_usage(Master.Execute)
            lTime = (time.time() - lStart)
            lAcoTime[lIndex] += lTime
            lAcoMem[lIndex] += max(lMemUse)

            if i % 10 == 0:
                lLocationSize += 10
                lIndex += 1
        
        for index, x in enumerate(lAcoMem):
            lAcoMem[index] /= 10
            lAcoTime[index] /= 10

        lFile = open("TestResults.txt", "a")
        
        lFile.write("Method: " + lMethod.upper() + "\n")

        for index, j in enumerate(lAcoTime):
            lFile.write("Locations (" + str((index + 1) * 10) + ")" + ": Average Time (" + str(lAcoTime[index]) + ") Max Memory (" +  str(lAcoMem[index]) + ") \n")


        lFile.close()

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




