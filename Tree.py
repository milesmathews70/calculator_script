#!/usr/bin/env python3

from Node import Node
from Expression import Expression
from Operations import Operations

class Tree:

    def __init__(self, expression):
       self.root = 'temp'
       self.root = self.writeTree(expression, self.root)
       self.operations_ = Operations()
    
    def __str__(self):
        return self.printTree()
    
    def writeTree(self, expression, subroot):
        if len(expression) == 0:
            return None
        elem = self.min(expression)
        subroot = Node(elem[0])
        subroot.leftChild_ = self.writeTree(expression[0:elem[1]], subroot.leftChild())
        # print(subroot.leftChild_)
        subroot.rightChild_ = self.writeTree(expression[elem[1]:], subroot.rightChild())
        # print(subroot.rightChild_)
        return subroot
            
    
    def root(self):
        return self.root

    def printTree(self):
        if self.root == None:
            return
        self.printTreeRecur(self.root)

    def printTreeRecur(self, node):
        # if node == None:
        #     return
        if node.leftChild() != None:
            self.printTreeRecur(node.leftChild())
        print node.value()
        if node.rightChild() != None:
            self.printTreeRecur(node.rightChild())

    def calculateTree(self):
        if self.root != None:
            return self.calculateTreeRecur(self.root)
        return 0

    def calculateTreeRecur(self, subroot):
        left = 1
        right = 1
        if subroot.leftChild().is_int():
            left = int(subroot.leftChild().value())
        else:
            left = self.calculateTreeRecur(subroot.leftChild())
        if subroot.rightChild().is_int():
            right = int(subroot.rightChild().value())
        else:
            right = self.calculateTreeRecur(subroot.rightChild())
        
        if subroot.value() == '+':
            print(left + right)
            return left + right
        if subroot.value() == '-':
            print(left - right)
            return left - right
        if subroot.value() == '*':
            print(left * right)
            return left * right
        if subroot.value() == '/':
            print(left / right)
            return left / right
        
        

    def min(self, expression):
        operations = Operations()
        min_ = 6
        idx = -1
        for i, item in enumerate(expression):
            if min_ > operations.getLevel(item):
                min_ = operations.getLevel(item)
                idx = i
        elem = expression.pop(idx)
        self.expression = expression
        return (elem, idx)