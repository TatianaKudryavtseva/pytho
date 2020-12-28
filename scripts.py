# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:05:16 2020

@author: lexta
"""

from itertools import count, cycle

for el in count(10):
    if el > 15:
        break
    else:
        print(el)
        

num = 0    
for el in cycle(['p','y','t','h','o','n']):
    if num > 20:
        break
    else:
        print(el)
        num +=1
    