# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 18:19:50 2021

@author: dan christopher
"""

import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir("C:/Users/dan christopher/Documents")
iris = pd.read_csv('Iris.csv')
print(iris.head())
print(iris.describe())
sns.countplot(x='Species', data = iris)
plt.show()
sns.scatterplot('SepalLengthCm','SepalWidthCm', hue='Species',data = iris)
plt.show()
sns.pairplot(iris.drop(['Id'],axis =1), hue= 'Species', height= 2)
plt.show()
sns.heatmap(iris.corr(), data = iris)
plt.show()
x= iris.corr(method= 'pearson')
print(x)
sns.heatmap(iris.corr(method='pearson').drop(['Id'],axis=1).drop(['Id'],axis=0))
