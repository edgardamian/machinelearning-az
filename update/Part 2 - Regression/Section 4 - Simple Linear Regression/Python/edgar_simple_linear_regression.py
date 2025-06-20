#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 22:30:38 2025

@author: edgarmora
"""
# regresion lineal simple
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# quitar la notación científica de los resultados
np.set_printoptions(suppress=True)

############### 1.setear el directorio de trabajo #############################
os.chdir("/Users/edgarmora/Documents/GitHub/machinelearning-az/update/Part 2 - Regression/Section 4 - Simple Linear Regression/Python")
os.getcwd()
os.listdir()

########################### 2.Importar el dataset #############################
# Asegúrate de que 'Data.csv' esté en el mismo directorio o proporciona la ruta completa.
dataset = pd.read_csv('Salary_Data.csv')

x = dataset.iloc[:,[ 0]].values  
y = dataset.iloc[:, [1]].values  

###################### 3.dividir datos para entrenamiento #####################
from sklearn.model_selection import train_test_split
# Usamos 20 para train (entrenamiento) y 10 para test (prueba)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=0)

################# 4.Creare modelo de regresion lineal simple ##################
from sklearn.linear_model import LinearRegression
regresion = LinearRegression()
regresion.fit(x_train, y_train)
