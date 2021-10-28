# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 19:28:09 2021

@author: admin
"""

import pandas as pd
import numpy as py
import seaborn as sns
import matplotlib.pyplot as plt
inc = pd.read_csv('C:/Users/admin/Downloads/insurance.csv')
print(inc.head())
print(inc.describe())
sns.countplot(x = 'smoker', data= inc)
plt.show()
sns.scatterplot(x= 'sex',y= 'age',hue='smoker', data=inc)
plt.show()
sns.pairplot(inc.drop(['region'], axis = 1), hue='smoker', height=2)
plt.show()
sns.boxenplot('charges', data = inc)
plt.show()
sns.heatmap(inc.corr(), data = inc)
plt.show()
x = inc.corr(method = 'pearson')
print(x) 