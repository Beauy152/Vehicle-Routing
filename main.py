import TestData
import Packages
from MasterAgent import MasterRouter


#Create Master Router
Master = MasterRouter()

#Create Each Vehicle
#Each vehicle has a referece to the master router, this is essentially
#the same as having the contact details of the master, this is used for comms.
Vehices = TestData.TestVehicles()

#Each vehicle will send a message to the master in a specified format
#Master will keep track of vehicle information in an array of dicts.
#each place in the array represents a vehicle, with the dict storing
#various attributes
for v in Vehices:
    #Tell master : sender id,, content
    #prefixes here might make arranging data easier gl_ for global information, and identifiers for others
    Master.Tell(v.id,"(= (capacity {0}) {1})".format(v.id,v.capacity))#spacing between terms is important


Packages.GeneratePackages()