#!/usr/bin/env python3

from Node import Node
from Expression import Expression

class Tree:
	
    def __init__(self, expression):
       self.expression_ = expression
       self.writeTree(expression)

    def writeTree(self, expression):
        list_of_nodes = []
        currentNode = None
        idx = 0
        maxLevel = -1
        maxLevelidx = -1
        while (len(expression) > 0):
            if maxLevel < expression[idx][1]:
                maxLevel = expression[idx][1]
                maxLevelidx = idx
            if idx == len(expression):
                if maxLevelidx - 1 > 0 && maxLevelidx + 1 < len(expression) && self.is_int(expression[maxLevelidx - 1][0]) && self.is_int(expression[maxLevelidx + 1][0]):
                    currentNode = Node(expression[maxLevelidx], expression[maxLevelidx - 1][0], expression[maxLevelidx + 1][0])
                    list_of_nodes.append(currentNode)
                    expression.remove(maxLevelidx + 1)
                    expression.remove(maxLevelidx)
                    expression.remove(maxLevelidx - 1)
                elif maxLevelidx - 1 > 0 && self.is_int(expression[maxLevelidx - 1][0]):
                    list_of_nodes.append(Node(expression[maxLevelidx], currentNode, expression[maxLevelidx - 1][0]))
                    expression.remove(maxLevelidx)
                    expression.remove(maxLevelidx)
                elif maxLevelidx + 1 < len(expression) && self.is_int(expression[maxLevelidx + 1][0]):
                    list_of_nodes.append(Node(expression[maxLevelidx], currentNode, expression[maxLevelidx + 1][0]))
                    expression.remove(maxLevelidx - 1)
                    expression.remove(maxLevelidx - 1)
                else:
                    list_of_nodes.append(Node(expression[maxLevelidx], 'temp', 'temp'))
                    expression.remove(maxLevelidx)
                idx = 0
                maxLevel = -1
                maxLevelidx = -1
            else:
                idx += 1
        self.root = self.min(list_of_nodes)
        writeTreeRecur(list_of_nodes, self.root)
        # self.root = Node(expression.dequeue())
        # self.writeTreeRecur(expression, self.root)
    
    def __str__:
        return printTree()
    
    def writeTreeRecur(self, expression, currentNode):
        if len(expression) == 0:
            return
        if currentNode.leftChild().value() == 'temp':
            currentNode.leftChild(self.min(list_of_nodes))
        if currentNode.rightChild().value() == 'temp':
            currentNode.rightChild(self.min(list_of_nodes))
        self.writeTreeRecur(expression, currentNode.leftChild())
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

    def is_int(self, elem):
        return type(elem) == int or type(elem) == float

    def min(self, nodes):
        return nodes[len(nodes) - 1]

