#!/usr/bin/env python3

from Operations import Operations

class Expression:
    def __init__(self, expression):
        self.operations = Operations()
        self.items_ = list(expression)
        # self.levels_ = self.operations.processLevels(self.items_)
        self.size_ = len(self.items_)

    def insert(self, value):
        self.items_.append(value)
        # self.levels_.append(operations.getLevel(value))
        self.size_ += 1

    def pop(self, idx):
        elem = self.items_[idx]
        self.items_.remove(self.items_[idx])
        # self.levels_.remove(self.levels_[idx])
        self.size_ -= 1
        return elem
            
    def __getitem__(self, idx):
        return self.items_[idx]

    def levels(self):
        return self.levels_
    
    def __len__(self):
        return self.size_
    
    def __str__(self):
        return ''.join(self.items_)
    

    # def empty(self):
    #     return (self.size_ == 0)
    