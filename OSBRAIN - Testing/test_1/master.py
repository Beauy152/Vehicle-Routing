from osbrain import Agent
from osbrain import run_agent
from osbrain import run_nameserver


class MasterRouter(Agent):
    def on_init(self):
        pass#self.bind()
        #self.bind('PUB',alias='main')
    
    def hello(self,name):
        self.send('main','Hello, %s!.' % (name))
