# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:29:31 2019

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np

veriler=pd.read_csv("veriler.csv")
print(veriler)

ulke=veriler.iloc[:,0:1].values
print(ulke)

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
#ulkeleri sayısal kavramlara çevirdik
ulke[:,0]=le.fit_transform(ulke[:,0])
print(ulke)
Yas=veriler.iloc[:,1:4].values

ohe=OneHotEncoder(categorical_features='all')
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)
#cinsiyetleri aldık
c=veriler.iloc[:,-1:].values
print(c)

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
#cinsiyetleri de aynı şekilde sayısal kavramlara çeviridk
c[:,0]=le.fit_transform(c[:,0])
print(ulke)

ohe=OneHotEncoder(categorical_features='all')
c=ohe.fit_transform(c).toarray()
print(c)

#sonuc içine ulkeleri sayısal ulke kategorilerinde sayısal karşılıklara çeviridik
sonuc=pd.DataFrame(data=ulke,index=range(22),columns=['fr','tr','us'])
print(sonuc)

#boy kilo yası kategoriledik
sonuc2=pd.DataFrame(data=Yas,index=range(22),columns=['boy','kilo','yas'])
print(sonuc2)

cinsiyet=veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3=pd.DataFrame(data=c[:,:1],index=range(22),columns=['Cinsiyet'])
print(sonuc3)
#concat fonksiyonunu değerleri birleştirmek için kullandık

s=pd.concat([sonuc,sonuc2],axis=1)
print(s)

s2=pd.concat([s,sonuc3],axis=1)
print(s2)
#verilerimizi makinemizi eğitmek için kullandık
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(s,sonuc3,test_size=0.33,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

boy=s2.iloc[:,3:4].values
print(boy)
sol=s2.iloc[:,:3]
sag=s2.iloc[:,4:]

veri=pd.concat([sol,sag],axis=1)
x_train,x_test,y_train,y_test=train_test_split(veri,boy,test_size=0.33,random_state=0)

r2=LinearRegression()
r2.fit(x_train,y_train)
y_pred=r2.predict(x_test)








































