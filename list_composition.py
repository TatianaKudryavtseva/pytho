# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:55:30 2020

@author: lexta
"""
from functools import reduce

user_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(lambda a, b: a * b, user_list))
