#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 17:59:56 2018

@author: sebastianhiguita
"""

import pandas as pd
import numpy as np

datos = pd.read_csv('ATP.csv', encoding = 'iso-8859-1')

print(datos.info())
print(datos.head())

nuevo = pd.DataFrame(datos)

print(nuevo)

nuevo = nuevo.replace(np.nan, '0')

print('Impresión sin NaN')

print(nuevo.info())

print('\n' * 5)

print('*****Estadísticas sin NaN*****')

print(nuevo.describe())

print('\n' * 5)

print('*****Estadísticas solamente números*****')

print(nuevo.describe(include = [np.number]))

print('\n' * 5)

nuevo = nuevo.replace('N/A', '0')
nuevo = nuevo.replace('NR', '0')

print('*****Estadísticas sin N/Ao NR*****')

print(nuevo.describe())

print(list(nuevo))

nuevo['Wsets'] = nuevo.Wsets.astype(int)

nuevo['WRank'] = nuevo.WRank.astype(int)

print('\n' * 5)

print('*****Estadísticas con Ranking y Sets*****')

print(nuevo.describe())

nuevo.dropna(how = 'any', inplace = True)

print(nuevo.head())