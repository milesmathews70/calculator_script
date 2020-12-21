#!/usr/bin/env python3

class Node:
        def __init__(self, v=None, left=None, right=None, level=10):
            self.value_ = v
	        if left != None:
            	self.leftChild_ = Node(left)
            else:
                self.leftChild_ = None
	        if right != None:
		        self.rightChild_ = Node(right)
            else:
                self.rightChild_ = None
            self.level_ = level
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
