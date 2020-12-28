# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:49:29 2020

@author: lexta
"""

def int_func(text):
    return text.title()
    
for word in input().split():
    print(int_func(word), end=' ')