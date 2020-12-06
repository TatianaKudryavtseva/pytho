# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:51:15 2020

@author: lexta
"""

def my_del(num1, num2):
    return (num1 / num2) if num2 != 0 else 'На ноль делить нельзя'    
 
    
print(my_del(86, 9))  
print(my_del(84, 0))  


print(my_del(int(input('Введите первое число')), 
             int(input('Введите второе число'))))