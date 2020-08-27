from random import choice,randint
# from TestData import TestLocations


def GeneratePackages(total_capacity,_locations):
    """Create a list of packages, with a max weight
    of no more than the combined carry capacity of
    all delivery agents"""
    Packages = []
    locations = _locations#TestLocations()
    remaining_capacities = total_capacity

    while remaining_capacities > 0:
        rand_weight = randint(1,25)

        if (remaining_capacities - rand_weight) < 0:
            rand_weight = remaining_capacities
            # remaining_capacities = 0
            break
        else:
            remaining_capacities = remaining_capacities - rand_weight

        #time windows
        #lets random generate a prefered time no less than 0600 and no greater than 1600; these can be the working hours
        earliest = randint(6,16)
        desired = earliest + 1
        latest = desired + 1
        if len(str(earliest)) == 1: earliest = "0{0}00".format(earliest)
        else: earliest = "{0}00".format(earliest)
        # print("earliest: %s" % earliest)

        if len(str(desired)) == 1: desired = "0{0}00".format(desired)
        else: desired = "{0}00".format(desired)
        # print("desired: %s" % desired)

        if len(str(latest)) == 1: latest = "0{0}00".format(latest)
        else: latest = "{0}00".format(latest)
        # print("latest: %s" % latest)

        Packages.append( 
            Package(
                choice(locations),
                rand_weight,
                earliest,
                desired,
                latest
                ) 
            )
    
    #print(Packages)
    return Packages



class Package():
    def __init__(self,_location,_weight,_earliest,_desired,_latest):
        self.location = _location
        self.weight   = _weight
        self.earliest = _earliest
        self.desired  = _desired
        self.latest   = _latest

    def __repr__(self):
        return "for:{0},{1}kg,e:{2},d:{3},l:{4}".format(self.location,
                                                        self.weight,
                                                        self.earliest,
                                                        self.desired,
                                                        self.latest)