# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:34:27 2019

@author: Lenovo
"""

#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#kodlar
#veri yükleme
veriler=pd.read_csv('eksikveriler.csv')#tek tırnak yerine çift tırnakta olabilir

print(veriler)
boy=veriler[['boy']]
print(boy)

boykilo=veriler[['boy','kilo']]
print(boykilo)

x=10
class insan:
    boy=180
    def kosmak(self,b):
        return b+10
    
ali=insan()
print(ali.boy)
print(ali.kosmak(90))

#eksik veiler
#sci-kit learn
from sklearn.preprocessing import Imputer

imputer=Imputer(missing_values="NaN",strategy="mean",axis=0)#değerleri olmayanlara yas değerlerinin ortalamasını alan strateji
Yas=veriler.iloc[:,1:4].values
print(Yas)
imputer=imputer.fit(Yas[:,1:4])#stratejiyi veri üzerine uyguluyoruz
Yas[:,1:4]=imputer.transform(Yas[:,1:4])
print(Yas)
#Kategorik Veriler
ulke=veriler.iloc[:,0:1].values
print(ulke)
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
ulke[:,0]=le.fit_transform(ulke[:,0])
print(ulke)

ohe=OneHotEncoder(categorical_features='all')
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)

     