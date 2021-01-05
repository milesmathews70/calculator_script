#!/usr/bin/env python3

from Operations import Operations
from Element import Element

class Expression:
    def __init__(self, expression):
        self.operations = Operations()
        self.items_ = self.processExpression(expression)
        self.size_ = len(self.items_)

    def processExpression(self, expression):
        l = []
        paranthesis_counter = 0
        previous_integer = ''
        for element in expression:
            if element in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                previous_integer += element
            else:
                if previous_integer != '':
                    l.append(Element(previous_integer, self.operations[previous_integer] + 4*paranthesis_counter))
                    previous_integer = ''
                if element is '(':
                    paranthesis_counter += 1
                    continue

                elif element is ')':
                    paranthesis_counter -= 1
                    continue
                
                elif element is ' ':
                    continue

                else:
                    l.append(Element(element, self.operations[element] + 4*paranthesis_counter))
        if previous_integer != '':
            l.append(Element(previous_integer, self.operations[previous_integer]))
        return l

    def insert(self, value):
        self.items_.append(value)
        self.size_ += 1

    def pop(self, idx):
        elem = self.items_[idx]
        self.items_.remove(self.items_[idx])
        self.size_ -= 1
        return elem
            
    def __getitem__(self, idx):
        return self.items_[idx]

    def levels(self):
        return self.levels_
    
    def __len__(self):
        return self.size_
    
    def __str__(self):
        response = [str(items.e) for items in self.items_]
        return ''.join(response)
    