# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:40:58 2019

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
import statsmodels.api as sm


veriler=pd.read_csv("maaslar_yeni.csv")
x=veriler.iloc[:,2:5]
y=veriler.iloc[:,5:]
X=x.values
Y=y.values

#Bu ödev için linear (doğrusal) regression
#kütüphaneyi import ettik
from sklearn.linear_model import LinearRegression

lin_reg=LinearRegression()
#verilerimizle makineyi eğittik
lin_reg.fit(X,Y)
#Tahmin algoritmaları
model=sm.OLS(lin_reg.predict(X),X)
print(model.fit().summary())

print("Linear R2 değeri:")
print(r2_score(Y,lin_reg.predict(X)))

#polynomial regresyon
#kütüphanemizi import ettik
from sklearn.preprocessing import PolynomialFeatures
#polynom derecesini ayarladık
poly_reg=PolynomialFeatures(degree=4)

x_poly=poly_reg.fit_transform(X)
print(x_poly)
#linear regresyon ve polynomial regresyon aynıdır tek değişik derecesi
#Fonksiyonumuzu alıştırdık
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)
#OLS r2 gibi ölçme fonksiyonudur onu çalıştırdık
model2=sm.OLS(lin_reg2.predict(poly_reg.fit_transform(X)),X)
print("polynomial R2 değeri")
#r2 yi çalıştırdık
print(r2_score(Y,lin_reg2.predict(poly_reg.fit_transform(X))))
#Verilerimizi svr için scale ettik
from sklearn.preprocessing import StandardScaler
sc1=StandardScaler()
x_olcekli=sc1.fit_transform(X)
sc2=StandardScaler()
y_olcekli=sc2.fit_transform(Y)
#svr kütüphanesini import ettik
from sklearn.svm import SVR
#Kernelımızın türünü belirledik
svr_reg=SVR(kernel='rbf')
#Makinemizi eğittik
svr_reg.fit(x_olcekli,y_olcekli)

model3=sm.OLS(svr_reg.predict(x_olcekli),x_olcekli)
print(model3.fit().summary())
print("SVR R2 değeri")
print(r2_score(y_olcekli,svr_reg.predict(x_olcekli)))
#DecisionTree kutuphanesini import ettik
from sklearn.tree import DecisionTreeRegressor
#fonksiyonu random state parametresiyle çağırdık
r_dt=DecisionTreeRegressor(random_state=0)
#Makinemizi eğittik
r_dt.fit(X,Y)
print('dt ols')
model4=sm.OLS(r_dt.predict(X),X)
print(model4.fit().summary())
print("Decision Tree R2 değeri:")
print(r2_score(Y,r_dt.predict(X)))

from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators=10,random_state=0)
rf_reg.fit(X,Y)
print('dt ols')
model5=sm.OLS(rf_reg.predict(X),X)
print(model5.fit().summary())
print("Random forest R2 değeri")
print(r2_score(Y,rf_reg.predict(X)))





















































