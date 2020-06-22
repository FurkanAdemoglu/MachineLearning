# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:34:27 2019

@author: Lenovo
"""

#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler = pd.read_csv('satislar.csv')
#print(veriler)
aylar=veriler[['Aylar']]
print(aylar)
satislar=veriler[['Satislar']]
print(satislar)


'''
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(s,sonuc3,test_size=0.33,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)
'''


     