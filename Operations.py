#!/usr/bin/env python3

class Operations:

    def __init__(self):
        self.operations = {"+" : 1, "-" : 1, "*" : 2, "/" : 2, "^" : 3, "(" : 4, ")" : 4}
    
    def __getitem__(self, input_):
        if input_ in self.operations:
            return self.operations[input_]
        else:
            return 5

    def processLevels(self, input_):
        levels = []
        for i in input_:
            levels.append(self.getLevel(i))
        return levels

    def __contains__(self, item):
        return item in self.operations.keys()