# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 22:56:23 2019

@author: Matthew Rabanes
"""

import pandas as pd

cars = pd.read_csv('cars.csv')

odd = cars.iloc[[0,1,2,3,4],[1,3,5,7,9]]
m = cars.loc[cars['Model'] == 'Mazda RX4']
c = cars.loc[cars['Model'] == 'Camaro Z28', ['Model','cyl']]
cg = cars.loc[[1,28,18],['Model','cyl','gear']]

print('The first five odd-numbered columns of cars are: \n' +str(odd))
print('--------------------------------------------')
print('Mazda RX4 \n' +str(m))
print('--------------------------------------------')
print('Number of Cylinders for Camaro Z28 \n' +str(c))
print('--------------------------------------------')
print('Number of Cylinders and Gear Type for specified cars: \n' +str(cg))