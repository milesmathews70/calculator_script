#!/usr/bin/env python3

class Operations:

    def __init__(self):
        self.operations = {"+" : 1, "-" : 1, "*" : 2, "/" : 2, "**" : 3, "(" : 4, ")" : 4}
    
    def getLevel(self, input):
        if input in self.operations:
            return self.operations[input]
        else:
            return 0

    def processLevels(self, input):
        levels = []
        for i in input:
            levels.append(self.getLevel(i))
        return levels

    def __contains__(self, item):
        return item in self.operations.keys()