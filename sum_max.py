# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:55:57 2020

@author: lexta
"""

def my_func(num1, num2, num3):
    if num1 >= num2:
        if num3 >= num2:
            return (num1 + num3)
        else:
            return (num1 + num2)
    elif num2 >= num1:
        if num1 >= num3:
            return (num1 + num2)
        else:
            return (num2 + num3)
        

print(my_func(2, 5, 8))
print(my_func(7, 1, 6))
print(my_func(4, 7, 2))
print(my_func(9, 4, 4))
print(my_func(3, 6, 5))
print(my_func(7, 4, 10))
print(my_func(63, 57, 4))