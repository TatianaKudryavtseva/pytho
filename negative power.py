# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:25:57 2020

@author: lexta
"""

def my_func_1(x, y): 
    return x ** y

def my_func_2(x, y):
    count = 1
    while y != 0:
        count *= x
        y += 1
    return 1 / count
        
    

print(my_func_1(5, -4))
print(my_func_2(5, -4))