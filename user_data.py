# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:12:09 2020

@author: lexta
"""

def user_data(name, lastname, year_birth, city, email, tel):
    print(name, lastname, year_birth, city, email, tel)
    
user_data(name = input('Введите имя'), lastname = input('Введите фамилию'), 
          year_birth = input('Введите год рождения'), 
          city = input('Введите город проживания'), 
          email = input('введите email'), tel = input('Введите телефон'))
   
