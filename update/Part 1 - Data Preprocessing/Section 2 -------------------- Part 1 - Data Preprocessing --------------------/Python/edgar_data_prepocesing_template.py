#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 22:52:30 2025

@author: edgarmora
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# quitar la notación científica de los resultados
np.set_printoptions(suppress=True)

############### 1.setear el directorio de trabajo #############################
os.chdir("/Users/edgarmora/Documents/GitHub/machinelearning-az/update/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Python")
os.getcwd()
os.listdir()

########################### 2.Importar el dataset ###############################
# Asegúrate de que 'Data.csv' esté en el mismo directorio o proporciona la ruta completa.
dataset = pd.read_csv("Data.csv")

x = dataset.iloc[:,:]
x
x = dataset.iloc[:, :-1].values # todo menos la ultima columna
x
x = dataset.iloc[:, [0,3]].values# ultima columna
x
x = dataset.iloc[:, [0,3]].values# primera y ultima columna
x

############################## 3.Manejo de datos faltantes ######################
# Utilizamos SimpleImputer para reemplazar valores nulos con la media de la columna
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')  # Estrategia: reemplazar valores nulos con la media


X = dataset.iloc[:, :-1].values  # Seleccionamos todas las columnas excepto la última como variables independientes
y = dataset.iloc[:, -1].values  # Seleccionamos la última columna como la variable dependiente (objetivo)
X
y

##### remplazo de los valores calculados en las columnas 1 y 3 con valores faltantes
imputer.fit(X[:, 1:3])  # Aplicamos el ajuste a las columnas 1 y 2 (índices 1:3)
print(imputer.statistics_)
X[:, 1:3] = imputer.transform(X[:, 1:3])  # Reemplazamos los valores nulos en las columnas seleccionadas
X

###################### datos categóricos #######################################










