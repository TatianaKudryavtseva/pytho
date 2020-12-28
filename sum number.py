# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:45:34 2020

@author: lexta
"""

def sum_numbers(symbol):
    total = 0
    a = True
    while a:
        numbers = input(f'Введите числа через пробел или {symbol} для завершения').split()
        for num in numbers:
            if num != symbol:
                total += int(num)
            else:
                a = False
        print(total)     
    
sum_numbers('%')    