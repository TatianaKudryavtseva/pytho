# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:17:07 2020

@author: lexta
"""
from math import factorial

def fact(n):
    fact = [factorial(el) for el in range(1, n + 1) ]
    return fact    
        

def generator(n):
    for el in fact(n):
        yield el

      
x = generator(8)   
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))