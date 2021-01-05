#!/usr/bin/env python3

class Node:
        def __init__(self, v=None):
            self.value_ = v
            if v != None:
                self.leftChild_ = Node()
                self.rightChild_ = Node()
            else:
                self.leftChild_ = None
                self.rightChild_ = None
                
        def leftChild(self, v=None):
            if v != None: 
                self.leftChild_ = Node(v)
            return self.leftChild_

        def rightChild(self, v=None):
            if v != None:
                self.rightChild_ = Node(v)
            return self.rightChild_

        def setValue(self, v):
            self.value_ = v

        def value(self):
            return self.value_

        def __str__(self):
            return self.value_

        def is_int(self):
            try:
                int(self.value_)
                return True
            except:
                return False

        def equals(self, other):
            self.leftChild_ = other.leftChild_
            self.rightChild_ = other.rightChild_
            self.value_ = other.value_
        
        def __call__(self):
            return self.value_
