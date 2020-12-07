#!/usr/bin/env python

class Queue:
    def __init__(self):
        self.items_ = []
        self.size_ = 0

    def enqueue(self, value):
        self.items_.append(value)
        self.size_ += 1

    def dequeue(self):
        if self.size_ == 0:
            return None
        self.size_ -= 1
        value = self.items_[0]
        self.items_.remove(value)
        return value

    def items(self):
        return self.items_
    
    def size(self):
        return self.size_

    def empty(self):
        if self.size_ == 0:
            return True
        return False
