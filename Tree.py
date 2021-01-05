#!/usr/bin/env python3

from Node import Node
from Expression import Expression
from Operations import Operations

class Tree:

    def __init__(self, expression):
       self.root = 'temp'
       self.root = self.writeTree(expression, self.root)
       print("---Tree Built---")
       self.operations_ = Operations()
    
    def __str__(self):
        return self.printTree()
    
    def writeTree(self, expression, subroot):
        if len(expression) == 0:
            return None
        elem = self.min(expression)
        subroot = Node(elem[0])
        subroot.leftChild_ = self.writeTree(expression[0:elem[1]], subroot.leftChild())
        subroot.rightChild_ = self.writeTree(expression[elem[1]:], subroot.rightChild())
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
            return left + right
        if subroot.value() == '-':
            return left - right
        if subroot.value() == '*':
            return left * right
        if subroot.value() == '/':
            return left / right
        if subroot.value() == '^':
            return left ** right
        
        

    def min(self, expression):
        operations = Operations()
        min_ = 100000
        idx_nodes = []
        for i, item in enumerate(expression):
            if min_ > item.l:
                min_ = item.l
        for i, item in enumerate(expression):
            if min_ == item.l:
                idx_nodes.append(i)
        elem = expression.pop(idx_nodes[len(idx_nodes) - 1]).e
        return (elem, idx_nodes[len(idx_nodes) - 1])