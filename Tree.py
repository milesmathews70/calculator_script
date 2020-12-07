#!/usr/bin/env python

from Node import Node
from Queue import Queue

class Tree:
    def __init__(self, expression):
       self.root = Node(expression.dequeue())
       self.writeTreeRecur(expression, self.root)
       temp_one = self.root.rightChild().leftChild().value()
       temp_two = self.root.rightChild().rightChild().leftChild().value()
       
       self.root.rightChild().leftChild().leftChild().equals(self.root)

        #More to come later

    def writeTree(self, expression):
        self.root = Node(expression.dequeue())
        self.writeTreeRecur(expression, self.root)
    
    def writeTreeRecur(self, expression, currentNode):
        if expression.empty():
            return currentNode
        currentNode.leftChild(expression.dequeue())
        currentNode.rightChild(expression.dequeue())
        self.writeTreeRecur(expression, currentNode.rightChild())
    
    def root(self):
        return self.root

    def printTree(self):
        if self.root == None:
            return
        print(self.printTreeRecur(self.root))

    def printTreeRecur(self, node):
        if node == None:
            return
        self.printTreeRecur(node.leftChild())
        print(node.value())
        self.printTreeRecur(node.rightChild())
    
    def editTree(self):
        pass
        if self.root != None:
            self.root = self.editTreeRecur(self.root)

    def editTreeRecur(self, currentNode):
        if currentNode.rightChild() != None:
            if currentNode.rightChild().is_int() == False:
                temp_one = currentNode.rightChild().leftChild().value()
                temp_two = currentNode.rightChild().rightChild().leftChild().value()

                #Opening parenthesis, repeat for all of the expressions inside the parentheses?
                currentNode.rightChild().leftChild(left=currentNode.leftChild())
                currentNode.equals(currentNode.rightChild())

                #Closing parenthesis
                currentNode.rightChild().setValue(temp_two)
                currentNode.rightChild().leftChild(left=currentNode)
                currentNode.setValue(currentNode.rightChild().value())
                #currentNode.leftChild().rightChild().setValue(temp_one)
                print(currentNode.value())
                print(currentNode.rightChild().value())
                #print(currentNode.rightChild().leftChild().value())
                print(currentNode.leftChild().value())
                #print(currentNode.leftChild().leftChild().rightChild())
                #print(currentNode.leftChild().rightChild().value())
                #self.printTreeRecur(currentNode)
        return currentNode
