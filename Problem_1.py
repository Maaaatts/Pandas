# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 22:53:42 2019

@author: Matthew Rabanes
"""

import pandas as pd

cars = pd.read_csv('cars.csv')

first = cars[0:5]
last = cars[27:32]

print('The first five cars are: \n \n' +str(first))
print('--------------------------------------------')
print('The last five cars are: \n' +str(last))