# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:59:12 2020

@author: lexta
"""

from sys import argv

prog_name, work_hours, rate_per_hour, prize = argv
salary = (int(work_hours) * int(rate_per_hour)) + int(prize)
print(salary)
