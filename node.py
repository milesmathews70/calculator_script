#!/usr/bin/env python

class Node:
        def __init__(self, v=None, left=None, right=None):
            self.value_ = v
            self.leftChild_ = left
            self.rightChild_ = right

        def leftChild(self, v=None, left=None, right=None):
            if v != None: 
                if self.leftChild_ == None:
                    self.leftChild_ = Node(v)
                else:
                    self.leftChild_.value_ = v
                self.leftChild_.leftChild_ = left
                self.leftChild_.rightChild_ = right
            return self.leftChild_

        def rightChild(self, v=None, left=None, right=None):
            if v != None:
                if self.rightChild_ == None:
                    self.rightChild_ = Node(v)
                else:
                    self.rightChild_.value_ = v
                self.rightChild_.leftChild_ = left
                self.rightChild_.rightChild_ = right
            return self.rightChild_

        def setValue(self, v):
            self.value_ = v

        def value(self):
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
