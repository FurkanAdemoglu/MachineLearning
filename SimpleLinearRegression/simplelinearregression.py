# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:51:26 2019

@author: Lenovo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler=pd.read_csv("satislar.csv")

aylar=veriler[['Aylar']]
#Ayları aylara atatık
print(aylar)

satıslar=veriler[['Satislar']]
#Satisları satıslara atatık
print(satıslar)


#veriler test ve train için bölündü
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(aylar,satıslar,test_size=0.33,random_state=0)


#verilerin ölçeklenmesi
'''from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)
Y_train=sc.fit_transform(y_train)
Y_test=sc.fit_transform(y_test)
'''
#model inşası(linear regression)
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)

#verilerimizi linearRegression ile tahmin ettik
tahmin=lr.predict(x_test)
#verilerimi sıralamak için kullandık
x_train=x_train.sort_index()
y_train=y_train.sort_index()

#grafiği ekrana çizdirmek için kullanılır
plt.plot(x_train,y_train)

#tahmin ettiğimiz sonuçları grafiğe çizdirdik

plt.plot(x_test,lr.predict(x_test))
#grafik başlığı
plt.title("aylara göre satışlar")

plt.xlabel("aylar")
plt.ylabel("satıslar")

