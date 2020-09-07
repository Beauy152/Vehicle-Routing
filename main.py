#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#main.py

import TestData
import Packages as _packages_
from MasterAgent import MasterRouter
from random import sample, randint

#Get list of Locations
Locations = TestData.TestLocations()

#Create Master Router
Master = MasterRouter()

#initialise master's world view 
Master.SetWorld(Locations[0],Locations[1:])

#Create Each Vehicle
#Each vehicle has a referece to the master router, this is essentially
#the same as having the contact details of the master, this is used for comms.
Vehicles = TestData.TestVehicles()

#Each vehicle will send a message to the master in a specified format
#Master will keep track of vehicle information in an array of dicts.
#each place in the array represents a vehicle, with the dict storing
#various attributes
for v in Vehicles:
    #Tell master : sender id,, content
    #prefixes here might make arranging data easier gl_ for global information, and identifiers for others
    Master.Tell(v.id,"(= (capacity {0}) {1})".format(v.id,v.capacity))#spacing between terms is important

#Tell Master to sum capacities of registered vehicles
#this could be made more verbose by adding a lookup dictionary on the recieving end.
print("Sum of Vehicle Capacities: %s" % Master.Perform("SumCapacities") )

#Ask master for total capacity of vehicle, generate package list accordingly
Packages = _packages_.GeneratePackages( Master.Ask("(total_capacity {0})".format(Master.id)),Locations )

#Send package list to master
Master.SetPackages(Packages)

#Test Line Show combined weight of packages
print ("sum of package weights:%s" % sum(package.weight for package in Packages) )


#For testing purposes#
#for vehicle in Vehicles:
temp_route = [Master.world.warehouse[0]]
temp_route.extend(sample(Master.world.locations,randint(1,8)))
temp_route.append(Master.world.warehouse[0])
#print(temp_route)
Vehicles[0].route = temp_route#vehicle.route = temp_route

Master.Draw(Locations,Vehicles)
#Testline#
# for l in Master.world.locations:
#     print(l)

#Master computes routes


#Send Routes to Delivery Agents


#Execute Delivery

#