import time

from osbrain import Agent
from osbrain import run_agent
from osbrain import run_nameserver

from master import MasterRouter
from vehicle import Vehicle

if __name__ == '__main__':
    #sys deployment
    ns = run_nameserver()
    #
    master = run_agent('main',base=MasterRouter)
    bob = run_agent('bob',base=Vehicle)
    job = run_agent('job',base=Vehicle)
    #

    # bob.connect(master.addr('main'),handler=Vehicle.custom_log)
    # job.connect(master.addr('main'),handler=Vehicle.custom_log)
    master.connect(bob.bind('REP',alias='bob',handler=Vehicle.reply),alias='bob')
    master.connect(job.bind('REP',alias='job',handler=Vehicle.reply),alias='job')

    # master.send('main_1','capacities please::')
    # master.send('main_2','capacities please::')
    # reply = master.recv('main_1')
    # print(reply)
    # reply = master.recv('main_2')
    # print(reply)

    print((ns.agents())[1:])#list all agents

    for a in (ns.agents())[1:]:#ignore first name: main
        master.send( a ,'main to {0} - capacity please:'.format(a))
        print(master.recv(a))
    # master.send('main_1','capacities please::')
    # master.send('main_2','capacities please::')
    # reply = master.recv('main_1')
    # print(reply)
    # reply = master.recv('main_2')
    # print(reply)
    #send messages
    # for _ in range(6):
    #     time.sleep(1)
    #     master.send('main',"Hello All")



    ns.shutdown()