#!/usr/bin/env python

from Node import Node
from Tree import Tree
from Expression import Expression

def main():
    expression = '300*5'
    e = Expression(expression)
    print(e)
    # print(e[0])
    t = Tree(e)
    # t.printTree()
    print(t.calculateTree())

main()
