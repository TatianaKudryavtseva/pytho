# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:24:55 2020

@author: lexta
"""

user_list = input('введите последовательность чисел через пробел').split()
list_next_max = [user_list[i] for i in range(1, len(user_list)) 
                 if int(user_list[i]) > int(user_list[i - 1])]
print(list_next_max)