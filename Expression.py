#!/usr/bin/env python3

class Expression:
    def __init__(self, expression):
        self.operations = Operations()
        self.items_ = list(expression)
        self.levels_ = self.operations.processLevels(self.items_)
        self.size_ = len(self.items_)

    def insert(self, value):
        self.items_.append(value)
        self.levels_.append(operations.getLevel(value))
        self.size_ += 1

    def remove(self, idx):
        self.items_.remove(self.items_[idx])
        self.levels_.remove(self.levels[idx])
        self.size_ -= 1
            
    def __getitem__(self, idx):
        return (self.items_[idx], self.levels_[idx])

    def levels(self):
        return self.levels_
    
    def __len__(self):
        return self.size()

    # def empty(self):
    #     return (self.size_ == 0)
    