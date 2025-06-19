#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 22:03:13 2025

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

x = dataset.iloc[:,:-1].values
x
y = dataset.iloc[:,3].values
y

##################### 4.datos categóricos #######################################
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# Aplicamos OneHotEncoder a la primera columna (índice 0)
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))  # Transformamos X y lo convertimos a un array de NumPy
print(x)


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)  # Transformamos las etiquetas categóricas en valores numéricos
print(y)

###################### 5.dividir datos para entrenamiento #######################################
from sklearn.model_selection import train_test_split
# Usamos 80% para entrenamiento y 20% para prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

###################### 6.escalar datos #######################################
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)"""