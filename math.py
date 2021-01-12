#!/usr/bin/env python3

from Node import Node
from Tree import Tree
from Expression import Expression
import sys

def main():
    if len(sys.argv) > 1:
        expression = sys.argv[1]
        e = Expression(expression)
        print(e)
        # print(e[0])
        t = Tree(e)
        # t.printTree()
        print(t.calculateTree())
    else:
        print("Need an expression to calculate!")

main()
