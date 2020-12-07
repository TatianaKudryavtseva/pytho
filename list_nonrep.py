# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:44:52 2020

@author: lexta
"""

user_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in user_list if user_list.count(el) == 1])
