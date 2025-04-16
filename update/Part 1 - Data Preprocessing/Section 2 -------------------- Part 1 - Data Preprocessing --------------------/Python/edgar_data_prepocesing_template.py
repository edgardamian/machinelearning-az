#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 22:52:30 2025

@author: edgarmora
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Data.csv")

x = dataset.iloc[:, :-1].values
x
x = dataset.iloc[:, 3].values
x