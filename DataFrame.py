#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:41:13 2018

@author: sebastianhiguita
"""

import pandas as pd
import numpy as np

datos = {'Nombre': ['Chalio', 'Marisol', 'Yolanda', 'Tina'], 
    'Calificaciones': ['100', '90', '100', '80'], 
    'Deportes': ['Futbol', 'Natación', 'Basquetbol', 'Beisbol'], 
    'Materias': ['Calculo', 'Metodos numericos', 'Cocina', 'Quimica']}
    
df = pd.DataFrame(datos)
print(df)
print('\n' * 2)

# Datos no validos
datos2 = {'Nombre': ['Chalio', 'Marisol', 'Yolanda', 'N/A'], 
    'Calificaciones': ['100', np.nan, '100', '80'], 
    'Deportes': ['Futbol', 'Natación', 'Basquetbol', 'N/A'], 
    'Materias': ['Calculo', 'Metodos numericos', 'N/A', 'Quimica']}
df2 = pd.DataFrame(datos2)
print(df2)

print('\n' * 2)

print(df2.info())

print('\n' * 4)

# Estadisticas básicas
print(df2.describe())

print('\n' * 4)

nuevo = pd.DataFrame(df2)
nuevo = nuevo.replace(np.nan, "0")
print(nuevo)
print('\n' * 4)

nuevo2 = pd.DataFrame(df2)
nuevo2.dropna(how = 'any', inplace = True)
print(nuevo2)
print('\n' * 4)

# Eliminar registro buscando por columna
columna = df2[df2['Nombre'] != 'N/A']
print(columna)
print('\n' * 4)

# Llenar con ceros cualquier valor NAN en el DF
nuevo3 = pd.DataFrame(df2)
nuevo3.fillna(0, inplace = True)
print(nuevo3)
print('\n' * 4)

# Estadistircas
print(nuevo3.describe())
print('\n' * 4)

# Convertir a numeros enteros
nuevo2['Calificaciones'] = nuevo2.Calificaciones.astype(int)
print(nuevo2.describe())
print('\n' * 4)

# Estadisticas individuales
print("Promedio", nuevo2['Calificaciones'].mean())