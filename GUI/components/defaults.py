
def defaultsParser(filename):
    """Opens given file and parses as gui defaults format"""
    defaults = {}
    with open(filename,'r') as file:
        lines = [line.split(':') for line in file]
        #print(lines)
        for line in lines:
            defaults.update({line[0]:line[1].rstrip() })
    return defaults