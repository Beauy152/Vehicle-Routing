import TestData

from MasterRouter import MasterRouter
from GUI import InitialSetupGUI
import Packages as _Packages
from tkinter import Tk
import time
#import resource
from memory_profiler import memory_usage

def main():
    """GUI Manager for inital setup of values"""
    root = Tk()
    InitalSetupView = InitialSetupGUI("title",root)
    root.mainloop()

    Inital_vals = InitalSetupView.getData()
    print( InitalSetupView.getData() )
    #example output
    #{'num_locations': 16, 'num_vehicles': 1, 'useGoogleData': 1}



    if (Inital_vals['method'].lower() == "test") :
        #Loop for both methods
        for x in range(3):
            if x == 0:
                lMethod = 'aco'
            elif x == 1:
                lMethod = 'pso_s1'
            else:
                lMethod = 'pso_s2'
            #Initialize variables
            Master = MasterRouter(lMethod,500,500)
            lAcoMem = [0] * 5
            lAcoTime = [0] * 5
            lAcoRoute= [0] * 5
            lIndex = 0
            lLocationSize = 10
            #Loop over 50 iterations (10 per location size iteration)
            for i in range(1,50):
                #Create world and agents
                Locations = TestData.RandomLocations(lLocationSize)
                Vehicles = TestData.RandomVehicles( Inital_vals['num_vehicles'] )
                Master.setVehicles(Vehicles)
                Packages = _Packages.GeneratePackages(Master.getField('capacity_sum'),Locations )
                Master.setPackages(Packages)
                Master.setWorld(Locations)

                #Start timer
                lStart = time.time()
                #Execute algorithm checking memory usage
                lMemUse = memory_usage(Master.Execute)
                #Stop time
                lTime = (time.time() - lStart)

                #Add to sum
                lAcoRoute[lIndex] += Master.RouteSum()
                lAcoTime[lIndex] += lTime
                lAcoMem[lIndex] += max(lMemUse)

                # print("master.rountesum")
                # print(Master.RouteSum())
                #Check if locationsize should increase
                if i % 10 == 0:
                    lLocationSize += 10
                    lIndex += 1
            
            #Calculate averages
            for index, x in enumerate(lAcoMem):
                lAcoRoute[index] /= 10
                lAcoMem[index] /= 10
                lAcoTime[index] /= 10


            lFile = open("TestResults.txt", "a")
            
            lFile.write("Method: " + lMethod.upper() + "\n")

            #Write to file
            for index, j in enumerate(lAcoTime):
                lFile.write("Locations ({0}) : Average Time ({1}), Max Memory ({2}), Average Route Length ({3})\n".format( (index + 1) * 10 , lAcoTime[index], lAcoMem[index], lAcoRoute[index] ))
                #lFile.write("Locations (" + str((index + 1) * 10) + ")" + ": Average Time (" + str(lAcoTime[index]) + ") Max Memory (" +  str(lAcoMem[index]) + ") \n")


            lFile.close()
    else:
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




if __name__ == '__main__':
    main()