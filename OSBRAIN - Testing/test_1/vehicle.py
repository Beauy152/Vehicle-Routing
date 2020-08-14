from osbrain import Agent
from osbrain import run_agent
from osbrain import run_nameserver
from random  import randint



class Vehicle(Agent):
    def reply(self,message):
        return "({0})My Capacity: {1}".format(self.name,self.vehicle_capacity)

    def on_init(self):
        self.vehicle_capacity = randint(1,10)
        #self.bind('REP',alias='main',handler=self.reply)

    def custom_log(self,message):
        self.log_info('Recieveed:%s' % message)