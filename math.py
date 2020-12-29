#!/usr/bin/env python

from Node import Node
from Tree import Tree
from Expression import Expression

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sub = Math(nums, "-")
    add = Math(nums, "_")
    div = Math(nums, "/")
    mul = Math(nums, "*")
    print("sub: " + str(sub.doOperation()))
    print("add: " + str(add.doOperation()))
    print("div: " + str(div.doOperation()))
    print("mul: " + str(mul.doOperation()))
    
    expression = "2*3*4+5/5*6"
    e = Expression(expression)
    print(e)
    t = Tree(e)
    # t.printTree()
    print(t.calculateTree())
    # t.editTree()
    #print(t.root().value())
  #  t.printTree()

class Math :
        def __init__(self, nums=[], o=""):
            self.arg = nums
            self.operation = o

        
        def doOperation(self):
            answer = 0
            if self.operation == "*":
                answer += 1    
                for nums in self.arg:
                    answer *= nums
            if self.operation == "/":
                answer += 1
                for nums in self.arg:
                    answer /= nums
            if self.operation == "-":
                for nums in self.arg:
                    answer -= nums
            else:
                for nums in self.arg:
                    answer += nums
            
            return answer

        def takeInput(self):
            answer = "yes"
            nums = []
            while answer != "no":
                ansr = input("Type out a number, no if you wanna stop")
                if ansr == "no":
                    self.arg = nums
                    break
                else:
                    nums.append(int(ansr))

        def takeOperation(self):
            op = input("What operation?")
            self.operation = op


main()
